# Generated by Django 4.2.2 on 2023-07-06 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0003_feedback_alter_testimonial_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='name',
        ),
        migrations.AddField(
            model_name='testimonial',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=200),
        ),
    ]
