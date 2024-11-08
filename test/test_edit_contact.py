# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_edit_contact(app, db, check_ui):
    contact_new = Contact(firstname="Dima", lastname="Filimonov", company="Dom",
                      address="Ryazan", homephone="444", mobilephone="555",
                      workphone="666", email="dima@mail.ru", email2="dima2@mail.ru", email3="dima3@mail.ru",
                      homepage="dima.ru", bday="3", bmonth="October", byear="2020")
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="John"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.edit_contact_by_id(contact.id, contact_new)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[new_contacts.index(contact_new)] = contact_new
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
