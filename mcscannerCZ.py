from mcstatus import MinecraftServer
import os
import math
import threading
import time

masscan = []




print('Multiprocesovy minecraft server hledac by Footsiefat (prelozil Lojstr)')

time.sleep(1)

inputfile = input('Jaky je nazev souboru s ip adresama (I s .txt): ')

outputfile = input('Jaky je nazev souboru kde se ulozi IP adresy? (I s .txt): ')

publicserverlist = input('Jaky je nazev souboru s verejnymi IP adresami? (I s .txt): ')

searchterm = input('Jakou verzi MC serveru hledate? Nechejte nic pro vsechny verze): ')

outfile = open(outputfile, 'a+')
outfile.close

fileHandler = open (inputfile, "r")
listOfLines = fileHandler.readlines()
fileHandler.close()

for line in listOfLines:
    if line.strip()[0] != "#":
        masscan.append(line.strip().split(' ',4)[3])



def split_array(L,n):
    return [L[i::n] for i in range(n)]


threads = int(input('Kolik procesu chcete pouzit? (Doporuceno: 20): '))

time.sleep(2)

if len(masscan) < int(threads):
    threads = len(masscan)


split = list(split_array(masscan, threads))

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print ("Starting Thread " + self.name)
        print_time(self.name)
        print ("Exiting Thread " + self.name)

def print_time(threadName):
    for z in split[int(threadName)]:
        if exitFlag:
            threadName.exit()
        try:
            ip = z
            server = MinecraftServer(ip,25565)
            status = server.status()
        except:
            print("Chyba pri pingovani serveru: " + ip)
        else:
            print("Server nalezen: " + ip + " " + status.version.name + " " + str(status.players.online))
            if searchterm in status.version.name:
                with open(outputfile) as f:
                    if ip not in f.read():
                        with open(publicserverlist) as g:
                            if ip not in g.read():
                                text_file = open(outputfile, "a")
                                text_file.write(ip + " " + status.version.name.replace(" ", "_") + " " + str(status.players.online))
                                text_file.write(os.linesep)
                                text_file.close()


for x in range(threads):
    thread = myThread(x, str(x)).start()
