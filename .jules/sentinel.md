## 2024-05-29 - Missing Content Security Policy
**Vulnerability:** Missing security headers (CSP) allowing potential XSS, data injection, and unauthorized resource loading.
**Learning:** Client-side React applications using Babel standalone require explicit 'unsafe-inline' and 'unsafe-eval' in script-src, making strict CSP challenging but necessary to restrict external domains.
**Prevention:** Implement a baseline CSP via meta tags or server headers restricting script-src, style-src, img-src, and media-src to explicitly whitelisted domains.
