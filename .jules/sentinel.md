## 2026-04-30 - Prevent Reverse Tabnabbing
**Vulnerability:** window.open calls with "_blank" target without "noopener,noreferrer"
**Learning:** Using window.open with "_blank" can allow the newly opened window to access the parent window's context, leading to reverse tabnabbing attacks.
**Prevention:** Always use "noopener,noreferrer" when opening links in a new tab via window.open(url, "_blank", "noopener,noreferrer").