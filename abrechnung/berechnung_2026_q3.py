# Provisionsabrechnung KaffeeKlatsch — Q3 2026 (Juli, August, September), laufend.
# Gleiche Logik wie Q2 (siehe berechnung_2026_q2.py).
# Objektzuordnung Booking: "Mountain View" = Apartment, "Deluxe City View" = Studio.
# Monatszuordnung nach Abreise-/Checkout-Datum:
#   - Passant (Abreise 03.07.) aus Q2 übertragen -> Juli (nicht in der Q3-Anreiseliste enthalten).
#   - Thalhammer & Coelho reisen erst am 04.08. ab -> August.
# Airbnb (pending = voraussichtliche Auszahlungen): payout (Betrag) = Nettobetrag nach Kommission;
#   Kommission = Bruttoeinkünfte - payout, damit Basis = brutto - Kommission - Pauschale = payout - Pauschale.
from collections import defaultdict

CLEAN = {"Studio": 100.0, "Apartment": 130.0}
THRESHOLD = 1600.0

# (Monat, Objekt, Portal, Gast, Zeitraum, Brutto, Kommission)
bookings = [
    # ================= JULI =================
    # -- Booking.com (Abreise Juli) --
    ("2026-07", "Apartment", "Booking.com", "Lucia Gonzalo",           "02.07.–06.07.", 721.36, 86.56),
    ("2026-07", "Studio",    "Booking.com", "Hanneke Ruijterlinde",    "04.07.–11.07.", 809.80, 97.18),
    ("2026-07", "Apartment", "Booking.com", "Kanyarat Suwannachairob", "08.07.–10.07.", 471.96, 56.64),
    ("2026-07", "Apartment", "Booking.com", "José Polidura",           "10.07.–17.07.", 973.60, 116.83),
    ("2026-07", "Apartment", "Booking.com", "Ingrid Boll-Mehler",      "22.07.–27.07.", 1060.00, 127.20),
    ("2026-07", "Studio",    "Booking.com", "Sylvie Passant",          "30.06.–03.07.", 428.53, 51.42),
    # -- Airbnb (Abreise Juli) --
    ("2026-07", "Studio",    "Airbnb",      "Parshwa Shah",            "11.07.–13.07.", 281.20, 44.15),
    ("2026-07", "Studio",    "Airbnb",      "Mustafa İnanç Balkan",    "13.07.–18.07.", 666.20, 111.60),
    ("2026-07", "Studio",    "Airbnb",      "Raphael Barbey",          "18.07.–25.07.", 1045.00, 175.10),
    ("2026-07", "Apartment", "Airbnb",      "Jieying Feng",            "19.07.–21.07.", 518.00, 86.80),
    ("2026-07", "Apartment", "Airbnb",      "Deborah",                 "28.07.–31.07.", 422.65, 66.35),
    # ================= AUGUST =================
    # -- Booking.com (Abreise August) --
    ("2026-08", "Studio",    "Booking.com", "Bianca Thalhammer",       "26.07.–04.08.", 1141.75, 137.01),
    ("2026-08", "Apartment", "Booking.com", "Fatima Coelho",           "29.07.–04.08.", 1090.00, 130.80),
    ("2026-08", "Apartment", "Booking.com", "Julia Hari",              "07.08.–09.08.", 553.60, 66.43),
    ("2026-08", "Studio",    "Booking.com", "Mirjam Werren",           "07.08.–09.08.", 380.80, 45.70),
    ("2026-08", "Studio",    "Booking.com", "Friederike Gondring",     "09.08.–11.08.", 317.62, 38.11),
    ("2026-08", "Studio",    "Booking.com", "Andreas Staab",           "16.08.–19.08.", 460.36, 55.24),
    ("2026-08", "Studio",    "Booking.com", "Vanessa Hudetzka",        "20.08.–23.08.", 373.78, 44.85),
    ("2026-08", "Apartment", "Booking.com", "Julia Strubel",           "21.08.–24.08.", 557.53, 66.90),
    ("2026-08", "Apartment", "Booking.com", "Christoph Orthuber",      "25.08.–28.08.", 514.72, 61.77),
    ("2026-08", "Studio",    "Booking.com", "Michael Hochhauser",      "28.08.–30.08.", 360.80, 43.30),
    ("2026-08", "Apartment", "Booking.com", "Gast (Booking 5780273760)","28.08.–30.08.", 544.00, 65.28),
    # -- Airbnb (Abreise August) --
    ("2026-08", "Studio",    "Airbnb",      "Victoria Kikko Kawashima","05.08.–07.08.", 400.00, 67.00),
    ("2026-08", "Apartment", "Airbnb",      "Simon Ruijsenaars",       "10.08.–21.08.", 1951.60, 327.00),
    ("2026-08", "Studio",    "Airbnb",      "Tom Lange",               "24.08.–28.08.", 700.00, 117.30),
    # ================= SEPTEMBER =================
    # -- Booking.com (Abreise September) --
    ("2026-09", "Studio",    "Booking.com", "Peter Merz",              "04.09.–11.09.", 1062.50, 127.50),
    ("2026-09", "Apartment", "Booking.com", "Yasmin Ali khan",         "05.09.–07.09.", 427.68, 51.32),
    ("2026-09", "Studio",    "Booking.com", "Felicity O'Carroll",      "15.09.–18.09.", 390.16, 46.82),
    ("2026-09", "Apartment", "Booking.com", "Vera Green",              "21.09.–25.09.", 737.44, 88.49),
    ("2026-09", "Studio",    "Booking.com", "Simone Basler",           "26.09.–29.09.", 451.00, 54.12),
    # -- Airbnb (Abreise September) --
    ("2026-09", "Apartment", "Airbnb",      "Carla Hartman",           "07.09.–18.09.", 1951.60, 327.00),
    ("2026-09", "Studio",    "Airbnb",      "Simone Thöni",            "11.09.–13.09.", 370.00, 62.00),
]

MONTHS = [("2026-07", "Juli"), ("2026-08", "August"), ("2026-09", "September")]
OBJECTS = ["Studio", "Apartment"]

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
                     brutto=g, kommission=comm, pauschale=CLEAN[obj], basis=base,
                     satz=rate[(m, obj)], provision=prov))

if __name__ == "__main__":
    qtot = defaultdict(float); qn = 0
    for mk, mlabel in MONTHS:
        print(f"\n===== {mlabel} 2026 =====")
        for obj in OBJECTS:
            rs = [r for r in rows if r["monat"] == mk and r["objekt"] == obj]
            if not rs:
                continue
            g = gross[(mk, obj)]
            b = sum(r["basis"] for r in rs); p = sum(r["provision"] for r in rs)
            qtot["gross"] += g; qtot["base"] += b; qtot["prov"] += p; qn += len(rs)
            print(f"  {obj:10s} Buch {len(rs)}  Umsatz {g:9.2f}  Satz {int(rate[(mk,obj)]*100)}%  Basis {b:9.2f}  Prov {p:8.2f}")
    print(f"\n=== Q3 TOTAL: Buchungen {qn}  Umsatz {qtot['gross']:.2f}  Basis {qtot['base']:.2f}  "
          f"Provision {qtot['prov']:.2f} (gerundet 0.05: {round(qtot['prov']*20)/20:.2f}) ===")
    # Monatszahlen für das Datenmodul
    print("\n--- Monatswerte (Objekt: Buch, Umsatz, Basis, Prov) ---")
    for mk, mlabel in MONTHS:
        for obj in OBJECTS:
            rs = [r for r in rows if r["monat"] == mk and r["objekt"] == obj]
            if not rs:
                continue
            print(f"{mlabel:10s} {obj:10s} {len(rs)} {gross[(mk,obj)]:.2f} "
                  f"{sum(r['basis'] for r in rs):.2f} {r2(sum(r['provision'] for r in rs)):.2f}")
