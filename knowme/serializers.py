from rest_framework import serializers

from .models import myDetails

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = myDetails
        fields=['name','email','phno','college','skills']