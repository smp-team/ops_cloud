'''
Created on 2016年1月25日

@author: javen
'''
from django.db import models
from _curses import version
from test.test_imageop import MAX_LEN

class Application(models.Model):
    id = models.CharField(max_length=36,unique=True, db_index=True)
    name = models.CharField(max_length=40, unique=True, db_index=True)
    type = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    host_group = models.TextField()
    

class AppInstance(models.Model):
    id = models.CharField(max_length=36,unique=True, db_index=True)
    app = models.ForeignKey(Application)
    version = models.CharField(max_length=20)
    