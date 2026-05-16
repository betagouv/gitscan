## Changelog : anssi-demain-specialiste-cyber (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la sécurité du site, notamment en corrigeant une potentielle injection et en renforçant les mesures de protection contre les vulnérabilités. Des ajustements ont également été apportés pour l'intégration de Sentry, un outil de surveillance des erreurs, et des optimisations de configuration ont été réalisées.

### Évolutions fonctionnelles
- Intégration de Sentry pour le suivi des erreurs frontales, permettant une meilleure réactivité en cas de problèmes rencontrés par les utilisateurs.
- Ajout d'informations pour Claude, sans précision sur la nature de ces informations.

### Évolutions techniques
- Correction d'une injection de nonce potentielle, améliorant la sécurité du site.
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité :
    - `postcss` vers la version 8.5.10
    - `axios` vers la version 1.15.2
    - `fast-xml-builder` vers la version 1.1.6
    - `fast-xml-parser` vers la version 5.7.0
    - `follow-redirects` vers la version 1.16.0
- Ajout de Content Security Policy (CSP) pour renforcer la sécurité du site.
- Suppression d'une CSP inutile.
- Ajout de `@sentry/browser` comme dépendance du front-end.
- Injection de Sentry dans les headers des pages pour le suivi des erreurs.
- Ajustement de la configuration ESLint pour améliorer la qualité du code.

### Autres changements
- Suppression d'un fichier inutile.
