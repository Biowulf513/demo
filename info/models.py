# -*- coding: utf-8 -*-
from django.db import models

class Music(models.Model):
    class Meta():
        db_table = 'db_info_music'

    group_name = models.CharField(max_length=20, verbose_name='Группа')
    track_name = models.CharField(max_length=40, verbose_name='Название трека')
    track_rating = models.SmallIntegerField(max_length=3, verbose_name='Рейтинг трека', blank=True, null=True)


class VkGroup(models.Model):
    class Meta():
        db_table = 'db_info_vk_group'

    name = models.CharField(max_length=40, verbose_name='Название группы')
    comment = models.TextField (max_length=200, verbose_name='Мнение о группе')

class Friend(models.Model):
    class Meta():
        db_table = 'db_info_friend'
    name = models.CharField(max_length=20, verbose_name='Имя')
    second_name = models.CharField(max_length=20, verbose_name='Фамилия')

class Note(models.Model):
    class Meta():
        db_table = 'db_info_note'

    text = models.TextField(max_length=200, verbose_name='Запиши мысль')
    time = models.DateTimeField(auto_now=True)


