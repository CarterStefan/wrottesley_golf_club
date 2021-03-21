# Generated by Django 3.1.6 on 2021-03-20 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210317_2021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blog_content',
            new_name='blog_content_one',
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_content_two',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='second_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='sub_title_one',
            field=models.CharField(default='Subtitle', max_length=300, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='sub_title_two',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]