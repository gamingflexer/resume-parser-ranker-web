from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from .serializers import FileSerializer,UserInfoSerializer,ResumesSerializer
from .models import UserInfo,Resumes
from api.config import basepath
from api.utils import uuid4_generator,to_json
import logging
# Create your views here.

class BaseAPI(APIView):

    def get(self, request):
        try:
            result = ""
            context = {
                'data': result
            }
            return Response(context, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_200_OK)
        
        
class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            username = str(request.user)
            file_serializer = FileSerializer(data=request.data)
            if file_serializer.is_valid():
                file_serializer.save()
                pathOfFile = file_serializer.data['file']
                logging.info("File Saved !")
                newPath = basepath + '/' + pathOfFile
                filename = newPath.split('/')[-1]
                file_id = uuid4_generator()
                #add extraction code here ...
                data_map = {"file_id":file_id,"file_name":filename,"user":username}
                serialized = ResumesSerializer(data=data_map)
                if serialized.is_valid():
                    serialized.save()
                return Response(file_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(file_serializer.errors['file'], status=status.HTTP_400_BAD_REQUEST)
            
# extra functions

def dashboard_data_main(user):
    users_list = UserInfo.objects.filter(user=user)
    users_list_serializer_data = UserInfoSerializer(users_list, many=True).data
    context = []
    for user_single in users_list_serializer_data:
        if user_single['user'] == user:
            context.append({"user":user,"total_uploads":user_single['total_uploads'],"in_progress":user_single['in_progress']})
            return context[0]
        else:
            data_map = {"user":user}
            serialized = UserInfoSerializer(data=data_map)
            if serialized.is_valid():
                serialized.save()
                dashboard_data(user)
            
def dashboard_data(user):
    resumes_list = Resumes.objects.filter(user=user)
    resumes_list_serializer_data = ResumesSerializer(resumes_list, many=True).data
    return to_json(resumes_list_serializer_data)
