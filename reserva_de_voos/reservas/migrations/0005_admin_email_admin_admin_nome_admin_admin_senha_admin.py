# Generated by Django 5.0.3 on 2024-03-24 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0004_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='email_admin',
            field=models.EmailField(default='admin@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='admin',
            name='nome_admin',
            field=models.CharField(default='admin', max_length=100),
        ),
        migrations.AddField(
            model_name='admin',
            name='senha_admin',
            field=models.CharField(default='admin123', max_length=255),
        ),
    ]
