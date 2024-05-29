from rest_framework import serializers

from config.settings import ALLOWED_EXTENSIONS, MAX_FILE_SIZE


class FileCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    data = serializers.CharField()

    def validate_name(self, value):
        name = value.rsplit('.')[-1].lower()
        if name not in ALLOWED_EXTENSIONS:
            raise serializers.ValidationError(
                f'Допустимое расширение файла: {ALLOWED_EXTENSIONS}'
            )
        return value

    def validate_data(self, value: str):
        if value.__sizeof__() > MAX_FILE_SIZE:
            raise serializers.ValidationError(
                f'Размер файла превышает допустимый лимит, максимум {MAX_FILE_SIZE} МБ'
            )
        return value


class FilesListSerializer(serializers.Serializer):
    mimeType = serializers.CharField()
    id = serializers.CharField()
    name = serializers.CharField()
