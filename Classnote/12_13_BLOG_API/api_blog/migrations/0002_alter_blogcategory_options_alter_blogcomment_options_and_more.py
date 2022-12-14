# Generated by Django 4.1.4 on 2022-12-22 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcategory',
            options={'verbose_name': 'Kategori', 'verbose_name_plural': 'Kategoriler'},
        ),
        migrations.AlterModelOptions(
            name='blogcomment',
            options={'verbose_name': 'Yorum', 'verbose_name_plural': 'Yorumlar'},
        ),
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name': 'Blog Yazısı', 'verbose_name_plural': 'Blog Yazıları'},
        ),
        migrations.AlterField(
            model_name='blogcategory',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='Kategori Adı'),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='blog_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_comments', to='api_blog.blogpost', verbose_name='Blog Yazısı'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='viewed',
            field=models.IntegerField(default=0, editable=False, verbose_name='Görüntüleme Sayısı'),
        ),
    ]
