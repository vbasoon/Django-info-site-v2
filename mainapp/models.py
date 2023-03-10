from django.db import models
from django.urls import reverse
# from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    # content = CKEditor5Field('Зміст', blank=True, config_name='extends')
    content = models.TextField('Зміст', blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    # video = models.FileField(upload_to='videos/%Y/%m/%d/', blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубліковано")
    categories = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категорії")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ['id']


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name="Новини розробки")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    # content = CKEditor5Field('Зміст', blank=True, config_name='extends')
    content = models.TextField('Зміст', blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    # video = models.FileField(upload_to='videos/%Y/%m/%d/', blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубліковано")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('develop', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Develop news"
        verbose_name_plural = "Develop News"
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категорії")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('categories', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['-name']