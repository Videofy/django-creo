# Generated by Django 2.1.2 on 2019-01-09 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creo', '0037_delete_testers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postsubmission',
            name='post_type',
            field=models.IntegerField(choices=[(0, 'Image'), (1, 'Video'), (2, 'Audio')]),
        ),
    ]