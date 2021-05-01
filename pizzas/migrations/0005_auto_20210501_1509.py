# Generated by Django 3.2 on 2021-05-01 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0004_auto_20210501_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='pizzas.pizza'),
        ),
    ]