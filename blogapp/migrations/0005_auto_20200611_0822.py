# Generated by Django 3.0.7 on 2020-06-11 08:22

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('blogapp', '0004_auto_20200611_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloggallery',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='bloggallery',
            name='page',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gallery_images', to='blogapp.BlogPage'),
        ),
    ]
