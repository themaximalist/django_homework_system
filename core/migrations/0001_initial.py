# Generated by Django 3.2.5 on 2021-07-16 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeWorks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='uploaded_files/teachers_quiz/')),
                ('is_enable', models.BooleanField(default=True)),
                ('student', models.ManyToManyField(limit_choices_to={'user_type': 1}, related_name='student_user', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(limit_choices_to={'user_type': 2}, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveSmallIntegerField()),
                ('homework', models.ManyToManyField(limit_choices_to={'is_enable': True}, to='core.HomeWorks')),
            ],
        ),
        migrations.CreateModel(
            name='HomeWorkUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploaded_files/students_answers/')),
                ('homework', models.ManyToManyField(limit_choices_to={'is_enable': True}, to='core.HomeWorks')),
                ('student', models.ForeignKey(limit_choices_to={'user_type': 1}, on_delete=django.db.models.deletion.CASCADE, related_name='student_user_upload', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]