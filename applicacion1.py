from selenium import webdriver


class Application1:
    def __init__(self):
        self.wd = webdriver.Firefox(firefox_binary=r'C:/Program Files/Mozilla Firefox/firefox.exe')
        self.wd.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def logout(self):
        wd = self.open_home_page()
        wd.find_element_by_link_text("Logout").click()

    def return_the_home_page(self):
        wd = self.open_home_page()
        wd.find_element_by_link_text("home").click()

    def submit_new_contact(self):
        wd = self.open_home_page()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_contact_form(self,contact):
        wd = self.open_home_page()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        self.return_the_home_page(wd)


    def init_new_contact_creation(self):
        wd = self.open_home_page()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()

    def open_new_page(self):
        wd = self.open_home_page()
        wd.find_element_by_link_text("add new").click()

    def login(self, username, password):
        wd = self.open_home_page()
        self.open_new_page()
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

    def destroy(self):
        self.wd.quit()

