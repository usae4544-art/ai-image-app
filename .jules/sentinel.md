## 2024-05-24 - Content Security Policy (CSP) Implementation
**Vulnerability:** Missing Content Security Policy (CSP). The application was missing a CSP, making it vulnerable to Cross-Site Scripting (XSS) and data injection attacks.
**Learning:** For standalone Babel applications using React without a build step, `unsafe-inline` and `unsafe-eval` are necessary in the `script-src` directive. External APIs and image/video domains must be explicitly whitelisted to prevent functional breakage.
**Prevention:** Implement a strict CSP from the start of the project and update it as new external dependencies are added. Avoid relying solely on `default-src`.
