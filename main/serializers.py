# serializers.py
from rest_framework import serializers
from main.models import Braider, PublicInfo, SocialMedia, LocationInfo, BusinessInfo, Customer
import re
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password 

class SearchSerializer(serializers.Serializer):
    keyword = serializers.CharField(max_length=128)

    

