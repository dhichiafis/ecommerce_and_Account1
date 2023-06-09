# Generated by Django 4.1.7 on 2023-03-27 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=123)),
                ('slug', models.SlugField(max_length=123)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=123)),
                ('slug', models.SlugField(max_length=123)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField()),
            ],
        ),
    ]
