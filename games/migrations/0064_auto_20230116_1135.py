# Generated by Django 2.2.12 on 2023-01-16 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0063_auto_20230114_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installer',
            name='draft',
            field=models.BooleanField(default=False),
        ),
    ]