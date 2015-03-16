#-*- coding:utf-8 -*-
from django.db import models
from datetime import datetime,date
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model) :
    title = models.CharField(max_length = 100)  #博客题目
    category = models.CharField(max_length = 50, blank = True)  #博客标签
    date_time = models.DateTimeField(auto_now_add = True)  #博客日期
    #content = models.TextField(blank = True, null = True)  #博客文章正文
    content = RichTextField('内容', config_name = 'mummy_default')
    #获取URL并转换成url的表示格式
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id':self.id})
        return "http://121.43.225.213%s" % path
    def __unicode__(self) :
        return self.title

    class Meta:  #按时间下降排序
        ordering = ['-date_time']

'''
class WebCount(models.Model):
    date = models.DateField(auto_now = True,default = date.today())
    homevisit_day = models.IntegerField(default = 1) #主页访问量统计——当天
    homevisit_sum = models.IntegerField(default = 1) #主页访问量统计——总

    def  __unicode__(self) :
        return unicode(self.date)
'''
