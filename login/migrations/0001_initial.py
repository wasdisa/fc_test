# Generated by Django 4.2.11 on 2024-03-05 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='username')),
                ('password', models.CharField(max_length=20, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='permissions')),
            ],
        ),
    ]