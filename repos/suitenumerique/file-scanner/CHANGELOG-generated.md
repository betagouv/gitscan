## Changelog : file-scanner (30 derniers jours, au 21 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations de sécurité, de robustesse et de gestion des erreurs au service de scan de fichiers. Les scans sont maintenant plus fiables et protégés contre les vulnérabilités potentielles.

### Évolutions fonctionnelles
- Amélioration de la gestion des erreurs lors des scans, avec une distinction entre les erreurs transitoires et les erreurs liées aux fichiers [#12](https://github.com/suitenumerique/file-scanner/pull/12).
- Les scans par URL sont maintenant protégés contre les attaques SSRF ciblant des adresses non publiques [#12](https://github.com/suitenumerique/file-scanner/issues/12).

### Évolutions techniques
- Renforcement de la fonction `scan_task` pour éviter l'épuisement du disque et les faux échecs [#12](https://github.com/suitenumerique/file-scanner/issues/12).
- Revue globale du code et améliorations générales [#14](https://github.com/suitenumerique/file-scanner/pull/14).
- Suppression de l'attestation dans le workflow CI [#12](https://github.com/suitenumerique/file-scanner/pull/12).
