from rest_framework import serializers
from .models import *

# -------------------- FixSerializer --------------------------------------

class FixSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True) # Sadece görüntüle. (User otomatik kaydedilecek.)
    user = serializers.StringRelatedField() # Hangi kullanıcı olduğunu göster.
    
    class Meta:
        # 1. Yöntem: Hepsini göster
        # fields = '__all__'
        # 2. Yöntem: Belirttiklerimi göster
        # fields = ('blog_category', 'title', 'content')
        # 3. Yöntem: Belirtiklerim dışındakileri getir.
        exclude = [
            # 'created',
            # 'updated',
        ]

    # Override: Her yeni_kayıt için user_id otomatik ekle (o anki giriş yapmış user):
    def create(self, validated_data):
        # Her kayıt eklemede user_id otomatik eklensin:
        validated_data["user_id"] = self.context['request'].user.id
        return super().create(validated_data)

# -------------------- Serializers --------------------------------------

class BlogCommentSerializer(FixSerializer):
    blog_post_id = serializers.IntegerField() # Üst kayıt ID
    blog_post = serializers.StringRelatedField() # Üst kayıt ismi
    
    class Meta(FixSerializer.Meta):
        model = BlogComment


class BlogPostSerializer(FixSerializer):
    blog_category_id = serializers.IntegerField() # Üst kayıt ID
    blog_category = serializers.StringRelatedField() # Üst kayıt ismi
    blog_comments = BlogCommentSerializer(read_only=True, many=True) # Alt kayıtlar related_name ile çağrılabilir.
    
    class Meta(FixSerializer.Meta):
        model = BlogPost


class BlogCategorySerializer(FixSerializer):
    
    class Meta(FixSerializer.Meta):
        model = BlogCategory