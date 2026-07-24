## Changelog : file-scanner (30 derniers jours, au 23 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations de sécurité importantes, notamment en bloquant les vulnérabilités SSRF lors des analyses d'URL. Des corrections ont également été apportées pour améliorer la robustesse du service et éviter les erreurs liées à l'espace disque. Enfin, des optimisations générales et des corrections de CI ont été effectuées.

### Évolutions fonctionnelles
- Amélioration de la robustesse des tâches d'analyse pour éviter les échecs liés à l'espace disque insuffisant et les fausses erreurs. [#12](https://github.com/suitenumerique/file-scanner/pull/12)
- Blocage des requêtes SSRF (Server-Side Request Forgery) vers des adresses non publiques lors des analyses d'URL, renforçant la sécurité.

### Évolutions techniques
- Mise à jour du pipeline CI pour préserver la commande `HEALTHCHECK` en forçant l'utilisation du manifest Docker v2 lors de la publication. [#15](https://github.com/suitenumerique/file-scanner/pull/15)
- Suppression de l'attestation dans le pipeline CI.
- Revue globale du code et améliorations diverses. [#14](https://github.com/suitenumerique/file-scanner/pull/14)
