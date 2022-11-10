from django import forms
from django.contrib.auth.models import User
from . import models




class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = '__all__'
        exclude = ('user',)





class UserForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Senha'
    )

    password2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Confirmação senha'
    )

    def __init__(self, user=None, *args, **kwargs ):
        super().__init__(*args, **kwargs)

        self.user= user

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password',
                'password2', 'email')


    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data
        validation_error_msgs = {}

        user_data = cleaned.get('username')
        email_data = cleaned.get('email')
        password_data = cleaned.get('password')
        password2_data = cleaned.get('password2')
        


        user_db = User.objects.filter(username=user_data).first()
        email_db = User.objects.filter(email=email_data).first()

        error_msg_user_exists= 'Usuário já existe'
        error_msg_email_exists= 'E-mail já existe'
        error_msg_password_match= 'As duas senhas não conferem'
        error_msg_password_short= 'Sua senha precisa de pelo menos 11 caracteres'
        error_msg_required_field = 'Este campo é obrigatório.'


        #Usuarios Logados
        if self.user:
            if user_db:
                if user_data != user_db.username:
                    validation_error_msgs['username'] = error_msg_user_exists
            
            if email_db:
                if email_data != email_db.email:
                    validation_error_msgs['email'] = error_msg_email_exists

            if password_data:
                if password_data != password2_data:
                    validation_error_msgs['password'] = error_msg_password_match
                    validation_error_msgs['password2'] = error_msg_password_match

                if len(password_data) <11:
                    validation_error_msgs['password'] = error_msg_password_short


        #Usuarios nao logados
        else:
            if user_db:
                validation_error_msgs['username'] = error_msg_user_exists

            if email_db:
                validation_error_msgs['email'] = error_msg_email_exists

            if not password_data:
                validation_error_msgs['password'] = error_msg_required_field

            if not password2_data:
                validation_error_msgs['password2'] = error_msg_required_field

            if password_data != password2_data:
                validation_error_msgs['password'] = error_msg_password_match
                validation_error_msgs['password2'] = error_msg_password_match

            if len(password_data) <11:
                validation_error_msgs['password'] = error_msg_password_short


        if validation_error_msgs:
            raise(forms.ValidationError(validation_error_msgs))