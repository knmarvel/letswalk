from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    display_name = models.CharField(
        max_length=150,
        null=True,
        blank=True
    )
    slug = models.SlugField(
        null=False,
        unique=True,
    )


    REQUIRED_FIELDS = ['display_name']


    def get_absolute_url(self):
        return reverse("Team_detail", kwargs={"slug": self.slug})


    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.username)
        return super().save(*args, **kwargs)


class Team(models.Model):
    TEAM_STATUSES = [
        ('New', 'New'),
        ('In Process', 'In Process'),
        ('Done', 'Done'),
        ('Invalid', 'Invalid')
    ]

    title = models.CharField(
        max_length=200
    )

    class Meta:
        ordering = ['title']

    creation_date = models.DateTimeField(
        default=datetime.now
    )

    team_members = models.ManyToManyField(MyUser, related_name='teammember')

    team_admins = models.ManyToManyField(MyUser, related_name='teamadmin')

    description = models.TextField(
        max_length=200
    )

    team_owner = models.ForeignKey(
        MyUser,
        related_name="owner",
        null=True, 
        on_delete=models.SET_NULL
    )

    status = models.CharField(
        max_length = 10,
        choices=TEAM_STATUSES
    )

    slug = models.SlugField(
        null=False,
        unique=True,
    )
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Team_detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    