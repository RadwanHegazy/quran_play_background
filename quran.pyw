# import packeges
import sqlite3, requests, os, win32api
from playsound import playsound
from time import sleep


# set the file which will save the quran AYAs
drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]

db_path = f'{drives[1]}aya.txt'

try :
    with open(db_path, mode='r') as check :
        check.read()
        check.close()
        
except FileNotFoundError :
    with open(db_path, mode='w') as check :
        check.write('1')
        check.close()





# access aya file read and write 
def aya_file (**info) : 


    with open (info['db_path'], info['mode']) as aya :

        if info['mode'] == 'r' :
            return aya.read()

        else :
            aya.write(info['aya_number'])
            




# fuction that return mp3 url 
def create_audio (url) :
    return "https://verses.quran.com/" + url



# number of AYAs which it will said
loop = 20



# Say Aya Function
def SayAya(aya) :
    

    if aya < 6236 : 
    


        try : 
            # play the sound of the aya
            for i in range(0,loop) :
                
                # play the sound of aya
                main_url = f"https://api.quran.com/api/v4/recitations/7/by_ayah/{ aya }"

                req = requests.get(main_url).json()

                # sound url
                audio_link = create_audio(req['audio_files'][0]['url'])

                # play the sound
                playsound(audio_link)

                # save the last aya
                aya_file(db_path=db_path,mode='w',aya_number=f'{aya + 1}')
                

                aya = aya + 1 
            
        except :
            pass
    
    else :
        aya_file(db_path=db_path,mode='w',aya_number=f'1')
    


while True :

    # get last aya number
    last_aya = aya_file(db_path=db_path,mode='r')
    

    SayAya(int(last_aya))

    half_an_hour = 60 * 30
    
    sleep( half_an_hour )
