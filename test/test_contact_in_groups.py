from model.contact import Contact
import re
import random

def test_add_contact_to_group(app, db):
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.add_contact_to_group(contact)


    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for contact_home, contact_db in zip(contact_from_home_page, contact_from_db):
        assert contact_home.firstname == contact_db.firstname
        assert contact_home.lastname == contact_db.lastname
        assert contact_home.address == contact_db.address
        assert contact_home.all_phones_from_home_page == merge_phones_like_on_home_page(contact_db)
        assert contact_home.all_email_from_home_page == merge_email_like_on_home_page(contact_db)
    assert contact_from_home_page == contact_from_db


def test_del_contact_from_group(app, db):
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.del_contact_from_group(contact)


    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for contact_home, contact_db in zip(contact_from_home_page, contact_from_db):
        assert contact_home.firstname == contact_db.firstname
        assert contact_home.lastname == contact_db.lastname
        assert contact_home.address == contact_db.address
        assert contact_home.all_phones_from_home_page == merge_phones_like_on_home_page(contact_db)
        assert contact_home.all_email_from_home_page == merge_email_like_on_home_page(contact_db)
    assert contact_from_home_page == contact_from_db

def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone]))))


def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))
