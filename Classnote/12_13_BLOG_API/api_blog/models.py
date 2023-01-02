from django.db import models
from django.contrib.auth.models import User

# -------------------- FixModels --------------------------------------

class FixModel(models.Model):
    user = models.ForeignKey(User, verbose_name='Kullanıcı', on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='Oluşturulma Tarihi', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Güncelleme Tarihi', auto_now=True)

    class Meta:
        abstract = True # Bu model için tablo oluşturma.

# -------------------- Models --------------------------------------

# Blog Kategori:
class BlogCategory(FixModel):
    name = models.CharField(verbose_name='Kategori Adı', max_length=50, default='')

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"

    def __str__(self):
        return self.name


# Blog Yazıları:
class BlogPost(FixModel):
    blog_category = models.ForeignKey(BlogCategory, verbose_name='Kategori', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Başlık', max_length=50)
    description = models.CharField(verbose_name='Açıklama', max_length=50)
    content = models.TextField(verbose_name='İçerik')
    viewed = models.IntegerField(verbose_name='Görüntüleme Sayısı', editable=False, default=0)

    class Meta:
        verbose_name = 'Blog Yazısı'
        verbose_name_plural = "Blog Yazıları"

    def __str__(self):
        return self.title


# Blog Yorumları:
class BlogComment(FixModel):
    blog_post = models.ForeignKey(BlogPost, verbose_name='Blog Yazısı', on_delete=models.CASCADE, related_name='blog_comments')
    first_name = models.CharField(verbose_name='İsim', max_length=50)
    last_name = models.CharField(verbose_name='Soyisim', max_length=50)
    comment = models.TextField(verbose_name='Yorum')

    class Meta:
        verbose_name = "Yorum"
        verbose_name_plural = "Yorumlar"

    def __str__(self):
        return f'{self.blog_post} - {self.first_name} {self.last_name}'
