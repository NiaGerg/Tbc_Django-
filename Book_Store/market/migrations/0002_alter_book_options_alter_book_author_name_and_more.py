# Generated by Django 5.0.4 on 2024-04-11 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.AlterField(
            model_name='book',
            name='author_name',
            field=models.CharField(max_length=100, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(max_length=50, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='book_images/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='book',
            name='page_count',
            field=models.IntegerField(verbose_name='Page Count'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price'),
        ),
    ]
