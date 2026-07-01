## 2024-07-01 - Reverse Tabnabbing in window.open
**Vulnerability:** The application used `window.open(url, "_blank")` without specifying the `'noopener,noreferrer'` features. This could allow an opened third-party site to maliciously redirect the parent page using `window.opener.location`.
**Learning:** This vulnerability occurs because developers may be aware of `rel="noopener noreferrer"` for `<a>` tags but fail to apply the same concept when using JavaScript's `window.open()` to open new tabs.
**Prevention:** Always pass `'noopener,noreferrer'` as the third argument (window features) when using `window.open()` to open untrusted links in a new tab, or use `rel="noopener noreferrer"` on anchor tags.
