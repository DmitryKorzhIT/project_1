# Generated by Django 3.2.9 on 2021-12-07 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('basket_id', models.AutoField(default=5000000000000, primary_key=True, serialize=False, verbose_name='Basket id')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Total price')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(default=2000000000000, primary_key=True, serialize=False, verbose_name='Customer id')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(default=7000000000000, primary_key=True, serialize=False, verbose_name='Product id')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(null=True, verbose_name='Description')),
                ('basket_card_description', models.CharField(max_length=350, null=True, verbose_name='Basket card description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Price')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('category_id', models.AutoField(default=8000000000000, primary_key=True, serialize=False, verbose_name='Category id')),
                ('category_name', models.CharField(default='', max_length=255, verbose_name='Category name')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(default=1000000000000, primary_key=True, serialize=False, verbose_name='User id')),
                ('role', models.BooleanField(verbose_name='Role')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('password', models.CharField(max_length=255, verbose_name='Password')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('wishlist_id', models.AutoField(default=3000000000000, primary_key=True, serialize=False, verbose_name='Wishlist id')),
                ('slug', models.SlugField(unique=True)),
                ('customer_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.customer', verbose_name='Customer id')),
            ],
        ),
        migrations.CreateModel(
            name='WishlishCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product', verbose_name='Product id')),
                ('wishlist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.wishlist', verbose_name='Wishlist id')),
            ],
        ),
        migrations.CreateModel(
            name='ProductBasketCard',
            fields=[
                ('product_basket_card_id', models.AutoField(default=6000000000000, primary_key=True, serialize=False, verbose_name='Product basket card id')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantity')),
                ('slug', models.SlugField(unique=True)),
                ('basket_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.basket', verbose_name='Basket id')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product', verbose_name='Product id')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.productcategory', verbose_name='Category id'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(default=4000000000000, primary_key=True, serialize=False, verbose_name='Order id')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Total price')),
                ('comment', models.TextField(null=True, verbose_name='Comment')),
                ('slug', models.SlugField(unique=True)),
                ('basket_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.basket', verbose_name='Basket id')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.customer', verbose_name='Customer id')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.user', verbose_name='User id'),
        ),
        migrations.AddField(
            model_name='basket',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.customer', verbose_name='Customer id'),
        ),
    ]
