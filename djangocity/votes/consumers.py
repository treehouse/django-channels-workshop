import json

from channels import Group

from .models import Vote, Voter


def vote_saved(message):
    data = {}
    for voter in Voter.objects.all():
        blank_data = {}
        for choice in Vote.CATEGORIES:
            blank_data[choice[0]] = {'yes': 0, 'no': 0}
        data[voter.id] = blank_data

    for vote in Vote.objects.all():
        for voter in vote.yes_votes.all():
            data[voter.id][vote.category]['yes'] += 1
        for voter in vote.no_votes.all():
            data[voter.id][vote.category]['no'] += 1

    Group('dashboard').send({
        'text': json.dumps(data)
    })


def ws_connect(message):
    Group('dashboard').add(message.reply_channel)


def ws_disconnect(message):
    Group('dashboard').discard(message.reply_channel)
