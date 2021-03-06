# Generated by Django 2.2.10 on 2020-04-26 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maracay', '0003_auto_20181120_1826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='name_image',
        ),
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(default=str, upload_to='images/'),
            preserve_default=False,
        ),
    ]
