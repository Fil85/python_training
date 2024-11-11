from tokenize import group

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
    app.contact.add_contact_to_group(contact.id)
    assert contact in db.get_contacts_in_group(groups[0])


def test_del_contact_from_group(app, db):
    groups = db.get_group_list()
    contacts = db.get_contacts_in_group(groups[0])
    contact = random.choice(contacts)
    app.contact.delete_contact_from_group(groups[0].id, contact.id)
    assert contact in db.get_contacts_not_in_group()
