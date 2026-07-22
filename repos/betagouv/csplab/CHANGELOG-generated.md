## Changelog : csplab (30 derniers jours, au 21 juillet 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'interface utilisateur, notamment avec l'ajout de fonctionnalités de recherche et de filtrage, ainsi que sur la migration de données vers de nouvelles sources et l'optimisation de l'infrastructure. Des améliorations ont également été apportées à l'ingestion de données et à la gestion des rôles des agents.

### Évolutions fonctionnelles
- Ajout du traitement par lot des candidatures et modification de l'étape correspondante [#948](https://github.com/betagouv/csplab/issues/948).
- Implémentation de la gestion des étapes de recrutement via Colada mutations [#1011](https://github.com/betagouv/csplab/issues/1011).
- Migration des données de candidatures vers une requête Colada partagée [#983](https://github.com/betagouv/csplab/issues/983).
- Mise en place des modèles de rôles pour les agents [#1000](https://github.com/betagouv/csplab/issues/1000).
- Correction d'un bug empêchant le chargement de l'application en production [#1001](https://github.com/betagouv/csplab/issues/1001).
- Ajout de la possibilité de filtrer et rechercher des candidatures [#977](https://github.com/betagouv/csplab/issues/977) et [#900](https://github.com/betagouv/csplab/issues/900).
- Intégration du Kanban et ajout d'un switch pour afficher les candidatures en liste [#947](https://github.com/betagouv/csplab/issues/947).
- Ajout d'un composant de notification (Toast) pour afficher des messages à l'utilisateur [#815](https://github.com/betagouv/csplab/issues/815) et [#910](https://github.com/betagouv/csplab/issues/910).
- Amélioration de l'interface pour la gestion des recrutements, avec l'ajout de pages et de composants dédiés [#946](https://github.com/betagouv/csplab/issues/946), [#897](https://github.com/betagouv/csplab/issues/897), [#898](https://github.com/betagouv/csplab/issues/898), [#851](https://github.com/betagouv/csplab/issues/851), [#856](https://github.com/betagouv/csplab/issues/856), [#838](https://github.com/betagouv/csplab/issues/838).
- Ajout de la possibilité de mettre à jour les étapes d'un organisme [#835](https://github.com/betagouv/csplab/issues/835) et [#819](https://github.com/betagouv/csplab/issues/819).
- Transmission des coordonnées GPS des offres via l'API web [#969](https://github.com/betagouv/csplab/issues/969).
- Ajout des dates de début de vacances de poste et de fin de candidature aux données des offres [#970](https://github.com/betagouv/csplab/issues/970).

### Évolutions techniques
- Migration des étapes de recrutement vers Colada [#1011](https://github.com/betagouv/csplab/issues/1011).
- Migration des listes de recrutements vers des requêtes Colada Pinia [#1003](https://github.com/betagouv/csplab/issues/1003).
- Refactorisation de la gestion des queryset avec des mappers [#976](https://github.com/betagouv/csplab/issues/976).
- Mise en place d'une configuration configurable pour la Django Debug Toolbar [#974](https://github.com/betagouv/csplab/issues/974).
- Refactorisation de l'interface utilisateur avec l'ajout de composants réutilisables [#944](https://github.com/betagouv/csplab/issues/944), [#852](https://github.com/betagouv/csplab/issues/852), [#853](https://github.com/betagouv/csplab/issues/853), [#857](https://github.com/betagouv/csplab/issues/857).
- Amélioration de la gestion des dépendances et des workflows CI/CD.
- Mise à jour des dépendances pour plusieurs modules (web, ocr, ingestion) [#952](https://github.com/betagouv/csplab/issues/952), [#829](https://github.com/betagouv/csplab/issues/829), [#831](https://github.com/betagouv/csplab/issues/831).
- Ajout de tests et amélioration de la couverture de code.
- Suppression de la forme de contrat "STAGE" [#998](https://github.com/betagouv/csplab/issues/998).
- Suppression de l'option d'affichage de l'API browsable dans DRF [#1004](https://github.com/betagouv/csplab/issues/1004).

### Autres changements
- Remplacement de "Temps partiel" par "Temps incomplet" dans le référentiel [#999](https://github.com/betagouv/csplab/issues/999).
- Ajout de documentation pour l'API et les processus métier.
- Mise à jour du CHANGELOG.md pour les versions 0.1.13 et 0.1.12 [#896](https://github.com/betagouv/csplab/issues/896) et [#799](https://github.com/betagouv/csplab/issues/799).
- Ajout de la sauvegarde de la base de données via un cron job Scalingo [#833](https://github.com/betagouv/csplab/issues/833).
- Ajout de la gestion des logs d'audit [#738](https://github.com/betagouv/csplab/issues/738).
