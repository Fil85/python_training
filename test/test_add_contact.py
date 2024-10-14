# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan", lastname="Ivanov", company="GazProm",
                      address="Saint Petersburg", home_phone="111111", mobile_phone="222222",
                      work_phone="333333", email="ivan@mail.ru", homepage="ivan.ru",
                      bday="14", bmonth="May", byear="1988")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", lastname="", company="",
                      address="", home_phone="", mobile_phone="",
                      work_phone="", email="", homepage="",
                      bday="10", bmonth="April", byear="1990")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
