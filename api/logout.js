const { clearCookie, json } = require("./_lib/auth");

module.exports = (req, res) => {
  return json(res, 200, { ok: true }, { "Set-Cookie": clearCookie() });
};
