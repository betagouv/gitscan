## Changelog : reva (30 derniers jours, au 30 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment dans la gestion des organismes certificateurs et des candidatures. Des corrections ont été apportées pour améliorer la fiabilité et la précision des données, et des fonctionnalités ont été ajoutées pour faciliter l'administration et l'interopérabilité du système. Des efforts importants ont également été consacrés à la sécurité et à la gestion des accès.

### Évolutions fonctionnelles
- Ajout de la possibilité de mettre à jour l'organisme certificateur d'une candidature directement depuis la page de résumé de la candidature dans l'interface d'administration.
- Amélioration de l'interface utilisateur pour la sélection des formacodes (v2) dans l'administration.
- Ajout d'une page de détails de l'organisme certificateur pour les candidats, avec la possibilité de modifier l'organisme certificateur associé à la candidature.
- Implémentation d'un système de gestion des accès plus granulaire basé sur des rôles et des politiques.
- Ajout de la possibilité de contacter l'équipe de support via un formulaire Crisp depuis différentes parties de l'application.
- Amélioration de la gestion des candidatures et des organismes certificateurs dans l'interopérabilité.
- Ajout de la gestion du format de dématérialisation autonome (DF_DEMAT_AUTONOME) pour les candidatures, incluant de nouvelles pages et fonctionnalités pour la gestion des pièces justificatives et des compétences.
- Ajout de la possibilité de filtrer les candidatures par statut DV dans l'administration.
- Amélioration de l'affichage des organismes certificateurs et des informations associées dans l'interface d'administration.

### Évolutions techniques
- Refactorisation de nombreux resolvers API pour utiliser le système `withPolicies` pour une meilleure gestion des autorisations.
- Migration de plusieurs composants vers TypeScript.
- Amélioration de la gestion des erreurs et des messages d'erreur.
- Mise à jour de nombreuses dépendances pour corriger des vulnérabilités et améliorer les performances.
- Suppression de code obsolète et simplification de certaines parties du code.
- Amélioration des tests unitaires et d'intégration.
- Ajout de tests HTTP pour l'interopérabilité.
- Centralisation de la logique d'autorisation et des messages d'erreur.
- Suppression de l'authentification par cookie et simplification du processus de connexion.
- Amélioration de la gestion des transactions et des performances des requêtes en base de données.
- Ajout de scripts pour rafraîchir les données des organismes certificateurs.

### Autres changements
- Mise à jour de la page CGU avec un lien vers le formulaire de contact.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Amélioration de la documentation.
- Correction de problèmes de compatibilité avec différents navigateurs.
- Mise à jour des dépendances de l'infrastructure (Strapi, PostgreSQL, etc.).
- Amélioration de la configuration et des scripts de déploiement.
- Correction de problèmes de performance.
- Suppression de l'outil Produkly.
