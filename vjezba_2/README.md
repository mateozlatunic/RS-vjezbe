
### Vježba 2 - Priprema podataka za web-aplikaciju
---

<br>

#### Opis podataka i operacija

- program simulira dohvaćanje podataka za web-aplikaciju restorana iz tri neovisna izvora. 
- simulira se pomoću `asyncio.sleep()`, a podaci su definirani unutar programa.
- sadrži tri korutine, te ispisuje poruku za svoju početnu i krajnju vremensku fazu trajanja.

<br>

#### Korutine i vrijeme čekanja

- `dohvati_jelovnik(cekanje)` - 2.28s
- `dohvati_recenzije(cekanje)` - 1.05s
- `dohvati_stolove(cekanje)` - 1.55s

<br>

- izvršava se na dva načina:
  - sekvencijalno: svaka korutina se čeka s `await` prije pokretanja sljedeće
  - konkurentno: sve tri se pokreću zajedno pomoću `asyncio.gather()`

<br>

- Sekvencijalno izvođenje: 4.88 s
- Konkurentno izvođenje: 2.28 s

<br>

#### Rezultat

- lista jela: `id`, `naziv` i `cijena`
- lista recenzija: `gost`, `ocjena` i `komentar`
- lista stolova: `oznaka` i `slobodna mjesta`

<br>

#### Važno je znati
  - sekvencijalna obrada traje duze, jer se funkcije izvršavaju jedna za drugom
  - svaki njezin `await` se mora završiti prije nego što se pozove sljedeća korutina, pa se čekanja zbrajaju
  - konkurentna obrada traje kraće, jer se funkcije izvršavaju paralelno
  - `await asyncio.gather()` omogućuje da se sve korutine pokrenu istovremeno
  - sekvencijalna operacija se ne započinje dok se prethodna ne završi
  - konkurentno se sve operacije započinju, a čekanja se preklapaju
  - zamijenom `asyncio.sleep` sa `time.sleep` konkurentna obrada postaje jednako spora kao i sekvencijalna obrada, jer `asyncio.sleep` ne uspavljuje dretvu, dretva je cijelo vrijeme slobodna za rad na drugim korutinama
  - `gather()` rezultate uvijek vraća redoslijedom kojim su korutine proslijeđene, a ne redoslijedom dovršavanja.

<br>
