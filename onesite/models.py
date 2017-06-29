# -*- coding: utf-8 -*-
from django.db import models

class OneSiteDemo(models.Model):
    class Meta():
        db_table ='db_one_site_demo'

    """
    первая проба пера
    """

    onesitedemo_title = models.CharField(max_length=200, verbose_name='Заголовок')
    onesitedemo_text = models.TextField(verbose_name='Текст', blank=True, null=True)
    onesitedemo_date = models.DateTimeField(verbose_name='Время публикации')

    def __unicode__(self):
        return self.onesitedemo_title


