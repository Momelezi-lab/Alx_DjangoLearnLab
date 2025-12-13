from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True
    )
    # Single field for directed follows; reverse via related_name='followers'
    following = models.ManyToManyField(
        'self',
        symmetrical=False,  # Directed: A follows B != B follows A
        related_name='followers',
        blank=True
    )

    def __str__(self):
        return self.username

    def follow(self, user):
        if user != self:  # Prevent self-follow
            self.following.add(user)

    def unfollow(self, user):
        self.following.remove(user)

    def is_following(self, user):
        return user in self.following.all()


def follow(self, user):
    if user != self:  # Prevent self-follow
            self.following.add(user)

    def unfollow(self, user):
        self.following.remove(user)

    def is_following(self, user):
        return user in self.following.all()