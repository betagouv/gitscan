## Changelog : csplab (30 derniers jours, au 23 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des recrutements, notamment l'ajout de contrôles d'accès basés sur les rôles (RBAC), l'intégration de nouvelles fonctionnalités pour les recruteurs et l'amélioration de l'ingestion et de la gestion des données. Des améliorations significatives ont également été apportées à l'interface utilisateur et à l'expérience développeur.

### Évolutions fonctionnelles
- **Recrutement :** Mise en place du contrôle d'accès basé sur les rôles (RBAC) pour la liste et le détail des recrutements [#1026, #1030]. Les agents disposent désormais de permissions spécifiques pour accéder aux informations de recrutement.
- **Recrutement :** Implémentation du RBAC pour la création d'organismes [#1025].
- **Recruteur :** Ajout de la possibilité de se déconnecter et refactorisation du stockage des informations utilisateur [#1022].
- **Ingestion :** Gestion des codes NIV_DIPL dans le mapping du niveau d'études [#1028].
- **Ingestion :** Prise en charge des dates de modification nulles lors de l'ingestion de données [#1019].
- **Frontend :** Traitement par lot des candidatures pour changer d'étape [#948].
- **Frontend :** Ajout d'un composant Kanban et d'un commutateur de vue liste pour la gestion des candidatures [#947].
- **Frontend :** Composants d'interface utilisateur améliorés, notamment des breadcrumbs, des composants de tri et des composants pour l'affichage des étapes du pipeline de recrutement [#852, #828, #821].
- **Frontend :** Ajout de guidance utilisateur pour les étapes du pipeline de recrutement [#915].
- **Recruteur :** Interface pour la gestion des recrutements et des organismes [#963, #911, #856].
- **Ingestion :** Ajout de la transmission des coordonnées GPS des offres vers l'API web [#969].
- **Ingestion :** Ajout des dates de début de vacances de poste et de fin de candidature aux données ingérées [#970].

### Évolutions techniques
- **Architecture :** Migration des données de recrutement vers Pinia Colada pour une meilleure gestion de l'état de l'application [#1011, #1003, #983].
- **Refactoring :** Refactorisation des tests pour améliorer la lisibilité et la maintenabilité [#1017, #320ea6b].
- **Infrastructure :** Amélioration de la configuration des review apps pour faciliter les tests et les déploiements [#975].
- **CI/CD :** Ajout de la création de releases Sentry lors des déploiements pour un meilleur suivi des erreurs [#850].
- **Ingestion :** Suppression du cycle d'importation circulaire pour Celery, améliorant la stabilité et la performance [#862].
- **Ingestion :** Ajout de mécanismes de retry pour la récupération des tokens Talentsoft [#873].
- **Documentation :** Ajout d'une ADR (Architecture Decision Record) concernant l'emplacement des modèles de lecture [#958].
- **Tooling :** Amélioration de la configuration de Django Debug Toolbar [#974].
- **Tooling :** Amélioration des commandes de vérification frontend pour faciliter le développement [#916, #926].
- **Tests :** Renforcement des tests RBAC pour la gestion des organismes [#1027].

### Autres changements
- **Documentation :** Ajout d'une documentation sur les règles métier dans la couche domaine [#863].
- **Nettoyage :** Suppression de la forme de contrat "STAGE" [#998].
- **Correction :** Correction d'un bug empêchant le chargement de l'application en production [#1001].
- **Correction :** Correction d'un bug lié à la sérialisation des dates dans les conditions d'offre [#888].
- **Correction :** Correction d'un bug empêchant la création d'utilisateurs et de sources [#986].
- **Correction :** Correction d'un bug lié à l'affichage des organismes [#893].
- **Correction :** Correction d'un bug lié à l'activation des cellules ou lignes dans les tableaux [#851].
- **Mises à jour :** Mise à jour des dépendances pour améliorer la sécurité et la stabilité [#952, #950, #951, #368b2a3].
- **Amélioration :** Amélioration des noms de loggers [#986].
- **Amélioration :** Amélioration de la lisibilité des tests en utilisant le décorateur `@patch` [#848].
- **Amélioration :** Remplacement de "Temps partiel" par "Temps incomplet" dans le référentiel [#999].
- **Amélioration :** Ajout de la possibilité de configurer la variable d'environnement pour activer/désactiver Django Debug Toolbar [#972].
- **Amélioration :** Amélioration de la gestion des erreurs Celery en capturant les exceptions dans Sentry [#861].
- **Amélioration :** Amélioration de la configuration des identifiants TalentSoft pour une plus grande flexibilité [#892].
- **Amélioration :** Amélioration de la configuration des tâches cron [#874].
- **Amélioration :** Ajout de la possibilité d'authentification par API key sur OffersBySourceView [#877].
- **Amélioration :** Amélioration du schéma OpenAPI pour la pagination [#875].
