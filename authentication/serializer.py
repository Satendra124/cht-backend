from authentication.utils import FirebaseAPI, Student
from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User
import logging
logger = logging.getLogger('django')

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=500)


class LoginSerializer(serializers.Serializer):
    id_token = serializers.CharField(max_length=2400)

    def access_token_validate(self, access_token):
        """
        Validate the firebase access token.
        """
        try:
            return FirebaseAPI.verify_id_token(access_token)
        except serializers.ValidationError as e:
            raise serializers.ValidationError(
                "Invalid Firebase token!") from e

    def validate(self, attrs):
        id_token = attrs.get('id_token', None)
        current_user = None
        jwt = self.access_token_validate(id_token)
        uid = jwt['uid']
        # pylint: disable=no-member
        profile = UserProfile.objects.filter(uid=uid)

        if profile:
            current_user = profile[0].user
        else:
            email = jwt['email']
            if not Student.verify_email(email):
                raise serializers.ValidationError(
                    "Please login using @itbhu.ac.in student email id only")
            name = jwt['name']
            user = User()
            user.username = jwt['uid']
            user.email = email
            user.save()
            current_user = user
            department = Student.get_department(email)
            year_of_joining = Student.get_year(email)
            # pylint: disable=no-member
            profile = UserProfile.objects.create(
                uid=uid, user=user, name=name, email=email, department=department,
                year_of_joining=year_of_joining, photo_url=jwt['picture'])

        attrs['user'] = current_user
        logger.info('[POST Response] User Login : %s', current_user)
        return attrs
