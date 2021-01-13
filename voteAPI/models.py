from django.db import models
from django.conf import settings

class vote (models.Model) :
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=60)
    item1 = models.CharField(max_length=20)
    item2 = models.CharField(max_length=20)
    item3 = models.CharField(max_length=20, null=True)
    item4 = models.CharField(max_length=20, null=True)
    item5 = models.CharField(max_length=20, null=True)
    item1Cnt = models.IntegerField(default=0)
    item2Cnt = models.IntegerField(default=0)
    item3Cnt = models.IntegerField(null=True)
    item4Cnt = models.IntegerField(null=True)
    item5Cnt = models.IntegerField(null=True)
    is_consent = models.BooleanField(default=False)
    is_denied = models.BooleanField(default=False)
    select = models.CharField(max_length=7, choices=(('accept', 'accept'), ('deny', 'deny')))
    
    def __str__ (self) :
        return self.subject