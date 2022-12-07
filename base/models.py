from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Event(models.Model):
    EVENT_TYPE = (
        ('1', 'کتاب گرد'),
        ('2', 'پخش مستند'),
        ('3', 'دوره های آموزشی'),
        ('4', 'همایش')
    )
    type = models.CharField(max_length=200, choices=EVENT_TYPE)
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    location = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    capacity = models.IntegerField()
    enrolled = models.IntegerField(default=0, null=True, blank=True)
    held = models.BooleanField(default=False, blank=True, null=True)
    date_time = models.DateTimeField()

    def __str__(self):
        return str(self.title)

    class Meta:
        # A USER CAN NOT CREATE MORE THAN ONE EVENT WITH SAME TITLE, TYPE AND DATE TIME
        unique_together = [['owner', 'title', 'type', 'date_time']]


class Registrant(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=11, null=True, blank=True)
    phone_number = models.CharField(max_length=11)
    university = models.CharField(max_length=100, null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['event', 'phone_number']]

    def __str__(self):
        return f"{self.first_name} {self.event}"
