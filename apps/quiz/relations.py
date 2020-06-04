from rest_framework import serializers


class CustomPrimaryKeyField(serializers.PrimaryKeyRelatedField):
    """
    Custom DRF serializer field for proper handling of
    Foreign Key by ListSerializer on validation error
    """
    def to_representation(self, value):
        """
        Return pk value of serialized Node object
        if available else return given ID value
        """
        if self.pk_field is not None:
            return self.pk_field.to_representation(value.pk)
        return getattr(value, 'pk', value)
