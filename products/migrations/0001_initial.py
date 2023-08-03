# Generated by Django 3.2.20 on 2023-07-28 11:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('sku', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField(max_length=500)),
                ('quantity', models.IntegerField()),
                ('status', models.BooleanField()),
            ],
        ),
    ]