from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, company=None, address=None, homephone=None, mobilephone=None,
                 workphone=None, all_phones_from_home_page=None, email=None, email2=None, email3=None,
                 all_email_from_home_page=None, homepage=None, bday=None, bmonth=None, byear=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_email_from_home_page = all_email_from_home_page
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.address, self.homephone,
                                         self.mobilephone, self.workphone, self.email)

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname
                and self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
