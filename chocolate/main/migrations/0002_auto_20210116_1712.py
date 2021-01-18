# Generated by Django 3.1.5 on 2021-01-16 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Название')),
                ('place', models.TextField(verbose_name='Расположение')),
            ],
            options={
                'verbose_name': 'Фабрики',
                'verbose_name_plural': 'Фабрики',
            },
        ),
        migrations.AlterModelOptions(
            name='types',
            options={'verbose_name': 'Шоколад', 'verbose_name_plural': 'Виды'},
        ),
        migrations.AddField(
            model_name='types',
            name='factory',
            field=models.ManyToManyField(related_name='Types_Factory', to='main.Factory', verbose_name='Шоколад'),
        ),
    ]
