## 2024-06-09 - Missing Reverse Tabnabbing Protection
**Vulnerability:** window.open calls with target "_blank" lack the "noopener,noreferrer" features. This exposes the application to reverse tabnabbing, where the opened tab can gain reference to the window.opener object and potentially redirect the original page to a malicious site.
**Learning:** Even simple UI functions like "Download" or "Full Size" buttons that open new windows or tabs can be a vector for phishing attacks if they don't explicitly drop the window.opener reference.
**Prevention:** Always include 'noopener,noreferrer' as the third argument when using window.open(url, '_blank') or add rel='noopener noreferrer' for anchor tags with target='_blank'.
