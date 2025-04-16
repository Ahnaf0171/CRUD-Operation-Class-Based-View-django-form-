# Generated by Django 5.2 on 2025-04-15 13:33

import gadget.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gadgets',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('SAMSUNG', 'SAMSUNG'), ('OPPO', 'OPPO'), ('REDMI', 'REDMI'), ('VIVO', 'VIVO')], max_length=50)),
                ('picture', models.ImageField(upload_to=gadget.models.add_image)),
                ('price', models.IntegerField()),
                ('about', models.CharField(max_length=500)),
                ('agree', models.BooleanField()),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
