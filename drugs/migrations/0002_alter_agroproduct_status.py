# Generated by Django 5.1.6 on 2025-02-24 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agroproduct',
            name='status',
            field=models.CharField(choices=[('DRUG', 'Drug'), ('FERTILIZER', 'Fertilizer'), ('NOT_INCLUDED', 'not_included')], default='NOT_INCLUDED', max_length=12),
        ),
    ]
