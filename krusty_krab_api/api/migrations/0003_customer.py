# Generated by Django 3.2.8 on 2021-10-26 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('order_number', models.IntegerField()),
                ('order_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
