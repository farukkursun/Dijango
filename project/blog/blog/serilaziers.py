from rest_framework import serializers
from .models import Category, Post, Comment


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'created_time',
            'update_time'

        )


class PostSerializers(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    category_id=serializers.IntegerField()
    user=serializers.StringRelatedField()
    user_id=serializers.IntegerField()
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'description',
            'content',
            'user_id',
            'user',
            'category',
            'category_id',
            'created_time',
            'update_time'


        )

class CommentSerializers(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    user_id=serializers.IntegerField()
    post=serializers.StringRelatedField()
    post_id=serializers.IntegerField()
    class Meta:
        model = Comment
        fields= (
            'first_name',
            'last_name',
            'comment',
            'post',
            'post_id',
            'user',
            'user_id',
            'created_time',
            'update_time'

        )



