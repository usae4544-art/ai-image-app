## 2024-04-22 - [Add security enhancements: Input validation and tabnabbing prevention]
**Vulnerability:** Found missing input length limits on user prompts and potential reverse tabnabbing risks due to `window.open` calls without `noopener,noreferrer`.
**Learning:** The single-page React app lacked foundational input validation, presenting a potential DoS vector through overly large payloads. The `_blank` target was used without proper security attributes, exposing the application to tabnabbing.
**Prevention:** Ensure `maxLength` is implemented on UI inputs and validated in backend logic (or state-handling functions). Always include `"noopener,noreferrer"` when using `window.open` with `_blank`.
