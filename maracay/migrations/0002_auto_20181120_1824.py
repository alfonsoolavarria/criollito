# Generated by Django 2.0.3 on 2018-11-20 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maracay', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchasehistory',
            old_name='total',
            new_name='total_purchase',
        ),
    ]
