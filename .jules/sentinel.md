## 2024-04-24 - [CSP Considerations for Babel Standalone]
**Vulnerability:** Missing Content Security Policy (CSP) allowed unauthorized resource loading and left the app vulnerable to Cross-Site Scripting (XSS).
**Learning:** Babel standalone requires `unsafe-inline` and `unsafe-eval` in the CSP `script-src` directive, necessitating stronger alternative protections.
**Prevention:** Always implement a strict CSP, explicitly defining directives like `img-src` and `media-src` to allow core functionalities without falling back to a restrictive `default-src`.
