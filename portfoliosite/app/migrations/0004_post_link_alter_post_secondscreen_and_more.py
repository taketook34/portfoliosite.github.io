# Generated by Django 4.2.1 on 2023-06-06 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_post_secondscreen_post_thirdscreen'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='secondscreen',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='thirdscreen',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
