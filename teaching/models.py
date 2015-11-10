from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=128)
    per_address = models.CharField(max_length=128)
    temp_address = models.CharField(max_length=128)
    class_location = models.CharField(max_length=128)
    phone = models.IntegerField()
    email = models.EmailField()
    class_days = models.IntegerField()
    available_days = models.CharField(max_length=128)
    qualification = models.CharField(max_length=128)
    specialisation = models.CharField(max_length=128)
    experience = models.IntegerField()
    shift_type = models.CharField(max_length=128)
    teaching_level = models.CharField(max_length=128,default=None,blank=True)
    rating = models.IntegerField(default=0,blank=True)
    profile_pic = models.ImageField()
    signature_pic = models.ImageField(default=None,blank=True)
    varification_doc1 = models.CharField(max_length=128,default=None,blank=True)
    verification_doc2 = models.CharField(max_length=128,default=None,blank=True)
    def __unicode__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.IntegerField(default=None)
    per_address = models.CharField(max_length=128,default=None)
    temp_address = models.CharField(max_length=128,default=None)
    class_location = models.CharField(max_length=128,default=None)
    language = models.CharField(max_length=128,default=None)
    subjects = models.CharField(max_length=128,default=None)
    qualification = models.CharField(max_length=128,default=None,blank=True)
    standard = models.CharField(max_length=128,default=None,blank=True)
    def __unicode__(self):
        return self.name

