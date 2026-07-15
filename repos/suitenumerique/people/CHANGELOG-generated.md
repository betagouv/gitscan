## Changelog : people (30 derniers jours, au 24 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à l'intégration avec DiMail, permettant l'import automatique de boîtes aux lettres et une gestion accrue des codes de connexion. Des corrections de sécurité et des mises à jour de dépendances ont également été effectuées pour assurer la stabilité et la sécurité de l'application.

### Évolutions fonctionnelles
- Possibilité d'importer automatiquement les boîtes aux lettres depuis DiMail. [#issue-non-disponible]
- Augmentation du nombre maximal d'utilisations pour les codes de connexion DiMail, améliorant la flexibilité et la sécurité. [#issue-non-disponible]
- Mise à jour du script de publication pour utiliser `uv`, optimisant le processus de déploiement. [#issue-non-disponible]

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité :
    - `cryptography` et `tornado`
    - `PyJWT` (version 2.13.0)
    - `i18next-parser`
    - `mjml` (version 4.18.0)
    - `@html-to/text-cli` (version 0.6.0)
- Amélioration de la sécurité du Dockerfile pour réduire les vulnérabilités. [#issue-non-disponible]
- Mise à jour des chaînes de traduction pour l'internationalisation (i18n). [#issue-non-disponible]

### Autres changements
- Ajout d'une entrée au changelog pour le dernier commit. [#issue-non-disponible]
- Mise à jour de la version de l'application à 1.26.0.
