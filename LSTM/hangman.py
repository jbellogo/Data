# f = open("/mnt/storage/home/jbellogo/TrexQuant/words_250000_train.txt", "r")
# mydict = {}

# for w in f:
#     key = len(w)-1
#     # ##### Get carinalities. 
#     # if key in mydict: 
#     #     mydict[key] +=1
#     # else:
#     #     mydict[key] = 1
#     ##### Partition universe into length
#     g = open(f"words_by_length/length-{key}.txt", "a")
#     g.write(w)
#     g.close()


# # 28 different word lengths. 
# word_len_frequency = {
#     3: 2201, 6: 19541, 4: 5287, 5: 11274, 8: 30452, 7: 25948,
#  10: 26953, 9: 30906, 11: 22786, 12: 18178, 13: 12956, 15: 5211,
#  14: 8710, 20: 225, 17: 1775, 16: 3143, 2: 264, 21: 98, 18: 859,
#  19: 441, 25: 3, 22: 44, 1: 17, 23: 14, 29: 2, 24: 9, 28: 1, 27: 2}

# HELPERS 
def contains_ALL_letters(letters, word):
    for l in letters:
        if l not in word:
            return False 
    return True 

def contains_NO_letters(letters, word):
    for l in letters:
        if l in word:
            return False 
    return True 


contains_ALL_letters('abcdk', "hello a son b edddf c")
# contains_NO_letters("ab0", "helldedeefeco")

# Calculate Letter Distributions: 
def get_new_universe(wlen, correct, incorrect, parent, level):
    '''
    should not create a new one once there is only one word!
    if universe length==1 simplify things.
    '''
    newfile = f"./support/universe_depth={level}.txt"
    with open(parent, "r") as parent_file:
        with open(newfile, "w") as g:
            for word in parent_file:
                if contains_ALL_letters(correct, word) and contains_NO_letters(incorrect, word):
                    g.write(word)
    return newfile


def guess_next_letter(universe, used):
    '''
    calculates distributions, keeping the mode letter to be returned. 
    gets next highest frequency letter until there is an unused one. 
    '''
    ## Calculates frequencies. 
    f = open(universe,"r")
    alph = {} # alphabet
    COUNT = 0
    word = ""

    for w in f:
        word = w
        COUNT +=1
        for letter in w:
            if letter in alph:
                alph[letter] += 1
            else:
                if letter != '\n' and letter not in used:
                    alph[letter] = 1
    #####3
    if COUNT == 1:
        for letter in word:
            if letter in "abcdefghijklmnopqrstuvwxyz" and letter not in used:
                return letter
    f.close()
        
    ### guess the highest frequency
    max_key = 0
    for key, freq in alph.items():
        
        if max_key == 0:
            max_key = key
        else:
            if alph[max_key] < freq:
                max_key = key
    ## if it returns 0 then you are done! guessed all the letters. 
    return max_key
        

# guess_next_letter("words_by_length/length-23.txt")
    
def try_guess(word, guess):
    print(guess)
    print(word)
    return guess in word


def guess(word):
    wlen = len(word)
    correct, incorrect = "", ""
    def make_guess(universe):
        nonlocal correct
        nonlocal incorrect
        guess = guess_next_letter(universe, correct)
        if guess == 0:
            print("GAME OVER, WON")
            return
        guess_result = try_guess(word, guess)
        if guess_result:
            correct+=guess
            print("CORRECT GUESS")
        else:
            incorrect+=guess
            print("INCORRECT GUESS")
            
    universe = f"words_by_length/length-{wlen}.txt"
    i=1
    make_guess(universe)
    while len(correct) != wlen:
        print("==============")
        print(f"correct: {correct}")
        print(f"incorrect: {incorrect}")
        universe = get_new_universe(wlen, correct, incorrect, universe, i)
        print(f"NEW universe: {universe}")
        make_guess(universe)
        i+=1
        
## we shouldnt add repeated guesses 
## we neeed to cycle through guesses
