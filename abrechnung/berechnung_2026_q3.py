# Provisionsabrechnung KaffeeKlatsch — Q3 2026, Stand: Juli 2026.
# Gleiche Logik wie Q2 (siehe berechnung_2026_q2.py).
# Objektzuordnung Booking: "Mountain View" = Apartment, "Deluxe City View" = Studio.
# Monatszuordnung nach Abreise-/Checkout-Datum:
#   - Passant (Anreise 30.06., Abreise 03.07.) zählt zu Juli (aus Q2 übertragen).
#   - Bianca Thalhammer & Fatima Coelho (Abreise 04.08.) gehören zu August, nicht Juli.
# Airbnb: payout (Betrag) = Nettobetrag nach Kommission; Kommission = Bruttoeinkünfte - payout,
#         damit Basis = brutto - Kommission - Reinigungspauschale = payout - Pauschale.
# Airbnb-Datei ist "pending" = voraussichtliche Auszahlungen.
from collections import defaultdict

CLEAN = {"Studio": 100.0, "Apartment": 130.0}
THRESHOLD = 1600.0

# (Monat, Objekt, Portal, Gast, Zeitraum, Brutto, Kommission)
# Booking: Kommission = ausgewiesener Kommissionsbetrag.
# Airbnb:  Kommission = Bruttoeinkünfte - Betrag(Auszahlung).
bookings = [
    # ---- Booking.com (Abreise Juli) ----
    ("2026-07", "Apartment", "Booking.com", "Lucia Gonzalo",          "02.07.–06.07.", 721.36, 86.56),
    ("2026-07", "Studio",    "Booking.com", "Hanneke Ruijterlinde",   "04.07.–11.07.", 809.80, 97.18),
    ("2026-07", "Apartment", "Booking.com", "Kanyarat Suwannachairob","08.07.–10.07.", 471.96, 56.64),
    ("2026-07", "Apartment", "Booking.com", "José Polidura",          "10.07.–17.07.", 973.60, 116.83),
    ("2026-07", "Apartment", "Booking.com", "Ingrid Boll-Mehler",     "22.07.–27.07.", 1060.00, 127.20),
    ("2026-07", "Studio",    "Booking.com", "Sylvie Passant",         "30.06.–03.07.", 428.53, 51.42),
    # Bianca Thalhammer (Studio) & Fatima Coelho (Apartment) reisen am 04.08. ab -> August.
    # ---- Airbnb (pending) ----
    ("2026-07", "Studio",    "Airbnb",      "Parshwa Shah",           "11.07.–13.07.", 281.20, 44.15),
    ("2026-07", "Studio",    "Airbnb",      "Mustafa İnanç Balkan",   "13.07.–18.07.", 666.20, 111.60),
    ("2026-07", "Studio",    "Airbnb",      "Raphael Barbey",         "18.07.–25.07.", 1045.00, 175.10),
    ("2026-07", "Apartment", "Airbnb",      "Jieying Feng",           "19.07.–21.07.", 518.00, 86.80),
    ("2026-07", "Apartment", "Airbnb",      "Deborah",                "28.07.–31.07.", 422.65, 66.35),
]

gross = defaultdict(float)
for m, obj, portal, guest, period, g, comm in bookings:
    gross[(m, obj)] += g
rate = {k: (0.10 if v > THRESHOLD else 0.05) for k, v in gross.items()}

def r2(x):
    return round(x + 1e-9, 2)

rows = []
for m, obj, portal, guest, period, g, comm in bookings:
    base = r2(g - comm - CLEAN[obj])
    prov = r2(base * rate[(m, obj)])
    rows.append(dict(monat=m, objekt=obj, portal=portal, gast=guest, zeitraum=period,
                     brutto=g, kommission=comm, netto=r2(g - comm),
                     pauschale=CLEAN[obj], basis=base, satz=rate[(m, obj)], provision=prov))

if __name__ == "__main__":
    tot = 0.0
    for obj in ("Studio", "Apartment"):
        rs = [r for r in rows if r["objekt"] == obj]
        g = gross[("2026-07", obj)]
        b = sum(r["basis"] for r in rs)
        p = sum(r["provision"] for r in rs)
        tot += p
        print(f"\n{obj:10s} Buchungen {len(rs)}  Umsatz brutto {g:9.2f}  Satz {int(rate[('2026-07',obj)]*100)}%  Basis {b:9.2f}  Provision {p:8.2f}")
        for r in rs:
            print(f"    {r['portal']:12s} {r['gast']:26s} {r['zeitraum']:14s} {r['brutto']:8.2f} -{r['kommission']:7.2f} -{r['pauschale']:6.2f} = {r['basis']:8.2f} -> {r['provision']:7.2f}")
    gtot = sum(gross.values()); btot = sum(r["basis"] for r in rows)
    print(f"\nTOTAL Juli: Buchungen {len(rows)}  Umsatz {gtot:.2f}  Basis {btot:.2f}  Provision {tot:.2f}  (gerundet 0.05: {round(tot*20)/20:.2f})")
