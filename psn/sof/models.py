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



class SofAnswers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    post_id = models.IntegerField(unique=True, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    body = models.TextField(blank=True)
    title = models.CharField(max_length=500, blank=True)
    owner_user_id = models.IntegerField(blank=True, null=True)
    tags = models.CharField(max_length=500, blank=True)
    comment_count = models.IntegerField(blank=True, null=True)
    body_annotation = models.TextField(blank=True)
    title_annotation = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'sof_answers'

    def __unicode__(self):
        return unicode(self.post_id) or u''


class SofPosts(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    post_id = models.IntegerField(blank=True, null=True)
    post_type_id = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    accepted_answer_id = models.IntegerField(blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    view_count = models.IntegerField(blank=True, null=True)
    body = models.TextField(blank=True)
    owner_user_id = models.IntegerField()
    title = models.CharField(max_length=500, blank=True)
    tags = models.CharField(max_length=500, blank=True)
    answer_count = models.IntegerField(blank=True, null=True)
    comment_count = models.IntegerField(blank=True, null=True)
    favourite_count = models.IntegerField(blank=True, null=True)
    body_annotation = models.TextField(blank=True)
    title_annotation = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'sof_posts'

    def __unicode__(self):
        return unicode(self.post_id) or u''


class SofQuestions(models.Model):
    id = models.IntegerField()
    post_id = models.IntegerField(unique=True)
    accepted_answer_id = models.IntegerField(blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    view_count = models.IntegerField(blank=True, null=True)
    owner_user_id = models.IntegerField()
    body = models.TextField(blank=True)
    title = models.CharField(max_length=500, blank=True)
    tags = models.CharField(max_length=500, blank=True)
    answer_count = models.IntegerField(blank=True, null=True)
    comment_count = models.IntegerField(blank=True, null=True)
    favourite_count = models.IntegerField(blank=True, null=True)
    body_annotation = models.TextField(blank=True)
    title_annotation = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'sof_questions'

    def __unicode__(self):
        return unicode(self.post_id) or u''


class SofTag(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    tag = models.CharField(max_length=100, blank=True)
    tag_url = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'sof_tag'

    def __unicode__(self):
        return unicode(self.tag) or u''


class SofUsers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user_id = models.IntegerField(blank=True, null=True)
    reputation = models.IntegerField(blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)
    display_name = models.CharField(max_length=50, blank=True)
    email_hash = models.CharField(max_length=100, blank=True)
    last_access_date = models.DateTimeField(blank=True, null=True)
    website_url = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)
    about_me = models.TextField(blank=True)
    views = models.IntegerField(blank=True, null=True)
    upvotes = models.IntegerField(blank=True, null=True)
    downvotes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sof_users'

    def __unicode__(self):
        return unicode(self.display_name) or u''


class SofVotes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    vote_id = models.IntegerField(blank=True, null=True)
    post_id = models.IntegerField(blank=True, null=True)
    vote_type_id = models.IntegerField(blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    bounty_amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sof_votes'

    def __unicode__(self):
        return unicode(self.post_id) or u''
