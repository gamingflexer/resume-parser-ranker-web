from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class File(models.Model):
  file = models.FileField(blank=False, null=False)
  timestamp = models.DateTimeField(auto_now_add=True)
  
class UserInfo(models.Model):
  user = models.CharField(max_length=100, default="")
  total_uploads = models.IntegerField(default=0)
  in_progress = models.IntegerField(default=0)
    
class Resumes(models.Model):
  user = models.CharField(max_length=100, default="")
  file_name = models.CharField(max_length=1000, default="")
  file_Id = models.CharField(max_length=1000, default="")
  date = models.DateTimeField(auto_now_add=True)
  #summary
  summary = models.TextField(max_length=10000, default="")
  #personal
  name = models.CharField(max_length=100, default="")
  phone_number = models.CharField(max_length=100, default="")
  email = models.CharField(max_length=100, default="")
  linkdien_link = models.CharField(max_length=1000, default="")
  github_link = models.CharField(max_length=1000, default="")
  personal_website = models.CharField(max_length=1000, default="")
  personal_details = models.TextField(max_length=1000, default="")
  #education
  expirence = models.TextField(max_length=10000, default="")
  total_exp = models.CharField(max_length=100, default="")
  university = models.CharField(max_length=100, default="")
  designition = models.CharField(max_length=100, default="")
  degree = models.CharField(max_length=100, default="")
  skills = models.TextField(max_length=10000, default="")
  #companies & awards
  companies_worked_at = models.TextField(max_length=1000, default="")
  current_job = models.CharField(max_length=1000, default="")
  refrence = models.TextField(max_length=1000, default="")
  awards = models.TextField(max_length=1000, default="")
  #comments
  accuracy = models.CharField(max_length=100, default="")
  total_entites_extracted = models.IntegerField(default=0)
  
  #boboxes coordinates
  img_annotated = models.TextField(max_length=10000, default="")
  personal_info_bobox = models.TextField(max_length=10000, default="")
  education_bobox = models.TextField(max_length=10000, default="")
  expirence_bobox = models.TextField(max_length=10000, default="")
  awards_bobox = models.TextField(max_length=10000, default="")
  projects_bobox = models.TextField(max_length=10000, default="")
  
  
  
  
  
    