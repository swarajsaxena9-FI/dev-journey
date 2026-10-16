#1
def even_squares(num):
    sqr=[i*i  for i in num if i%2 == 0 ]
    return sqr


def test_even_squares():
    assert even_squares([1,2,3,4,5])==[4,16]
    assert even_squares([]) ==[]
    assert even_squares([3,5,7,9])==[]


#2

def word_lengths(words):
    w_dict = {k:len(k) for k in words}
    return w_dict

def test_word_lengths():
    assert word_lengths(['name','gender','age'])=={'name':4,'gender':6,'age':3}
    
#3
def first_letters(words):
    word_set={word[0] for word in words}
    return word_set

def test_first_letters():
    assert first_letters(["apple", "avocado", "banana"])=={'a','b'}

#4
def sort_by_length(words):
    sort_words = sorted(words,key=lambda word: len(word))
    return sort_words
def test_sort_by_length():
    assert sort_by_length(["banana", "kiwi", "apple"])==["kiwi", "apple", "banana"]


#5
def numbered(words):    
    words_list = [f'{n}. {word}' for n,word in enumerate(words,start=1)]
    return words_list
def test_numbered():
    assert numbered(["apple", "kiwi"])==["1. apple", "2. kiwi"]

#6
def make_marks_dict(names, marks):
    name_marks = {name:mark for name,mark in zip(names,marks)}
    return name_marks
def test_make_marks_dict():
    assert make_marks_dict(["asha", "ravi"],[90, 75])=={'asha': 90, 'ravi': 75}
    assert make_marks_dict([],[])=={}
#7

def has_negative(nums):
    return any(num<0 for num  in nums)
    
def all_positive(nums):
    return all(num >0 for num in nums)

def test_has_negative():
    assert has_negative([1, -2, 3] )==True
    assert has_negative([1, 2, 3] )==False
    assert has_negative([]) == False
def test_all_positive():
    assert all_positive([1, 2, 3] )==True
    assert all_positive([1, -2, 3] )==False
    assert all_positive([0, 1, 2]) == False
    assert all_positive([]) == True

#8

def sort_students(students):
    sort_list = sorted(students,key= lambda s:(-s['marks'],s['name']))
    return sort_list

def test_sort_students():
    assert sort_students([{"name":"ravi","marks":90}, {"name":"asha","marks":90}, {"name":"tina","marks":75}])==[{"name":"asha","marks":90}, {"name":"ravi","marks":90}, {"name":"tina","marks":75}]

