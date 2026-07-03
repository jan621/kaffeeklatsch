const { authenticate, json } = require("./_lib/auth");
const { getUser } = require("./_lib/users");

// Datenmodule pro Kunde; neue Kunden hier registrieren.
const DATA = {
  kaffeeklatsch: () => require("./_data/kaffeeklatsch"),
};

module.exports = (req, res) => {
  const clientId = authenticate(req);
  if (!clientId || !DATA[clientId]) return json(res, 401, { error: "unauthorized" });
  const user = getUser(clientId);
  return json(res, 200, {
    user: { clientId, displayName: user ? user.displayName : clientId },
    data: DATA[clientId](),
  });
};
