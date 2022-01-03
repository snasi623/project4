# Generated by Django 4.0 on 2022-01-03 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0006_rename_answer_text_answer_option_a_answer_option_b_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='selected_answer',
        ),
        migrations.AddField(
            model_name='question',
            name='correct_option',
            field=models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=1),
        ),
        migrations.AddField(
            model_name='question',
            name='option_1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='option_2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='option_3',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='option_4',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Response',
        ),
    ]