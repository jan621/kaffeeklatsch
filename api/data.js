// Offener Datenendpunkt (kein Login). Liefert die Abrechnungsdaten je Kunde.
// Aufruf: /api/data?client=<id>
const CLIENTS = {
  kaffeeklatsch: () => require("./_data/kaffeeklatsch"),
  msds: () => require("./_data/msds"),
};

module.exports = (req, res) => {
  const url = new URL(req.url, "http://localhost");
  const client = url.searchParams.get("client") || "kaffeeklatsch";
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  res.setHeader("Cache-Control", "no-store");
  const load = CLIENTS[client];
  if (!load) {
    res.statusCode = 404;
    res.end(JSON.stringify({ error: "unknown_client" }));
    return;
  }
  const data = load();
  res.statusCode = 200;
  res.end(JSON.stringify({
    user: { clientId: data.clientId, displayName: data.clientName },
    data,
  }));
};
