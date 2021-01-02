import pytest

from weixin_api.tag import Tag


class TestTag:
    def setup(self):
        self.tag = Tag()

    @pytest.mark.parametrize('group_name, name1, name2', [
        ['group_name1', 'name1', 'name2'],
        ['group_name啦啦', 'name1啦啦', 'name2啦啦'],
        ['group_name啦啦>?<', 'name1啦啦>?<', 'name2啦啦>?<'],
        ['', '', '']
    ])
    def test_add(self, group_name, name1, name2):
        self.tag.add(group_name, name1, name2)
        r = self.tag.get_tag()
        for group in r.json()['tag_group']:
            if group['group_name'] == group_name:
                for tag in group['tag']:
                    if tag['name'] == name1 or tag['name'] == name2:
                        assert True

    @pytest.mark.parametrize('id, name', [
        ['etJ5uFBwAAv47exAk3KjnNha-rUS66Zw', 'name_new'],
        ['etJ5uFBwAAv47exAk3KjnNha-rUS66Zw', 'name_new_123'],
        ['etJ5uFBwAAv47exAk3KjnNha-rUS66Zw', 'name_new_啦啦'],
        ['etJ5uFBwAAv47exAk3KjnNha-rUS66Zw', 'name_new_>?<'],
        ['etJ5uFBwAAv47exAk3KjnNha-rUS66Zw', 'name_new_>?<啦啦1234']
    ])
    def test_update(self, id, name):
        self.tag.update(id, name)
        r = self.tag.get_tag()
        tags = [tag for group in r.json()['tag_group']
                if group['group_name'] == 'group_name1'
                for tag in group['tag']
                if tag['name'] == name]
        assert tags != []

    def test_delete(self):
        r = self.tag.delete('etJ5uFBwAASBCvH0v6D3kmgH2ho44oFg', None, None, None)
        assert r.json()['errcode'] == 0
