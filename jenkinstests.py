from jenkins_func import func

def test_answer():
    assert func('Hello') == 'World'

def test_answer2():
    assert func('Hey') == 'Hello'

def test_answer3():
    assert func('Helloo') == 'Hello'
