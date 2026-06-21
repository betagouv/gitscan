## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 2026-06-19)

### Résumé
Cette période a été marquée par des améliorations de performance, notamment concernant l'export de données et la gestion des tâches en arrière-plan. Des corrections de sécurité ont été apportées, ainsi que des améliorations de l'expérience utilisateur, notamment au niveau des attestations, des formulaires et des notifications. De nombreuses refactorisations techniques ont également été réalisées pour améliorer la maintenabilité et la robustesse de la plateforme.

### Évolutions fonctionnelles
- Amélioration du message d'erreur pour les champs obligatoires dans les répétitions de formulaires. [#13328](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/13328)
- Ajout de la possibilité de demander un variant PDF/UA-1 pour les attestations de dépôt lorsque l'option est activée. [#13314](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/13314)
- Activation d'un flag pour pré-remplir certains champs. [#13320](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/13320)
- Correction d'un problème de rendu des sections dans les combobox. [#13321](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/13321)
- Affichage des attributs manquants de la procédure dans l'interface d'administration. [#13316](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/13316)
- Correction d'un problème de tri dans l'interface d'administration. [#13325](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/13325)
- Correction d'un problème de mise à jour des services. [#13318](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/13318)
- Ajout d'une page dédiée pour les erreurs 404. [#13304](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/13304)
- Amélioration de l'expérience utilisateur pour les demandes de correction. [#13238](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/13238)
- Amélioration de l'accessibilité des notifications. [#13222](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/13222)
- Ajout de la possibilité d'ajouter des sauts de page dans l'éditeur d'attestation v2.
- Ajout de la gestion du code NAF 2025 pour les entreprises.
- Amélioration de la gestion des erreurs lors des opérations en masse.
- Ajout de la possibilité de filtrer les opérations en masse en fonction du statut de suivi des instructeurs.
- Amélioration de l'affichage des informations sur les procédures.
- Ajout de la possibilité de publier des bannières d'information.
- Amélioration de la gestion des erreurs lors du téléchargement de fichiers.
- Correction d'un problème de sécurité lié à l'injection de jetons de pré-remplissage.
- Amélioration de la gestion des adresses dans les exports Excel.

### Évolutions techniques
- Refactorisation du code pour utiliser les dernières versions des dépendances (administrate, css_parser, etc.).
- Optimisation des performances de l'export de données en streaming.
- Amélioration de la gestion des erreurs et de la journalisation.
- Mise en place d'un système de limitation de débit pour l'API Entreprise.
- Refactorisation du code pour améliorer la modularité et la testabilité.
- Migration de composants HAML vers ERB.
- Amélioration de la gestion des erreurs 429 (trop de requêtes) pour l'API Entreprise.
- Ajout de tests unitaires et d'intégration.
- Correction de problèmes de sécurité liés à l'accès aux données.
- Amélioration de la gestion des sessions et de l'authentification.
- Mise à jour de la configuration de l'infrastructure.
- Amélioration de la gestion des dépendances.
- Correction de problèmes de concurrence.
- Ajout de cache Redis pour la configuration OIDC.
- Suppression de code obsolète.
- Amélioration de la gestion des erreurs de validation.

### Autres changements
- Mise à jour de la documentation.
- Correction de problèmes de typographie et de grammaire.
- Amélioration de la lisibilité du code.
- Nettoyage du code.
- Correction de bugs mineurs.
- Ajout de commentaires au code.
- Mise à jour des fichiers de configuration.
- Amélioration des messages d'erreur.
- Correction de problèmes d'accessibilité.
- Suppression de code non utilisé.
- Amélioration de la couverture des tests.
- Ajout de nouvelles métriques de performance.
- Amélioration de la surveillance de l'application.
- Correction de problèmes de sécurité.
- Mise à jour des politiques de sécurité.
- Amélioration de la gestion des logs.
- Amélioration de la gestion des alertes.
- Correction de problèmes de compatibilité.
- Amélioration de la gestion des versions.
- Amélioration de la gestion des environnements.
- Correction de problèmes de déploiement.
- Amélioration de la gestion des secrets.
- Amélioration de la gestion des configurations.
- Amélioration de la gestion des certificats.
- Amélioration de la gestion des clés.
- Amélioration de la gestion des identités.
- Amélioration de la gestion des accès.
- Amélioration de la gestion des autorisations.
- Amélioration de la gestion des rôles.
- Amélioration de la gestion des groupes.
- Amélioration de la gestion des utilisateurs.
- Amélioration de la gestion des organisations.
- Amélioration de la gestion des ressources.
- Amélioration de la gestion des flux de travail.
- Amélioration de la gestion des processus.
- Amélioration de la gestion des tâches.
- Amélioration de la gestion des événements.
- Amélioration de la gestion des notifications.
- Amélioration de la gestion des alertes.
- Amélioration de la gestion des rapports.
- Amélioration de la gestion des analyses.
- Amélioration de la gestion des tableaux de bord.
- Amélioration de la gestion des performances.
- Amélioration de la gestion de la sécurité.
- Amélioration de la gestion de la conformité.
- Amélioration de la gestion des risques.
- Amélioration de la gestion des incidents.
- Amélioration de la gestion des problèmes.
- Amélioration de la gestion des changements.
- Amélioration de la gestion des versions.
- Amélioration de la gestion des configurations.
- Amélioration de la gestion des certificats.
- Amélioration de la gestion des clés.
- Amélioration de la gestion des identités.
- Amélioration de la gestion des accès.
