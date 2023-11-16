# Generated by Django 4.2.7 on 2023-11-13 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_alter_profile_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100)),
                ('group_description', models.TextField(max_length=400)),
                ('img', models.ImageField(upload_to='media')),
                ('profiles', models.ManyToManyField(to='users.profile')),
            ],
        ),
    ]