from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from config import basepath
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
        
        
class FileView(APIView):  # for getting REPORT upload
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            pathOfFile = file_serializer.data['file']
            logging.info("Report File Saved !")
            newPath = basepath + '/' + pathOfFile
            print("File Saved: ", newPath)
            try:
                context = {"data": "File Uploaded Successfully"}
                return Response(context, status=status.HTTP_200_OK)
            except Exception as e:
                print("Report Gen File error - DJANGO SIDE - ", e)
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(file_serializer.errors['file'], status=status.HTTP_400_BAD_REQUEST)