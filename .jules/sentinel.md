## 2024-05-24 - Missing Security Headers and Tabnabbing
**Vulnerability:** The application was missing a Content Security Policy (CSP), allowing potential execution of untrusted scripts or loading of unauthorized resources. Additionally, `window.open` calls lacked `noopener,noreferrer`, exposing the app to Reverse Tabnabbing.
**Learning:** For standalone Babel applications, CSP requires `unsafe-inline` and `unsafe-eval` for scripts, but explicit directives for `img-src` and `media-src` prevent fallback to a restrictive `default-src`.
**Prevention:** Always define explicit CSP headers and use `noopener,noreferrer` when opening external links in new tabs.
