# Generated by Django 4.0.5 on 2022-07-10 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raxit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='block_unblock',
            field=models.CharField(choices=[('null', 'Null'), ('block', 'Block'), ('unblock', 'Unblock')], default='null', max_length=10),
        ),
        migrations.AlterField(
            model_name='signup',
            name='user_city',
            field=models.CharField(choices=[('null', 'Null'), ('rajkot', 'Rajkot'), ('junagadh', 'Junagadh')], default='null', max_length=200),
        ),
        migrations.AlterField(
            model_name='signup',
            name='user_country',
            field=models.CharField(choices=[('null', 'Null'), ('india', 'India'), ('austrila', 'Austrila')], default='null', max_length=200),
        ),
    ]
