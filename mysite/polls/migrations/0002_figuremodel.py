# Generated by Django 3.0.4 on 2020-03-31 07:40

from django.db import migrations, models
import django_matplotlib.fields


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FigureModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_plot', django_matplotlib.fields.MatplotlibFigureField()),
                ('sine_plot', django_matplotlib.fields.MatplotlibFigureField()),
                ('imshow_demo', django_matplotlib.fields.MatplotlibFigureField()),
                ('with_args', django_matplotlib.fields.MatplotlibFigureField()),
                ('countour_plot', django_matplotlib.fields.MatplotlibFigureField()),
            ],
        ),
    ]
