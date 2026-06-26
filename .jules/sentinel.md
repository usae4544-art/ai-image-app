## 2024-06-26 - Add Content Security Policy
**Vulnerability:** Missing Content Security Policy (CSP) headers in `index.html`.
**Learning:** For standalone Babel applications, `unsafe-inline` and `unsafe-eval` are required for scripts to work properly. Additionally, explicit directives like `media-src`, `img-src`, `font-src`, and `connect-src` must be defined to whitelist required external domains (like image.pollinations.ai, pexels, etc.) and prevent falling back to a restrictive `default-src` which would break core application functionality.
**Prevention:** Always implement a restrictive but functional CSP in frontend applications, ensuring necessary third-party domains and scripts are explicitly permitted while blocking unexpected external resources.
