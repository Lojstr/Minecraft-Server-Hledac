# Minecraft-Server-Hledac
Czech translated version of "Minecraft-Server-Scanner" by Footsiefat.

Tento program prohledá celý internet za pár hodin aby identifikoval všechny Minecraftové servery na ip adrese typu IPV4.

Instalace a instrukce jsou tady:





1) sudo apt install masscan (Nebo jiný distro specifický příkaz)
2) wget https://raw.githubusercontent.com/robertdavidgraham/masscan/master/data/exclude.conf
3) sudo masscan -p25565 0.0.0.0/0 --max-rate <maxrate> --excludefile exclude.conf -oL masscan.txt (Nastavte max-rate posílání packetů na limit se kterým jste komfortní. Doporučeno: 1500)

4) pip3 install mcstatus
5) python3 mcscannerCZ.py

  
  
  

Poté odpovídejte na otázky co se na vás program zeptá (Pro filtrování veřejných serverů můžete použít soubor public.txt ale už bude trochu zastaralý)
Zmáčkněte enter a počkejte než program posbírá všechna data pro servery co byly nalezeny, pokud tohle bude hotové, budete mít masivní množství MC serverů (hodně z nich budou privátní) na hraní s nimi. Výstupový soubor obsahuje IP adresy, verze a hráči co hrají na serveru.
  
UPOZORNĚNÍ: TENHLE PROGRAM JE JEN PRO EDUKATIVNÍ DŮVODY, TVŮRCE NENÍ ZODPOVĚDNÝ ZA ZNEUŽITÍ TOHOHLE PROGRAMU!

 
Program modified and translated by Lojstr / Program upravil a přeložil Lojstr
Program made by Footsiefat. All rights go to him. (Original repository here: https://github.com/Footsiefat/Minecraft-Server-Scanner)
  
  
MOTD Update coming soon - waiting for the original author.
