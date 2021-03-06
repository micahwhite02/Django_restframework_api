# Generated by Django 3.2.8 on 2021-10-24 03:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PayRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.CharField(max_length=120)),
                ('transaction_id', models.UUIDField(default=uuid.uuid4)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
