# Generated by Django 2.0.3 on 2018-04-22 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='作者')),
                ('age', models.IntegerField(verbose_name='年龄')),
            ],
            options={
                'verbose_name': '作者',
                'verbose_name_plural': '作者',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='app02.Author', verbose_name='作者'),
        ),
    ]
