#jaden Wright_Maurais
#261176273
#Brief description 

right_direction = 1 #moving forward through a word list
left_direction = -1 #moving backwards through a word list


def is_outside_list(letter_list, index):
    
    """
    (list of strings, int) --> Boolean (True or False)
    
    function will return True if the the index is out of bounds
    with regards to the length of the list. It will return False is
    index is inside the bounds with regard to the length of the list
    
    Examples:
    >>> is_outside_list(['A','B','C','D'], 1)
    False
    >>> is_outside_list(['A','B','C','D'], 0)
    False
    >>> is_outside_list(['A','B','C','D'], -1)
    True

    """
   
    if 0 <= index <= len(letter_list)-1 :
        return False 
    else:
        return True 
    
    
    

def letter_positions(letter_list,character):

    """
    (list of strings, string) --> list of integers
    
    function will return a list of indices where the character is
    found within the letter list.
    
    Examples:
    
    >>> letter_positions(['A','B','B','D'],'B')
    [1, 2]
    >>> letter_positions(['A','B','A','D','A'],'A')
    [0, 2, 4]
    >>> letter_positions(['A','B','A','D','A'],'R')
    []

    """
    result = []
    for i in range (len(letter_list)):
        if letter_list[i] == character:
            result.append(i)
            
    return result
    


    
def valid_word_pos_direction(letter_list,word,index,direction):
    """
    (list of string, string, int, int) -> Boolean (True or False)
    
    Function will return Boolean value indicating if the given word can
    be found in the letter list, at a given index and direction

    Examples:
    >>> valid_word_pos_direction( ['A','B','C','D','C','M'],'ABC',0,1)
    True
    >>>valid_word_pos_direction( ['A','B','C','D','C','M'],'DCB',3,-1)
    True
    >>> valid_word_pos_direction( ['A','B','C','D','C','M'],'AMC',0,-1)
    False
    """
        
    for letter in word:
        
        if is_outside_list(letter_list, index) == True:
            return False
        if letter_list[index]==letter:
            index +=direction
        elif letter_list[index] != letter:
            return False
        
    return True



def direction_word_given_position(letter_list,word,index):
    """
    (list of string,string,int) --> list of integers
    
    Function wil print a list of directions in which the given word was found
    from the letter list, at a given index
    
    Examples:
    
    >>> direction_word_given_position(['A','M','C','D','C','M'],'DCM',3)
    [-1, 1]
    >>> direction_word_given_position(['A','B','C','D','C','M'],'CBA',2)
    [-1]
    >>> direction_word_given_position(['A','B','C','D','C','M'],'ABC',0)
    [1]
    """
    
    result = []
    for letter in word:
        if letter_list[index] != letter:
            return result
        
        if valid_word_pos_direction(letter_list,word,index,left_direction)==True:
            result.append(left_direction)
            
        if valid_word_pos_direction(letter_list,word,index,right_direction)==True:
            result.append(right_direction)

    return result



def position_direction_word(letter_list,word):
    """
    
    (list string, string) --> nested list
    
    Function will return a nested list of indices and positions indicating
    at where a given word was found in a list of letters
    
    Examples:
    >>> position_direction_word(['A','B','C','D','C','M'],'CDC')
    [[2, 1], [4, -1]]
    >>> position_direction_word(['A','B','C','A','T','M'],'CAT')
    [[2, 1]]
    >>> position_direction_word(['A','B','C','A','T','M'],'CYU')
    []

    """
    
    dir_pos_list = []
    index_pos = letter_positions(letter_list, word[0])
    
    for index in index_pos:
        direction_of_word = direction_word_given_position(letter_list,word,index)
        for direction_of_word in direction_of_word:
            dir_pos_list.append([index,direction_of_word])
        
   
    return dir_pos_list


    


def cross_word_position_direction(bool_letter_list,length_word,
index,direction):
    """

    (list of boolean values, int, int, num) -> None
    
    Function will replace the values in boolean letter list at the given
    index and direction by value True. Then update bool letter
    list accordingly
    
    
    Exmaples:
    >>>bool_letter_list = [False,False,False,False,False,False]
    >>>
    >>>cross_word_position_direction(bool_letter_list,3,0,1)
    >>>bool_letter_list 
    [True, True, True, False, False, False]
    
    >>> cross_word_position_direction(bool_letter_list, 3, 0, -1)
    >>>bool_letter_list
    [True, False, False, False, True, True]
    
    >>> cross_word_position_direction(bool_letter_list, 6, 0, -1)
    >>>bool_letter_list
    [True, True, True, True, True, True]
    """
    
    
    for i in range (length_word):
        bool_letter_list[index] = True
        index += direction
    


    
def cross_word_all_position_direction(bool_letter_list, length_word,
list_position_direction):
    """

    (list of Boolean values, int, nested list of int ) -> None
    
    Function will call cross_word_position_direction to update
    the bool_letter_list
    
    
    Examples:
    >>>bool_letter_list = ['False','Flase','Flase','Flase','Flase','False','Flase']
    >>>
    >>> cross_word_all_position_direction(bool_letter_list, 2, [[3,-1], [3,1]])
    >>>bool_letter_list 
    ['False', 'Flase', True, True, True, 'False', 'Flase']
    
    cross_word_all_position_direction(bool_letter_list, 1, [[0,-1], [6,1]])
    >>>bool_letter_list
    [True, 'Flase', 'Flase', 'Flase', 'Flase', 'False', True]
    
    >>> cross_word_all_position_direction(bool_letter_list,2, [[0,1],[6,-1]])
    >>>bool_letter_list
    [True, True, 'Flase', 'Flase', 'Flase', True, True]
    
    
    """
    
    for each_position_direction in list_position_direction:
        cross_word_position_direction(bool_letter_list,length_word,
        each_position_direction[0],each_position_direction[1])
        

        
        
    
def find_magic_word(letter_list,bool_letter_list):
    """

    (list of letters, list of boolean values) -> string
    
    If both input lists are not of the same size, the function will raise a
    ValueError. The function goes through letter list from left to right and
    grouping all the characters where their corresponding value in bool
    letter list is False to construct and print the magic word
    
    
    Examples:
    >>> find_magic_word(['C','A','B','C','D','O','M','P'],
        [False,True,True,True,True,False,False,False])
    'COMP'
    >>> find_magic_word(['H','H','E','C','L','O','L','O'],
        [True,False,False,True,False,True,False,False])
    'HELLO'
    >>> find_magic_word(['M','H','E','C','L','G','L','O'],
        [False,True,False,True,True,False,True,True])
    'MEG'

    """
    
    
    if len(letter_list) != len(bool_letter_list):
        raise ValueError('Both lists should have the same size')
    
    magic_word =[]
    for index in range(len(letter_list)):
        if bool_letter_list[index] == False:
            magic_word.append(letter_list[index])
    
    
    return "".join(magic_word)
    
    
         
   
def word_search(letter_list,word_list):

    """
    (list of letters, list of words) -> string
    
    Function will go through each word in the list of words and calling
    both position direction word and cross word all position direction
    to find and then cross out all the words in the list. At the end,
    it will call find magic word and return the magic word
    
    Examples:
    >>> word_search(['C','W','I','K','I','P','E','D','I','A','O','M',
    'M','O','D','N','A','R','P'], ['WIKIPEDIA', 'RANDOM'])
    COMP
    >>>>>> word_search(['C','H','I','A','B','I','R','D','T'], ['HI', 'BIRD'])
    CAT
    >>> word_search(['F','I','O','L','O','V','E','O','Y','O','U','D'],
    ['I', 'LOVE','YOU'])
    FOOD


    """

    bool_letter_list = len(letter_list)*[False]
    
    for word in word_list: 
        list_position_direction = position_direction_word(letter_list,word)
        
        length_word = len(word)
        cross_word_all_position_direction(bool_letter_list,length_word,list_position_direction)
        
    return(find_magic_word(letter_list,bool_letter_list))
    


    
def word_search_main(letters,words):
    """
    (strings, list of strings) -> string
    
    Function will convert letters into list of characters, then create a
    word list using each word listed in words, seperated by a dash. The function
    then call word_search and return the magic word
    
    Examples:
    
    >>> letters = 'PjAVA++CJSYLQSPHPTGOHNILTOKOmatLABNTFIWSRUSTYBURTRAd'
    >>> words = 'java-C++-JS-SQL-php-GO-kotlin-MATLaB-SWIFT-RUSt-ruby-DART'
    >>> word_search_main(letters,words)
    PYTHON
    
    >>>letters = 'YcANyOUFINDeTHEMaGICswORD'
    >>>words = 'CaN-yOu-FinD-tHE-mAGIC-WoRD'
    >>>word_search_main(letters,words)
    YES
    
    >>>letters = 'FTVrifoodenisDGOoDs'
    >>>words = 'Tv-Food-is-good'
    >>>word_search_main(letters,words)
    Friends
    


    """

    letter_list= list(letters.upper())
    word_list = words.upper().split("-")
    return (word_search(letter_list,word_list))
    
    
#running code, feel free to change
letters = 'PjAVA++CJSYLQSPHPTGOHNILTOKOmatLABNTFIWSRUSTYBURTRAd'
words = 'java-C++-JS-SQL-php-GO-kotlin-MATLaB-SWIFT-RUSt-ruby-DART'
print(word_search_main(letters,words))