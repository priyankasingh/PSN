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


class Abc(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    abc = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'abc'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PollsChoice(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('PollsQuestion')

    class Meta:
        managed = False
        db_table = 'polls_choice'


class PollsQuestion(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'polls_question'


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


class SofTag(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    tag = models.CharField(max_length=100, blank=True)
    tag_url = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'sof_tag'


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
