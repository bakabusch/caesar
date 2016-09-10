
from sys import argv, exit
from helpers import alphabet_position, rotate_character


#def user_input_is_valid(cl_args):
#    if len(argv) < 2:
        #print('usage: python3 caesar.py n')
        #exit()
#    elif argv[1].isdigit() == False:
        #print('usage: python3 caesar.py n')
        #exit()

#    else:
#        print('I know that these are the words the user typed on the command line: ', argv)

#user_input_is_valid(argv)
#print('I know that these are the words the user typed on the command line: ', argv)
#rot = int(argv[1])
#text = input('Type a message: \n' )

def encrypt(scram, rot):
    krypto = ""
    for i in scram:
        if i.isalpha():
            krypto += rotate_character(i , rot)
        else:
            krypto += i
    return krypto

#print(encrypt(text, rot))
