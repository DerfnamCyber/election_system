from django.db import models
from django.contrib.auth.models import User


class Candidate(models.Model):
    POSITION_CHOICES = [
        ('head_boy', 'Head Boy'),
        ('head_girl', 'Head Girl'),
        ('sports_prefect', 'Sports Prefect')
    ]
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='candidate_photos/', blank=True, null=True)
    manifesto = models.TextField()
    position = models.CharField(max_length=30, choices=POSITION_CHOICES)
    
    def __str__(self):
        return f"{self.name} ({self.get_position_display()})"
    
class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
class Meta:
    unique_together = ('voter', 'candidate__position')   #One vote per position per voter
            
        
        
