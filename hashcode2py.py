from simplecrypt import *
from tkinter import *
from firebase import firebase

firebase = firebase.FirebaseApplication("https://encrypt-decrept-default-rtdb.firebaseio.com", )

login_window = Tk()
login_window.geometry("394x403")
login_window.config(bg='#367f79')

username = ''
your_code = ''
your_friends_code = ''
message_text = ''
message_entry = ''
last_value = ''

def getData():
    global message_text
    global last_value
    global your_code
    global your_friends_code
    get_your_data = firebase.get('/', your_code)
    print(get_your_data)
    byte_str = bytes.fromhex(get_your_data)
    original = decrypt('AIM', byte_str)
    print("original data",original)
    final_message = original.decode("utf-8")
    print(final_message)
    message_text.insert(END, final_message+"\n")
    
    get_friends_data = firebase.get('/', your_friends_code)
    if(get_friends_data !=None):
        print("data : ",get_friends_data)
        byte_str = bytes.fromhex(get_friends_data)
        original = decrypt('AIM', byte_str)
        final_message = original.decode("utf-8")
        if (final_message not in last_value):
            print(final_message)
            message_text.insert(END, final_message+"\n")
            last_value = final_message
            
def sendData():
    global username
    global message_entry
    global your_code
    message = username+ " : "+message_entry.get()
    ciphercode = encrypt('AIM', message)
    hex_string = ciphercode.hex()
    put_date = firebase.put("/", your_code, hex_string)
    print(put_date)
    getData()