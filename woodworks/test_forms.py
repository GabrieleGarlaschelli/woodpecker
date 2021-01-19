from django.test import TestCase

from accounts.forms import CustomUserCreationForm


class TestFormsRegistration(TestCase):
    #Test con inserimenti validi da parte dell'utente
    def test_create_user_form_valid_data(self):
        form=CustomUserCreationForm(data={
            'first_name': 'Emanuele',
            'last_name': 'Moia',
            'username': 'emamoia',
            'email': 'emanuele.moia@hotmail.com',
            'password1': 'ciao1234$',
            'password2': 'ciao1234$'
        })
        self.assertTrue(form.is_valid())

    #test con inserimento della seconda password sbagliata
    def test_create_user_form_password_not_valid(self):
        form = CustomUserCreationForm(data={
            'first_name': 'Gabriele',
            'last_name': 'Garlaschelli',
            'username': 'gabbogarla',
            'email': 'gabriele.garlaschelligg@gmail.com',
            'password1': 'ciao123',
            'password2': 'ciao14$'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], ['The two password fields didn\'t match.'])

    #test con inserimento della mail in formato errato
    def test_create_user_form_email_not_valid(self):
        form = CustomUserCreationForm(data={
            'first_name': 'Stefano',
            'last_name': 'Valla',
            'username': 'ste',
            'email': 'stefano.valla.com',
            'password1': 'ciao123',
            'password2': 'ciao123'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])


