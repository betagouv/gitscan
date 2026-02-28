## Changelog : rapportnav2 (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à rapportnav2 au cours des 30 derniers jours. Les mises à jour incluent des corrections de bugs, des améliorations de la sécurité, de nouvelles fonctionnalités pour l'administration et l'interface utilisateur, ainsi que des optimisations techniques pour la gestion des erreurs et des tests.

### Évolutions fonctionnelles
- Ajout de la pagination et de la recherche sur la page "Informations générales" dans l'interface d'administration. (#1231)
- Amélioration de l'interface pour la saisie des coordonnées GPS. (#1217)
- Implémentation de l'affichage du nombre de cibles sur le titre. (#1206)
- Ajout de la gestion du nombre de cibles dans l'interface utilisateur. (#1206)

### Évolutions techniques
- Renforcement de la sécurité avec l'ajout de logs d'audit pour les clés API et l'authentification.
- Amélioration de la configuration de la sécurité CORS et CSRF.
- Mise en place de la journalisation Sentry pour le suivi des erreurs et des performances.
- Refactorisation de la gestion des erreurs avec l'implémentation des réponses "Problem Detail" selon RFC 7807.
- Amélioration des tests unitaires et d'intégration, notamment pour les entités JPA et les cas d'utilisation.
- Mise à jour des dépendances : `monitor-ui`, `aquasecurity/trivy-action`, `flyway`.
- Correction de problèmes liés à la configuration de Spring et à l'emplacement des fichiers de configuration.
- Amélioration de la gestion des erreurs lors de l'exportation de données.
- Correction d'un problème de chargement des données dans l'interface utilisateur.
- Correction d'un problème lié à l'utilisation de l'ID de l'unité de contrôle lors de la mise à jour des ressources.
- Correction d'un bug empêchant la suppression de missions. (#1233)
- Correction d'un bug lié à la complétion des statistiques de ressources. (#1253)

### Autres changements
- Ajout de tests pour MonitorEnv.
- Nettoyage du code et refactorisation de certaines parties du backend.
- Mise à jour de la documentation.
- Corrections de vulnérabilités identifiées par les outils d'analyse de sécurité (npm audit, Trivy).
- Amélioration de la configuration de l'image Docker pour la sécurité.
- Suppression de données sensibles dans les logs.
- Ajout de la validation des données sur le contrôleur `MissionGeneralInfoRestController`.
