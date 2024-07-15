import time
from lib2to3.pgen2 import driver

import pytest
from pages.registration_page import Registration


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegistration:

    def test_registration_page_availability(self):
        registration = Registration(self.driver)
        registration.close()
        registration.login()
        registration.register1()
        registration.assert_tc1()

    def test_registration_with_blank_details(self):
        registration = Registration(self.driver)
        registration.close()
        registration.login()
        registration.register1()
        registration.register2()
        # registration.assert_tc1()
        current_url = self.driver.current_url
        expected_url = "https://www.cocojalila.com/login"
        assert current_url == expected_url

    def test_registration_with_already_registered_details(self):
        registration = Registration(self.driver)
        registration.close()
        registration.login()
        registration.register1()
        registration.add()
        registration.register2()
        registration.assert_tc2()

    def test_password_strength(self):
        registration = Registration(self.driver)
        registration.close()
        registration.login()
        registration.register1()
        registration.password_strength_verification()
        registration.register2()
        registration.assert_tc3()
        time.sleep(2)

    def test_password_mismatch(self):
        registration = Registration(self.driver)
        registration.close()
        registration.login()
        registration.register1()
        registration.password_mismatch()
        registration.register2()
        registration.assert_tc4()
        time.sleep(2)

    def test_first_name_field_availability(self):
        registration = Registration(self.driver)
        registration.close()
        registration.login()
        registration.register1()
        registration.assert_tc5()

    def test_email_field_availability(self):
        registration = Registration(self.driver)
        registration.close()
        registration.login()
        registration.register1()
        registration.assert_tc6()

    def test_password_field_availability(self):
        registration = Registration(self.driver)
        registration.close()
        registration.login()
        registration.register1()
        registration.assert_tc7()

    def test_confirm_password_field_availability(self):
        registration = Registration(self.driver)
        registration.close()
        registration.login()
        registration.register1()
        registration.assert_tc8()

    def test_registration_button_availability(self):
        registration = Registration(self.driver)
        registration.close()
        registration.login()
        registration.register1()
        registration.assert_tc9()













