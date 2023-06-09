# Generated by Django 4.1.4 on 2023-02-08 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=3)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
