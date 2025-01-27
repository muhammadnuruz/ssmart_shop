# Generated by Django 5.0.1 on 2024-07-15 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=255, null=True)),
                ('full_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255, null=True)),
                ('language', models.CharField(choices=[('ru', 'Ru'), ('uz', 'Uz')], default='uz', max_length=2)),
                ('district', models.CharField(max_length=50, null=True)),
                ('region', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Telegram User',
                'verbose_name_plural': 'Telegram Users',
            },
        ),
    ]
