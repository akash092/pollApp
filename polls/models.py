from django.db import models
from django.utils import timezone
from django.contrib import admin
from datetime import timedelta


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date to be published')
    total_votes = models.PositiveSmallIntegerField(default=0)
    # audit fields
    created_date = models.DateTimeField('date created', auto_now_add=True)
    created_by = models.CharField('creator name', max_length=200, default='Not Specified')
    updated_date = models.DateTimeField('date updated', auto_now=True)
    updated_by = models.CharField('updated by name', max_length=200, default='Not Specified')
    row_version = models.PositiveSmallIntegerField('total iterations')

    def __str__(self):
        return self.question_text

    def before_create(self):
        self.row_version = 1  # set version to 1
        self.updated_by = self.created_by  # make updated by same as created by
        if self.pub_date is None:  # if no published date is defined, set it to right now
            self.pub_date = timezone.now()

    def before_update(self):
        self.row_version += 1  # increment row version to indicate an update being made

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
