## 2026-05-20 - Fix Reverse Tabnabbing
**Vulnerability:** window.open calls with '_blank' missing 'noopener,noreferrer' features
**Learning:** React elements in inline script tags must include the third argument 'noopener,noreferrer' when using window.open to mitigate reverse tabnabbing attacks, as standard React 'target=_blank rel=noopener noreferrer' only applies to anchoring tags.
**Prevention:** Always append 'noopener,noreferrer' as the third argument to any window.open(url, '_blank') invocation.
