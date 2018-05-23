# Generated by Django 2.0.3 on 2018-04-23 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='作者')),
                ('age', models.IntegerField(default=17, verbose_name='年龄')),
            ],
            options={
                'verbose_name': '作者',
                'verbose_name_plural': '作者',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='书名')),
                ('price', models.IntegerField(default=99, verbose_name='价格')),
                ('pub_date', models.DateField(verbose_name='出版时间')),
                ('author', models.ManyToManyField(to='app03.Author', verbose_name='作者')),
            ],
            options={
                'verbose_name': '图书',
                'verbose_name_plural': '图书',
            },
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='出版社')),
                ('city', models.CharField(max_length=40, verbose_name='出版社所在城市')),
            ],
            options={
                'verbose_name': '出版社',
                'verbose_name_plural': '出版社',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='publish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app03.Publish', verbose_name='出版社'),
        ),
    ]
