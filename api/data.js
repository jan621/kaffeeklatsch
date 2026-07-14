// Offener Datenendpunkt (kein Login). Liefert die Abrechnungsdaten des Kunden.
// Weitere Kunden: hier ggf. anhand eines Query-Parameters unterscheiden.
const data = require("./_data/kaffeeklatsch");

module.exports = (req, res) => {
  res.statusCode = 200;
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  res.setHeader("Cache-Control", "no-store");
  res.end(JSON.stringify({
    user: { clientId: data.clientId, displayName: data.clientName },
    data,
  }));
};
