import pytest
from collections import namedtuple
Task = namedtuple('Task',['summary','owner','done','id'])
Task.__new__.__defaults__ = (None,None,False,None)

def test_defaults():
    t1 = Task()
    t2 = Task(None,None,False,None)
    assert t1 == t2

@pytest.mark.important_test
def test_member():
    t = Task('Potluck','SQE')
    assert t.summary == "Potluck"
    assert t.owner == "SQE"
    assert (t.done,t.id) == (False,None)