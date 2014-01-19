from django.db import models

# Create your models here.
class Link(models.Model):
    url = models.CharField(max_length=100)
    tags = models.ManyToManyField('Tag', blank=True)
    def __unicode__(self):
        return "%s"%(self.url)



class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return "%s"%(self.name)
