# Generated by Django 4.2.7 on 2023-11-09 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('videos', '0002_alter_video_dislikes_alter_video_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='publishedBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]