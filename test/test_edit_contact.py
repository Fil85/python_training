# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_contact(app):
    contact = Contact(firstname="Dima", lastname="Filimonov", company="Dom",
                      address="Ryazan", homephone="001", mobilephone="002",
                      workphone="003", email="dima@mail.ru", homepage="dima.ru",
                      bday="3", bmonth="October", byear="2020")
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="John"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
