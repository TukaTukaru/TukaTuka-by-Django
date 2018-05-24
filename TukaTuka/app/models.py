from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from phonenumber_field.modelfields import PhoneNumberField

class Mail(models.Model):
    email = models.EmailField(unique=True,db_index=True)
    def __str__(self):
        return f"{self.email}"
    class Meta:
         verbose_name = 'email'
         verbose_name_plural = 'emails'

class Comment(models.Model):
	rating_choice = (
        (1, "Ужасно"),
        (2, "Плохо"),
        (3, "Нормально"),
        (4, "Хорошо"),
        (5, "Отлично"),
    )

	user = models.ForeignKey(on_delete=models.CASCADE,to=settings.AUTH_USER_MODEL,blank=True, null=True)
	comment_text = models.TextField(blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(choices=rating_choice, default=0)
	content_type = models.ForeignKey(ContentType,null=True, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField(null=True)
	content_object = GenericForeignKey()


	def __str__(self):
		return f"Компания: {self.content_object}, пользователь: {self.user}, оценка: {self.rating}, дата: {self.date}"

	class Meta:
		ordering = ['-rating']
		verbose_name = 'Отзыв'
		verbose_name_plural = 'Отзывы'


class Ad(models.Model):
	name = models.CharField(max_length=200)
	price_min = models.PositiveIntegerField(blank=True, null=True)
	price_max = models.PositiveIntegerField(blank=True, null=True)
	volume = models.PositiveIntegerField(blank=True, null=True)
	position = models.CharField(blank=True, max_length=200, db_index=True)
	photo = models.ImageField(upload_to='prod_img', blank=True, verbose_name='Фото продукции')
	phone_number = PhoneNumberField()
	phone_another = PhoneNumberField(blank=True)
	company_name = models.CharField(max_length=200, db_index=True)
	company_adress = models.CharField( max_length=200, db_index=True)
	category_choice = (
        (1, "Купить вторичное сырье на переработку"),
        (2, "Купить переработанное сырье"),
        (3, "Продать вторичное сырье на переработку"),
        (4, "Продать переработанное сырье"),
    )

	category_raw = (
		(1, "ПП"),
		(2, "ПНД"),
		(3, "ПВД"),
		(4, "Стрейч"),
		(5, "ПЭТ"),
		(6, "Другое"),

	)

	category_granule = (
		(1, "Гранула ПП"),
		(2, "Гранула ПНД"),
		(3, "Гранула ПВД"),
		(4, "Гранула стрейч"),
		(5, "Другое"),

	)
	title = models.CharField(max_length=255)
	description = models.TextField()
	author = models.ForeignKey(
		on_delete=models.CASCADE, to=settings.AUTH_USER_MODEL,blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	category = models.IntegerField(choices=category_choice, default=0)
	category = models.IntegerField(choices=category_raw, default=0)
	category = models.IntegerField(choices=category_granule, default=0)


	def __str__(self):
		return f"{self.title}, дата: {self.created_at}"
	class Meta:
		verbose_name = 'Объявление'
		verbose_name_plural = 'Объявления'


class Company(models.Model):
	first_name = models.CharField(max_length=35)
	last_name = models.CharField(max_length=40)
	middle_name = models.CharField(max_length=40)
	phone_number = PhoneNumberField()
	position = models.CharField(max_length=200, db_index=True)
	company_name = models.CharField(blank=True, null=True,max_length=200, db_index=True,unique=True)
	company_type = models.CharField(max_length=20)
	company_adress = models.CharField(max_length=200, db_index=True)
	email = models.EmailField(blank=True, null=True,unique=True,db_index=True)
	site = models.URLField(blank=True, null=True)
	ad = models.ForeignKey(Ad, on_delete=models.CASCADE, null=True, blank=True)
	comment = GenericRelation(Comment)

	def __str__(self):
		return f"{self.last_name} {self.first_name}"
	class Meta:
		verbose_name = 'Компания'
		verbose_name_plural = 'Компании'

	
class RatingAd(models.Model):
	rating_choice = (
        (1, "Ужасно"),
        (2, "Плохо"),
        (3, "Нормально"),
        (4, "Хорошо"),
        (5, "Отлично"),
    )

	user = models.ForeignKey(on_delete=models.CASCADE,to=settings.AUTH_USER_MODEL,blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(choices=rating_choice, default=0)
	ad = models.ForeignKey(Ad, on_delete=models.CASCADE, null=True, blank=True)


	def __str__(self):
		return f"Объявление: {self.ad}, оценка: {self.rating}"

	class Meta:
		ordering = ['-rating']
		verbose_name = 'Оценка'
		verbose_name_plural = 'Оценки'
		
class Complaint(models.Model):
	complaint_choice = (
        (1, "Товар продан"),
        (2, "Неверное описание, фото"),
        (3, "Не дозвониться"),
        (4, "Непорядочный продавец"),
        (5, "Другая причина"),
    )

	user = models.ForeignKey(on_delete=models.CASCADE,to=settings.AUTH_USER_MODEL,blank=True, null=True)
	complaint_text = models.TextField(blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)
	complaint_type = models.IntegerField(choices=complaint_choice, default=0)
	ad = models.ForeignKey(Ad, on_delete=models.CASCADE, null=True, blank=True)


	def __str__(self):
		return f"Объявление: {self.ad}, дата: {self.date}"

	class Meta:
		
		verbose_name = 'Жалоба'
		verbose_name_plural = 'Жалобы'

class News(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	date = models.CharField(max_length=255,blank=True, null=True)
	author = models.ForeignKey(
		on_delete=models.CASCADE, to=settings.AUTH_USER_MODEL,blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	photo = models.ImageField(upload_to='images', blank=True, verbose_name='Фото новости')

	def __str__(self):
		return f"Загаловок {self.title}, дата: {self.created_at}"

	class Meta:
		ordering = ['-created_at']
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'
		
