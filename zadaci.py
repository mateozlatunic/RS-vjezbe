
import asyncio
import random
import time

"""
Zadatak 1:
    - kreirati korutinu i ispisati listu brojeva od 1 do 10 nakon 3 sekunde.
    - listu definirati comprehensionom, te u korutini ispisati poruku: Podaci dohvaćeni.
"""

async def dohvacanje_podataka():
    await asyncio.sleep(3)  
    podaci = [broj for broj in range(1, 11)]
    print("Podaci dohvaćeni.")
    return podaci

async def main():
    rezultat = await dohvacanje_podataka()
    print(rezultat)

asyncio.run(main())






"""
Zadatak 2:
    - definirati dvije korutine 
    - jedna korutina nakon 3s vraca listu korisnika, dok druga nakon 5s vraca listu proizvoda
    - koristiti asyncio.gather(), zatim ispisati liste
"""

async def rijecnik_korisnika():
    await asyncio.sleep(3)
    return [
        {"id": 343, "ime": "Silvestar", "email": "silver5@gmail.com"},
        {"id": 12, "ime": "Anabel", "email": "bela3@gmail.com"},
        {"id": 8, "ime": "Kevin", "email": "kec1@gmail.com"},
        {"id": 66, "ime": "Ira", "email": "ira@gmail.com"},
        {"id": 117, "ime": "Laki", "email": "laki6@gmail.com"}
    ]

async def rijecnik_proizvoda():
    await asyncio.sleep(5)
    return [
        {"id": 343, "naziv": "Laptop", "cijena": 754.99},
        {"id": 12, "naziv": "Miš", "cijena": 15.99},
        {"id": 8, "naziv": "Zaslon", "cijena": 100.99},
        {"id": 66, "naziv": "Pojacalo", "cijena": 35.99},
        {"id": 117, "naziv": "Mobitel", "cijena": 314.99}
    ]

async def main():
    start = time.perf_counter()

    korisnici, proizvodi = await asyncio.gather(
        rijecnik_korisnika(), rijecnik_proizvoda()
    )

    for k in korisnici:
        print(k)

    for p in proizvodi:
        print(p)

    print(f"Trajanje: {time.perf_counter() - start:.1f} s") 

asyncio.run(main())






"""
Zadatak 3:
    - definirati korutinu autentifikacija() koja simulira autentifikaciju korisnika
    - korutina kao parametar prima rijecnik korisnik koji sadrzi korisnicko_ime, email i lozinku
    - korutina nakon 3s provjerava da li se korisnik nalazi u bazi
        - ako validno, poziva se druga korutina autorizacija() koja nakon 2s provjerava da li je lozinka ispravna
"""

baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]


async def autorizacija(korisnik_baze, lozinka):
    await asyncio.sleep(2)  

    for zapis in baza_lozinka:
        if zapis['korisnicko_ime'] == korisnik_baze['korisnicko_ime']:
            if zapis['lozinka'] == lozinka:
                return f"Korisnik {korisnik_baze['korisnicko_ime']}: Autorizacija uspješna."
            break

    return f"Korisnik {korisnik_baze['korisnicko_ime']}: Autorizacija neuspješna."


async def autentifikacija(korisnik):
    print(f"Provjera korisnika: {korisnik['korisnicko_ime']}...")

    await asyncio.sleep(3)  

    for zapis in baza_korisnika:
        if (zapis['korisnicko_ime'] == korisnik['korisnicko_ime']
                and zapis['email'] == korisnik['email']):
            return await autorizacija(zapis, korisnik['lozinka'])

    return f"Korisnik {korisnik['korisnicko_ime']}: Autentifikacija neuspješna."


async def main():
    korisnik = {
        'korisnicko_ime': 'mirko123',
        'email': 'mirko123@gmail.com',
        'lozinka': 'lozinka123'
    }
    rezultat = await autentifikacija(korisnik)
    print(rezultat)

asyncio.run(main())






"""
Zadatak 4:
    - definirati korutinu provjeri_parnost() koja prima broj i nakon 2s provjerava da li je paran ili neparan
    - koristiti asyncio.gather() za provjeru parnosti 10 nasumicnih brojeva
    - ispisati rezultate
"""

async def provjeri_parnost(broj):
    await asyncio.sleep(2)  
    if broj % 2 == 0:
        return f"Broj {broj} je paran."
    return f"Broj {broj} je neparan."


async def main():
    brojevi = [random.randint(1, 100) for _ in range(10)]

    zadaci = [asyncio.create_task(provjeri_parnost(broj)) for broj in brojevi]

    rezultati = await asyncio.gather(*zadaci)

    for rezultat in rezultati:
        print(rezultat)

asyncio.run(main())






"""
Zadatak 5:
    - definirati korutinu secure_data() koja prima osjetljive podatke i nakon 3s enkriptira broj kartice i CVV
    - koristiti asyncio.gather() za enkripciju 3 osjetljivih podataka
    - ispisati rezultate
"""

async def secure_data(podaci):
    await asyncio.sleep(3)  
    return {
        'prezime': podaci['prezime'],
        'broj_kartice': hash(podaci['broj_kartice']),
        'CVV': hash(podaci['CVV'])
    }

async def main():
    osjetljivi_podaci = [
        {'prezime': 'Bojka', 'broj_kartice': '424424424424424', 'CVV': '666'},
        {'prezime': 'Dimitrijski', 'broj_kartice': '585858585858585858', 'CVV': '777'},
        {'prezime': 'Novica', 'broj_kartice': '7676767676767676', 'CVV': '888'}
    ]

    zadaci = [asyncio.create_task(secure_data(podaci)) for podaci in osjetljivi_podaci]

    rezultati = await asyncio.gather(*zadaci)

    for rezultat in rezultati:
        print(rezultat)

asyncio.run(main())






"""
Zadatak 6:
    - main ceka task1, dok asyncio.run() otkazuje zadatke koji nisu dovrseni
    - task2 se ne dovrsava, jer main ceka samo task1, a task2 traje 2 sekunde
    - main stoga mora cekati task2, optimalno 1.5s da se moze dovrsiti
"""

async def fetch_data(param):
    print(f"Nešto radim s {param}...")
    await asyncio.sleep(param)
    print(f'Dovršio sam s {param}.')
    return f"Rezultat za {param}"

async def main():
    task1 = asyncio.create_task(fetch_data(1)) 
    task2 = asyncio.create_task(fetch_data(2)) 
    result1 = await task1
    print("Fetch 1 uspješno završen.")
    # -> await asyncio.sleep(1.5) <-
    return [result1]

t1 = time.perf_counter()
results = asyncio.run(main())
t2 = time.perf_counter()
print(results)
print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")





"""
Zadatak 7:
    - asyncio.run(main()) stvara event loop i pokrece main()
    - main poziva create_task(), pri cemu se timeri samo zakazuju
    - na await gather(*timers) main zapocinje cekati i kontrolu preuzima event loop
    - event loop redom pokrece timer 1, 2 i 3
        - svaki ispisuje poruku i na await asyncio.sleep(1) se suspendira
    - svake sekunde timeri se probude, ispisuju preostalo vrijeme i opet zaspu, u meduvremenu petlja samo ceka
    - timeri imaju razlicit broj iteracija pa zavrsavaju u različito vrijeme
        - Timer 1 nakon 3s, Timer 2 nakon 5s, Timer 3 nakon 7s
    - kad zavrsi zadnji timer, gather vraća rezultate, main se nastavlja i zavrsava, a event loop zatvara
    - ukupno traje 7s (ne 15 s) jer se čekanja preklapaju
"""

async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        await asyncio.sleep(1)
    print(f'{name}: Vrijeme je isteklo!')

async def main():
    timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
    ]

    await asyncio.gather(*timers)

asyncio.run(main())