from django.db import models

class Staff(models.Model):
	Sex = (("Female","Female"),("Male","Male"))
	first_name = models.CharField(max_length = 40)
	lust_name = models.CharField(max_length = 40)
	age = models.IntegerField(max_length = 3)
	sex = models.CharField(max_length = 7,choices = Sex, default = "Male")
	salary = models.IntegerField()
	position = models.CharField(max_length = 50)
	def __str__(self):
		return self.first_name + " " + self.lust_name
		



