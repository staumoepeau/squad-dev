from django.db import models


class Robot(models.Model):
	name = models.CharField(max_length=100)
	host = models.CharField(max_length=100)
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=50)
	serial_no = models.CharField(max_length=100)
	status = models.CharField(max_length=10)
	is_delete = models.BooleanField(default=False)

	def __str__(self):
		return str(self.name)