# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Ivan", lastname="Ivanov", company="GazProm",
                               address="Saint Petersburg", home_phone="111111", mobile_phone="222222",
                               work_phone="333333", email="ivan@mail.ru", homepage="ivan.ru",
                               bday="14", bmonth="May", byear="1988"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", company="",
                               address="", home_phone="", mobile_phone="",
                               work_phone="", email="", homepage="",
                               bday="10", bmonth="April", byear="1990"))
