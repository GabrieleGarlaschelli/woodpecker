# Generated by Django 3.1.4 on 2021-01-03 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('woodworks', '0007_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='WoodworkImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('image', models.FileField(upload_to='woodworks/static/woodworks_images')),
                ('woodwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='woodworks.woodwork')),
            ],
            options={
                'db_table': 'woodwork_images',
            },
        ),
    ]
