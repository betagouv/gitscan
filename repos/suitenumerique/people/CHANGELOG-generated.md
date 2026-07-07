## Changelog : people (30 derniers jours, au 24 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à l'intégration avec DiMail, permettant notamment l'import automatique de boîtes aux lettres. Des corrections de sécurité ont également été apportées, ainsi que des mises à jour de l'interface utilisateur et des scripts de publication.

### Évolutions fonctionnelles
- Possibilité d'importer automatiquement des boîtes aux lettres depuis DiMail. [#issue liée à l'import DiMail]
- Augmentation du nombre d'utilisations maximales des codes de connexion DiMail pour plus de flexibilité.
- Amélioration de l'interface utilisateur avec l'intégration de la nouvelle suite UI Kit et un nouveau layout.
- Ajout d'icônes pour configurer un domaine dans l'interface.
- Possibilité de trier les listes de boîtes aux lettres et de domaines.
- Possibilité de supprimer des invitations par email pour les domaines.
- Possibilité de rafraîchir les invitations expirées.

### Évolutions techniques
- Mise à jour de l'outil de publication pour utiliser `uv` au lieu de `pip`.
- Mise à jour des paquets `cryptography` et `tornado` pour corriger des failles de sécurité.
- Mise à jour de la librairie PyJWT vers la version 2.13.0 pour corriger une vulnérabilité de sécurité.
- Amélioration de la sécurité du Dockerfile.
- Correction de vulnérabilités dans les dépendances `mjml`, `@html-to/text-cli` et `i18next-parser`.

### Autres changements
- Mise à jour des traductions.
- Ajout d'une entrée au changelog pour le dernier commit.
- Correction du trailing slash sur l'endpoint de vérification DiMail.
- Amélioration des messages d'erreur pour les boîtes aux lettres.
- Passage des liens de connexion à des liens de connexion au lieu de mots de passe.
