from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class UserProfile(models.Model):
    useruid = models.CharField(max_length=64)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    department = models.CharField(max_length=60)
    year_of_joining = models.CharField(max_length=10)
    photo_url = models.URLField(null=True, blank=True, editable=False)
    token = models.CharField(max_length=100)
    # pylint: disable=invalid-str-returned
    def __str__(self):
        return self.name

class ExtendedUserProfile(models.Model):
    useruid = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    height = models.DecimalField(decimal_places=2,max_digits=4)
    weight = models.DecimalField(decimal_places=2,max_digits=4)
    age = models.IntegerField()
    quiz_answer_string = models.CharField(max_length=100)
    calculated_scores = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.user

'''
TIPI
Quiz:
Extraverted, enthusiastic.
Critical, quarrelsome.
Dependable, self-disciplined.
Anxious, easily upset.
Open to new experiences, complex.
Reserved, quiet.
Sympathetic, warm.
Disorganized, careless.
Calm, emotionally stable.
Conventional, uncreative.


calculated_scores:
Extroversion -	Agreeableness -	Conscientiousness -	Emotional Stability - Openness


http://gosling.psy.utexas.edu/scales-weve-developed/ten-item-personality-measure-tipi/ten-item-personality-inventory-tipi/
'''