# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    app.contact.edit(Contact(firstname="Dima", lastname="Filimonov", company="Dom",
                               address="Ryazan", home_phone="001", mobile_phone="002",
                               work_phone="003", email="dima@mail.ru", homepage="dima.ru",
                               bday="3", bmonth="October", byear="2020"))
