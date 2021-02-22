from django.db import models
from django.urls import reverse

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Course(models.Model):
	name = models.CharField('Kurs nomi', max_length=150)
	time = models.CharField('Kurs vaqti', max_length=50)
	image = models.ImageField(upload_to='course_images/')
	price = models.PositiveIntegerField('Narxi', default=0)
	student_age = models.CharField('Talabalar yosh chegarasi', max_length=50)
	size = models.CharField('Talabalar soni', max_length=50)
	teacher = models.CharField('Ustoz', max_length=150)
	duration = models.CharField('Davom etish vaqti', max_length=50, blank=True)

	class  Meta:
		verbose_name = 'Kurs'
		verbose_name_plural = 'Kurslar'

	def __str__(self):
		return "Kurs nomi {}".format(self.name)

class Contact(models.Model):
	name = models.CharField('Ismi', max_length=50)
	email = models.EmailField('Email', max_length=250)
	message = models.TextField('Xabar',)

	class  Meta:
		verbose_name = 'Aloqa'
		verbose_name_plural = 'Aloqalar'

	def __str__(self):
		return f"{self.name}"




class Categories(models.Model):
	name = models.CharField('Kategoriya nomi', max_length=70)
	slug = models.SlugField('*', max_length=50, unique=True, db_index=True)

	class Meta:
		verbose_name = 'Kategoriya'
		verbose_name_plural = 'Kategoriyalar'

	def __str__(self):
		return f"{self.name}"


class Tag(models.Model):
	name = models.CharField('Tag nomi', max_length=70)
	slug = models.SlugField('*', max_length=50, unique=True, db_index=True)

	class Meta:
		verbose_name = 'Tag'
		verbose_name_plural = 'Taglar'

	def __str__(self):
		return f"{self.name}"


class Post(models.Model):
	title = models.CharField('Maqola nomi', max_length=250)
	slug = models.SlugField('*',max_length=100, unique=True, db_index=True)
	image = models.ImageField('rasmi', upload_to='post_poster/')
	body = RichTextField()
	category = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True, null=True)
	tag = models.ForeignKey(Tag,on_delete=models.PROTECT, blank=True, null=True)
	author = models.CharField('Muallif', default='Admin',max_length=100, blank=True)
	published = models.DateTimeField("Qo'shilgan vaqti", auto_now_add=True)
	most_read = models.BooleanField(default=False)
	top = models.BooleanField(default=False)


	class Meta:
		verbose_name = 'Maqola'
		verbose_name_plural = 'Maqolalar'

	def get_absolute_url(self):
		return reverse('main:blogDetailPage', kwargs={'post_slug':self.slug})

	def __str__(self):
		return f"{self.title}"


class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
	name = models.CharField('Ismi', max_length=50)
	email = models.EmailField('Email', max_length=250)
	subject = models.CharField('Mavzudi', max_length=250)
	message = models.TextField('Xabar',)

	class  Meta:
		verbose_name = 'Muhokama'
		verbose_name_plural = 'Muhokamalar'

	def __str__(self):
		return f"{self.name}"

class Register(models.Model):
	CHOICES = (
		('Python','python'),
		('Javascript','javascript'),
		('C++','cpp'),
		('C#','csharp'),
		('Ruby','ruby'),
		('Flutter','flutter'),
		)
	name = models.CharField('Ism-Familya', max_length=50)
	email = models.EmailField()
	course = models.CharField('Tanlagan kursi', max_length=50, choices=CHOICES)
	message = models.TextField("Qo'shimcha xabar")

	class  Meta:
		verbose_name = "A'zo bo'lish"
		verbose_name_plural = "A'zo bo'lganlar"

	def __str__(self):
		return f"{self.name}"