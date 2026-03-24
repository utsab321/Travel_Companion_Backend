from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    bio = models.TextField(blank=True)
    location= models.CharField(max_length=100, blank=True)
    preferred_destinations = models.CharField(max_length=255, blank=True)
    travel_style =models.CharField(max_length=50, choices=[('budget', 'Budget'), ('luxury', 'Luxury'), ('adventure','Adventure')])

    pace = models.CharField(
        max_length=50,
        choices =[('relaxed' ,'Relaxed'),('moderate','Moderate'),('fast_paced', 'Fast_paced')],
        blank=True
    )

    accomodation_preference = models.CharField(
        max_length=50,
        choices=[('hostel','Hostel'),('hotel','Hotel'),('inn','Inn'),('camping', 'Camping')],
        blank=True
    )



    profile_picture = models.ImageField(upload_to='profiles/',blank=True)
    budget_level= models.IntegerField(default=5, help_text="0= cheap,  1 = expensive")
    adventure_level = models.IntegerField(default=5, help_text="0= safe & calm, 10 = adventurous")
    social_level = models.IntegerField(default=5, help_text="0 = solo_traveller, 10= group")
   
    preference_vector = models.JSONField(null=True, blank=True)
    def __str__(self):
        return self.user.username
    
class Match(models.Model):

    user1 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="initiated_matches"
    )

    user2 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="received_matches"
    )

    similarity_score = models.FloatField()

    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('accepted', 'Accepted'),
            ('rejected', 'Rejected')
        ],
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user1} ↔ {self.user2}"
    
class UserLoginHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Connect to User model
    login_time = models.DateTimeField(auto_now_add=True)       # Timestamp of login
    ip_address = models.GenericIPAddressField(null=True, blank=True)  # Optional
    user_agent = models.TextField(null=True, blank=True)      # Optional browser info

    def __str__(self):
        return f"{self.user.username} logged in at {self.login_time}"
# Create your models here.