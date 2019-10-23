#!/bin/python
from json import load
#we need json.load() function to store json data as a dictionary

"""
################################################################################
# Developed by zanamziry720@gmail.com                                          #
# i only tested this code on one file, im not sure if its gonna work perfectly #
# and sorry for the ugly code, im not a pro programmer tbh LoL                 #
################################################################################

printConv() function prints the conversation you want to select
because every DM haves a number
for example i had a DM with a friend named tony
and the number of the DM with tony is 1
i need to print jsondata[1]['conversation']
to get the conversation between me and tony
"""
def printConv(jsdata,convNum):
    jsdata[convNum]['conversation'].reverse()
    if len(jsdata[convNum]['conversation'])<1:
        print("Empty")
    for i in jsdata[convNum]['conversation']:
        if 'media' in i:
            print(i['sender'],":",i['media'])
        if 'text' in i:
            print(i['sender'],":",i['text'])
        if 'voice_media' in jsdata[convNum]['conversation']:
            print(i['sender'],":",i['voice_media'])
        if 'story_share' in jsdata[convNum]['conversation']:
            print(i['sender'],":",i['story_share'])
        if 'media_share_url' in jsdata[convNum]['conversation']:
            print(i['sender'],":",i['media_share_url'])

"""
this function imports all the usernames you DMed from the message.json
and returns a list variable
to get usernames of a conversation you need to print jsondata[num]['participants']
"""
def getNames(jsdata):
    users=[]
    for i in range(len(jsdata)):
        if 'participants' in jsdata[i]:
            if len(jsdata[i]['participants'])>2:
                groupname='group'+str(i)
                users.append(groupname)
            elif len(jsdata[i]['participants'])<3 and not 0:
                for j in jsdata[i]['participants']:
                    users.append(j)
    un=""
    for i in users:
        if users.count(i) >= len(jsdata)-1:
            un=i
    while(users.count(un)>0):
        users.remove(un)
    return users

if __name__ == '__main__':
    js = load(open("messages.json")) #change this to the direction of your json file
    DMS = getNames(js)
    print("Directs:")
    getNames(js)
    for i in range(len(DMS)):
        print(i,"-",DMS[i])
    cn = int(input("choose a Conversation:"))
    printConv(js,cn)
