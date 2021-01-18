# Generated by Django 3.1.5 on 2021-01-11 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Вид')),
                ('task', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Какой бывает шоколад',
                'verbose_name_plural': 'Виды',
            },
        ),
    ]
