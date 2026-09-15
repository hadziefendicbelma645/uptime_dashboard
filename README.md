# Real-time Chat Aplikacija

Jednostavna real-time chat aplikacija napravljena koristeći **Node.js**, **Express** i **Socket.IO**.

## Funkcionalnosti
- Dvosmjerna komunikacija u realnom vremenu preko WebSockets protokola.
- Automatsko dodjeljivanje nasumičnog korisničkog imena pri ulazu.
- Obavještenja kada se korisnik pridruži ili napusti chat.
- Indikator statusa konekcije (automatsko prepoznavanje prekida veze i ponovnog spajanja).

## Kako pokrenuti i testirati lokalno

1. **Instalacija zavisnosti:**
   Provjeri da imaš instaliran Node.js, pa u terminalu pokreni:
   ```bash
   npm install

   Pokretanje servera:
   npm start
   Testiranje lokalno (sa dva prozora)
   Pokreni server u terminalu:
   npm start

   Otvori prvi prozor: Pokreni preglednik (Chrome, Firefox, Edge) i otvori http://localhost:3000. Automatski će ti biti dodijeljeno ime (npr. Korisnik_123) a status gore desno će postati zeleni Online.

Otvori drugi prozor: Otvori novi prozor pretraživača ili Inkognito/Private prozor te idi na istu adresu http://localhost:3000. Vidjet ćeš sistemsku poruku da se novi korisnik pridružio.

Testiraj real-time poruke: Piši poruku u prvom prozoru i pritisni Pošalji – poruka se trenutno prikazuje u drugom prozoru (i obratno).

Testiraj puknuće veze (Disconnect / Reconnect):

Ugasi server u terminalu pritiskom na Ctrl + C. Status u oba prozora će se promijeniti u crveni (Veza pukla / Ponovno spajanje....)

Ponovo pokreni server sa npm start. Socket.IO će se automatski ponovo povezati i status će se vratiti na Online.
