import requests
from requests.structures import CaseInsensitiveDict
import threading
import ctypes

url = 'https://docs.google.com/forms/u/1/d/e/1FAIpQLSe_l-EcfP5soISz-tCGjuyTWJgloGerTZQawjT2Q1fFAbjc1Q/viewform'
url2 = 'https://docs.google.com/forms/u/1/d/e/1FAIpQLSe_l-EcfP5soISz-tCGjuyTWJgloGerTZQawjT2Q1fFAbjc1Q/formResponse'
form_data = {"entry.44366011":"Homme","fvv":1,"draftResponse":'[]',"pageHistory":0,"fbzx":-6718008993703688486}
nb_vote = 0;

def loop1_10():
    
    for i in range(0,int(nb_vote_final/nb_thread)):
        global nb_vote;
        ctypes.windll.kernel32.SetConsoleTitleW("GOOGLE FORMS CHEAT | Made by Asgal | Nombre de vote fait : "+ str(nb_vote) + "/"+str(nb_vote_final))
        s = requests.Session()
        s.get(url)
        r = s.post(url2, data=form_data)
        nb_vote+=1
        print("Nombre de vote fait : "+ str(nb_vote))
        i=+1
    
nb_vote_final = int(input("Combien de vote voulez vous ? :"))
nb_thread = int(input('Combien de thread voulez vous ? :'))    
for j in range(0,nb_thread):
    threading.Thread(target=loop1_10).start()