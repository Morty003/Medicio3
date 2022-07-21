from django.db import models
from uuid import uuid4
from os import path
from django.core.validators import RegexValidator

class Doctors(models.Model):
    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/doctors', filename)





    name = models.CharField(max_length=50, unique=True)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField(unique=True)
    desc = models.TextField(max_length=500, blank=True)
    post = models.CharField(max_length=50, unique=False)
    photo = models.ImageField(upload_to=get_file_name)
    facebook = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)




    def __str__(self):
        return f'{self.name}: {self.position}'

class Meta:
    ordering = ('position', )

class Services(models.Model):
    icon = (
        ("fas fa-heartbeat", 'Cardiology'),
        ("fas fa-pills", 'Pills'),
        ("fas fa-hospital-user", 'Hospital'),
        ("fas fa-dna", 'DNA-TEST'),
        ("fas fa-wheelchair", 'Disabled-person'),
        ("fas fa-notes-medical", 'Appointments'),
        ("fas fa-thermometer", 'Thermometer'),



    )



    name = models.CharField(max_length=50, unique=True)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField(unique=True)
    desc = models.TextField(max_length=500, blank=True)
    icons = models.CharField(choices=icon, max_length=50)


class UserReservation(models.Model):
    # mobile_regex = RegexValidator(regex='^(\d{3}[- .]?){2}\d{4}$', message='Phone format in xxx xxx xxxx')
    name = models.CharField(max_length=50, unique=True, db_index=True)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=15)
    message = models.TextField(max_length=500, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)


    class Meta:
        ordering = ('-date',)


    def __str__(self):
        return f'{self.name}, {self.phone}: {self.message[:30]}'


class Pricing(models.Model):
    position = (
        ("col-lg-3 col-md-6", '1'),
        ("col-lg-3 col-md-6 mt-4 mt-md-0", '2'),
        ("col-lg-3 col-md-6 mt-4 mt-lg-0", '3'),
        ("col-lg-3 col-md-6 mt-4 mt-lg-0", '4'),
    )

    cross_out = (
        ('class=na', 'Yes'),
        ('', 'No'),
    )


    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    positions = models.CharField(choices=position, max_length=50)
    option_1 = models.CharField(max_length=50)
    option_2 = models.CharField(max_length=50)
    option_3 = models.CharField(max_length=50)
    option_4 = models.CharField(max_length=50)
    option_5 = models.CharField(max_length=50)
    cross_out_option_1 = models.CharField(choices=cross_out, max_length=50, blank=True)
    cross_out_option_2 = models.CharField(choices=cross_out, max_length=50, blank=True)
    cross_out_option_3 = models.CharField(choices=cross_out, max_length=50, blank=True)
    cross_out_option_4 = models.CharField(choices=cross_out, max_length=50, blank=True)
    cross_out_option_5 = models.CharField(choices=cross_out, max_length=50, blank=True)
    is_visible = models.BooleanField(default=True)




class Departaments(models.Model):
    def get_file_name2(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/departments', filename)


    name = models.CharField(max_length=50, unique=True, db_index=True)
    small_desc = models.TextField(max_length=150, blank=True)
    desc = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to=get_file_name2)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField(unique=True)

class About_Us(models.Model):
    def get_file_name3(self, filename: str):
        ext = filename.strip().strip('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/about_us', filename)


    desc = models.CharField(max_length=300, blank=True)
    photo = models.ImageField(upload_to=get_file_name3)
    small_desc = models.CharField(max_length=200, blank=True)
    option_1 = models.CharField(max_length=200)
    option_2 = models.CharField(max_length=200)
    option_3 = models.CharField(max_length=200)
    big_desc = models.TextField(max_length=500)


class Awards(models.Model):
    award = models.PositiveIntegerField(default=0)


class Questions(models.Model):
    position = (
        ("faq1", '1'),
        ("faq2", '2'),
        ("faq3", '3'),
        ("faq4", '4'),
        ("faq5", '5'),
        ("faq6", '6'),
        ("faq7", '7'),
        ("faq8", '8'),




    )


    name = models.CharField(max_length=200)
    desc = models.TextField(max_length=500)
    position = models.CharField(choices=position, max_length=50)
    is_visible = models.BooleanField(default=True)


class Info(models.Model):
    address = models.CharField(max_length=70)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=200)
    facebook = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)


class Contact(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    email = models.EmailField(max_length=250)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=500, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)



    class Meta:
        ordering = ('-date',)


    def __str__(self):
        return f'{self.name}, {self.subject}: {self.message[:30]}'


class Features(models.Model):
    def get_file_name4(self, filename: str):
        ext = filename.strip().strip('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/features', filename)


    icon = (
        ("fas fa-heartbeat", 'Cardiology'),
        ("fas fa-pills", 'Pills'),
        ("fas fa-hospital-user", 'Hospital'),
        ("fas fa-dna", 'DNA-TEST'),
        ("fas fa-wheelchair", 'Disabled-person'),
        ("fas fa-notes-medical", 'Appointments'),
        ("fas fa-thermometer", 'Thermometer'),
        ("bx bx-receipt", 'Receipt'),
        ("bx bx-cube-alt", 'Cube'),
        ("bx bx-images", 'Images'),
        ("bx bx-shield", 'Shield'),
    )


    name = models.CharField(max_length=25)
    desc = models.CharField(max_length=120)
    icon = models.CharField(choices=icon, max_length=50)


class Testimonials(models.Model):
    def get_file_name5(self, filename: str):
        ext = filename.strip().strip('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/testimonials', filename)

    desc = models.CharField(max_length=150)
    photo = models.ImageField(upload_to=get_file_name5)
    name = models.CharField(max_length=50)
    post = models.CharField(max_length=50)



