# Generated by Django 3.1 on 2020-08-18 20:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Anonymous', max_length=200, null=True)),
                ('website', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('link', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('created_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('show', models.BooleanField(blank=True, default=True, null=True)),
                ('image', models.CharField(blank=True, default='https://res.cloudinary.com/raghavdhingra/image/upload/v1574935065/pc_bg9yoh.jpg', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Anonymous', max_length=200, null=True)),
                ('image', models.CharField(blank=True, default='https://res.cloudinary.com/raghavdhingra/image/upload/v1574788770/img_k2mozj.png', max_length=500, null=True)),
                ('created_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('show', models.BooleanField(blank=True, default=True, null=True)),
                ('user_desc', models.CharField(blank=True, default='Customer', max_length=200, null=True)),
                ('testimonial', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]
