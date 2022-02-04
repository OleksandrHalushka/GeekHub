from django.db import models


class Askstory(models.Model):
    id = models.IntegerField(primary_key=True)
    by = models.CharField(max_length=100)
    descendants = models.CharField(max_length=4)
    score = models.CharField(max_length=100)
    text = models.TextField(default='', null=True, max_length=100)
    time = models.CharField(max_length=10, default='', null=True)
    title = models.CharField(default='', null=True, max_length=100)
    type = models.CharField(default='', null=True, max_length=100)

    class Meta:
        verbose_name_plural = 'Askstories'


class Showstory(models.Model):
    id = models.IntegerField(primary_key=True)
    by = models.CharField(max_length=100)
    descendants = models.CharField(max_length=4)
    score = models.CharField(max_length=100)
    text = models.TextField(default='', null=True, max_length=100)
    time = models.CharField(max_length=10, default='', null=True)
    title = models.CharField(default='', null=True, max_length=100)
    type = models.CharField(default='', null=True, max_length=100)
    url = models.URLField(default='', null=True, max_length=100)

    class Meta:
        verbose_name_plural = 'Showstories'


class Newstory(models.Model):
    id = models.IntegerField(primary_key=True)
    by = models.CharField(max_length=100)
    descendants = models.CharField(max_length=4)
    score = models.CharField(max_length=100)
    text = models.TextField(default='', null=True, max_length=100)
    time = models.CharField(max_length=10, default='', null=True)
    title = models.CharField(default='', null=True, max_length=100)
    type = models.CharField(default='', null=True, max_length=100)
    url = models.URLField(default='', null=True, max_length=100)

    class Meta:
        verbose_name_plural = 'Newstories'


class Jobstory(models.Model):
    id = models.IntegerField(primary_key=True)
    by = models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    text = models.TextField(default='', null=True, max_length=100)
    time = models.CharField(max_length=10, default='', null=True)
    title = models.CharField(default='', null=True, max_length=100)
    type = models.CharField(default='', null=True, max_length=100)
    url = models.URLField(default='', null=True, max_length=100)

    class Meta:
        verbose_name_plural = 'Jobstories'