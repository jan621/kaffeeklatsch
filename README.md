# Hostflow Kundenportal

Kundenportal für Provisionsabrechnungen des Ferienwohnungs-Managements.
Kunden melden sich mit Benutzername und Zahlencode an und sehen ihre
Abrechnungen pro Quartal sowie eine Jahresübersicht. Erster Kunde:
**KaffeeKlatsch Wallis AG** (B&B Brig by KaffeeKlatsch, Studio & Apartment).

Gehostet auf Vercel: statisches Frontend aus `docs/`, Login und Daten über
Serverless Functions in `api/` (Session-Cookie, HttpOnly, 12 h gültig).
Die Abrechnungsdaten sind nur mit gültiger Anmeldung abrufbar.

## Struktur

| Pfad | Inhalt |
|---|---|
| `docs/index.html` | Login-Seite |
| `docs/portal.html` | Dashboard (Quartals- & Jahresansicht, rein datengetrieben) |
| `docs/assets/` | Stylesheet & Logo (`logo.png` durch Original ersetzbar) |
| `api/login.js` / `logout.js` / `data.js` | Auth- und Daten-Endpunkte |
| `api/_lib/users.js` | Kundenkonten (Benutzername + gehashter Zahlencode) |
| `api/_lib/auth.js` | Session-Handling (HMAC-signierte Cookies) |
| `api/_data/<kunde>.js` | Abrechnungsdaten pro Kunde |
| `abrechnung/` | Berechnungsskripte & Excel-Abrechnung Q2 2026 |

## Neuen Kunden anlegen

1. Datenmodul `api/_data/<kunde>.js` erstellen (Struktur wie `kaffeeklatsch.js`;
   die Berechnungslogik kann pro Kunde abweichen — das Portal zeigt nur die
   fertig berechneten Werte an).
2. Konto in `api/_lib/users.js` ergänzen. Hash für den Zahlencode erzeugen:
   ```
   node -e "const c=require('crypto');const salt=c.randomBytes(8).toString('hex');const code='123456';console.log(salt, c.createHash('sha256').update(salt+':'+code).digest('hex'))"
   ```
3. Datenmodul in `api/data.js` unter `DATA` registrieren.

## Neues Quartal erfassen

Im Datenmodul des Kunden einen Eintrag im Array `quarters` ergänzen
(Monatszeilen, Totale, Buchungsliste). Quartals-Tab und Jahresübersicht
erscheinen automatisch.

## Betrieb

- **Vercel:** deployt automatisch bei Push auf `main`. `vercel.json` setzt
  `docs/` als statisches Output-Verzeichnis; `api/` wird als Functions erkannt.
- **Empfohlen:** In Vercel die Umgebungsvariable `SESSION_SECRET` setzen
  (beliebiger langer Zufallswert), damit Sessions nicht vom eingecheckten
  Fallback-Secret abhängen.
- Zahlencodes liegen nur als Hash im Repo; die Klartext-Codes werden den
  Kunden direkt mitgeteilt.
