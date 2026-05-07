## 2024-11-21 - [Reverse Tabnabbing Vulnerability]
**Vulnerability:** window.open calls with target `_blank` lack `noopener,noreferrer` arguments, exposing the application to reverse tabnabbing.
**Learning:** This occurs when a script opens a new window/tab without securing the opener reference, which malicious sites can abuse to redirect the original page or access its context.
**Prevention:** Always append `noopener,noreferrer` as the third argument when using `window.open(url, "_blank")` or use `rel="noopener noreferrer"` for anchor tags with `target="_blank"`.