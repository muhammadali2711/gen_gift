# Generated by Django 4.0.6 on 2023-01-14 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg_bot', '0009_rename_age_agee'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]