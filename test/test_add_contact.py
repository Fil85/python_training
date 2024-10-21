# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan", lastname="Ivanov", company="GazProm",
                      address="Saint Petersburg", homephone="111111", mobilephone="222222",
                      workphone="333333", email="ivan@mail.ru", email2="ivan2@mail.ru", email3="ivan3@mail.ru",
                      homepage="ivan.ru", bday="14", bmonth="May", byear="1988")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(firstname="", lastname="", company="",
#                      address="", homephone="", mobilephone="",
#                     workphone="", email="", homepage="",
#                      bday="10", bmonth="April", byear="1990")
#    app.contact.create(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
