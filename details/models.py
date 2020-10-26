from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sur_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    image = models.ImageField(upload_to='details/images/')
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    relationship = models.CharField(max_length=30,null=True)
    relationtoreferred = models.CharField(max_length=30,null=True,default='')
    invitationID = models.IntegerField(default=" ")
    parentID = models.IntegerField()
    CreatedBy = models.CharField(max_length=30)
    CreatedDate = models.DateField()
    ModifiedBY = models.CharField(max_length=30)
    ModifiedDate = models.DateField()

    class Meta:
        # exclude = ('id',)
        unique_together = (("first_name", "last_name","sur_name","city"),)


class Invitations(models.Model):
    sentby = models.IntegerField()
    sentto_mailid = models.CharField(max_length=30)
    relation = models.CharField(max_length=30)
