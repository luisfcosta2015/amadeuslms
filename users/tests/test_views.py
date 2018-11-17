"""
Copyright 2016, 2017 UFPE - Universidade Federal de Pernambuco

Este arquivo é parte do programa Amadeus Sistema de Gestão de Aprendizagem, ou simplesmente Amadeus LMS

O Amadeus LMS é um software livre; você pode redistribui-lo e/ou modifica-lo dentro dos termos da Licença Pública Geral GNU como publicada pela Fundação do Software Livre (FSF); na versão 2 da Licença.

Este programa é distribuído na esperança que possa ser útil, mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a Licença Pública Geral GNU para maiores detalhes.

Você deve ter recebido uma cópia da Licença Pública Geral GNU, sob o título "LICENSE", junto com este programa, se não, escreva para a Fundação do Software Livre (FSF) Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA.
"""

from django.test import TestCase, RequestFactory, Client
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import AnonymousUser
from unittest.mock import patch, MagicMock
from ..models import User
from .. import views
from log.models import Log
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.messages import get_messages
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.contrib.sessions.middleware import SessionMiddleware


class UserTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create(
            username='erik',
            email='egz@cin.ufpe.br',
            password='amadeus')
        self.admin = User.objects.create_superuser(
            'admin_test',
            email='admin_test@amadeus.com',
            password='teste')

    def test_login_get_anonymous_auth(self):
        request = self.factory.get(reverse_lazy('users:login'))

        request.user = AnonymousUser()

        response = views.login(request)

        self.assertEquals(response.status_code, 200)

    def test_login_get_auth(self):
        request = self.factory.get(reverse_lazy('users:login'))

        request.user = self.user

        response = views.login(request)

        self.assertEquals(response.status_code, 302)

    def test_login_ok(self):
        data = {
            'email': 'admin_test@amadeus.com',
            'password': 'teste'
        }

        response = self.client.post(reverse_lazy('users:login'), data)

        self.assertEquals(response.status_code, 302)

    def test_login_log(self):
        # test if register logs
        # test if register logs only if sucessful
        request = self.factory.get(reverse_lazy('users:login'))
        request.user = self.user
        response = views.login(request)

        # if the logs are registered then the count must be equal 1
        self.assertEquals(Log.objects
                          .filter(action="access", resource="system")
                          .count(), 1)

    def test_login_post_invalid(self):
        data = {
            'email': 'test@amadeus.com.br',
            'password': 'anything'
        }

        response = self.client.post(reverse_lazy('users:login'), data)
        messages = response.context['messages']

        self.assertEquals(response.status_code, 200)
        self.assertIsNotNone(messages)  # checking if message was sent

    def test_signup_get(self):
        request = self.factory.get(reverse_lazy('users:signup'))
        request.user = AnonymousUser()
        response = views.RegisterUser.as_view()(request)

        self.assertEquals(response.status_code, 200)

    @patch('users.models.User.save', MagicMock(name="save"))
    def test_signup_post(self):
        data = {
            'username': 'Teste',
            'last_name': 'Amadeus',
            'email': 'teste@amadeus.com.br',
            'new_password': 'teste',
            'password2': 'teste'
        }

        response = self.client.post(reverse_lazy('users:signup'), data)

        self.assertEquals(response.status_code, 302)
        self.assertTrue(User.save.called)
        # call with commit=False first and then saving it
        self.assertEquals(User.save.call_count, 2)

    def test_forgot_pass_real_user(self):
        # test to check if the forgot password works
        # and sends the correct message to the user
        data = {"email": self.user.email}
        request = self.factory.post(reverse_lazy('users:forgot_pass'), data)

        request.user = self.user

        # because we have to mock the class on tests
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        response = views.ForgotPassword.as_view()(request)

        storage = get_messages(request)

        self.assertEquals(response.status_code, 302)
        # I use str so I can compare the content of the messages
        # storage can't be indexed so I have to iterate over it
        for message in storage:
            self.assertEquals(str(message),
                              str(views.ForgotPassword.success_message))

    def test_forgot_password_missing_user(self):
        # test if a request is sent for a user that doesn't exist
        data = {"email": "non-existant@email.com"}
        request = self.factory.post(reverse_lazy('users:forgot_pass'), data)

        # because we have to mock the class on tests
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        response = views.ForgotPassword.as_view()(request)

        storage = get_messages(request)

        self.assertEquals(response.status_code, 200)
        # I use str so I can compare the content of the messages
        # storage can't be indexed so I have to iterate over it
        for message in storage:
            self.assertEquals(str(message),
                              str(views.ForgotPassword.error_message))

    def test_logout_reoute(self):
        # test if logout URL works and if user loses authentication
        # set up a logged in user
        request = self.factory.get(reverse_lazy('users:login'))
        request.user = self.user

        response = views.login(request)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(request.user.is_authenticated(), True)

        request = self.factory.post(reverse_lazy('users:logout'))
        # add middleware session onto the request
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        request.session[LANGUAGE_SESSION_KEY] = 'en'
        request.user = self.user

        response = views.logout(request)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(request.user.is_authenticated, False)

    def test_logout_log(self):
        # test that if after logout the system logs the action
        pass

    def test_search_user(self):
        # test if the context possess the variables we expect to have
        # if the URL returns 200
        pass

    def test_remove_account(self):
        # test if the account is really removed
        # test if the return code is correct
        pass

    def test_remove_account_logs(self):
        # test if after the account is removed a log is setted with the
        # correct values in the field
        pass

    def test_update_view(self):
        # test
        pass

    def test_update_logs(self):
        # test if after call a log is created
        # and if it possess the fields filled on the context
        pass
