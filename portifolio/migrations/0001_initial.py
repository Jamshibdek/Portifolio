# Generated by Django 4.1.5 on 2024-06-18 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='about_imgs/')),
                ('name', models.CharField(max_length=100)),
                ('profile', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=13)),
                ('about', models.TextField()),
                ('html', models.IntegerField()),
                ('css', models.IntegerField()),
                ('javascript', models.IntegerField()),
                ('bootstrap', models.IntegerField()),
                ('python', models.IntegerField()),
                ('django', models.IntegerField()),
                ('drf', models.IntegerField()),
            ],
        ),
    ]