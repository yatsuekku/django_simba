from django.db import models
from django.utils import timezone

class Address(models.Model):
	city = models.TextField()
	postal_code = models.CharField(max_length=6)
	street = models.TextField()
	home_nr = models.CharField(max_length=5)
	apartment_no = models.CharField(max_length=4)

	def __str__(self):
		return (str(self.postal_code) + " " + str(self.city) + " " + str(self.street) + " " +
		str(self.home_nr) + "/" + str(self.apartment_no))

class Office(models.Model):
	name = models.TextField()
	address = models.ForeignKey(
		'Address',on_delete=models.CASCADE)
	def __str__(self):
		return self.name

class Person(models.Model):
	PESEL = models.CharField(max_length=11)
	name = models.TextField()
	surname = models.TextField()
	date_of_birth = models.DateTimeField(
		blank=True,null=True)

	def __str__(self):
		return self.PESEL

class Company(models.Model):
	company_name = models.TextField()
	REGON = models.CharField(max_length=9,primary_key=True)

	def __str__(self):
		return self.company_name

class Type_of_car(models.Model):
	name = models.TextField(primary_key=True)

	def __str__(self):
		return self.name

class Car_brand(models.Model):
	brand_name = models.TextField(primary_key=True)

	def __str__(self):
		return self.brand_name

class Car_model(models.Model):
	model_name = models.TextField()
	type_name = models.ForeignKey(
		'Car_brand',on_delete=models.CASCADE)

	def __str__(self):
		return self.model_name

class Car_const(models.Model):
	VIN = models.CharField(max_length=17)
	car_type = models.ForeignKey(
		'Type_of_car',on_delete=models.CASCADE)
	car_brand = models.ForeignKey(
		'Car_brand',on_delete=models.CASCADE)
	car_model = models.ForeignKey(
		'Car_model',on_delete=models.CASCADE)
	year = models.PositiveSmallIntegerField()
	description = models.TextField(null=True)
	def __str__(self):
		return self.VIN

class Car_var(models.Model):

	insert_date = models.DateTimeField(
			blank=True, null=True)
	const_vin = models.ForeignKey(
		'Car_const',on_delete=models.CASCADE)
	owner = models.ForeignKey(
		'Person',on_delete=models.CASCADE)
	#co_owner = models.ForeignKey(
	#	'Person',on_delete=models.CASCADE) # It should be optional.
	registration_no = models.CharField(max_length=10)

	def __str__(self):
		return str(self.const_vin) + "||" + str(self.insert_date)

class Car_application(models.Model):
	REGISTER = 1
	UNREGISTER = 2
	TEMP_REGISTER = 3
	CHOICES = (
		(REGISTER,'Register'),
		(UNREGISTER,'Unregister'),
		(TEMP_REGISTER,'Temporary Register'),
	)
	case = models.PositiveSmallIntegerField(choices=CHOICES)
	applicant_private = models.ForeignKey(
		'Person',on_delete=models.CASCADE,blank=True,null=True)
	applicant_company = models.ForeignKey(
		'Company',on_delete=models.CASCADE,blank=True,null=True)
	creation_time = models.DateTimeField(auto_now=True)
	application_date = models.DateField()
	application_place= models.TextField()
	office = models.ForeignKey(
		'Office',on_delete=models.CASCADE)
	owner_address = models.ForeignKey(
		'Address',on_delete=models.CASCADE)
	car = models.ForeignKey(
		'Car_var',on_delete=models.CASCADE)
	attachment_no_1 = models.TextField(blank = True)
	attachment_no_2 = models.TextField(blank = True)
	attachment_no_3 = models.TextField(blank = True)
	attachment_no_4 = models.TextField(blank = True)
	attachment_no_5 = models.TextField(blank = True)
	attachment_no_6 = models.TextField(blank = True)

	def __str__(self):
		return ( str(self.case) + " " + str(self.applicant_private) + " " + str(self.applicant_company) +
		str(self.car) )

	#Something something
# Create your models here.
