# Generated by Django 4.0.5 on 2022-07-12 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilesAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.FileField(upload_to='meadia')),
                ('t', models.CharField(max_length=50)),
            ],
        ),
    ]
