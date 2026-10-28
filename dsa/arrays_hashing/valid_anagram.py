from collections import Counter

def is_anagram(s, t):
    s_sort= sorted(s)
    t_sort = sorted(t)

    return s_sort == t_sort
   
    
def test_is_anagram():
    assert is_anagram('listen','silent') == True
    assert is_anagram('rat','car') == False
    assert is_anagram('aab','ab') == False
    assert is_anagram('aab','abb') == False



def is_anagram2(s, t):
    return Counter(s)==Counter(t)

def test_is_anagram2():
    assert is_anagram2('listen','silent') == True
    assert is_anagram2('rat','car') == False
    assert is_anagram2('aab','ab') == False
    assert is_anagram2('aab','abb') == False
