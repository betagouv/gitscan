## Changelog : people (30 derniers jours, au 24 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à l'intégration avec DiMail, permettant notamment l'import automatique de boîtes aux lettres. Des corrections de sécurité ont également été apportées, ainsi que des mises à jour de traductions et de la gestion des invitations.

### Évolutions fonctionnelles
- Possibilité d'importer automatiquement des boîtes aux lettres depuis DiMail. [#issue liée à l'import dimail]
- Augmentation du nombre maximal d'utilisations des codes de connexion DiMail pour une meilleure sécurité.
- Amélioration de l'interface d'administration pour la gestion des informations de contact des domaines. [#1061](https://github.com/suitenumerique/people/issues/1061)
- Possibilité de supprimer des invitations à des domaines par un administrateur. [#1040](https://github.com/suitenumerique/people/issues/1040)
- Rafraîchissement des invitations expirées. [#1050](https://github.com/suitenumerique/people/issues/1050)

### Évolutions techniques
- Mise à jour de l'outil de publication (release script) pour utiliser `uv` au lieu de `pip`.
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité : PyJWT, cryptography, tornado, i18next-parser, mjml, @html-to/text-cli.
- Amélioration de la sécurité du Dockerfile.
- Passage à Python version plus récente pour corriger une vulnérabilité. [#1010](https://github.com/suitenumerique/people/issues/1010)

### Autres changements
- Mise à jour des traductions.
- Publication de la version 1.26.0.
- Ajout d'une entrée au changelog pour le dernier commit.
