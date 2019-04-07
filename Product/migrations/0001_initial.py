<<<<<<< HEAD
# Generated by Django 2.1.7 on 2019-04-07 14:51
=======
# Generated by Django 2.1.7 on 2019-04-07 16:46
>>>>>>> c7ba35879c6a5d3e7539c72145a31f6b677ae9f3

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stock', models.PositiveIntegerField()),
                ('profileImage', models.ImageField(upload_to='static/product_img')),
                ('Description', models.TextField()),
                ('Discount', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='singleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name_plural': 'zimageContainer',
            },
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Product.Product')),
                ('quantity', models.PositiveIntegerField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='singleimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.Category'),
        ),
        migrations.AddField(
            model_name='cart',
            name='container',
            field=models.ManyToManyField(to='Product.Container'),
        ),
    ]
