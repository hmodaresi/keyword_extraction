# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-01-14 12:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=20)),
                ('rank', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='keyword',
            name='text',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='text_parser.Text'),
        ),
        migrations.AddField(
            model_name='keyword',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='text_parser.Topic'),
        ),
        migrations.AddField(
            model_name='gameid',
            name='texts',
            field=models.ManyToManyField(to='text_parser.Text'),
        ),
    ]
