# Generated by Django 2.1.2 on 2018-12-27 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creo', '0017_commentpost_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentpost',
            name='title',
        ),
        migrations.DeleteModel(
            name='CommentPost',
        ),
    ]