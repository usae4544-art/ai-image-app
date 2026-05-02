## 2026-05-02 - Reverse Tabnabbing and Missing CSP
**Vulnerability:** window.open calls without noopener/noreferrer and missing Content-Security-Policy
**Learning:** External links and popups can expose the original tab's window object unless secured. Also, external domains for dynamically fetched media need to be explicitly allowed in img-src and media-src, not just connect-src.
**Prevention:** Always use noopener,noreferrer with window.open and target=_blank. Ensure CSP is restrictive but explicit about all required domains for scripts, styles, images, and media.
