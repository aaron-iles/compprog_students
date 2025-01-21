#!/usr/bin/env python3

# You're allowed to do either of these!
from mypackage import mymodule
import mypackage


def test_add_1_and_2():
    assert mypackage.mymodule.add(1, 2) == 3

def test_add_2_and_3():
    assert mymodule.add(2, 3) == 5

def test_add_failure():
    assert mymodule.add(2, 3) == 5

