# Generated by Django 3.2.19 on 2023-05-12 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_login_require'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(verbose_name='date_published'),
        ),
    ]
