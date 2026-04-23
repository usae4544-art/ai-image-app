## 2024-10-24 - [CRITICAL] Missing Content Security Policy in Standalone Babel React Apps

**Vulnerability:** The application completely lacked a Content Security Policy (CSP), X-Content-Type-Options, and Referrer-Policy headers. It heavily relies on external CDNs (Cloudflare, Google Fonts, image.pollinations.ai) to execute and render.

**Learning:** Single-file HTML apps that use Babel standalone to transpile React in the browser (`text/babel`) need `unsafe-inline` and `unsafe-eval` for scripts to work properly, making strict CSPs harder to implement but all the more necessary. Without CSP, these types of standalone apps are highly vulnerable to XSS and data exfiltration since there's no server-side component or build step to enforce security defaults or sanitize things at build time.

**Prevention:** Always include at least a basic `Content-Security-Policy` meta tag for any standalone, client-side heavy application, particularly those transpiling code at runtime. Always define allowed `script-src` explicitly, and include `img-src`, `style-src`, and `connect-src` specifically targeting the expected APIs. Limit lengths on input elements, e.g. `<textarea maxLength={1000} />` to mitigate potential DoS or massive payload submissions.
