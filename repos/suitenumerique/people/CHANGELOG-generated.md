## Changelog : people (30 derniers jours, au 24 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à l'intégration avec DiMail, permettant l'import automatique de boîtes aux lettres et une gestion accrue des codes de connexion. Des mises à jour de sécurité ont également été implémentées pour protéger l'application et ses utilisateurs.

### Évolutions fonctionnelles
- Possibilité d'importer automatiquement les boîtes aux lettres depuis DiMail. [#2026-06-23-d83023d](https://github.com/suitenumerique/people/commit/d83023d)
- Augmentation du nombre maximal d'utilisations pour les codes de connexion DiMail, améliorant la flexibilité et la sécurité. [#2026-06-23-5df0df5](https://github.com/suitenumerique/people/commit/5df0df5)

### Évolutions techniques
- Mise à jour du script de publication pour inclure l'outil `uv`, optimisant la gestion des dépendances. [#2026-06-24-7a002ed](https://github.com/suitenumerique/people/commit/7a002ed)
- Amélioration de la sécurité en mettant à jour les paquets `cryptography` et `tornado`. [#2026-06-23-c5c9bcc](https://github.com/suitenumerique/people/commit/c5c9bcc)
- Mise à jour de la dépendance `PyJWT` pour corriger une vulnérabilité de sécurité. [#2026-06-23-8ee5a67](https://github.com/suitenumerique/people/commit/8ee5a67)
- Correction du Dockerfile pour réduire les vulnérabilités. [#2026-06-23-b3f36a7](https://github.com/suitenumerique/people/commit/b3f36a7)

### Autres changements
- Mise à jour des chaînes de traduction pour l'internationalisation (i18n). [#2026-06-24-9bb1758](https://github.com/suitenumerique/people/commit/9bb1758)
- Ajout d'une entrée au changelog pour le dernier commit. [#2026-06-23-9702927](https://github.com/suitenumerique/people/commit/9702927)
- Mises à jour de dépendances mineures (mjml, @html-to/text-cli, i18next-parser) pour corriger des vulnérabilités.
