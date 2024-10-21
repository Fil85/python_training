# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_names(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phones(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", address="", homephone="", mobilephone="", workphone="", email="")] + [
    Contact(firstname=random_names("", 10), lastname=random_names("", 20),
          address=random_names("", 20), homephone=random_phones("", 10),
            mobilephone = random_phones("", 10), workphone=random_phones("", 10),
            email=random_names("", 10))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
