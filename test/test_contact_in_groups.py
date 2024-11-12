from model.contact import Contact
from model.group import Group
import re
import random


def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="John"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    contact = random.choice(contacts)
    group = random.choice(groups)
    app.contact.add_contact_to_group(contact.id, group.id)
    assert contact.id in db.get_contact_list_in_our_group(group)


def test_del_contact_from_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="John"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups = db.get_group_list()
    group = random.choice(groups)
    contacts = db.get_contact_list_in_our_group(group)
    if len(contacts) == 0:
        contacts_all = db.get_contact_list()
        contact = random.choice(contacts_all)
        app.contact.add_contact_to_group(contact.id, group.id)
    contacts = db.get_contact_list_in_our_group(group)
    contact_id = random.choice(contacts)
    app.contact.delete_contact_from_group(contact_id, group.id)
    assert contact_id not in db.get_contact_list_in_all_groups()
