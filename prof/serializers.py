# serializers.py
from rest_framework import serializers
from main.models import Braider, PublicInfo, SocialMedia, LocationInfo, BusinessInfo, Post

class LocationInfoProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationInfo
        fields = '__all__'

class BusinessInfoProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessInfo
        fields = '__all__'

class PublicInfoSProfileerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicInfo
        fields = '__all__'

class SocialMediaProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'

class PostProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class BraiderProfileSerializer(serializers.ModelSerializer):

    businessinfo = BusinessInfoProfileSerializer()
    locationinfo = LocationInfoProfileSerializer()
    publicinfo = PublicInfoSProfileerializer()
    socialmedia = SocialMediaProfileSerializer()
    post = PostProfileSerializer(required=False)

    class Meta:
        model = Braider
        fields = ['locationinfo', 'businessinfo', 'socialmedia', 'publicinfo', 'post', 'user_name']

