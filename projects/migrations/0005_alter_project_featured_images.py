# Generated by Django 4.1.7 on 2023-04-04 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured_images',
            field=models.ImageField(blank=True, default='profiles/default-project.jpg', null=True, upload_to=''),
        ),
    ]
