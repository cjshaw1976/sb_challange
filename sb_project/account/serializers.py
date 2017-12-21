from django.contrib.auth.models import User

from rest_framework import serializers

from datetime import datetime, date
import re

from .models import Customer, AccessLog


class CustomerSerializer(serializers.ModelSerializer):
    VALID_IMAGE_EXTENSIONS = [
        ".jpg",
        ".png",
        ".pdf",
    ]

    def validate(self, data):
        """
        Validate input
        """
        if not re.match("^(?=.*[!@#$%^&*()_+-=?|:;'/\])(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*\s).{6,15}$", data['password']):
            # Does not match
            raise serializers.ValidationError({'password': ['Password must be between 6 and 15 characters, include upper and lower case character, digits and special charters but no spaces.']})

        if not re.match("^(?:\d{2}(?:\s|\-)\d{6,7}[a-zA-Z]\d{2})|(?:\d{8,9}[a-zA-Z]\d{2})$", data['id_number']):
            # Does not match
            raise serializers.ValidationError({'id_number': ['Invalid ID Format']})

        # Remove spaces and special characters from phone number
        data['phone_number'] = re.sub('[^\d\+]', '', data['phone_number'])

        #  Match format +2637********
        if not re.match("^\+2637\d{8}$", data['phone_number']):
            raise serializers.ValidationError({'phone_number': ['Phone number must be in the format +2637********']})

        now = datetime.now()
        ago = date(now.year - 16, now.month, now.day)

        if data['birth_date'] > ago:
            raise serializers.ValidationError({'birth_date': ['Account Holder must be at least 16 years old']})

        if not data['headshot_image']:
            raise serializers.ValidationError({'headshot_image': ["Image must have .jpg, .png or .pdf extension"]})
        else:
            if not any([data['headshot_image'].name.endswith(e) for e in self.VALID_IMAGE_EXTENSIONS]):
                raise serializers.ValidationError({'headshot_image': ["Image must have .jpg, .png or .pdf extension"]})

        if not data['residence_image']:
            raise ValidationError({'residence_image': ["Image must have .jpg, .png or .pdf extension"]})
        else:
            if not any([data['residence_image'].name.endswith(e) for e in self.VALID_IMAGE_EXTENSIONS]):
                raise serializers.ValidationError({'residence_image': ["Image must have .jpg, .png or .pdf extension"]})

        if not data['signature_image']:
            raise serializers.ValidationError({'signature_image': ["Image must have .jpg, .png or .pdf extension"]})
        else:
            if not any([data['signature_image'].name.endswith(e) for e in self.VALID_IMAGE_EXTENSIONS]):
                raise serializers.ValidationError({'signature_image': ["Image must have .jpg, .png or .pdf extension"]})

        return data

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super(CustomerSerializer, self).create(validated_data)

    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ('created_by', 'created_date',)



class AccessLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessLog
        fields = '__all__'
