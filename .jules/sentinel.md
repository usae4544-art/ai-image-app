## 2024-05-15 - Reverse Tabnabbing via window.open in React
**Vulnerability:** The application used `window.open(url, "_blank")` without specifying `noopener,noreferrer` options in React onClick handlers.
**Learning:** While React automatically adds `rel="noopener noreferrer"` to `<a>` tags with `target="_blank"`, this protection does NOT extend to programmatic navigation via `window.open()`. This can allow the newly opened tab to access the `window.opener` object, leading to potential reverse tabnabbing attacks where the new page can navigate the original page to a malicious URL.
**Prevention:** Always explicitly include `"noopener,noreferrer"` as the third argument when using `window.open(url, "_blank")`, regardless of the framework being used.
