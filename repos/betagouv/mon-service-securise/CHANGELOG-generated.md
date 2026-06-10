## Changelog : mon-service-securise (30 derniers jours, au 09 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'administration des utilisateurs et des organisations, avec l'ajout de fonctionnalités pour gérer les rôles, les accès et les superviseurs. Des améliorations d'accessibilité et des corrections de bugs ont également été apportées pour améliorer l'expérience utilisateur. Enfin, des optimisations techniques ont été réalisées, notamment concernant la gestion des données et la sécurité.

### Évolutions fonctionnelles
- Ajout de la gestion des administrateurs d'organisations : possibilité de nommer, supprimer et lister les administrateurs d'une organisation.
- Implémentation de l'attribution de rôles aux utilisateurs administrés.
- Ajout d'une fonctionnalité permettant de retirer des accès aux utilisateurs administrés.
- Amélioration de l'interface utilisateur pour la gestion des entités et des services associés aux administrateurs.
- Affichage du nombre d'entités et de services par utilisateur administré.
- Possibilité de nommer un administrateur sur un périmètre complet.
- Ajout d'une page listant les utilisateurs pour un administrateur d'organisation.
- Ajout d'une fonctionnalité permettant d'exporter les mesures au format CSV.
- Mise en avant de la formation sur la page d'accueil.

### Évolutions techniques
- Refonte de la gestion des superviseurs avec un nouveau dépôt de données orienté objet.
- Chiffrement des données sensibles dans les tables `superviseur` et `admin_organisations`.
- Simplification et amélioration de la gestion des configurations Knex.
- Utilisation de composants DSFR pour améliorer la cohérence visuelle et l'accessibilité.
- Mise à jour de plusieurs dépendances (axios, @vitest/eslint-plugin, @axe-core/playwright, eslint, basic-ftp).
- Amélioration de la gestion des erreurs et des alertes.
- Optimisation du code et suppression de code obsolète.
- Ajout de tests et amélioration de la couverture de test.

### Autres changements
- Corrections d'accessibilité sur plusieurs pages (statistiques, CGU, mentions légales, activation, connexion, création de service, matrices de risques v2).
- Corrections de liens et d'URLs incorrectes.
- Amélioration de la documentation et des commentaires.
- Ajout de rapports de tests d'accessibilité.
- Ajout d'un script pour faciliter la mise à jour de l'UI Kit.
- Suppression de mocks et utilisation de la persistance mémoire.
- Amélioration de la gestion des événements et des logs.
- Ajout de badges et d'indicateurs visuels pour améliorer la clarté de l'interface.
- Correction de problèmes liés au calcul des services "seul propriétaire".
- Suppression de code dupliqué.
- Ajout d'un singleton pour la connexion Knex.
- Ajout d'une barre d'actions et d'un système de pagination.
- Amélioration de la gestion des erreurs et des exceptions.
