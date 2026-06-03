## 2024-06-03 - Inconsistent Reverse Tabnabbing Protections
**Vulnerability:** Reverse tabnabbing vulnerability via `window.open`.
**Learning:** While anchor tags (`<a target="_blank">`) in the codebase correctly used `rel="noopener noreferrer"`, the JavaScript `window.open` calls missed the equivalent parameter (`"noopener,noreferrer"`), leaving the application vulnerable to reverse tabnabbing attacks where malicious pages can access `window.opener`. This is a codebase-specific inconsistency pattern to watch for.
**Prevention:** Always verify that both anchor tags and programmatic `window.open` calls include appropriate `noopener` and `noreferrer` protections.
