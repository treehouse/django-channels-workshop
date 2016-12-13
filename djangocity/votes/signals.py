from django.db.models.signals import post_save
from django.dispatch import receiver

from channels import Channel

from .models import Vote


@receiver(post_save, sender=Vote)
def vote_save_handler(sender, **kwargs):
    Channel('vote-saved').send({
        'vote': sender.id
    })
