# Generated by Django 4.0 on 2021-12-29 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='quiz',
            name='correct_answer',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='name',
            field=models.CharField(max_length=40, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='tags',
            field=models.CharField(max_length=40, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='wrong_choice',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question',
            field=models.TextField(null=True),
        ),
    ]
