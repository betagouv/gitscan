## Changelog : mon-service-securise (30 derniers jours, au 01 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la gestion des administrateurs et des superviseurs, avec l'ajout de nouvelles fonctionnalités pour leur gestion via une interface dédiée. Des améliorations d'accessibilité et de correction de bugs ont également été apportées à l'ensemble de l'application. Enfin, une migration vers TypeScript est en cours pour améliorer la maintenabilité du code.

### Évolutions fonctionnelles
- Ajout d'une page d'administration des utilisateurs permettant de visualiser les administrateurs et leurs entités associées.
- Possibilité de nommer un autre utilisateur en tant qu'administrateur.
- Ajout de la suppression d'un administrateur.
- Ajout de la gestion des superviseurs, incluant la possibilité de rattacher une entité à un superviseur et de supprimer cette association.
- Affichage du badge "Admin" dans la liste des utilisateurs et dans le tableau de bord.
- Ajout d'une fonctionnalité permettant d'inviter des administrateurs et de gérer les invitations en cours.
- Affichage du nombre d'entités et de services par utilisateur administré.
- Amélioration de l'affichage des informations sur les contributeurs, incluant l'indication de leur statut d'administrateur.
- Ajout d'une page listant les utilisateurs pour un administrateur d'organisation.

### Évolutions techniques
- Migration progressive du code JavaScript vers TypeScript pour améliorer la robustesse et la maintenabilité.
- Refonte de l'architecture de la gestion des superviseurs avec un nouveau dépôt de données.
- Chiffrement des données sensibles dans les tables `superviseur` et `admin_organisations`.
- Extraction de composants Svelte réutilisables pour améliorer la cohérence de l'interface utilisateur.
- Amélioration de la structure du code et suppression de code obsolète.
- Utilisation de composants DSFR pour la page conseils cyber.
- Simplification de certains composants et logique métier.
- Mise à jour de plusieurs dépendances (axios, @tiptap/*, @sentry/vite-plugin, @electric-sql/pglite, uuid).

### Autres changements
- Améliorations de l'accessibilité sur plusieurs pages (statistiques, CGU, mentions légales, activation, connexion, matrice de risque).
- Correction de liens et d'éléments d'accessibilité sur différentes pages.
- Amélioration de l'affichage et du style de certains éléments de l'interface utilisateur (badges, blocs, images).
- Ajout de tests d'accessibilité et correction des problèmes détectés.
- Mise à jour de la documentation et des commentaires dans le code.
- Correction de bugs mineurs et améliorations de la performance.
- Suppression de mocks inutiles.
- Ajout de rapports d'erreurs plus précis.
- Correction de l'export CSV des mesures.
