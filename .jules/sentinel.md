## 2024-05-22 - Reverse Tabnabbing Vulnerability
**Vulnerability:** Found `window.open` calls used to open external URLs in new tabs (`_blank`) without specifying `noopener,noreferrer`.
**Learning:** This exposes users to Reverse Tabnabbing, where the newly opened page can maliciously redirect the parent page via the `window.opener` object, leading to potential phishing attacks.
**Prevention:** Always include `"noopener,noreferrer"` as the third argument when using `window.open` to open external links, and use `rel="noopener noreferrer"` for anchor tags with `target="_blank"`.
