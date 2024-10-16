from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.start_make_contact()
        # fill contact form
        self.input_data(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.return_home_page()
        self.contact_cache = None

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        self.select_contact_by_index(index)
        self.input_data(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_home_page()
        self.contact_cache = None

    def input_data(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("email", contact.email)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("bday", contact.bday)
        self.change_field_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            if field_name != "bday" and field_name != "bmonth":
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(text)
            elif field_name == "bday" or field_name == "bmonth":
                wd.find_element_by_name(field_name).click()
                Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def open_home_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_id("MassCB")) > 0):
            wd.find_element_by_link_text("home").click()

    def start_make_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + str(index + 2) + "]/td[8]/a/img").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            i = 2
            for element in wd.find_elements_by_name("entry"):
                lastname = element.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + str(i) + "]/td[2]").text
                firstname = element.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + str(i) + "]/td[3]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                i += 1
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)
