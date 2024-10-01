# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Ivan", lastname="Ivanov", company="GazProm",
                                   address="Saint Petersburg", home_phone="111111", mobile_phone="222222",
                                   work_phone="333333", email="ivan@mail.ru", homepage="ivan.ru",
                                   bday="14", bmonth="May", byear="1988"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", lastname="", company="",
                               address="", home_phone="", mobile_phone="",
                               work_phone="", email="", homepage="",
                               bday="10", bmonth="April", byear="1990"))
    app.session.logout()
