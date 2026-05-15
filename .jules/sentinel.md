## 2024-05-15 - [CSP implementation for Babel standalone]
**Vulnerability:** Missing Content Security Policy (CSP) headers, making the app susceptible to XSS.
**Learning:** For standalone Babel applications, strict CSP cannot be fully applied as 'unsafe-inline' and 'unsafe-eval' are necessary for client-side transpilation to function. A restrictive CSP that falls back to 'default-src' can also unexpectedly block core image/video functionalities without explicit 'media-src' and 'img-src' definitions.
**Prevention:** Always ensure 'script-src' includes 'unsafe-inline' and 'unsafe-eval' in similar standalone Babel architectures, and explicitly whitelist external API domains across all necessary resource types (img-src, media-src, connect-src).
