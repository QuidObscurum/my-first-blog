from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
	"""models.Model : Post object is a Django model ->
	-> Django understands that it should save it to the DB 
	models.CharField - field type with limited qty of chars
	models.TextField - limitlessly long text field type
	models.ForeignKey - references to another model"""
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title
		