# instanties DONE
# 
# can add toys DONE
# - throws exception if not toy passed in DONE
#
# can list toys DONE
# 
# can return a string with all toys names eg.:
#       You have 5 toys: "Teddy", "Bear", "Ball", "Chess", "Flashlight"
from lib.toybox import ToyBox
from lib.toy import Toy
import pytest

def test_toybox_instantiates():
    toybox = ToyBox()

    assert toybox.toys == []

def test_toybox_add_works_correctly():
    # setup
    toybox = ToyBox()
    toy = Toy('Flashlight')

    # action
    toybox.add(toy)

    # assertion
    assert toybox.toys == [toy]

def test_toybox_add_throws_exception_if_not_toy_passed_in():
    # setup
    toybox = ToyBox()

    # action
    with pytest.raises(Exception) as e:
        toybox.add(1)
    
    # assertion 
    assert str(e.value) == "Can only accept Toy(s)"

def test_can_list_all_toys():
    # setup
    toybox = ToyBox()
    toy = Toy('Ball')
    toy2 = Toy('Flashlight')

    # action
    toybox.add(toy)
    toybox.add(toy2)
    print(toybox.get_toys())

    # assertion
    assert toybox.get_toys() == [toy, toy2]

# can return a string with all toys names eg.:
#       You have 5 toys: "Teddy", "Bear", "Ball", "Chess", "Flashlight"
def test_toybox_can_return_number_and_names_of_toys():
    # setup
    toybox = ToyBox()
    toy = Toy('Ball')
    toy2 = Toy('Flashlight')

    # action
    toybox.add(toy)
    toybox.add(toy2)

    # assertion
    assert toybox.count_and_list_toy() == "You have 2 toys: Ball, Flashlight"
