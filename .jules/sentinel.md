## 2024-05-18 - Reverse Tabnabbing via window.open
**Vulnerability:** The application used `window.open(url, "_blank")` without the `"noopener,noreferrer"` arguments. This exposes the application to Reverse Tabnabbing, where the newly opened tab can access the original window's `window.opener` object and potentially redirect the original page to a malicious site.
**Learning:** Even in modern React applications, direct DOM manipulation methods like `window.open` need explicit security configurations, unlike React's target="_blank" which usually auto-adds rel="noopener noreferrer".
**Prevention:** Always include `"noopener,noreferrer"` as the third argument when using `window.open(url, '_blank')`.
