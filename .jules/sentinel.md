## 2024-05-16 - Prevent Reverse Tabnabbing
**Vulnerability:** Reverse Tabnabbing via `window.open` calls without `noopener,noreferrer`. The newly opened tab could potentially redirect the original tab to a malicious site.
**Learning:** React applications using `window.open(url, "_blank")` are vulnerable to reverse tabnabbing unless explicitly protected. The `rel="noopener noreferrer"` attribute in `<a>` tags does not apply to programmatic window opening.
**Prevention:** Always pass `"noopener,noreferrer"` as the third parameter to `window.open` when opening external URLs, e.g., `window.open(url, "_blank", "noopener,noreferrer")`.
