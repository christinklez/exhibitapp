# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-12-10 22:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('short_title', models.CharField(blank=True, max_length=255)),
                ('blockquote', models.CharField(blank=True, max_length=512)),
                ('byline', models.TextField(blank=True, help_text='Curator name(s) and titles, Any other collaborators, Institutional affiliation, Date of publication', verbose_name='Credits')),
                ('byline_render_as', models.CharField(choices=[('H', 'HTML'), ('T', 'Plain Text'), ('M', 'Markdown')], default='H', max_length=1, verbose_name='Render credits as')),
                ('curator', models.TextField()),
                ('copyright_year', models.IntegerField()),
                ('copyright_holder', models.TextField()),
                ('overview', models.TextField(blank=True, verbose_name='Exhibit Overview')),
                ('render_as', models.CharField(choices=[('H', 'HTML'), ('T', 'Plain Text'), ('M', 'Markdown')], default='H', max_length=1)),
                ('publish', models.BooleanField(default=False, verbose_name='Ready for publication?')),
                ('color', models.CharField(blank=True, max_length=20)),
                ('scraped_from', models.CharField(blank=True, max_length=250)),
                ('hero', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Hero Image')),
                ('lockup_derivative', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Lockup Image')),
                ('alternate_lockup_derivative', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Alternate Lockup Image')),
                ('item_id', models.CharField(blank=True, max_length=200)),
                ('hero_first', models.BooleanField(default=False, verbose_name='Use hero for lockups?')),
                ('meta_description', models.CharField(blank=True, max_length=255)),
                ('meta_keywords', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ExhibitItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=200)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('lesson_plan_order', models.IntegerField(blank=True, null=True)),
                ('historical_essay_order', models.IntegerField(blank=True, null=True)),
                ('publish', models.BooleanField(default=True, verbose_name='Ready for publication?')),
                ('essay', models.TextField(blank=True, verbose_name='Item-level exhibit information')),
                ('render_as', models.CharField(choices=[('H', 'HTML'), ('T', 'Plain Text'), ('M', 'Markdown')], default='T', max_length=1)),
                ('custom_crop', models.ImageField(blank=True, null=True, upload_to='uploads/custom_item_crop/')),
                ('custom_metadata', models.TextField(blank=True, verbose_name='Custom metadata')),
                ('metadata_render_as', models.CharField(choices=[('H', 'HTML'), ('T', 'Plain Text'), ('M', 'Markdown')], default='M', max_length=1)),
                ('custom_link', models.CharField(blank=True, max_length=512)),
                ('custom_title', models.CharField(blank=True, max_length=512)),
                ('lat', models.FloatField(default=37.8086906)),
                ('lon', models.FloatField(default=-122.2675416)),
                ('place', models.CharField(blank=True, max_length=512)),
                ('exact', models.BooleanField(default=False)),
                ('exhibit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exhibits.Exhibit')),
            ],
        ),
        migrations.CreateModel(
            name='ExhibitTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(blank=True, null=True)),
                ('exhibit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exhibits.Exhibit')),
            ],
            options={
                'verbose_name': 'Exhibit',
            },
        ),
        migrations.CreateModel(
            name='HistoricalEssay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('hero', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Hero Image')),
                ('lockup_derivative', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Lockup Image')),
                ('alternate_lockup_derivative', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Alternate Lockup Image')),
                ('item_id', models.CharField(blank=True, max_length=200)),
                ('hero_first', models.BooleanField(default=False, verbose_name='Use hero for lockups?')),
                ('blockquote', models.CharField(blank=True, max_length=200)),
                ('essay', models.TextField(blank=True)),
                ('render_as', models.CharField(choices=[('H', 'HTML'), ('T', 'Plain Text'), ('M', 'Markdown')], default='H', max_length=1)),
                ('byline', models.TextField(blank=True, help_text='Curator name(s) and titles, Any other collaborators, Institutional affiliation, Date of publication', verbose_name='Credits')),
                ('byline_render_as', models.CharField(choices=[('H', 'HTML'), ('T', 'Plain Text'), ('M', 'Markdown')], default='H', max_length=1, verbose_name='Render credits as')),
                ('curator', models.TextField()),
                ('copyright_year', models.IntegerField()),
                ('copyright_holder', models.TextField()),
                ('go_further', models.TextField(blank=True)),
                ('go_further_render_as', models.CharField(choices=[('H', 'HTML'), ('T', 'Plain Text'), ('M', 'Markdown')], default='H', max_length=1, verbose_name='Render as')),
                ('publish', models.BooleanField(default=False, verbose_name='Ready for publication?')),
                ('color', models.CharField(blank=True, help_text='Please provide color in <code>#xxx</code>, <code>#xxxxxx</code>, <code>rgb(xxx,xxx,xxx)</code>, or <code>rgba(xxx,xxx,xxx,x.x)</code> formats.', max_length=20)),
                ('meta_description', models.CharField(blank=True, max_length=255)),
                ('meta_keywords', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalEssayExhibit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(blank=True, null=True)),
                ('exhibit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exhibits.Exhibit')),
                ('historicalEssay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exhibits.HistoricalEssay')),
            ],
            options={
                'verbose_name': 'Historical Essay',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalEssayTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(blank=True, null=True)),
                ('historicalEssay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exhibits.HistoricalEssay')),
            ],
            options={
                'verbose_name': 'Historical Essay',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='LessonPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('sub_title', models.CharField(blank=True, max_length=512)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('lockup_derivative', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Lockup Image')),
                ('item_id', models.CharField(blank=True, max_length=200)),
                ('overview', models.TextField(blank=True)),
                ('render_as', models.CharField(choices=[('H', 'HTML'), ('T', 'Plain Text'), ('M', 'Markdown')], default='H', max_length=1)),
                ('lesson_plan', models.CharField(blank=True, max_length=255, verbose_name='Lesson Plan File URL')),
                ('grade_level', models.CharField(blank=True, max_length=200)),
                ('byline', models.TextField(blank=True, help_text='Curator name(s) and titles, Any other collaborators, Institutional affiliation, Date of publication', verbose_name='Credits')),
                ('byline_render_as', models.CharField(choices=[('H', 'HTML'), ('T', 'Plain Text'), ('M', 'Markdown')], default='H', max_length=1, verbose_name='Render credits as')),
                ('curator', models.TextField()),
                ('copyright_year', models.IntegerField()),
                ('copyright_holder', models.TextField()),
                ('publish', models.BooleanField(default=False, verbose_name='Ready for publication?')),
                ('meta_description', models.CharField(blank=True, max_length=255)),
                ('meta_keywords', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LessonPlanExhibit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(blank=True, null=True)),
                ('exhibit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exhibits.Exhibit')),
                ('lessonPlan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exhibits.LessonPlan')),
            ],
            options={
                'verbose_name': 'Lesson Plan',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='LessonPlanTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(blank=True, null=True)),
                ('lessonPlan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exhibits.LessonPlan')),
            ],
            options={
                'verbose_name': 'Lesson Plan',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='NotesItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('essay', models.TextField(blank=True, verbose_name='Note')),
                ('render_as', models.CharField(choices=[('H', 'HTML'), ('T', 'Plain Text'), ('M', 'Markdown')], default='T', max_length=1)),
                ('exhibit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exhibits.Exhibit')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('sort_title', models.CharField(blank=True, max_length=200, verbose_name='Sortable Title')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('color', models.CharField(blank=True, max_length=20)),
                ('byline', models.TextField(blank=True, help_text='Curator name(s) and titles, Any other collaborators, Institutional affiliation, Date of publication', verbose_name='Credits')),
                ('byline_render_as', models.CharField(choices=[('H', 'HTML'), ('T', 'Plain Text'), ('M', 'Markdown')], default='H', max_length=1, verbose_name='Render credits as')),
                ('curator', models.TextField()),
                ('copyright_year', models.IntegerField()),
                ('copyright_holder', models.TextField()),
                ('essay', models.TextField(blank=True, verbose_name='Theme overview')),
                ('render_as', models.CharField(choices=[('H', 'HTML'), ('T', 'Plain Text'), ('M', 'Markdown')], default='H', max_length=1)),
                ('hero', models.ImageField(blank=True, upload_to='uploads/', verbose_name='Hero Image')),
                ('lockup_derivative', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Lockup Image')),
                ('alternate_lockup_derivative', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Alternate Lockup Image')),
                ('item_id', models.CharField(blank=True, max_length=200)),
                ('hero_first', models.BooleanField(default=False, verbose_name='Use hero for lockups?')),
                ('publish', models.BooleanField(default=False, verbose_name='Ready for publication?')),
                ('meta_description', models.CharField(blank=True, max_length=255)),
                ('meta_keywords', models.CharField(blank=True, max_length=255)),
                ('category', models.CharField(blank=True, choices=[('cal-history', 'California History'), ('cal-cultures', 'California Cultures'), ('jarda', 'JARDA')], max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='lessonplantheme',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exhibits.Theme'),
        ),
        migrations.AddField(
            model_name='historicalessaytheme',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exhibits.Theme'),
        ),
        migrations.AddField(
            model_name='exhibittheme',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exhibits.Theme'),
        ),
        migrations.AddField(
            model_name='exhibititem',
            name='historical_essay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exhibits.HistoricalEssay'),
        ),
        migrations.AddField(
            model_name='exhibititem',
            name='lesson_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exhibits.LessonPlan'),
        ),
        migrations.AlterUniqueTogether(
            name='lessonplantheme',
            unique_together=set([('lessonPlan', 'theme')]),
        ),
        migrations.AlterUniqueTogether(
            name='lessonplanexhibit',
            unique_together=set([('exhibit', 'lessonPlan')]),
        ),
        migrations.AlterUniqueTogether(
            name='historicalessaytheme',
            unique_together=set([('historicalEssay', 'theme')]),
        ),
        migrations.AlterUniqueTogether(
            name='historicalessayexhibit',
            unique_together=set([('exhibit', 'historicalEssay')]),
        ),
        migrations.AlterUniqueTogether(
            name='exhibittheme',
            unique_together=set([('exhibit', 'theme')]),
        ),
    ]
