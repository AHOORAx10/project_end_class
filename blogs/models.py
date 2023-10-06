from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url_title = models.CharField(unique=True, max_length=300, verbose_name='عنوان در url')

    def __str__(self):
        self.slug = slugify(self.title)
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ProductInformation(models.Model):
    color = models.CharField(max_length=200, verbose_name='رنگ')
    size = models.CharField(max_length=200, verbose_name='سایز')

    def __str__(self):
        return f'{self.color}----{self.size}'

    class Meta:
        verbose_name = 'اطلاعات تکمیلی'
        verbose_name_plural = 'لیست اطلاعات تکمیلی'


class ProductTag(models.Model):
    tag = models.CharField(max_length=200, verbose_name='عنوان تگ')

    def __str__(self):
        return f'{self.tag}'

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, verbose_name='دسته بندی')
    product_information = models.OneToOneField(ProductInformation, on_delete=models.CASCADE, null=True, blank=True,
                                               related_name='product_info', verbose_name='اطلاعات تکمیلی')
    product_tag=models.ManyToManyField(ProductTag,verbose_name='تگ محصول')


    title = models.CharField(max_length=50, verbose_name='نام محصول')
    price = models.IntegerField(verbose_name='قیمت محصول')
    description = models.CharField(max_length=300, verbose_name='توضیحات محصول')
    is_active = models.BooleanField(verbose_name='موجود/ناموجود بودن محصول')
    ratings = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)],
                                  verbose_name='امتیاز محصول')
    slug = models.SlugField(default='', unique=True, null=False, db_index=True, verbose_name='عنوان در url')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return f'{self.title}---{self.description}---{self.price}'

    def get_absolute_url(self):
        return reverse('product-detail', args={self.slug})

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class Karbaran(models.Model):
    name = models.CharField(max_length=20)
    family = models.CharField(max_length=20)
    age = models.IntegerField()
    # emailk=models.EmailField()
    is_active = models.BooleanField()
