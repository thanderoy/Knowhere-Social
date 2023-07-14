from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings



class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(
        upload_to="users/profile_photos/%Y/%m/%d", blank=True
    )

    def __str__(self):
        return f"Profile: {self.user.username}"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def user_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
