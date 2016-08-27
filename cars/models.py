from django.db import models


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
        'Address', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Person(models.Model):
    PESEL = models.CharField(max_length=11)
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    date_of_birth = models.DateTimeField(
        blank=True, null=True)

    def __str__(self):
        return self.PESEL


class Company(models.Model):
    company_name = models.TextField()
    REGON = models.CharField(max_length=9, primary_key=True)

    def __str__(self):
        return self.company_name


class Car(models.Model):
    insert_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    owner = models.ForeignKey('Person', on_delete=models.CASCADE)
    registration_no = models.CharField(max_length=10)
    vin = models.CharField(max_length=17)
    model = models.CharField(max_length=25)
    brand = models.CharField(unique=True, max_length=25)
    type = models.CharField(unique=True, max_length=25)
    year = models.PositiveSmallIntegerField()
    description = models.TextField(null=True)

    def __str__(self):
        return str(self.vin) + "||" + str(self.insert_date)


class CarApplication(models.Model):
    REGISTER = 1
    UNREGISTER = 2
    TEMP_REGISTER = 3
    CHOICES = (
        (REGISTER, 'Register'),
        (UNREGISTER, 'Unregister'),
        (TEMP_REGISTER, 'Temporary Register'),
    )
    case = models.PositiveSmallIntegerField(choices=CHOICES)
    applicant_private = models.ForeignKey(
        'Person', on_delete=models.CASCADE, blank=True, null=True)
    applicant_company = models.ForeignKey(
        'Company', on_delete=models.CASCADE, blank=True, null=True)
    creation_time = models.DateTimeField(auto_now=True)
    application_date = models.DateField()
    application_place = models.TextField()
    office = models.ForeignKey(
        'Office', on_delete=models.CASCADE)
    owner_address = models.ForeignKey(
        'Address', on_delete=models.CASCADE)
    car = models.ForeignKey(
        'Car', on_delete=models.CASCADE)
    # DRY - Don't repeat yourself
    attachment_no_1 = models.TextField(blank=True)
    attachment_no_2 = models.TextField(blank=True)
    attachment_no_3 = models.TextField(blank=True)
    attachment_no_4 = models.TextField(blank=True)
    attachment_no_5 = models.TextField(blank=True)
    attachment_no_6 = models.TextField(blank=True)

    def __str__(self):
        return (str(self.case) + " " + str(self.applicant_private) + " " + str(self.applicant_company) +
                str(self.car))
