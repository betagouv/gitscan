## Changelog : people (30 derniers jours, au 24 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à l'intégration avec DiMail, permettant notamment l'import automatique de boîtes aux lettres. Des corrections de sécurité ont également été implémentées, ainsi que des mises à jour de traductions et de la gestion des codes de connexion.

### Évolutions fonctionnelles
- Possibilité d'importer automatiquement les boîtes aux lettres depuis DiMail. [#1040](https://github.com/suitenumerique/people/issues/1040)
- Augmentation du nombre d'utilisations maximales pour les codes de connexion DiMail, améliorant la robustesse du processus.
- Amélioration de l'export des informations de contact des domaines dans l'interface d'administration. [#1061](https://github.com/suitenumerique/people/issues/1061)

### Évolutions techniques
- Mise à jour de l'outil de publication (release script) pour utiliser `uv` à la place de `pip`.
- Amélioration de la sécurité en mettant à jour les paquets `cryptography` et `tornado`.
- Correction de vulnérabilités dans le Dockerfile.
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité (PyJWT, i18next-parser, mjml, @html-to/text-cli).

### Autres changements
- Mise à jour des chaînes de traduction.
- Publication de la version 1.26.0.
- Ajout d'une entrée au changelog pour le dernier commit.
