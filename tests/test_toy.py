# instantiates name
# can tell name
from lib.toy import Toy

def test_toy_instantiates():
    toy = Toy('Flashlight')

    assert toy.name == 'Flashlight'

def test_toy_get_name():
    # setup
    toy = Toy('Flashlight')

    # action
    # assertion
    assert toy.get_name() == 'Flashlight'