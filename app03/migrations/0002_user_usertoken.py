# Generated by Django 3.2.12 on 2022-03-30 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app03', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('user_type', models.IntegerField(choices=[(1, '管理员'), (2, '普通员工'), (3, '访客')])),
            ],
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app03.user')),
            ],
        ),
    ]