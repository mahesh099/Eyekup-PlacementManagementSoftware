# Generated by Django 3.2.4 on 2021-06-26 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0023_alter_company_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(null=True, upload_to='media/img'),
        ),
    ]