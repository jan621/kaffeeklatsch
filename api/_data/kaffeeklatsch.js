// Abrechnungsdaten KaffeeKlatsch Wallis AG — B&B Brig by KaffeeKlatsch.
// Quelle: abrechnung/berechnung_2026_q2.py (Q2 2026).
// Neues Quartal: Objekt in "quarters" ergänzen; Jahres-Ansicht aggregiert automatisch.
module.exports = {
  clientId: "kaffeeklatsch",
  clientName: "KaffeeKlatsch Wallis AG",
  property: "B&B Brig by KaffeeKlatsch",
  objects: ["Studio", "Apartment"],
  currency: "CHF",
  quarters: [
    {
      id: "2026-Q2",
      year: 2026,
      quarter: 2,
      label: "Q2 2026",
      sublabel: "April – Juni 2026",
      months: [
        {
          key: "2026-04", label: "April",
          rows: [
            { object: "Studio", bookings: 2, gross: 634.76, base: 344.73, provision: 17.24 },
            { object: "Apartment", bookings: 5, gross: 2603.44, base: 1572.81, provision: 157.29 },
          ],
        },
        {
          key: "2026-05", label: "Mai",
          rows: [
            { object: "Studio", bookings: 9, gross: 3079.32, base: 1711.69, provision: 171.18 },
            { object: "Apartment", bookings: 4, gross: 2835.58, base: 1891.08, provision: 189.12 },
          ],
        },
        {
          key: "2026-06", label: "Juni",
          rows: [
            { object: "Studio", bookings: 8, gross: 3321.93, base: 2089.56, provision: 208.96 },
            { object: "Apartment", bookings: 3, gross: 1703.40, base: 1056.72, provision: 105.68 },
          ],
        },
      ],
      totals: { bookings: 31, gross: 14178.43, base: 8666.59, provision: 849.47, billed: 849.45 },
      bookings: [
        { month: "April 2026", guest: "Michel Corpataux", object: "Studio", portal: "Booking.com", stay: "03.04.–06.04.", gross: 342.76, commission: 41.13, cleaning: 100, base: 201.63, provision: 10.08 },
        { month: "April 2026", guest: "Markus Spillmann", object: "Studio", portal: "Airbnb", stay: "21.04.–23.04.", gross: 292.00, commission: 48.90, cleaning: 100, base: 143.10, provision: 7.16 },
        { month: "April 2026", guest: "Nicole Meier", object: "Apartment", portal: "Airbnb", stay: "02.04.–04.04.", gross: 481.20, commission: 80.65, cleaning: 130, base: 270.55, provision: 27.06 },
        { month: "April 2026", guest: "Suzanne Caliendo", object: "Apartment", portal: "Booking.com", stay: "06.04.–08.04.", gross: 395.68, commission: 47.48, cleaning: 130, base: 218.20, provision: 21.82 },
        { month: "April 2026", guest: "Johannes Schneider", object: "Apartment", portal: "Booking.com", stay: "12.04.–16.04.", gross: 482.24, commission: 57.87, cleaning: 130, base: 294.37, provision: 29.44 },
        { month: "April 2026", guest: "Fabian Jenelten", object: "Apartment", portal: "Booking.com", stay: "18.04.–20.04.", gross: 291.12, commission: 34.93, cleaning: 130, base: 126.19, provision: 12.62 },
        { month: "April 2026", guest: "Russell Stott", object: "Apartment", portal: "Airbnb", stay: "21.04.–28.04.", gross: 953.20, commission: 159.70, cleaning: 130, base: 663.50, provision: 66.35 },
        { month: "Mai 2026", guest: "Bella Abrego", object: "Studio", portal: "Airbnb", stay: "27.04.–01.05.", gross: 624.00, commission: 104.55, cleaning: 100, base: 419.45, provision: 41.95 },
        { month: "Mai 2026", guest: "Lionel Müller", object: "Studio", portal: "Airbnb", stay: "01.05.–03.05.", gross: 400.00, commission: 67.00, cleaning: 100, base: 233.00, provision: 23.30 },
        { month: "Mai 2026", guest: "Richard Wadsworth", object: "Studio", portal: "Airbnb", stay: "14.05.–16.05.", gross: 268.00, commission: 44.90, cleaning: 100, base: 123.10, provision: 12.31 },
        { month: "Mai 2026", guest: "Manuela Schön Bachmann", object: "Studio", portal: "Booking.com", stay: "16.05.–18.05.", gross: 319.02, commission: 38.28, cleaning: 100, base: 180.74, provision: 18.07 },
        { month: "Mai 2026", guest: "David Kirchner", object: "Studio", portal: "Booking.com", stay: "19.05.–21.05.", gross: 377.68, commission: 45.32, cleaning: 100, base: 232.36, provision: 23.24 },
        { month: "Mai 2026", guest: "Melody Fanning", object: "Studio", portal: "Airbnb", stay: "21.05.–22.05.", gross: 190.00, commission: 31.85, cleaning: 100, base: 58.15, provision: 5.82 },
        { month: "Mai 2026", guest: "Frank Diener", object: "Studio", portal: "Airbnb", stay: "22.05.–24.05.", gross: 280.00, commission: 46.90, cleaning: 100, base: 133.10, provision: 13.31 },
        { month: "Mai 2026", guest: "Paul Warpeha", object: "Studio", portal: "Airbnb", stay: "25.05.–27.05.", gross: 301.60, commission: 50.55, cleaning: 100, base: 151.05, provision: 15.11 },
        { month: "Mai 2026", guest: "Christina Siffert", object: "Studio", portal: "Booking.com", stay: "29.05.–31.05.", gross: 319.02, commission: 38.28, cleaning: 100, base: 180.74, provision: 18.07 },
        { month: "Mai 2026", guest: "Dóra Domboróczky", object: "Apartment", portal: "Airbnb", stay: "30.04.–03.05.", gross: 537.00, commission: 90.00, cleaning: 130, base: 317.00, provision: 31.70 },
        { month: "Mai 2026", guest: "Veronique Mauron Frank", object: "Apartment", portal: "Booking.com", stay: "14.05.–17.05.", gross: 676.00, commission: 81.12, cleaning: 130, base: 464.88, provision: 46.49 },
        { month: "Mai 2026", guest: "Elisabeth Reutimann", object: "Apartment", portal: "Airbnb", stay: "22.05.–28.05.", gross: 1234.00, commission: 206.75, cleaning: 130, base: 897.25, provision: 89.73 },
        { month: "Mai 2026", guest: "Uli Kausche", object: "Apartment", portal: "Booking.com", stay: "29.05.–31.05.", gross: 388.58, commission: 46.63, cleaning: 130, base: 211.95, provision: 21.20 },
        { month: "Juni 2026", guest: "Pei Zhou", object: "Studio", portal: "Airbnb", stay: "01.06.–03.06.", gross: 310.00, commission: 51.95, cleaning: 100, base: 158.05, provision: 15.81 },
        { month: "Juni 2026", guest: "Ronald Cordier", object: "Studio", portal: "Booking.com", stay: "04.06.–07.06.", gross: 465.04, commission: 55.80, cleaning: 100, base: 309.24, provision: 30.92 },
        { month: "Juni 2026", guest: "Leanne O'Hara", object: "Studio", portal: "Airbnb", stay: "10.06.–12.06.", gross: 400.00, commission: 67.00, cleaning: 100, base: 233.00, provision: 23.30 },
        { month: "Juni 2026", guest: "Chiu Kwan Lam", object: "Studio", portal: "Booking.com", stay: "13.06.–14.06.", gross: 219.34, commission: 26.32, cleaning: 100, base: 93.02, provision: 9.30 },
        { month: "Juni 2026", guest: "Kai Choy Wong", object: "Studio", portal: "Booking.com", stay: "14.06.–18.06.", gross: 474.40, commission: 56.93, cleaning: 100, base: 317.47, provision: 31.75 },
        { month: "Juni 2026", guest: "Katrin Koyro", object: "Studio", portal: "Booking.com", stay: "19.06.–20.06.", gross: 237.28, commission: 28.47, cleaning: 100, base: 108.81, provision: 10.88 },
        { month: "Juni 2026", guest: "Elisabeth Schamber", object: "Studio", portal: "Booking.com", stay: "20.06.–27.06.", gross: 1006.36, commission: 120.76, cleaning: 100, base: 785.60, provision: 78.56 },
        { month: "Juni 2026", guest: "Tonacie Courtiade", object: "Studio", portal: "Booking.com", stay: "27.06.–28.06.", gross: 209.51, commission: 25.14, cleaning: 100, base: 84.37, provision: 8.44 },
        { month: "Juni 2026", guest: "Nikki Zijderveld", object: "Apartment", portal: "Airbnb", stay: "16.06.–19.06.", gross: 516.40, commission: 86.55, cleaning: 130, base: 299.85, provision: 29.99 },
        { month: "Juni 2026", guest: "Jenny VansCoy", object: "Apartment", portal: "Airbnb", stay: "19.06.–22.06.", gross: 583.00, commission: 97.65, cleaning: 130, base: 355.35, provision: 35.54 },
        { month: "Juni 2026", guest: "Maria Luisa Martinez Oliver", object: "Apartment", portal: "Booking.com", stay: "23.06.–27.06.", gross: 604.00, commission: 72.48, cleaning: 130, base: 401.52, provision: 40.15 },
      ],
    },
  ],
};
