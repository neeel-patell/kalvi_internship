from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField, TimeField, URLField

class Schedule(models.Model):
    topic = CharField(null=False, max_length=50)
    subject = IntegerField(null=False)
    clss = IntegerField(null=False)
    board = CharField(null=False, max_length=10)
    description = CharField(null=False, max_length=50)
    date = DateField(null=False)
    start_time = TimeField(null=False)
    end_time = TimeField(null=False)
    meeting_link = URLField(null=False, max_length=50)
    language = IntegerField(null=False)

    class Meta:
        db_table = 'scheduled_classes'