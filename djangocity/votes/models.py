from django.db import models

class Voter(models.Model):

    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True)

    def __str__(self):
        if self.title:
            return "{} {}".format(self.title, self.name)
        return self.name


class Vote(models.Model):
    CATEGORIES = (
        ('housing', 'Housing'),
        ('parks', 'Parks'),
        ('schools', 'Schools'),
        ('safety', 'Public Safety'),
    )

    issue = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORIES, blank=True)
    yes_votes = models.ManyToManyField(Voter, blank=True, related_name='yes')
    no_votes = models.ManyToManyField(Voter, blank=True, related_name='no')

    def __str__(self):
        return "{}: {}".format(self.category, self.issue)