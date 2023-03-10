# Generated by Django 4.0.6 on 2022-12-28 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg_bot', '0003_rename_age_situation_human'),
    ]

    operations = [
        migrations.CreateModel(
            name='Savat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField()),
                ('slug', models.SlugField(max_length=128, null=True)),
                ('product', models.CharField(max_length=256)),
                ('amount', models.IntegerField(null=True)),
                ('priceproduct', models.CharField(max_length=128, null=True)),
                ('summ', models.IntegerField(null=True)),
                ('til', models.IntegerField(default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='cash',
        ),
        migrations.AddField(
            model_name='category',
            name='til',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='human',
            name='til',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='interests',
            name='til',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='product',
            name='til',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='situation',
            name='til',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='cash',
            name='cash',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.RemoveField(
            model_name='cash',
            name='interests',
        ),
        migrations.AddField(
            model_name='cash',
            name='interests',
            field=models.ManyToManyField(to='tg_bot.interests'),
        ),
        migrations.RemoveField(
            model_name='interests',
            name='situation',
        ),
        migrations.AddField(
            model_name='interests',
            name='situation',
            field=models.ManyToManyField(to='tg_bot.situation'),
        ),
        migrations.AlterField(
            model_name='situation',
            name='content',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='situation',
            name='human',
        ),
        migrations.AddField(
            model_name='situation',
            name='human',
            field=models.ManyToManyField(to='tg_bot.human'),
        ),
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=128, null=True)),
                ('cash', models.ManyToManyField(to='tg_bot.cash')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='age',
            field=models.ManyToManyField(to='tg_bot.age'),
        ),
    ]
