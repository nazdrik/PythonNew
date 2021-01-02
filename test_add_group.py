# -*- coding: utf-8 -*-
from _pytest import unittest
from selenium.webdriver.firefox.webdriver import WebDriver
from group import Group

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_group(self):

        wd = self.open_page()
        self.login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_new_group(wd, Group(name="test group", header="ddf", footer="fdf"))
        self.logout(wd)
        self.return_to_groups_page(wd)

    def test_add_empty_group(self):
        wd = self.open_page()
        self.login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_new_group(wd, Group(name="", header="", footer=""))
        self.logout(wd)
        self.return_to_groups_page(wd)

    def return_to_groups_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def create_new_group(self, wd, group):
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("%s" % group.name)
        if not wd.find_element_by_xpath(
                "//div[@id='content']//select[normalize-space(.)='[none]']//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']//select[normalize-space(.)='[none]']//option[1]").click()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("%s" % group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("%s" % group.footer)
        wd.find_element_by_xpath("//div[@id='content']/form").click()
        wd.find_element_by_name("submit").click()




    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        return wd

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
