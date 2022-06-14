from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.CharField(max_length=50)
    subject = models.CharField(max_length=20, default='')
    flag = models.CharField(max_length=2, default='1')
    priority = models.CharField(max_length=2,default='0')
    pubtime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(default='')

    def __unicode__(self):
        return u'%d %s %s'%(self.id, self.todo, self.flag)

    class Meta:
        ordering = ['subject','deadline']
