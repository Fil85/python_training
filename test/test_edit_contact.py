# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    contact = Contact(firstname="Dima", lastname="Filimonov", company="Dom",
                      address="Ryazan", home_phone="001", mobile_phone="002",
                      work_phone="003", email="dima@mail.ru", homepage="dima.ru",
                      bday="3", bmonth="October", byear="2020")
    if app.contact.count() == 0:
        app.contact.create(contact)
    old_contacts = app.contact.get_contact_list()
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
