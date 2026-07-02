## Changelog : csplab (30 derniers jours, au 01 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'ingestion des offres d'emploi, notamment avec l'ajout de la gestion des sources et des webhooks Talentsoft. L'interface utilisateur a également été enrichie avec de nouveaux composants et des améliorations de l'expérience utilisateur, en particulier pour la gestion des recrutements et des organismes. Des efforts ont été faits pour améliorer la robustesse et la surveillance de l'application, avec l'ajout de logs et de mécanismes de reprise après erreur.

### Évolutions fonctionnelles
- Ajout de la gestion des sources d'offres, avec la possibilité de lier des utilisateurs à des sources spécifiques et d'autoriser l'accès aux endpoints d'ingestion en fonction de la source [#721](https://github.com/betagouv/csplab/issues/721).
- Implémentation de l'importation de toutes les offres Talentsoft via des webhooks CREE [#858](https://github.com/betagouv/csplab/issues/858).
- Possibilité d'authentification par API key sur l'endpoint des offres par source [#877](https://github.com/betagouv/csplab/issues/877).
- Amélioration de l'interface utilisateur pour le processus organisme, affichant le pipeline actif [#821](https://github.com/betagouv/csplab/issues/821).
- Ajout d'une interface pour la gestion des étapes de recrutement d'un organisme [#856](https://github.com/betagouv/csplab/issues/856).
- Interface pour la mise à jour des étapes de recrutement d'un organisme [#835](https://github.com/betagouv/csplab/issues/835).
- Ajout d'une interface pour afficher les détails d'un recrutement [#856](https://github.com/betagouv/csplab/issues/856).
- Ajout d'une interface pour la gestion de mes recrutements [#838](https://github.com/betagouv/csplab/issues/838).
- Implémentation de la soumission de candidature [#729](https://github.com/betagouv/csplab/issues/729).
- Ajout d'une page de connexion avec une interface utilisateur [#752](https://github.com/betagouv/csplab/issues/752).
- Ajout de la possibilité de visualiser le métier dans la liste des offres [#747](https://github.com/betagouv/csplab/issues/747).
- Ajout d'une authentification 2FA sur l'admin Django [#699](https://github.com/betagouv/csplab/issues/699).

### Évolutions techniques
- Séparation de `IOffersRepository` en une interface de base et une interface pour l'ingestion des offres [#887](https://github.com/betagouv/csplab/issues/887).
- Refactorisation du Storybook, incluant des améliorations des workflows de déploiement et de prévisualisation [#871](https://github.com/betagouv/csplab/issues/871), [#872](https://github.com/betagouv/csplab/issues/872), [#867](https://github.com/betagouv/csplab/issues/867).
- Amélioration de la lisibilité des tests avec l'utilisation du décorateur `@patch` [#848](https://github.com/betagouv/csplab/issues/848).
- Ajout de la gestion des erreurs Celery dans Sentry [#861](https://github.com/betagouv/csplab/issues/861).
- Mise en place de tâches quotidiennes pour le calcul des statistiques [#884](https://github.com/betagouv/csplab/issues/884).
- Amélioration de la gestion des tâches cron pour l'ingestion [#874](https://github.com/betagouv/csplab/issues/874).
- Ajout de retries pour la récupération du token Talentsoft [#873](https://github.com/betagouv/csplab/issues/873).
- Déplacement du modèle `Source` dans une librairie partagée [#847](https://github.com/betagouv/csplab/issues/847).
- Ajout de releases Sentry lors des déploiements [#850](https://github.com/betagouv/csplab/issues/850).
- Suppression du cycle d'import Celery app -> container [#862](https://github.com/betagouv/csplab/issues/862).
- Utilisation de `include` pour enregistrer les tâches Celery [#883](https://github.com/betagouv/csplab/issues/883).
- Amélioration de la gestion des logs API, avec ajout de logs et d'une interface d'administration [#720](https://github.com/betagouv/csplab/issues/720), [#733](https://github.com/betagouv/csplab/issues/733).
- Mise en place d'un script de sauvegarde de la base de données Scaleway via Scalingo cron job [#833](https://github.com/betagouv/csplab/issues/833).
- Amélioration de la gestion des erreurs et des exceptions dans les tâches asynchrones [#783](https://github.com/betagouv/csplab/issues/783).

### Autres changements
- Correction de la sérialisation JSON des dates dans les conditions d'offre [#888](https://github.com/betagouv/csplab/issues/888).
- Correction du schéma OpenAPI de OffersListView pour la pagination [#875](https://github.com/betagouv/csplab/issues/875).
- Ajout de règles métier dans la couche domaine [#863](https://github.com/betagouv/csplab/issues/863).
- Ajout de documentation pour l'API [#813](https://github.com/betagouv/csplab/issues/813).
- Ajout d'un script pour mettre à jour les dépendances [#832](https://github.com/betagouv/csplab/issues/832).
- Ajout d'un script pour installer les dépendances [#834](https://github.com/betagouv/csplab/issues/834).
- Ajout de tests unitaires et d'intégration.
- Amélioration de la structure des tests et refactorisation de certains tests [#849](https://github.com/betagouv/csplab/issues/849), [#745](https://github.com/betagouv/csplab/issues/745).
- Ajout de la documentation de l'API dans un fichier markdown [#820](https://github.com/betagouv/csplab/issues/820).
- Ajout d'un fichier `security.txt` [#695](https://github.com/betagouv/csplab/issues/695).
- Correction de divers bugs et améliorations de la qualité du code.
