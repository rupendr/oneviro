from django.db import models


# Create your models here.
class AboutTeam(models.Model):
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    profile_image = models.ImageField(upload_to='profile-image/', default='default/user_image.jpg')
    facebook_link = models.URLField(max_length=200, null=True, blank=True)
    twitter_link = models.URLField(max_length=200, null=True, blank=True)
    linkedin_link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
