from django.db import models

# Create your models here.
class farmdata(models.Model):
	humidity = models.CharField(max_length=128)
	temparature = models.CharField(max_length=128)
	time = models.DateTimeField( auto_now=True)
	def __str__(self):
		return str(self.time.strftime("%d%m%Y - %H:%M:%S"))
