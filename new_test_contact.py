# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact

class NewTestContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox(firefox_binary=r'C:/Program Files/Mozilla Firefox/firefox.exe')
        self.wd.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_new_test_contact(self):
        wd = self.open_home_page()
        self.login(wd, "admin", "secret")
        self.init_new_contact_creation(wd)
        self.fill_contact_form(wd, Contact (firstname="Sasha", middlename="Alex", nickname="Sa"))
        self.submit_new_contact(wd)
        self.logout(wd)

    def test_empty_test_contact(self):
        wd = self.open_home_page()
        self.login(wd, "admin", "secret")
        self.init_new_contact_creation(wd)
        self.fill_contact_form(wd, Contact(firstname="", middlename="", nickname=""))
        self.submit_new_contact(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_the_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def submit_new_contact(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_contact_form(self, wd, contact):
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        self.return_the_home_page(wd)


    def init_new_contact_creation(self, wd):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()

    def open_new_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        self.open_new_page(wd)
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        return wd

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.wd.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
