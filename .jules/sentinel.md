## 2024-05-24 - Add Content Security Policy
**Vulnerability:** Missing Content Security Policy exposing the app to XSS.
**Learning:** For standalone Babel applications, 'unsafe-inline' and 'unsafe-eval' must be included in the `script-src` directive for React and Babel to function correctly.
**Prevention:** Always implement a strict CSP that whitelists necessary external domains while restricting unknown sources.