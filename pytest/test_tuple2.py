import pytest
from test_tuple import Task

#Converting tupple to dictionary (Key: value)
@pytest.mark.important_test
def test_dict():
    t_task = Task('do something','SQE',True,2) #Task Tupple
    t_dict = t_task._asdict() #Converting to Dict
    expected = {'summary':'do something',
                'owner':'SQE',
                'done':True,
                'id':2}
    assert t_dict == expected #Asserting dict conversion as expected
    
def test_replace():
    t_before = Task('work done','tuple',False)
    t_after = t_before._replace(id=10,done=True)
    t_expected = Task('work done','tuple',True,10)
    assert t_after == t_expected