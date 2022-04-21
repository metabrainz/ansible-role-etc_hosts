from collections import abc

def test_list(value):
    return isinstance(value, list)

def test_valid_entry(value):
    if isinstance(value, abc.Mapping):
        return bool(value.get('address')) and bool(value.get('hostnames'))
    else:
        return bool(value)

class TestModule(object):

    def tests(self):
        return {
            'list': test_list,
            'valid_entry': test_valid_entry
        }
