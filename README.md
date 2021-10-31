# Minecraft-Server-Hledac
Czech translated version of "Minecraft-Server-Scanner" by Footsiefat.

Tento program prohledá celý internet za pár hodin aby identifikoval všechny Minecraftové servery na ip adrese typu IPV4.

Instalace a instrukce jsou tady:

---
sudo apt install masscan (Nebo jiný distro specifický příkaz)
wget https://raw.githubusercontent.com/robertdavidgraham/masscan/master/data/exclude.conf
sudo masscan -p25565 0.0.0.0/0 --max-rate <maxrate> --excludefile exclude.conf -oL masscan.txt (Nastavte max-rate posílání packetů na limit se kterým jste komfortní. Doporučeno: 1500)

pip3 install mcstatus
python3 mcscanner.py
---

Poté odpovídejte na otázky co se na vás program zeptá (Pro filtrování veřejných serverů můžete použít soubor public.txt ale už bude trochu zastaralý)
Zmáčkněte enter a počkejte než program posbírá všechna data pro servery co byly nalezeny, pokud tohle bude hotové, budete mít masivní množství MC serverů (hodně z nich budou privátní) na hraní s nimi. Výstupový soubor obsahuje IP adresy, verze a hráči co hrají na serveru.
  
UPOZORNĚNÍ: TENHLE PROGRAM JE JEN PRO EDUKATIVNÍ DŮVODY, TVŮRCE NENÍ ZODPOVĚDNÝ ZA ZNEUŽITÍ TOHOHLE PROGRAMU!

 
Program modified and translated by Lojstr / Program upravil a přeložil Lojstr
Program made by Footsiefat. All rights go to him. (Original repository here: https://github.com/Footsiefat/Minecraft-Server-Scanner)
