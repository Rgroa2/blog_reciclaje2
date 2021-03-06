# Generated by Django 4.0 on 2021-12-13 03:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('img', models.ImageField(blank=True, help_text='Seleccione una imagen para mostrar', null=True, upload_to='img/portfolio')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('categories', models.ManyToManyField(related_name='posts', to='ablog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('comment_body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved_comment', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ablog.post')),
            ],
        ),
    ]
