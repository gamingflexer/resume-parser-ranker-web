from rest_framework import serializers
from api.models import *

class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model = File
        fields = ('file', 'timestamp')
        
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta():
        model = UserInfo
        fields = "__all__"

class ResumesSerializer(serializers.ModelSerializer):
    class Meta():
        model = Resumes
        fields = "__all__"