## Changelog : proconnect-espace-partenaires (30 derniers jours, au 06 juillet 2026)

### Résumé
Les dernières mises à jour de l'espace partenaires ProConnect se concentrent sur l'amélioration de la documentation concernant l'authentification forte (MFA), notamment en clarifiant les niveaux de sécurité et en intégrant les recommandations de l'ANSSI. Des améliorations ont également été apportées à la gestion des collaborateurs et à la configuration de l'application.

### Évolutions fonctionnelles
- Possibilité pour les partenaires d'ajouter des collaborateurs à leur espace. Cette fonctionnalité a été temporairement revertée en raison de problèmes, mais est en cours de stabilisation. [#386](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/386)
- Amélioration de la documentation sur l'authentification à double facteur (MFA) et l'eIDAS, avec une distinction claire entre les niveaux de sécurité et l'intégration des guides de l'ANSSI. [#375](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/375), [#367](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/367), [#362](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/362)
- Clarification de la classification de l'authentification par email OTP comme MFA faible. [#388](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/388)

### Évolutions techniques
- Mise à jour des valeurs AMR (Authentication Method Reference) pour utiliser des standards. [#385](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/385)
- Mise à jour de la dépendance `proconnect-gouv/federation/api-partner`. [#366](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/366), [#356](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/356)
- Suppression d'une note de prudence concernant la définition du niveau ACR (Authentication Context Reference). [#369](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/369)
- Suppression d'anciennes adresses IP de la configuration. [#390](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/390)

### Autres changements
- Ajout d'un dossier `.idea` au `.gitignore` pour IntelliJ IDEA. [#391](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/391)
- Mise à jour de liens vers le code de calcul du service public. [#384](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/384)
- Améliorations de la documentation sur l'authentification forte et l'eIDAS. [#390](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/390)
