from namanga.apps.engine.models import User
from namanga.apps.engine.serializers_container import (serializers, transaction, AppStatus)


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True, "min_length": 8}}

    def create(self, validated_data):
        user = User.objects.filter(email=validated_data["email"]).first()
        if user and user.is_active:
            raise serializers.ValidationError(AppStatus.EMAIL_ALREADY_EXIST.message)

        with transaction.atomic():
            try:
                if not user:
                    user = User.objects.create_user(**validated_data)

            except Exception as e:
                transaction.rollback(True)
                raise serializers.ValidationError(AppStatus.REGISTER_USER_FAIL.message)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}, 'verify_code': {'write_only': True}}
