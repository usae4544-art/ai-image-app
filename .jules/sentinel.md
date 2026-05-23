## 2026-05-23 - Reverse Tabnabbing and Content Security Policy gaps
**Vulnerability:** Reverse tabnabbing via `window.open` without `noopener,noreferrer` and lack of a Content Security Policy (CSP) allowing inline scripts without restrictions.
**Learning:** React applications relying on client-side Babel transpilation need `unsafe-inline` and `unsafe-eval` for scripts to work properly when configuring a CSP. Furthermore, `window.open` should always include `noopener,noreferrer` to prevent a newly opened page from accessing the originating page's context.
**Prevention:** Always configure a strict CSP allowing only necessary external domains. And always use `noopener,noreferrer` with `window.open(url, "_blank")`.
