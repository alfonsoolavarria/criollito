# Generated by Django 2.0.3 on 2018-11-08 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maracay', '0004_tools'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=30)),
                ('description', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=50)),
                ('cant', models.PositiveSmallIntegerField(default=1)),
                ('category', models.PositiveSmallIntegerField(choices=[(1, 'Viveres'), (2, 'Frigorifico'), (3, 'Enlatados')])),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseConfirmation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_type', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('confirmation', models.BooleanField(default=False)),
                ('start_date', models.DateTimeField(null=True)),
                ('cant_product', models.PositiveSmallIntegerField(default=1)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='product_comprado', to='maracay.Product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_confirm', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantshopping', models.PositiveSmallIntegerField(default=0)),
                ('code', models.CharField(max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_products', to='maracay.Product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_shopping', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.AddField(
            model_name='profile',
            name='localphone',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='reference',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='rif',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='direction',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tools',
            name='costoenvio',
            field=models.PositiveSmallIntegerField(default=100),
        ),
    ]
