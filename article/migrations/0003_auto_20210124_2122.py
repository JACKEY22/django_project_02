# Generated by Django 3.1.5 on 2021-01-24 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('article', '0002_article_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='article', to='shop.shop'),
        ),
    ]
