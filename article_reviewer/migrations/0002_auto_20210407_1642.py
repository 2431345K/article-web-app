# Generated by Django 2.2.17 on 2021-04-07 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article_reviewer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='commentID',
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article_reviewer.UserProfile'),
        ),
    ]
