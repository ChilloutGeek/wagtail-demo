# Generated by Django 3.0.7 on 2020-06-11 08:49

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_auto_20200611_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloggallery',
            name='page',
            field=modelcluster.fields.ParentalKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='gallery_images', to='blogapp.BlogPage'),
            preserve_default=False,
        ),
    ]