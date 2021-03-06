# Generated by Django 3.2 on 2022-07-10 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('image_about', models.ImageField(upload_to='about/')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('decription', models.TextField()),
                ('logo', models.ImageField(upload_to='logo/')),
                ('tel', models.CharField(max_length=255)),
                ('facebook', models.CharField(max_length=255)),
                ('twitter', models.CharField(max_length=255)),
                ('google', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Настройка',
                'verbose_name_plural': 'Настройки',
            },
        ),
    ]
