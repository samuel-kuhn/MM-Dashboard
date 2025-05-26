# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

from django.contrib.auth.models import AbstractUser


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    port_range = models.CharField(max_length=30, blank=True, default="25565-25568")
    max_ram = models.IntegerField(blank=True, default=5, name="max_ram", verbose_name="Ram amount (in GB)")

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
