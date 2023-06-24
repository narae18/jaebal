# Generated by Django 4.2.1 on 2023-06-25 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_remove_post_num_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='somd',
            name='admins',
        ),
        migrations.RemoveField(
            model_name='somd',
            name='category',
        ),
        migrations.AlterField(
            model_name='somd',
            name='backgroundimage',
            field=models.ImageField(blank=True, default='somd/somdbackDefaultImage.png', null=True, upload_to='somd/'),
        ),
        migrations.AlterField(
            model_name='somd',
            name='profileimage',
            field=models.ImageField(blank=True, default='somd/somdDefaultImage.png', null=True, upload_to='somd/'),
        ),
    ]
