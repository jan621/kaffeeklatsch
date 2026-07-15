# Provisionsabrechnung MSDS Invest GmbH — Q1–Q3 2026.
# Objekt: "Zentrumsnahe Wohnung mit Blick" (1 Wohnung), Portale Booking.com & Airbnb.
# Regeln:
#   - Reinigung Booking:  100 + 25 * Personen.
#   - Reinigung Airbnb:   Reinigungsgebühr(min 60) + Bettwäsche(voll) + Verwaltung(40).
#                         Halbierte Zeilen (Verwaltung 19.50) -> volle Werte (x2).
#   - Provision: 20 % auf (Auszahlung nach Kommission - Reinigung), immer.
#   - Software: CHF 50 je Kalendermonat (Q1-Q3 durchgehend).
#   - Mediations-Anpassungen kürzen den Auszahlungsbetrag der Buchung.
#   - Monatszuordnung nach Checkout; negative Provision wird auf 0 gestellt.
from collections import defaultdict

def r2(x): return round(x + 1e-9, 2)

def airbnb_cleaning(rein, bett, verw):
    if abs(verw - 19.5) < 0.01:      # halbierte Zeile
        rein *= 2; bett *= 2
    return r2(max(rein, 60.0) + bett + 40.0)

# Booking: (monat, gast, stay, persons, preis, kommission)
booking = [
    ("2026-02", "Aaron Keller",        "31.01.–03.02.", 3, 1087.14, 130.46),
    ("2026-02", "Thomas Huber",        "13.02.–18.02.", 2, 1749.00, 209.88),
    ("2026-03", "Christian Nuss",      "26.02.–01.03.", 3, 1087.14, 130.46),
    ("2026-03", "Roger Borer",         "06.03.–08.03.", 2, 631.00,  75.72),
    ("2026-06", "Piotr Niemczyk",      "30.05.–01.06.", 3, 439.00,  52.68),
    ("2026-07", "Reza Serajeh",        "06.07.–08.07.", 4, 490.00,  58.80),
    ("2026-07", "johan gebhardt",      "10.07.–12.07.", 3, 490.00,  58.80),
    ("2026-07", "yaser ALahmadi",      "12.07.–15.07.", 2, 685.50,  82.26),
    ("2026-07", "Jonas Thomsen",       "15.07.–17.07.", 3, 490.00,  58.80),
    ("2026-07", "Katja Antoniadis",    "23.07.–25.07.", 4, 490.00,  58.80),
    ("2026-08", "Niko Proufas",        "30.07.–02.08.", 5, 685.50,  82.26),
    ("2026-08", "Robert van der Post", "16.08.–19.08.", 2, 685.50,  82.26),
    ("2026-08", "Denis Moschetto",     "27.08.–29.08.", 5, 490.00,  58.80),
    ("2026-09", "Mathieu Bohn",        "11.09.–13.09.", 3, 439.00,  52.68),
]

# Airbnb: (monat, gast, stay, brutto, betrag, rein, bett, verw, mediation)
airbnb = [
    ("2026-01", "Laila Buchser",       "16.01.–18.01.", 620.40, 516.45, 60, 100, 39, 0),
    ("2026-01", "Dennis Groß",         "23.01.–25.01.", 706.00, 591.50, 60,  75, 39, -50),
    ("2026-02", "Saina Schnocklake",   "18.02.–22.02.", 1111.00, 924.85, 60, 125, 39, 0),
    ("2026-05", "Saulean Ligia",       "21.05.–25.05.", 594.00, 494.50, 60,  75, 39, 0),
    ("2026-06", "Surbhi",              "29.05.–02.06.", 462.00, 384.60, 30, 62.5, 19.5, 0),
    ("2026-06", "Efe Yağcızeybek",     "04.06.–06.06.", 493.00, 410.40, 60, 100, 39, 0),
    ("2026-06", "Bugrahan Kumru",      "08.06.–10.06.", 516.60, 430.05, 60, 125, 39, 0),
    ("2026-06", "Gonzalo Jr Nora",     "13.06.–17.06.", 924.00, 769.20,  0,   0,  0, 0),
    ("2026-06", "Jas",                 "17.06.–21.06.", 839.00, 698.40, 160,  0,  0, -560.15),
    ("2026-07", "源权 欧阳",            "03.07.–05.07.", 544.20, 453.00, 60,  50, 39, 0),
    ("2026-07", "Ibrahim Alsulami",    "17.07.–21.07.", 1024.00, 852.45, 185, 0,  0, 0),
    ("2026-07", "Koushik B. Gangadharacharya", "21.07.–23.07.", 427.95, 360.75, 60, 75, 39, 0),
    ("2026-07", "Kristoffer Gadegaard","25.07.–27.07.", 624.00, 519.45, 60, 125, 39, 0),
    ("2026-07", "Tim Inderbitzin",     "28.07.–30.07.", 591.50, 498.65, 60, 100, 39, 0),
    ("2026-08", "Ramona Lupu",         "03.08.–06.08.", 599.40, 505.30, 60, 100, 39, 0),
    ("2026-08", "Mohammed H. J. Aldawsari", "06.08.–09.08.", 764.30, 644.35, 60, 75, 39, 0),
    ("2026-08", "Saeed Al",            "11.08.–14.08.", 739.60, 623.50, 60,  50, 39, 0),
    ("2026-08", "Griselle Vazquez Fresse", "25.08.–27.08.", 599.00, 498.65, 60, 100, 39, 0),
]

rows = []
for m, gast, stay, persons, preis, komm in booking:
    cleaning = 100.0 + 25.0 * persons
    base = r2(preis - komm - cleaning)
    prov = max(0.0, r2(0.20 * base))
    rows.append(dict(monat=m, portal="Booking.com", gast=gast, stay=stay,
                     gross=r2(preis), commission=r2(komm), cleaning=r2(cleaning),
                     base=base, provision=prov))
for m, gast, stay, brutto, betrag, rein, bett, verw, med in airbnb:
    cleaning = airbnb_cleaning(rein, bett, verw)
    comm = r2(brutto - betrag - med)      # Servicegebühr + |Mediation|
    base = r2(brutto - comm - cleaning)   # = betrag + med - cleaning
    prov = max(0.0, r2(0.20 * base))
    rows.append(dict(monat=m, portal="Airbnb", gast=gast, stay=stay,
                     gross=r2(brutto), commission=comm, cleaning=cleaning,
                     base=base, provision=prov))

MONTHS = {"2026-01": "Januar", "2026-02": "Februar", "2026-03": "März",
          "2026-05": "Mai", "2026-06": "Juni",
          "2026-07": "Juli", "2026-08": "August", "2026-09": "September"}
QUARTER = {1: ["2026-01", "2026-02", "2026-03"], 2: ["2026-04", "2026-05", "2026-06"],
           3: ["2026-07", "2026-08", "2026-09"]}
SOFT_PER_MONTH = 50.0
SOFT_MONTHS = {1: 3, 2: 3, 3: 3}   # jeden Kalendermonat

if __name__ == "__main__":
    for qn in (1, 2, 3):
        qkeys = QUARTER[qn]
        qrows = [r for r in rows if r["monat"] in qkeys]
        print(f"\n===== Q{qn} 2026 =====")
        for mk in qkeys:
            mr = [r for r in qrows if r["monat"] == mk]
            if not mr: continue
            print(f"  {MONTHS[mk]}: Buch {len(mr)}  Umsatz {sum(r['gross'] for r in mr):8.2f}  "
                  f"Basis {sum(r['base'] for r in mr):8.2f}  Prov {sum(r['provision'] for r in mr):7.2f}")
        gp = sum(r["provision"] for r in qrows); soft = SOFT_PER_MONTH * SOFT_MONTHS[qn]
        base = sum(r["base"] for r in qrows)
        print(f"  Q{qn} Provision {gp:.2f} + Software {soft:.0f} = Rechnung {gp+soft:.2f} | "
              f"Netto Eigentümer {base-gp-soft:.2f} | Buch {len(qrows)}")
    tp = sum(r["provision"] for r in rows)
    print(f"\nTOTAL Q1-Q3 Provision {tp:.2f} + Software {SOFT_PER_MONTH*9:.0f} = {tp+SOFT_PER_MONTH*9:.2f}")
    neg = [r for r in rows if r["base"] < 0]
    for r in neg:
        print(f"  HINWEIS negative Basis: {r['gast']} base {r['base']} -> Provision auf 0 gesetzt")
