from rest_framework import serializers

# 遵循RESTful规范, 一个名词url只处理一个资源, 所以, 不在嵌套的关系字段中同时创建对象
# /users/ POST 去创建user对象, 不会去/posts/中创建post对象的同时创建user
# 前后端协商接口的时候, 要将逻辑区分开, 不要混在一起
from posts.models import User, Topic, Post


class UserSerializer(serializers.ModelSerializer):
    # posts = serializers.StringRelatedField(many=True)
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # posts = serializers.HyperlinkedRelatedField(many=True, view_name="posts-detail", read_only=True)
    # posts = serializers.SlugRelatedField(many=True, slug_field='content', read_only=True)
    def validate(self, attrs):
        print(attrs)
        return attrs

    class Meta:
        model = User
        fields = ('id', 'username', 'posts')


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'name')


class PostsSerializer(serializers.ModelSerializer):
    """
    ModelSerializer根据model模型的定义
        自动生成默认字段
        自动生成相应的验证器
        实现了简单的create 和 update 方法
        自动默认将关系字段映射成PrimaryKeyRelatedField

    PostsSerializer():
        id = IntegerField(label='ID', read_only=True)
        title = CharField(max_length=128)
        content = CharField(style={'base_template': 'textarea.html'})
        user = UserSerializer():
            id = IntegerField(label='ID', read_only=True)
            username = CharField(max_length=128)
        topics = PrimaryKeyRelatedField(many=True, queryset=Topic.objects.all(), required=False)
    """
    user = UserSerializer()  # 以后 user 的处理, 使用UserSerializer

    # topics = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'user', 'topics')
        depth = 1

    def create(self, validated_data):
        user_data = validated_data.pop('user', None)
        user, flag = User.objects.get_or_create(username=user_data.get('username'))
        topics_data = validated_data.pop("topics", None)
        post = Post.objects.create(user=user, **validated_data)
        if topics_data:
            post.topics.add(*topics_data)
        return post

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        topics_data = validated_data.pop('topics', None)
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        if user_data:
            user, flag = User.objects.get_or_create(username=user_data["username"])
            instance.user = user
        if topics_data:
            instance.topics.clear()
            instance.topics.add(*topics_data)
        instance.save()
        return instance
