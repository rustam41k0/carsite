from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey, ManyToManyField, PositiveIntegerField, ImageField
from django.urls import reverse


class Cars(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)
    category = ForeignKey('Category', on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    description = models.TextField(default='car')
    mileage = models.PositiveIntegerField(default=0)
    transmission = models.TextField(default='manual')
    seats = models.PositiveIntegerField(default=5)
    luggage = models.PositiveIntegerField(default=4)
    fuel = models.TextField(default='petrol')

    class Meta:
        verbose_name_plural = 'Cars'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('car_single', kwargs={'car_slug': self.slug})


class Posts(models.Model):
    main_title = models.CharField(max_length=255, verbose_name="Главный заголовок")
    main_text = models.TextField(max_length=255, verbose_name="Главное описание")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)
    author = ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Описание")
    tags = ManyToManyField('Tags', related_name='tagsss')
    comments = ManyToManyField('Comments', blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.main_title

    def get_absolute_url(self):
        return reverse('blog_single', kwargs={'blog_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name

    def get_cat_count(self):
        return Cars.objects.filter(category__name=self.name).count()


class Comments(models.Model):
    text = models.TextField(max_length=255, verbose_name="Текст комментария")
    author = ForeignKey(User, on_delete=models.PROTECT)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время написания", null=True)

    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.text

    def get_com_count(self):
        return Posts.objects.filter(comments__text=self.text).count()


class Tags(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)

    class Meta:
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name
