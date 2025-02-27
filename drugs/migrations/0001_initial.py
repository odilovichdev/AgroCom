# Generated by Django 5.1.6 on 2025-02-24 05:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgroProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Name')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icons/', verbose_name='Icons')),
                ('status', models.CharField(choices=[('DR', 'drug'), ('FE', 'fertilizer'), ('IN', 'not_included')], default='IN', max_length=2)),
            ],
            options={
                'verbose_name': 'Drug',
                'verbose_name_plural': 'Drugs',
                'db_table': 'drug',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Name')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='AgroProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='agroProduct/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='drugs.agroproduct', verbose_name='Agro Product Image')),
            ],
            options={
                'verbose_name': 'Agro Product Image',
                'verbose_name_plural': 'Agro Product Images',
                'db_table': 'agro_product_images',
            },
        ),
        migrations.AddField(
            model_name='agroproduct',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agroProduct', to='drugs.category', verbose_name='Category'),
        ),
    ]
