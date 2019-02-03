from sys import exit
from string import whitespace
user_letter = input('Enter between 3 and 10 lowercase letters: ')
number_of_letter = 0
user_letter_list = []
for i in user_letter:
    if not (i.islower() or i == ' '):
        print('Incorrect input, giving up...')
        exit()
    if i.islower():
        number_of_letter +=1
        user_letter_list.append(i)
if not number_of_letter in range(3,11):
    print('Incorrect input, giving up...')
    exit()
user_letter = ''.join(i for i in user_letter_list)    

letters = 'abcdefghijklmnopqrstuvwxyz'
score = '25441655176352357212466757'
dictionary = {}
for i in range(len(letters)):
    dictionary[letters[i]] = score[i]
with open('wordsEn.txt','r') as f:
    content = f.readlines()
dic_words = []
user_letter_copy = user_letter
for i in content:
    i = i.strip('\n')
    for j in i:      
       if j in user_letter_copy:
           user_letter_copy = list(user_letter_copy)
           user_letter_copy.remove(j)
           user_letter_copy = ''.join(k for k in user_letter_copy)
       else: 
            break
    else:
        dic_words.append(i)
    user_letter_copy = user_letter
score_result = 0
score_result_dict = {}
if dic_words:
    for i in dic_words:
        for j in i:
            score_result += int(dictionary[j])
        score_result_dict[i] = score_result
        score_result = 0
    highest_keys = [x for x,y in score_result_dict.items() if y == max(score_result_dict.values())]
    highest_keys.sort()
    print('The highest score is {}'.format(max(score_result_dict.values())))
    if len(highest_keys) == 1:
        print('The highest scoring word is {}'.format(highest_keys[0]))
    else:
        print('The highest scoring word are, in alphabetical order:')
        for i in highest_keys:
            print('    {}'.format(i))
else:
    print('No word is built from some of those letters.')

        
        
        
        
