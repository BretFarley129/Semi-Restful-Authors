# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.

class UserManager(models.Manager):
    def validate(self, postData):
        print '~~~~~~~~~~~'
        errors = {}
        print postData
        my_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first']) < 2:
            errors['first'] = "First name must be at least 2 characters"

        if len(postData['last']) < 2:
            errors['last'] = "Last name must be at least 2 characters"

        if not my_re.match(postData['email']):
            errors['email'] = "Please enter a valid email format"

        return errors

class User(models.Model):
    first = models.CharField(max_length = 255)
    last = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __repr__(self):
        return "User: \n{}\n{}\n{}\n{}\n".format(self.id, self.first, self.last, self.email)


