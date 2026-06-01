## 2024-06-18 - Prevent Reverse Tabnabbing
**Vulnerability:** window.open was called without the third argument, exposing the window.opener reference.
**Learning:** React applications that open URLs dynamically via `window.open` rather than static `<a>` tags still suffer from Reverse Tabnabbing if `noopener,noreferrer` is omitted.
**Prevention:** Always include `"noopener,noreferrer"` as the third argument to `window.open` when opening an external or untrusted URL in a new tab (`_blank`).
