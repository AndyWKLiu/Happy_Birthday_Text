#IMPORTANT this works for MacBooks only 
import os 

def Get_Happy_Birthday_Text(file_path):
    with open(file_path, 'r') as x:
        text = x.readlines()[0]
    return text

def send_message(phone_number, message):
    os.system('osascript send.scpt {} "{}"' .format(phone_number, message))

if __name__ == '__main__':
    #input phone number between the two floating commas :D
    phone_number = ''
    text = Get_Happy_Birthday_Text('birthday.txt')
    send_message(phone_number, text)