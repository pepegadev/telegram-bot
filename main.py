import os
import telethon
from telethon.sync import TelegramClient
from telethon import functions
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors import SessionPasswordNeededError
import getpass
import time




api_id =input("id has")
api_hash =input("api hash")
phone =input("put phone number with +")




# Your Api ID
# Your Api Hash
# Your Phone Number With Country Code.

client = TelegramClient(phone, api_id, api_hash)

client.connect()

chats = []
last_date = None
chunk_size = 1000
groups = []
empty=""
dc=0


def group_scanner():
    chats = []
    last_date = None
    chunk_size = 1000
    groups = []

    result = client(GetDialogsRequest(
        offset_date=last_date,
        offset_id=3000,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash=3000
    ))
    chats.extend(result.chats)
    f2 = open("groups.txt", "a")
    d = 0
    test = []
    for chat in chats:
        if chat.title not in test:
            try:
                # print(chat)
                test.append(chat.title)

                f2.write(str(chat.title) + '\n')

                # if chat.megagroup== True:
            except:
                continue

    f2.close()


def invite():
    grop = input("please drag the list to add to new groups :)\n")
    file = open(grop, "+r")
    for x in file:
        try:

            name = client.get_entity(x)
            d = (client(functions.channels.JoinChannelRequest(name)))
            print("added ==>" + x)

        except Exception as  e:
            print(e.args)

        time.sleep(60)
    input("done")


# print(str(i) + '- ' + g.title)
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone)
    try:
        client.sign_in(code=input('Enter code: '))
    except SessionPasswordNeededError:
        client.sign_in(password=getpass.getpass())

t1 = input("how much timeout in each requests prefer 60s")
t2 = input("how much timeout in each cycle prefer 1h=3600")


def send_msg_to_group():
    d = ""
    count = 0
    # msg1=open("msg.txt","+r")
    msg = input("the name of channel just copy the msg that you want to forward to past it here \n")
    result = client(GetDialogsRequest(
        offset_date=last_date,
        offset_id=50000000,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash=30000000000))

    for dialog in client.iter_dialogs():
        if dialog.is_channel:
            print(f'{dialog.id}:{dialog.title}')
            if dialog.title=="free marketplace for all":
                messa=client.get_messages(dialog.id,limit=1)


    input()
    while True:
        count = count + 1

        print("cycle number " + str(count))
        for dialog in client.iter_dialogs():
            try:
                client.forward_messages(client.get_entity(dialog.id),messa)
                print(f'Sent==> {dialog.title}')
                time.sleep(int(t1))

            except Exception as error:
                print(error)
                try:
                    empty=""
                    for i in range(len(error)):
                        if (error[i].isdigit()):
                            empty = str(empty + error[i])
                    if(empty!=""):
                        print("error waiting "+empty)
                        time.sleep(int(empty))
                except:
                    continue


        print("waiting the timeout")
        time.sleep(int(t2))

