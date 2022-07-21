# Generated by Django 4.0.6 on 2022-07-20 18:45

from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(blank=True, max_length=200)),
                ('photo', models.ImageField(upload_to=main_page.models.About_Us.get_file_name3)),
                ('small_desc', models.CharField(blank=True, max_length=200)),
                ('option_1', models.CharField(max_length=200)),
                ('option_2', models.CharField(max_length=200)),
                ('option_3', models.CharField(max_length=200)),
                ('big_desc', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('email', models.EmailField(max_length=250)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField(blank=True, max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='Departaments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('small_desc', models.TextField(blank=True, max_length=100)),
                ('desc', models.TextField(blank=True, max_length=500)),
                ('photo', models.ImageField(upload_to=main_page.models.Departaments.get_file_name2)),
                ('is_visible', models.BooleanField(default=True)),
                ('position', models.PositiveSmallIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('position', models.PositiveSmallIntegerField(unique=True)),
                ('desc', models.TextField(blank=True, max_length=500)),
                ('post', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to=main_page.models.Doctors.get_file_name)),
                ('facebook', models.URLField()),
                ('linkedin', models.URLField()),
                ('instagram', models.URLField()),
                ('twitter', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('desc', models.CharField(max_length=120)),
                ('icon', models.CharField(choices=[('fas fa-heartbeat', 'Cardiology'), ('fas fa-pills', 'Pills'), ('fas fa-hospital-user', 'Hospital'), ('fas fa-dna', 'DNA-TEST'), ('fas fa-wheelchair', 'Disabled-person'), ('fas fa-notes-medical', 'Appointments'), ('fas fa-thermometer', 'Thermometer'), ('bx bx-receipt', 'Receipt'), ('bx bx-cube-alt', 'Cube'), ('bx bx-images', 'Images'), ('bx bx-shield', 'Shield')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=70)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=200)),
                ('facebook', models.URLField()),
                ('linkedin', models.URLField()),
                ('instagram', models.URLField()),
                ('twitter', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('positions', models.CharField(choices=[('col-lg-3 col-md-6', '1'), ('col-lg-3 col-md-6 mt-4 mt-md-0', '2'), ('col-lg-3 col-md-6 mt-4 mt-lg-0', '3'), ('col-lg-3 col-md-6 mt-4 mt-lg-0', '4')], max_length=50)),
                ('option_1', models.CharField(max_length=50)),
                ('option_2', models.CharField(max_length=50)),
                ('option_3', models.CharField(max_length=50)),
                ('option_4', models.CharField(max_length=50)),
                ('option_5', models.CharField(max_length=50)),
                ('cross_out_option_1', models.CharField(blank=True, choices=[('class=na', 'Yes'), ('', 'No')], max_length=50)),
                ('cross_out_option_2', models.CharField(blank=True, choices=[('class=na', 'Yes'), ('', 'No')], max_length=50)),
                ('cross_out_option_3', models.CharField(blank=True, choices=[('class=na', 'Yes'), ('', 'No')], max_length=50)),
                ('cross_out_option_4', models.CharField(blank=True, choices=[('class=na', 'Yes'), ('', 'No')], max_length=50)),
                ('cross_out_option_5', models.CharField(blank=True, choices=[('class=na', 'Yes'), ('', 'No')], max_length=50)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField(max_length=500)),
                ('position', models.CharField(choices=[('faq1', '1'), ('faq2', '2'), ('faq3', '3'), ('faq4', '4'), ('faq5', '5'), ('faq6', '6'), ('faq7', '7'), ('faq8', '8')], max_length=50)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('position', models.PositiveSmallIntegerField(unique=True)),
                ('desc', models.TextField(blank=True, max_length=500)),
                ('icons', models.CharField(choices=[('fas fa-heartbeat', 'Cardiology'), ('fas fa-pills', 'Pills'), ('fas fa-hospital-user', 'Hospital'), ('fas fa-dna', 'DNA-TEST'), ('fas fa-wheelchair', 'Disabled-person'), ('fas fa-notes-medical', 'Appointments'), ('fas fa-thermometer', 'Thermometer')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=150)),
                ('photo', models.ImageField(upload_to=main_page.models.Testimonials.get_file_name5)),
                ('name', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('email', models.EmailField(max_length=250)),
                ('phone', models.CharField(max_length=15)),
                ('message', models.TextField(blank=True, max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]