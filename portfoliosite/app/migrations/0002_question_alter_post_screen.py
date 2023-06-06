# Generated by Django 4.2.1 on 2023-06-05 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='screen',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
