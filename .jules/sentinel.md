## 2024-06-07 - Reverse Tabnabbing and Missing CSP
**Vulnerability:** The application was missing a Content-Security-Policy (CSP) and had Reverse Tabnabbing vulnerabilities where `window.open` with `_blank` was used without `noopener,noreferrer`.
**Learning:** React/Babel standalone apps require `unsafe-inline` and `unsafe-eval` for scripts to work properly. All domains for external assets (CDNs, APIs) need to be whitelisted explicitly in the CSP. `window.open` should always use `noopener,noreferrer`.
**Prevention:** Always set a strict but functional CSP for web applications and use `noopener,noreferrer` when using `window.open(url, "_blank")`.
