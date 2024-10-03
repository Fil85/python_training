from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name = "test333", header = "vool", footer = "kiol"))
    app.session.logout()