from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    states = (
        (None, 'City'),
        ("London", "London"), ("Bradford", "Bradford"),
        ("Wakefield", "Wakefield"), ("Nottingham", "Nottingham"),
        ("Westminster", "Westminster"), ("Coventry", "Coventry"),
        ("Birmingham", "Birmingham"), ("Liverpool", "Liverpool"),
        ("Leeds", "Leeds"), ("Bristol", "Bristol"),
        ("Manchester", "Manchester"), ("Leicester", "Leicester"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True
    )
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_state = models.CharField(
        choices=states, max_length=40, blank=False, null=False
    )
    default_street_address = models.CharField(
        max_length=80, null=True, blank=True
        )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
