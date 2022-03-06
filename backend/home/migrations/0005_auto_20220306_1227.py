# Generated by Django 2.2.27 on 2022-03-06 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_course_notification_wish'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Course'),
        ),
        migrations.AddField(
            model_name='notification',
            name='wish',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Wish'),
        ),
    ]