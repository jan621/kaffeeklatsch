# Hostflow Kundenportal

Kundenportal für Provisionsabrechnungen des Ferienwohnungs-Managements.
Es zeigt die Abrechnungen pro Quartal sowie eine Jahresübersicht mit
Kennzahlen (Provision, Netto Eigentümer, Auslastung, ADR, RevPAR).
Erster Kunde: **KaffeeKlatsch Wallis AG** (B&B Brig by KaffeeKlatsch,
Studio & Apartment).

Gehostet auf Vercel: statisches Frontend aus `docs/`, Daten über eine
Serverless Function in `api/`. **Der Zugriff ist offen (ohne Login)** –
das Dashboard ist direkt unter der Root-URL erreichbar.

> Hinweis: Ohne Login sind Gästenamen und Finanzzahlen öffentlich abrufbar.
> Wer die URL kennt, sieht alles. Bei Bedarf Gästenamen anonymisieren.

## Struktur

| Pfad | Inhalt |
|---|---|
| `docs/index.html` | Dashboard (Quartals- & Jahresansicht, datengetrieben) |
| `docs/assets/` | Stylesheet & Logo |
| `api/data.js` | Offener Datenendpunkt (liefert die Kundendaten als JSON) |
| `api/_data/<kunde>.js` | Abrechnungsdaten pro Kunde |
| `abrechnung/` | Berechnungsskripte & Excel-Abrechnung |

## Kennzahlen

- **Provision** je Objekt und Monat: Brutto-Monatsumsatz bis CHF 1'600 → 5 %,
  darüber → 10 %. Basis = Buchungswert ./. Portal-Kommission ./. Reinigung
  (Studio CHF 100, Apartment CHF 130).
- **Netto Eigentümer** = Provisionsbasis ./. Provision.
- **Auslastung / ADR / RevPAR**: Nächte werden aus den Aufenthalten
  kalendergenau dem Monat zugeteilt; ADR = Ø Umsatz pro belegte Nacht (brutto),
  RevPAR = Umsatz pro verfügbare Nacht.

## Neuen Kunden anlegen

1. Datenmodul `api/_data/<kunde>.js` erstellen (Struktur wie `kaffeeklatsch.js`).
2. In `api/data.js` das passende Modul liefern (z.B. anhand eines
   Query-Parameters, falls mehrere Kunden bedient werden).

## Neues Quartal / neuen Monat erfassen

Im Datenmodul des Kunden einen Eintrag im Array `quarters` ergänzen bzw. einen
Monat zum bestehenden Quartal hinzufügen (Monatszeilen, Totale, Buchungsliste).
Quartals-Tab, Jahresübersicht und Kennzahlen aktualisieren sich automatisch.

## Betrieb

- **Vercel** deployt automatisch bei Push auf `main`. `vercel.json` setzt
  `docs/` als statisches Output-Verzeichnis; `api/` wird als Functions erkannt.
