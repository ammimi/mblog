# mblog
学习django搭建的Blog

开发环境
  Python 2.7.3
  django 1.7.5

----------2015.3.16---------------------
1.增加ckeditor功能。
2.https://github.com/django-ckeditor/django-ckeditor (可以参考http://www.nanerbang.com/article/2/) 按照上面的步骤操作
tips：按照pillow是先要装以下两个库：
$ apt-get install libjpeg8 libjpeg8-dev
$ apt-get build-dep python-imaging
3.模板里的输出过滤  {{内容|safe}}
