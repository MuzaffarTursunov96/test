# Generated by Django 3.0.5 on 2023-01-16 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_student_status'),
        ('exam', '0005_auto_20201209_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('file', models.FileField(upload_to='docs/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Course')),
            ],
        ),
        migrations.CreateModel(
            name='studentAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.FileField(upload_to='answer')),
                ('marks', models.PositiveIntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Course')),
                ('question_sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.QuestionSheet')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
    ]
