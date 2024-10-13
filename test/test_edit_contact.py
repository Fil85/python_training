# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.edit(Contact(firstname="Dima", lastname="Filimonov", company="Dom",
                             address="Ryazan", home_phone="001", mobile_phone="002",
                             work_phone="003", email="dima@mail.ru", homepage="dima.ru",
                             bday="3", bmonth="October", byear="2020"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
