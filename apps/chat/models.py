from django.db import models
from apps.users.models import UserProfile
from apps.trips.models import Trip

class Message(models.Model):
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(UserProfile, on_delete= models.CASCADE, related_name= 'received_messages')
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    timestamp= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f" From {self.sender} to {self.receiver} at{self.timestamp}"

# Create your models here.
