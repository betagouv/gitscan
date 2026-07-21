## Changelog : transfers (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la sécurité et la robustesse du service. Une nouvelle fonctionnalité de scan antivirus a été intégrée pour protéger les fichiers stockés, et des corrections ont été apportées pour améliorer la fiabilité du processus de rescan.

### Évolutions fonctionnelles
- Ajout d'un scan antivirus pour les fichiers transférés afin d'empêcher le stockage de fichiers dangereux. [#9](https://github.com/suitenumerique/transfers/issues/9)
- Amélioration de la robustesse du scan antivirus en cas de scanner indisponible.

### Évolutions techniques
- Correction de la configuration de la politique de sécurité du contenu (CSP) pour autoriser les requêtes vers les origines S3 lors des uploads.
- Résolution des points soulevés lors de la revue de code concernant le flux de rescan.

### Autres changements
- Aucun changement significatif à signaler.
