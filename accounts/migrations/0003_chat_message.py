# Generated by Django 3.1.4 on 2021-01-01 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_liked_woodworks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('opened', 'Aperta'), ('closed', 'Chiusa')], default='opened', max_length=255)),
                ('created_at', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'chats',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('sender', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
                ('chat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.chat')),
            ],
            options={
                'db_table': 'messages',
            },
        ),
    ]
