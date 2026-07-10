## Changelog : csplab (30 derniers jours, au 9 juillet 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'interface utilisateur, notamment pour la gestion des recrutements et l'ajout de fonctionnalités de recherche et de filtrage. Des efforts importants ont également été consacrés à l'ingestion des offres d'emploi, avec des améliorations de la robustesse et de la gestion des sources de données. Enfin, des bases solides sont posées pour l'authentification et la gestion des utilisateurs.

### Évolutions fonctionnelles
- Ajout d'une page "Mes recrutements" avec des fonctionnalités de recherche, de filtrage et d'affichage des candidatures. [#900](https://github.com/betagouv/csplab/issues/900) [#899](https://github.com/betagouv/csplab/issues/899) [#898](https://github.com/betagouv/csplab/issues/898) [#897](https://github.com/betagouv/csplab/issues/897)
- Implémentation de l'interface pour la gestion des recrutements et des étapes associées. [#886](https://github.com/betagouv/csplab/issues/886) [#883](https://github.com/betagouv/csplab/issues/883) [#882](https://github.com/betagouv/csplab/issues/882) [#835](https://github.com/betagouv/csplab/issues/835)
- Ajout d'une guidance utilisateur pour les étapes du processus de recrutement. [#915](https://github.com/betagouv/csplab/issues/915)
- Possibilité de soumettre une candidature. [#729](https://github.com/betagouv/csplab/issues/729)
- Amélioration de l'affichage du pipeline de recrutement pour les organismes. [#821](https://github.com/betagouv/csplab/issues/821)
- Ajout d'un composant de notification (Toast). [#815](https://github.com/betagouv/csplab/issues/815)
- Ajout d'une page de connexion avec interface utilisateur. [#752](https://github.com/betagouv/csplab/issues/752)
- Ajout de la possibilité de créer des utilisateurs avec un profil candidat ou agent. [#744](https://github.com/betagouv/csplab/issues/744) [#735](https://github.com/betagouv/csplab/issues/735) [#722](https://github.com/betagouv/csplab/issues/722)

### Évolutions techniques
- Refactor de l'interface utilisateur frontend. [#944](https://github.com/betagouv/csplab/issues/944)
- Amélioration de la configuration de l'environnement de développement frontend. [#926](https://github.com/betagouv/csplab/issues/926)
- Ajout de modèles et d'entités pour la gestion du recrutement. [#913](https://github.com/betagouv/csplab/issues/913)
- Séparation des couches domaine et présentation pour une meilleure organisation du code.
- Refactor de l'architecture des tests pour une meilleure lisibilité.
- Mise en place d'un système de logs API pour le suivi des requêtes. [#720](https://github.com/betagouv/csplab/issues/720)
- Amélioration de la gestion des erreurs et des exceptions, notamment avec l'intégration de Sentry.
- Utilisation de Celery pour le traitement asynchrone des tâches d'ingestion.
- Amélioration de la gestion des dépendances et des déploiements.
- Sécurisation du déploiement avec la déclaration explicite des variables d'environnement.
- Ajout de tests et d'améliorations de la couverture de code.
- Mise en place de periodic tasks pour l'archivage des offres et le calcul des statistiques.
- Amélioration de la gestion des sources de données et de l'authentification.

### Autres changements
- Ajout de documentation pour l'API. [#865](https://github.com/betagouv/csplab/issues/865)
- Mise à jour de la documentation et du changelog.
- Correction de bugs et améliorations de la performance.
- Ajout de commandes de gestion pour faciliter l'administration du système.
- Amélioration de la lisibilité du code et refactoring de certaines parties.
- Ajout de modèles admin readonly pour les snapshots de statistiques. [#894](https://github.com/betagouv/csplab/issues/894)
- Configuration dynamique des identifiants TalentSoft. [#892](https://github.com/betagouv/csplab/issues/892)
- Ajout de scripts de sauvegarde de la base de données.
- Amélioration de la gestion des secrets et des clés API.
- Ajout de la gestion des événements de domaine.
- Ajout d'un composant de breadcrumb. [#852](https://github.com/betagouv/csplab/issues/852)
- Ajout d'un composant de tri. [#828](https://github.com/betagouv/csplab/issues/828)
- Ajout d'un composant de notification (Callout). [#910](https://github.com/betagouv/csplab/issues/910)
