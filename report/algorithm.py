from django.db.models.lookups import GreaterThan
from report.models import ActivityIndexDiscriptions, Index, Suggestions
from authentication.models import UserProfile
import datetime
from activity.models import DetailActivity
import datetime
from django.db.models import Q
class Sleep:
    def __init__(self, start, end):
        self.start = start
        self.end = start



def is_sleeping_activity(activity,lastLat,lastLng):
    """
    Returns:\n
    True - If this activity is a sleep event\n
    False - If not a sleep activity
    \n
    Condition:
    1 . Screen Time < 10s
    2 . Location Const.
    3 . Index - Sleepable
    """
    if abs(lastLat-activity.latitude) < 0.00001 and abs(lastLng-activity.longitude) < 0.00001 and activity.screenTime < datetime.timedelta(seconds=10) and activity.index.name == "Hostel":
        return True
    else:
        return False



def detect_sleep(activities):
    """
    Parameters:
    queryset (Queryset) : list of object which are sus of sleep \n
    Sleep is detected based on 3 main components :
    1. Phone State - OFF
    2. Location - Not Changing
    3. Index - Sleepable

    Returns:
    List of [Sleep] objects
    """

    now = datetime.datetime.now()
    sleepsus = activities.filter(timestamp__date__gte=now.replace(hour=21,minute=0,second=0,microsecond=0)) 
    sleeps = []
    isSleeping = False
    cursleep = Sleep(now,now)
    if(len(sleepsus)>0):
        lastLat = sleepsus[0].latitude
        lastLng = sleepsus[0].longitude
    else:
        lastLat = 0.0
        lastLng = 0.0
    for act in sleepsus:
        if(is_sleeping_activity(act,lastLat=lastLng,lastLng=lastLat)):
            if isSleeping:
                cursleep.end = act.timestamp
            else:
                isSleeping = True
                cursleep.start = act.timestamp
        else:
            if isSleeping:
                cursleep.end = act.timestamp
                sleeps.append(cursleep)
                isSleeping = False

    #chunks of sleep objects keep only those with 4 hours at least
    for sl in sleeps:
        if (sl.end - sl.start) < datetime.timedelta(hours=4):
            sleeps.remove(sl)
    return sleeps

def in_sleep_list(sleepArr,activity):
    for sl in sleepArr:
        if activity.timestamp>sl.start and activity.timestamp < sl.end :
            return True
    return False

def calculate_score(idealtime,timespent,indexs):
    score = 1.0
    totalItems = len(indexs)
    for idx in indexs:
        if(idealtime[idx]['greaterThan']<=timespent[idx]):
            score -= abs(timespent[idx] - idealtime[idx]['greaterThan'])/(idealtime[idx]['greaterThan'] * totalItems)
        elif idealtime[idx]['lessThan']>=timespent[idx]:
            score -= abs(idealtime[idx]['lessThan'] - timespent[idx])/(idealtime[idx]['lessThan']*totalItems)
    return score*10 

def get_report_today_live(userid):
    """
    Parameter: [userid]\n
    Returns: Report for [userid]
    """
    #USER FOR WHICH REPORT WILL BE MADE
    user = UserProfile.objects.get(uid=userid)
    #current time
    now = datetime.datetime.now()
    #this gives activity from 8am today
    todaysActivity =  DetailActivity.objects.filter(user=user,timestamp__date__gt=now.replace(hour=8,minute=0,second=0,microsecond=0))
    #DATA
    indexs = []  #should contain list of all indexs
    indexTimes = {} # dict as INDEX:duration
    indexIdealTime = {} #ideal time to spend
    indexObj = Index.objects.all()
    for idx in indexObj:
        indexs.append(idx.name)
        indexIdealTime[idx.name] = {"lessThan":idx.minHours * 60,"greaterThan":idx.maxHours * 60}
        indexTimes[idx.name] = 0.0
    #START - REPORT ALGORITHM-------------------------
    # part 1 ---- DETECT SLEEP -----------------------
    sleeps = detect_sleep(todaysActivity)
    #part 2 ------ INDEX DATA ----------------------
    #every activity is worth 5 minutes HARDCODED

    for activity in todaysActivity:
        if not in_sleep_list(activity=activity,sleepArr=sleeps):
            indexTimes[activity.index.name] += 5.0
    activityStr = ""
    for idx in indexs:
        activityStr += idx +","+ str(indexTimes[idx])+ ","+str(indexIdealTime[idx])+";"
    
    actTexts = []
    for idx in indexs:
        actTexts += ActivityIndexDiscriptions.objects.filter(Q(greaterThan__gte=indexTimes[idx]) | Q(lessThan__lte=indexTimes[idx]))
    #for tex in actTexts:
    #    tex = ActivityIndexSerializer(tex).data
    
    suggestions = []
    for idx in indexs:
        suggestions += Suggestions.objects.filter(Q(greaterThan__gte=indexTimes[idx]) | Q(lessThan__lte=indexTimes[idx]))
    #for tex in suggestions:
    #    tex = SuggestionSerializer(tex).data
    
    score = calculate_score(idealtime=indexIdealTime,timespent=indexTimes,indexs=indexs)

    return {
        "score" : score,
        "indexHours" : activityStr,
        "activityIndexDiscriptions" : actTexts,
        "suggestions" : suggestions
    }
    #END ------------------- REPORT ALGORITHM---------------------------