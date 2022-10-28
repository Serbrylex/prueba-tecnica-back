from rest_framework import serializers

from django.contrib.auth import password_validation, authenticate
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User

from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class UserSignUpSerializer(serializers.Serializer): 
	"""User sign up serializer.

	Handle sign up data validation and user creation.
	"""

	email = serializers.EmailField(
		validators=[UniqueValidator(queryset=User.objects.all())]
	)
	username = serializers.CharField(
		min_length=4, 
		max_length=20,
		validators=[UniqueValidator(queryset=User.objects.all())]
	)

	# Password
	password = serializers.CharField(min_length=8, max_length=64)
	password_confirmation = serializers.CharField(min_length=8, max_length=64)

	# Name
	first_name = serializers.CharField(min_length=2, max_length=30)
	last_name = serializers.CharField(min_length=2, max_length=30)

	def validate(self, data):
		"""Verify passwords match."""
		passwd = data['password']
		passwd_conf = data['password_confirmation']
		if passwd != passwd_conf:
			raise serializers.ValidationError("Passwords don't match.")
		password_validation.validate_password(passwd)
		return data

	def create(self, data):
		"""Handle user and profile creation."""
		data.pop('password_confirmation')
		user = User.objects.create_user(**data)
        		
		return user


class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=64)
    password = serializers.CharField(min_length=2, max_length=64)

    def validate(self, data):
        """Check credentials."""
        #user = User.objects.get(username=data['username'], password=data['password'])
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')

        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve new token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key