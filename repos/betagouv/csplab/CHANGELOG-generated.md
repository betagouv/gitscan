## Changelog : csplab (30 derniers jours, au 2026-07-09)

### Résumé
Ce mois-ci, l'équipe a continué de développer les fonctionnalités clés de la plateforme, notamment autour du recrutement et de la gestion des offres. Des améliorations significatives ont été apportées à l'interface utilisateur, avec l'ajout de nouvelles pages et composants, ainsi que des optimisations techniques pour améliorer la performance et la stabilité de l'application. L'ingestion de données et la gestion des sources ont également été améliorées.

### Évolutions fonctionnelles
- Ajout d'une vue simplifiée pour une offre de recrutement et intégration de la liste des candidatures. [#946](https://github.com/betagouv/csplab/issues/946)
- Ajout d'une fonctionnalité de recherche de clients dans "Mes recrutements". [#900](https://github.com/betagouv/csplab/issues/900)
- Ajout d'un filtre sur la page "Mes recrutements". [#899](https://github.com/betagouv/csplab/issues/899)
- Création des entités et des modèles ORM pour le module recrutement. [#913](https://github.com/betagouv/csplab/issues/913)
- Ajout de guidance utilisateur pour les étapes du pipeline de recrutement. [#915](https://github.com/betagouv/csplab/issues/915)
- Amélioration de la lisibilité de l'administration des profils utilisateurs. [#938](https://github.com/betagouv/csplab/issues/938)
- Possibilité de rendre la condition de gestion optionnelle. [#939](https://github.com/betagouv/csplab/issues/939)
- Ajout d'une commande pour faciliter la création d'utilisateurs et de sources. [#914](https://github.com/betagouv/csplab/issues/914)
- Interface pour la gestion des étapes de recrutement des organismes. [#880](https://github.com/betagouv/csplab/issues/880) et [#883](https://github.com/betagouv/csplab/issues/883) et [#886](https://github.com/betagouv/csplab/issues/886)
- Ajout d'une interface pour les détails d'un recrutement. [#912](https://github.com/betagouv/csplab/issues/912)
- Amélioration de l'interface pour l'affichage du pipeline actif des organismes. [#821](https://github.com/betagouv/csplab/issues/821)
- Ajout d'un composant de notification CspToast. [#815](https://github.com/betagouv/csplab/issues/815)
- Ajout d'une page "Mes recrutements" avec des tableaux. [#898](https://github.com/betagouv/csplab/issues/898)
- Ajout d'un composant de liste triable CspSortableList. [#828](https://github.com/betagouv/csplab/issues/828)
- Ajout d'un composant de breadcrumb CspBreadcrumb. [#852](https://github.com/betagouv/csplab/issues/852)
- Ajout d'un composant de tabs. [#812](https://github.com/betagouv/csplab/issues/812)
- Ajout d'une page de login avec l'interface utilisateur. [#752](https://github.com/betagouv/csplab/issues/752)
- Affichage du métier dans la liste des offres. [#747](https://github.com/betagouv/csplab/issues/747)

### Évolutions techniques
- Refactor du frontend. [#944](https://github.com/betagouv/csplab/issues/944)
- Amélioration de la configuration de l'environnement de développement. [#926](https://github.com/betagouv/csplab/issues/926)
- Ajout de tests et amélioration de la couverture de code.
- Séparation de l'interface utilisateur en vues plus petites. [#928](https://github.com/betagouv/csplab/issues/928)
- Ajout de modèles et d'agrégats pour la gestion des notes. [#879](https://github.com/betagouv/csplab/issues/879) et [#878](https://github.com/betagouv/csplab/issues/878)
- Amélioration de la gestion des événements de domaine. [#811](https://github.com/betagouv/csplab/issues/811)
- Restructuration de l'architecture des microservices et des dépendances.
- Amélioration de la configuration des tâches cron pour l'ingestion. [#874](https://github.com/betagouv/csplab/issues/874)
- Séparation de la gestion des sources API et des sources de base de données. [#887](https://github.com/betagouv/csplab/issues/887)
- Ajout de statistiques et d'un modèle pour l'historique des statistiques. [#884](https://github.com/betagouv/csplab/issues/884)
- Amélioration de la gestion des erreurs et ajout de logs.
- Amélioration de la sécurité en restreignant l'authentification API key par plages d'IP. [#885](https://github.com/betagouv/csplab/issues/885)
- Ajout de retries pour la récupération du token Talentsoft. [#873](https://github.com/betagouv/csplab/issues/873)
- Mise en place de releases Sentry lors des déploiements. [#850](https://github.com/betagouv/csplab/issues/850)

### Autres changements
- Mise à jour de la documentation.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Mise à jour des dépendances.
- Amélioration des scripts de CI/CD.
- Ajout d'un script pour faciliter la mise à jour des dépendances. [#832](https://github.com/betagouv/csplab/issues/832)
- Correction de la sérialisation JSON des dates dans les conditions d'offre. [#888](https://github.com/betagouv/csplab/issues/888)
- Correction d'un problème d'incompatibilité entre la PR de changelog et les actions GitHub. [#895](https://github.com/betagouv/csplab/issues/895)
- Ajout d'un modèle admin readonly pour StatSnapshot. [#894](https://github.com/betagouv/csplab/issues/894)
- Rendre la configuration des identifiants TalentSoft dynamique. [#892](https://github.com/betagouv/csplab/issues/892)
- Ajout de tests unitaires et d'intégration.
- Amélioration de la lisibilité des tests.
- Correction de problèmes liés à l'exécution de Celery.
- Ajout de commentaires et documentation pour faciliter la maintenance du code.
- Mise à jour du CHANGELOG.md pour la version 0.1.12. [#799](https://github.com/betagouv/csplab/issues/799) et 0.1.11. [#648](https://github.com/betagouv/csplab/issues/648)
