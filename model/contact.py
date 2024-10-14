from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, company=None, address=None, home_phone=None, mobile_phone=None,
                 work_phone=None, email=None, homepage=None, bday=None, bmonth=None, byear=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.email = email
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname
                and self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
