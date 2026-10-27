## Changelog : people (30 derniers jours, au 12 octobre 2026)

### Résumé
Les évolutions de ce mois se sont concentrées sur le renforcement de la sécurité des accès et de la confidentialité des données, ainsi que sur une modernisation importante de l'infrastructure de développement et des outils de qualité de code.

### Évolutions fonctionnelles
- **Sécurité et confidentialité** :
  - Renforcement de la validation des domaines d'e-mails pour les organisations.
  - Restriction de la visibilité des configurations de domaine pour les utilisateurs ayant uniquement des droits de lecture.

### Évolutions techniques
- **Infrastructure et CI/CD** :
  - Mise à jour majeure des actions GitHub (Checkout, Setup Python, Setup Node, Cache et Upload Artifact).
- **Qualité du code et Linting** :
  - Migration vers ESLint 9 et transformation de la configuration interne en plugin.
  - Application de nouvelles règles de linting et refactoring de variables pour la conformité Sonar.
- **Sécurité et Dépendances** :
  - Mise à jour de `urllib3` et `eslint` pour corriger des vulnérabilités.
- **Architecture et Backend** :
  - Suppression des tables liées aux fournisseurs OAuth de la base de données.
  - Mise à jour des configurations applicatives front-end (Desk app, i18n et E2E).

### Autres changements
- Mise à jour des chaînes de caractères traduites (i18n).
- Publication de la version 1.26.1.
