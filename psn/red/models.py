# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models



class RedComments(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    red_posts = models.ForeignKey('RedPosts')
    comment_id = models.CharField(unique=True, max_length=25, blank=True)
    body = models.TextField(blank=True)
    author = models.CharField(max_length=50, blank=True)
    up_vote = models.IntegerField(blank=True, null=True)
    down_vote = models.IntegerField(blank=True, null=True)
    parent_id = models.CharField(max_length=25, blank=True)
    post_id = models.CharField(max_length=25, blank=True)
    subreddit = models.CharField(max_length=50, blank=True)
    creation_date = models.IntegerField(blank=True, null=True)
    body_annotation = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'red_comments'

    def __unicode__(self):
        return unicode(self.comment_id) or u''


class RedPosts(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    post_id = models.CharField(unique=True, max_length=25, blank=True)
    title = models.CharField(max_length=500, blank=True)
    body = models.TextField(blank=True)
    author = models.CharField(max_length=50, blank=True)
    up_vote = models.IntegerField(blank=True, null=True)
    down_vote = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    permalink = models.CharField(max_length=500, blank=True)
    url = models.CharField(max_length=500, blank=True)
    creation_date = models.IntegerField(blank=True, null=True)
    subreddit = models.CharField(max_length=50, blank=True)
    flair = models.CharField(max_length=50, blank=True)
    annotation = models.TextField(blank=True)
    body_annotation = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'red_posts'

    def __unicode__(self):
        return unicode(self.post_id) or u''