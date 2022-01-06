from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, first_name=instance.first_name,
                               last_name=instance.last_name, email=instance.email)
        print('Profile created!')


# @receiver(post_save, sender=User)
# def update_profile(sender, instance, created, **kwargs):
#     if created == False:
#         instance.profile.save()
#         print("Profile updated!")
