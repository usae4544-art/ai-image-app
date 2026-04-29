## 2026-04-29 - Reverse Tabnabbing Vulnerability
**Vulnerability:** Found `window.open(url, "_blank")` without `noopener,noreferrer` arguments. This exposes the application to Reverse Tabnabbing.
**Learning:** `window.open` defaults to keeping a reference to the `window.opener` object, which a malicious page could exploit to redirect the original page to a phishing site.
**Prevention:** Always add `"noopener,noreferrer"` as the third argument to `window.open` calls when opening untrusted or external URLs.
