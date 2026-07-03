# Provisionsabrechnung KaffeeKlatsch Wallis AG — April bis Juni 2026
#
# Regeln:
# - Provisionssatz pro Objekt und Monat: Brutto-Monatsumsatz (vor Portal-Kommission)
#   bis CHF 1'600 -> 5 %, über CHF 1'600 -> 10 %
# - Provisionsbasis pro Buchung: Buchungswert ./. Portal-Kommission ./. Reinigungspauschale
#   (Studio CHF 100, Apartment CHF 130)
# - Airbnb zahlt netto aus (Servicegebühr bereits abgezogen): Basis = Auszahlung ./. Pauschale,
#   Brutto für Schwelle = Bruttoeinkünfte
# - Monatszuordnung: Abreise-/Check-out-Monat (entspricht der Rechnungsperiode von Booking.com)
# - Stornierte Buchungen (Betrag 0) ausgeschlossen; Zahlungsgebühr Booking.com nicht abgezogen
# - Buchung 6692826989 (Kolb, Abreise 01.04.) weggelassen: bereits mit März abgerechnet
# - Buchung 5147963708 (Passant, Abreise 03.07.) folgt mit der Juli-Abrechnung

from collections import defaultdict

CLEAN = {"Studio": 100.0, "Apartment": 130.0}

# (Monat, Objekt, Portal, Gast, Zeitraum, Brutto, Kommission, Auszahlung/Netto vor Pauschale)
# Booking.com: Netto = Brutto - Kommission ; Airbnb: Netto = Auszahlung (Kommission = Servicegebühr)
bookings = [
    # ---- April 2026 ----
    ("2026-04", "Studio",    "Booking.com", "Michel Corpataux",            "03.04.–06.04.", 342.76, 41.13),
    ("2026-04", "Apartment", "Booking.com", "Suzanne Caliendo",            "06.04.–08.04.", 395.68, 47.48),
    ("2026-04", "Apartment", "Booking.com", "Johannes Schneider",          "12.04.–16.04.", 482.24, 57.87),
    ("2026-04", "Apartment", "Booking.com", "Fabian Jenelten",             "18.04.–20.04.", 291.12, 34.93),
    ("2026-04", "Apartment", "Airbnb",      "Nicole Meier",                "02.04.–04.04.", 481.20, 80.65),
    ("2026-04", "Apartment", "Airbnb",      "Russell Stott",               "21.04.–28.04.", 953.20, 159.70),
    ("2026-04", "Studio",    "Airbnb",      "Markus Spillmann",            "21.04.–23.04.", 292.00, 48.90),
    # ---- Mai 2026 ----
    ("2026-05", "Apartment", "Booking.com", "Veronique Mauron Frank",      "14.05.–17.05.", 676.00, 81.12),
    ("2026-05", "Studio",    "Booking.com", "Manuela Schön Bachmann",      "16.05.–18.05.", 319.02, 38.28),
    ("2026-05", "Studio",    "Booking.com", "David Kirchner",              "19.05.–21.05.", 377.68, 45.32),
    ("2026-05", "Apartment", "Booking.com", "Uli Kausche",                 "29.05.–31.05.", 388.58, 46.63),
    ("2026-05", "Studio",    "Booking.com", "Christina Siffert",           "29.05.–31.05.", 319.02, 38.28),
    ("2026-05", "Studio",    "Airbnb",      "Bella Abrego",                "27.04.–01.05.", 624.00, 104.55),
    ("2026-05", "Apartment", "Airbnb",      "Dóra Domboróczky",            "30.04.–03.05.", 537.00, 90.00),
    ("2026-05", "Studio",    "Airbnb",      "Lionel Müller",               "01.05.–03.05.", 400.00, 67.00),
    ("2026-05", "Studio",    "Airbnb",      "Richard Wadsworth",           "14.05.–16.05.", 268.00, 44.90),
    ("2026-05", "Studio",    "Airbnb",      "Melody Fanning",              "21.05.–22.05.", 190.00, 31.85),
    ("2026-05", "Studio",    "Airbnb",      "Frank Diener",                "22.05.–24.05.", 280.00, 46.90),
    ("2026-05", "Apartment", "Airbnb",      "Elisabeth Reutimann",         "22.05.–28.05.", 1234.00, 206.75),
    ("2026-05", "Studio",    "Airbnb",      "Paul Warpeha",                "25.05.–27.05.", 301.60, 50.55),
    # ---- Juni 2026 ----
    ("2026-06", "Studio",    "Booking.com", "Ronald Cordier",              "04.06.–07.06.", 465.04, 55.80),
    ("2026-06", "Studio",    "Booking.com", "Chiu Kwan Lam",               "13.06.–14.06.", 219.34, 26.32),
    ("2026-06", "Studio",    "Booking.com", "Kai Choy Wong",               "14.06.–18.06.", 474.40, 56.93),
    ("2026-06", "Studio",    "Booking.com", "Katrin Koyro",                "19.06.–20.06.", 237.28, 28.47),
    ("2026-06", "Studio",    "Booking.com", "Elisabeth Schamber",          "20.06.–27.06.", 1006.36, 120.76),
    ("2026-06", "Apartment", "Booking.com", "Maria Luisa Martinez Oliver", "23.06.–27.06.", 604.00, 72.48),
    ("2026-06", "Studio",    "Booking.com", "Tonacie Courtiade",           "27.06.–28.06.", 209.51, 25.14),
    ("2026-06", "Studio",    "Airbnb",      "Pei Zhou",                    "01.06.–03.06.", 310.00, 51.95),
    ("2026-06", "Studio",    "Airbnb",      "Leanne O'Hara",               "10.06.–12.06.", 400.00, 67.00),
    ("2026-06", "Apartment", "Airbnb",      "Nikki Zijderveld",            "16.06.–19.06.", 516.40, 86.55),
    ("2026-06", "Apartment", "Airbnb",      "Jenny VansCoy",               "19.06.–22.06.", 583.00, 97.65),
]

THRESHOLD = 1600.0

# Monatsumsatz brutto pro Objekt -> Satz
gross = defaultdict(float)
for m, obj, *_rest in bookings:
    gross[(m, obj)] += _rest[3]
rate = {k: (0.10 if v > THRESHOLD else 0.05) for k, v in gross.items()}

rows = []
for m, obj, portal, guest, period, g, comm in bookings:
    base = round(g - comm - CLEAN[obj], 2)
    r = rate[(m, obj)]
    prov = round(base * r, 2)
    rows.append(dict(monat=m, objekt=obj, portal=portal, gast=guest, zeitraum=period,
                     brutto=g, kommission=comm, netto=round(g - comm, 2),
                     pauschale=CLEAN[obj], basis=base, satz=r, provision=prov))

if __name__ == "__main__":
    tot = 0.0
    for m in ("2026-04", "2026-05", "2026-06"):
        print(f"\n=== {m} ===")
        for obj in ("Studio", "Apartment"):
            rs = [r for r in rows if r["monat"] == m and r["objekt"] == obj]
            if not rs:
                continue
            g = gross[(m, obj)]
            p = sum(r["provision"] for r in rs)
            b = sum(r["basis"] for r in rs)
            tot += p
            print(f"{obj:10s} Umsatz brutto {g:9.2f}  Satz {rate[(m,obj)]*100:4.0f}%  Basis {b:9.2f}  Provision {p:8.2f}")
            for r in rs:
                print(f"    {r['portal']:12s} {r['gast']:30s} {r['zeitraum']:14s} "
                      f"{r['brutto']:8.2f} -{r['kommission']:7.2f} -{r['pauschale']:6.2f} = {r['basis']:8.2f} -> {r['provision']:7.2f}")
    print(f"\nTOTAL PROVISION Q2: {tot:.2f}  (gerundet auf 0.05: {round(tot*20)/20:.2f})")
