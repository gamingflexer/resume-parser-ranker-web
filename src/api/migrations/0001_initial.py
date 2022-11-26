# Generated by Django 3.2.6 on 2022-11-25 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resumes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=100)),
                ('file_name', models.CharField(default='', max_length=1000)),
                ('file_Id', models.CharField(default='', max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('summary', models.TextField(default='', max_length=10000)),
                ('name', models.CharField(default='', max_length=100)),
                ('phone_number', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('linkdien_link', models.CharField(default='', max_length=1000)),
                ('github_link', models.CharField(default='', max_length=1000)),
                ('personal_website', models.CharField(default='', max_length=1000)),
                ('personal_details', models.TextField(default='', max_length=1000)),
                ('expirence', models.TextField(default='', max_length=10000)),
                ('total_exp', models.CharField(default='', max_length=100)),
                ('university', models.CharField(default='', max_length=100)),
                ('designition', models.CharField(default='', max_length=100)),
                ('degree', models.CharField(default='', max_length=100)),
                ('skills', models.TextField(default='', max_length=10000)),
                ('companies_worked_at', models.TextField(default='', max_length=1000)),
                ('current_job', models.CharField(default='', max_length=1000)),
                ('refrence', models.TextField(default='', max_length=1000)),
                ('awards', models.TextField(default='', max_length=1000)),
                ('accuracy', models.CharField(default='', max_length=100)),
                ('total_entites_extracted', models.IntegerField(default=0)),
                ('img_annotated', models.TextField(default='', max_length=10000)),
                ('personal_info_bobox', models.TextField(default='', max_length=10000)),
                ('education_bobox', models.TextField(default='', max_length=10000)),
                ('expirence_bobox', models.TextField(default='', max_length=10000)),
                ('awards_bobox', models.TextField(default='', max_length=10000)),
                ('projects_bobox', models.TextField(default='', max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=100)),
                ('total_uploads', models.IntegerField(default=0)),
                ('in_progress', models.IntegerField(default=0)),
                ('user_name', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
