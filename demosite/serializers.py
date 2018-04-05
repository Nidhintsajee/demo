from rest_framework import serializers

from models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializing all the NearbyModel
    """
    class Meta:
        model = UserProfile
        depth=1
        fields = ('id','user','full_name','email')
