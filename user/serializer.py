# serializers.py
from rest_framework import serializers
from main.models import Braider, PublicInfo, SocialMedia, LocationInfo, BusinessInfo, Customer
import re
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password 



# {
#   "user_name": "example_username",
#   "email": "example@email.com",
#   "password": "example_password",
#   "phone_number": "+989387744584",
#   "public_info": {
#     "first_name": "John",
#     "last_name": "Doe"
#   },
#   "social_media": {
#     "instagram": "john_doe_insta"
#   },
#   "location_info": {
#     "country": "United States",
#     "city": "New York"
#   },
#   "business_info": {
#     "website": "https://example.com"
#   }
# }


# region register serializers

class RegisterPublicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicInfo
        fields = ['first_name', 'last_name']

class RegisterSocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ['instagram']

    def validate_instagram(self, value):
        if not re.match(r'^[a-zA-Z0-9_]+$', value):
            raise serializers.ValidationError("Invalid Instagram ID format.")
        return value

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        self.validate_instagram(attrs['instagram'])
        return validated_data    

class RegisterLocationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationInfo
        fields = ['country', 'city']

class RegisterBusinessInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessInfo
        fields = ['website']

        def validate_website(self, value):
            url_validator = URLValidator()

            try:
                url_validator(value)
            except ValidationError as e:
                raise serializers.ValidationError('URL Must Be Valid. Check Again.')

            return value

class RegisterBraiderSerializer(serializers.ModelSerializer):
    public_info = RegisterPublicInfoSerializer()
    social_media = RegisterSocialMediaSerializer()
    location_info = RegisterLocationInfoSerializer()
    business_info = RegisterBusinessInfoSerializer()

    class Meta:
        model = Braider
        fields = ['user_name', 'email', 'password', 'phone_number',
                  'public_info', 'social_media', 'location_info', 'business_info']
        
    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        
        numeric_count = sum(1 for char in value if char.isdigit())
        
        if numeric_count < 1:
            raise serializers.ValidationError( "Use numbers for more security.".title())

        uppercase_count = sum(1 for char in value if char.isupper())
        
        if uppercase_count < 1:
            raise serializers.ValidationError('Use UPPERCASE letters for more security.'.title())

        return value

    
    def validate_user_name(self, value):
        if not re.match(r'^[a-zA-Z0-9_]+$', value):
            raise serializers.ValidationError(f'Invalid Username "{value}". Ensure your username includes only letters, numbers, and underscores (_).'.title())
        return value
    

    
            
    def validate(self, data):
        user_name = data.get('user_name')
        email = data.get('email')
        phone_number = data.get('phone_number')

        # Check if any of the values already exist in the database
        if Braider.objects.filter(user_name=user_name).exists() or Customer.objects.filter(user_name=user_name).exists():
            raise serializers.ValidationError({'user_name': 'Username already exists.'.title()})

        if Braider.objects.filter(email=email).exists() or Customer.objects.filter(user_name=user_name).exists():
            raise serializers.ValidationError({'email': 'Email already exists.'.title()})

        if Braider.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError({'phone_number': 'Phone number must be unique.'})

        return data

    def create(self, validated_data):
        public_info_data = validated_data.pop('public_info')
        social_media_data = validated_data.pop('social_media')
        location_info_data = validated_data.pop('location_info')
        business_info_data = validated_data.pop('business_info')

        braider_instance = Braider.objects.create(
            user_name=validated_data['user_name'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone_number=validated_data['phone_number']
            # Add other fields as needed
        )

        PublicInfo.objects.create(rel=braider_instance, **public_info_data)
        SocialMedia.objects.create(rel=braider_instance, **social_media_data)
        LocationInfo.objects.create(rel=braider_instance, **location_info_data)
        BusinessInfo.objects.create(rel=braider_instance, **business_info_data)

        return braider_instance

#  endregion
    

class LoginBraiderSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=27)
    password = serializers.CharField()
    remember_me = serializers.BooleanField(default=False)

    def validate_username(self, value):
        if not re.match(r'^[a-zA-Z0-9_]+$', value):
            raise serializers.ValidationError(f'Invalid Username "{value}". Ensure your username includes only letters, numbers, and underscores (_).'.title())
        return value
    
    # def validate(self, attrs):
    #     validated_data = super().validate(attrs)
    #     self.validate_username(attrs['username'])
    #     return validated_data    

    
class RegisterCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
                    'user_name', 
                    'first_name', 
                    'last_name',
                    'email',
                    'password',
                  ]
        
    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        
        numeric_count = sum(1 for char in value if char.isdigit())
        
        if numeric_count < 1:
            raise serializers.ValidationError( "Use numbers for more security.".title())

        uppercase_count = sum(1 for char in value if char.isupper())
        
        if uppercase_count < 1:
            raise serializers.ValidationError('Use UPPERCASE letters for more security.'.title())

        return value
    
    def validate_user_name(self, value):
        if not re.match(r'^[a-zA-Z0-9_]+$', value):
            raise serializers.ValidationError(f'Invalid Username "{value}". Ensure your username includes only letters, numbers, and underscores (_).'.title())
        return value
            
    def validate(self, data):
        user_name = data.get('user_name')
        email = data.get('email')

        # Check if any of the values already exist in the database
        if Braider.objects.filter(user_name=user_name).exists() or Customer.objects.filter(user_name=user_name).exists():
            raise serializers.ValidationError({'user_name': 'Username already exists.'.title()})

        if Braider.objects.filter(email=email).exists() or Customer.objects.filter(user_name=user_name).exists():
            raise serializers.ValidationError({'email': 'Email already exists.'.title()})


        return data
