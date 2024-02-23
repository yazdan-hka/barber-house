# serializers.py
from rest_framework import serializers
from main.models import Braider, PublicInfo, SocialMedia, LocationInfo, BusinessInfo, Customer

class Search(serializers.Serializer):
    text = serializers.CharField(max_length=128)

class SearchLocationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationInfo
        fields = ['country', 'city']

class SearchBusinessInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessInfo
        fields = ['name', 'website']

class SearchPublicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicInfo
        fields = ['profile_picture']

class SearchSocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ['instagram']

class SearchBraiderSerializer(serializers.ModelSerializer):

    businessinfo = SearchBusinessInfoSerializer()
    locationinfo = SearchLocationInfoSerializer()
    publicinfo = SearchPublicInfoSerializer()
    socialmedia = SearchSocialMediaSerializer()

    class Meta:
        model = Braider
        fields = ['locationinfo', 'businessinfo', 'socialmedia', 'publicinfo', 'user_name']

