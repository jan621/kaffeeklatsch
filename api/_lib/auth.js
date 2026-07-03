// Session-Handling: signierte, zeitlich begrenzte Cookies (HMAC-SHA256).
// In Vercel als Umgebungsvariable SESSION_SECRET setzen; der eingebaute
// Fallback funktioniert, sollte aber produktiv überschrieben werden.
const crypto = require("crypto");

const SECRET = process.env.SESSION_SECRET || "303c8b9f35489142f7e093ecc9d0077941d137bcac6d752eb1ece8c256b0e21d";
const COOKIE = "hf_session";
const TTL_SECONDS = 12 * 60 * 60; // 12 Stunden

function sign(payload) {
  return crypto.createHmac("sha256", SECRET).update(payload).digest("base64url");
}

function createSession(clientId) {
  const exp = Math.floor(Date.now() / 1000) + TTL_SECONDS;
  const payload = Buffer.from(`${clientId}|${exp}`).toString("base64url");
  return `${payload}.${sign(payload)}`;
}

function verifySession(token) {
  if (!token || !token.includes(".")) return null;
  const [payload, sig] = token.split(".");
  const expected = sign(payload);
  const a = Buffer.from(sig), b = Buffer.from(expected);
  if (a.length !== b.length || !crypto.timingSafeEqual(a, b)) return null;
  const [clientId, exp] = Buffer.from(payload, "base64url").toString().split("|");
  if (!clientId || Number(exp) < Math.floor(Date.now() / 1000)) return null;
  return clientId;
}

function getCookie(req, name) {
  const header = req.headers.cookie || "";
  for (const part of header.split(";")) {
    const [k, ...v] = part.trim().split("=");
    if (k === name) return decodeURIComponent(v.join("="));
  }
  return null;
}

function sessionCookie(token) {
  return `${COOKIE}=${encodeURIComponent(token)}; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=${TTL_SECONDS}`;
}

function clearCookie() {
  return `${COOKIE}=; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=0`;
}

function authenticate(req) {
  return verifySession(getCookie(req, COOKIE));
}

function readJsonBody(req, limit = 10_000) {
  return new Promise((resolve, reject) => {
    let raw = "";
    req.on("data", chunk => {
      raw += chunk;
      if (raw.length > limit) { reject(new Error("body too large")); req.destroy(); }
    });
    req.on("end", () => {
      try { resolve(raw ? JSON.parse(raw) : {}); }
      catch { resolve({}); }
    });
    req.on("error", reject);
  });
}

function json(res, status, obj, headers = {}) {
  res.statusCode = status;
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  res.setHeader("Cache-Control", "no-store");
  for (const [k, v] of Object.entries(headers)) res.setHeader(k, v);
  res.end(JSON.stringify(obj));
}

module.exports = { createSession, authenticate, sessionCookie, clearCookie, readJsonBody, json };
