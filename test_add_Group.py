# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from group import Group



class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox(firefox_binary=r'C:/Program Files/Mozilla Firefox/firefox.exe')
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        self.login( username="admin", password="secret")
        self.init_group_creation()
        self.fill_group_form(Group(name="qwer", header="qwer1", footer="qwer3"))
        self.submit_group_creation()
        self.logout()

   # def test_empty_group(self):
   #     wd = self.wd
   #     self.login(wd, username="admin", password="secret")
   #    self.init_group_creation(wd)
   #     self.fill_group_form(wd, Group(name="", header="", footer=""))
   #     self.submit_group_creation(wd)
   #     self.logout(wd)


    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def return_the_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def submit_group_creation(self):
        wd = self.wd
        wd.find_element_by_name("submit").click()
        self.return_the_groups_page()

    def fill_group_form(self,group):
        wd = self.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def init_group_creation(self):
        wd = self.wd
        wd.find_element_by_name("new").click()


    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[4]").click()

    def login(self,username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def is_element_present(self, how, what):
        try:
           self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        wd = self.wd
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
