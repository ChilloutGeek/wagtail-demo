# Generated by Django 3.0.7 on 2020-06-12 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_auto_20200611_0914'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bloggallery',
            options={'ordering': ['sort_order']},
        ),
        migrations.RemoveField(
            model_name='bloggallery',
            name='page_ptr',
        ),
        migrations.AddField(
            model_name='bloggallery',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bloggallery',
            name='sort_order',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]
