from model.group import Group


def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New Group Name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New Group header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_footer(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(footer="New Group footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
