import asyncio
import random
import time
import json

random.seed(42)


async def dohvati_jelovnik(cekanje):
    print("Dohvatanje jelovnika...")
    await asyncio.sleep(cekanje)
    print("Jelovnik dohvaćen.")
    return [
        {"id": 1, "naziv": "Pizza Margherita", "cijena": 45.00},
        {"id": 2, "naziv": "Pasta Carbonara", "cijena": 55.00},
        {"id": 3, "naziv": "Salata Caprese", "cijena": 35.00},
    ]


async def dohvati_recenzije(cekanje):
    print("Dohvatanje recenzija...")
    await asyncio.sleep(cekanje)
    print("Recenzije dohvaćene.")
    return [
        {"gost": "Marko", "ocjena": 5, "komentar": "Odlična hrana!"},
        {"gost": "Hanna", "ocjena": 4, "komentar": "Dobar izbor jela."},
        {"gost": "Bob", "ocjena": 3, "komentar": "Prosječno iskustvo."},
    ]


async def dohvati_stolove(cekanje):
    print("Dohvatanje stolova...")
    await asyncio.sleep(cekanje)
    print("Stolovi dohvaćeni.")
    return [
        {"oznaka": "T1", "slobodna_mjesta": 4},
        {"oznaka": "T2", "slobodna_mjesta": 4},
        {"oznaka": "T3", "slobodna_mjesta": 8},
    ]


async def sekvencijalno(cekanja):
    start = time.perf_counter()

    jelovnik = await dohvati_jelovnik(cekanja["jelovnik"])
    recenzije = await dohvati_recenzije(cekanja["recenzije"])
    stolovi = await dohvati_stolove(cekanja["stolovi"])

    trajanje = time.perf_counter() - start
    return {"jelovnik": jelovnik, "recenzije": recenzije, "stolovi": stolovi}, trajanje


async def konkurentno(cekanja):
    start = time.perf_counter()

    jelovnik, recenzije, stolovi = await asyncio.gather(
        dohvati_jelovnik(cekanja["jelovnik"]),
        dohvati_recenzije(cekanja["recenzije"]),
        dohvati_stolove(cekanja["stolovi"]),
    )

    trajanje = time.perf_counter() - start
    return {"jelovnik": jelovnik, "recenzije": recenzije, "stolovi": stolovi}, trajanje


async def main():
    # nasumična vremena generiramo JEDNOM, prije mjerenja
    cekanja = {
        "jelovnik": random.uniform(1, 3),
        "recenzije": random.uniform(1, 3),
        "stolovi": random.uniform(1, 3),
    }

    print("Vrijeme čekanja:", {k: round(v, 2) for k, v in cekanja.items()})


    print("\nSekvencijalno:")
    rezultat_sek, t_sek = await sekvencijalno(cekanja)
    print(f"Trajanje: {t_sek:.2f} s")

    print("\nKonkurentno:")
    rezultat_kon, t_kon = await konkurentno(cekanja)
    print(f"Trajanje: {t_kon:.2f} s")

    print("\nIsti rezultat: ", rezultat_sek == rezultat_kon)

    with open("podaci.json", "w", encoding="utf-8") as f:
        json.dump(rezultat_kon, f, ensure_ascii=False, indent=2)


asyncio.run(main())
