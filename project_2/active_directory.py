class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(_user, _group):
    if _user in _group.get_users():
        return True

    for sub_group in _group.get_groups():
        return is_user_in_group(_user, sub_group)

    return False


# Test Case 1
print(is_user_in_group('sub_child_user', parent))
# Test Case 2
print(is_user_in_group(None, parent))
# Test Case 3
print(is_user_in_group(124234, parent))