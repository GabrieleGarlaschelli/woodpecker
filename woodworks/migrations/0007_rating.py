# Generated by Django 3.1.3 on 2020-12-22 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_liked_woodworks'),
        ('woodworks', '0006_auto_20201207_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
                ('woodwork', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='woodworks.woodwork')),
            ],
            options={
                'db_table': 'ratings',
            },
        ),
    ]