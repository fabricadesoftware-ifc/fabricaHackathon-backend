from rest_framework.serializers import ModelSerializer, SlugRelatedField
from hackathon.models import Project
from uploader.serializers import ImageSerializer
from uploader.models import Image


class ProjectListSerializer(ModelSerializer):
    photo = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Project
        fields = "__all__"
        depth = 0


class ProjectDetailSerializer(ModelSerializer):
    photo = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Project
        fields = "__all__"
        depth = 1


class ProjectCreateSerializer(ModelSerializer):
    photo = SlugRelatedField(
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )

    class Meta:
        model = Project
        fields = "__all__"
