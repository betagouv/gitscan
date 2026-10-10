## Changelog : people (30 derniers jours, au 08/10/2026)

### Résumé
Cette période est marquée par un renforcement de la sécurité et une simplification de l'application. Nous avons supprimé les fonctionnalités liées à l'authentification OAuth2 pour alléger le système et amélioré la confidentialité des données en limitant l'accès aux configurations de domaine pour certains profils d'utilisateurs.

### Évolutions fonctionnelles
- **Sécurité et confidentialité** : La configuration des domaines est désormais masquée pour les utilisateurs disposant uniquement de droits de lecture sur un domaine.

### Évolutions techniques
- **Sécurité** :
    - Amélioration de la précision de la correspondance des domaines d'e-mails pour les organisations.
    - Mise à jour de la bibliothèque `urllib3` vers la version 2.8.0 pour corriger des vulnérabilités.
- **Refactoring et simplification** :
    - Suppression des fonctionnalités et des tables de base de données liées à OAuth2 et aux fournisseurs d'identité (IdP).
- **Qualité de code et Frontend** :
    - Migration vers ESLint 9, incluant la transformation de la configuration de linting en un plugin dédié.
    - Mise à jour des configurations applicatives frontend (desk, i18n et e2e).

### Autres changements
- Mise à jour des chaînes de caractères traduites (i18n).
- Nettoyage de code pour la conformité aux standards de qualité (Sonar).
