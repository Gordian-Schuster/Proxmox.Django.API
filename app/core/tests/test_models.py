from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_and_email(self):
        """testing usercreation and email"""
        email = "test@gordianschuster.de"
        password = "Testpasswort1."
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
    
        self.asserertEqual(user.email, email)
        self.asserertTrue(user.check_password(password))
