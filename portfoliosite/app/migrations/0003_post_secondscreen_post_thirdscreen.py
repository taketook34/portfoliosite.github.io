# Generated by Django 4.2.1 on 2023-06-05 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_question_alter_post_screen'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='secondscreen',
            field=models.ImageField(null=True, upload_to='photos/'),
        ),
        migrations.AddField(
            model_name='post',
            name='thirdscreen',
            field=models.ImageField(null=True, upload_to='photos/'),
        ),
    ]
