from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Direction(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Student(models.Model):
    full_name = models.CharField(max_length=200)
    direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, null=True)
    study_start = models.DateField()
    study_end = models.DateField()
    image = models.ImageField(upload_to='images/', default='images/avatar.png')
    content = RichTextUploadingField(verbose_name="Content", null=True, blank=True)

    def __str__(self):
        return self.full_name
