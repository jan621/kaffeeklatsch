const { createSession, sessionCookie, readJsonBody, json } = require("./_lib/auth");
const { verifyCredentials } = require("./_lib/users");

module.exports = async (req, res) => {
  if (req.method !== "POST") return json(res, 405, { error: "method_not_allowed" });
  const body = await readJsonBody(req);
  const user = verifyCredentials(body.username, body.code);
  if (!user) {
    // Fehlversuche leicht bremsen
    await new Promise(r => setTimeout(r, 600));
    return json(res, 401, { error: "invalid_credentials" });
  }
  return json(res, 200, { ok: true }, { "Set-Cookie": sessionCookie(createSession(user.clientId)) });
};
