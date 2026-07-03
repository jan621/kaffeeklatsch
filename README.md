# KaffeeKlatsch — Abrechnung Objektmanagement

Provisionsabrechnungen für das Management der Ferienwohnungen
**B&B Brig by KaffeeKlatsch** (Studio & Apartment) für die KaffeeKlatsch Wallis AG,
vermarktet über Booking.com und Airbnb.

## Kundenseite (GitHub Pages)

`docs/index.html` ist die veröffentlichbare Kundenseite zur aktuellen Abrechnung
(Q2 2026) — minimalistisch, weiss, mit Kennzahlen, Charts, Monatsübersicht und
Details pro Buchung.

**Veröffentlichen:** Repository → *Settings → Pages → Build and deployment →
Deploy from a branch* → Branch `main`, Ordner `/docs`. Die Seite erscheint danach
unter `https://<owner>.github.io/kaffeeklatsch/`.

> Hinweis: GitHub-Pages-Seiten sind öffentlich zugänglich (auch bei privatem
> Repo). Die Detailtabelle enthält Gästenamen — bei Bedarf vor dem
> Veröffentlichen entfernen.

## Abrechnungslogik

- **Provisionssatz** pro Objekt und Monat, nach Brutto-Monatsumsatz
  (vor Abzug der Portal-Kommission): bis CHF 1'600 → **5 %**, darüber → **10 %**.
- **Provisionsbasis** pro Buchung: Buchungswert ./. Portal-Kommission
  ./. Reinigungspauschale (**Studio CHF 100**, **Apartment CHF 130**).
- Airbnb zahlt netto aus (Servicegebühr bereits abgezogen); für den
  Schwellenwert zählen die Bruttoeinkünfte.
- Monatszuordnung nach Abreisedatum (entspricht der Rechnungsperiode von
  Booking.com); stornierte Buchungen bleiben unberücksichtigt.

## Struktur

| Pfad | Inhalt |
|---|---|
| `docs/index.html` | Kundenseite Q2 2026 (GitHub Pages) |
| `abrechnung/berechnung_2026_q2.py` | Berechnungslogik & Buchungsdaten Q2 2026 |
| `abrechnung/erstelle_excel.py` | Erzeugt die Excel-Abrechnung |
| `abrechnung/Provisionsabrechnung_…xlsx` | Excel: Übersicht + Details pro Buchung |
| `abrechnung/kundenuebersicht.html` | Kundenübersicht (Claude-Artifact-Variante) |
| `abrechnung/dashboard.html` | Dashboard-Variante (Claude-Artifact) |

Neue Quartale: Buchungsdaten in einer Kopie von `berechnung_2026_q2.py` erfassen,
`erstelle_excel.py` darauf zeigen lassen und die Zahlen in `docs/index.html`
nachführen.
