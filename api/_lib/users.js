// Kundenkonten für das Portal.
// Neuen Kunden anlegen: Eintrag ergänzen und Zahlencode als Hash hinterlegen.
// Hash erzeugen:  node -e "const c=require('crypto');const salt=c.randomBytes(8).toString('hex');const code='123456';console.log(salt, c.createHash('sha256').update(salt+':'+code).digest('hex'))"
const crypto = require("crypto");

const USERS = {
  kaffeeklatsch: {
    clientId: "kaffeeklatsch",
    displayName: "KaffeeKlatsch Wallis AG",
    salt: "550e3bd280c7909a",
    codeHash: "6733e355cca87ed4bb00861269e4f6bbd4a350a67fe458eede7d17ca3bb7774f",
  },
};

function verifyCredentials(username, code) {
  const user = USERS[String(username || "").trim().toLowerCase()];
  if (!user) return null;
  const hash = crypto.createHash("sha256").update(`${user.salt}:${String(code || "").trim()}`).digest("hex");
  const a = Buffer.from(hash), b = Buffer.from(user.codeHash);
  if (a.length !== b.length || !crypto.timingSafeEqual(a, b)) return null;
  return user;
}

function getUser(clientId) {
  return USERS[clientId] || null;
}

module.exports = { verifyCredentials, getUser };
