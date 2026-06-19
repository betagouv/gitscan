## Changelog : csplab (30 derniers jours, au 2026-06-18)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'ingestion des offres d'emploi, notamment via l'intégration de sources externes comme Talentsoft, et sur le développement de l'interface utilisateur (ATS) pour la gestion des candidatures. Des améliorations techniques ont également été apportées à l'infrastructure, aux tests et à la documentation du projet.

### Évolutions fonctionnelles
- Ajout de la persistance des champs additionnels des offres via l'interface référentiel. [#809](https://github.com/betagouv/csplab/issues/809)
- Initialisation des interfaces Organisme et Etape de Recrutement d'un Organisme dans la présentation recruteur. [#798](https://github.com/betagouv/csplab/issues/798)
- Ajout d'une documentation non-technique pour l'ingestion des données. [#813](https://github.com/betagouv/csplab/issues/813)
- Ajout de composants d'interface utilisateur (UI) pour l'ATS, incluant des badges, avatars, formulaires, onglets et composants de base. [#741](https://github.com/betagouv/csplab/issues/741), [#790](https://github.com/betagouv/csplab/issues/790), [#795](https://github.com/betagouv/csplab/issues/795), [#787](https://github.com/betagouv/csplab/issues/787)
- Affichage du métier du candidat dans la liste des offres. [#747](https://github.com/betagouv/csplab/issues/747)
- Implémentation de la soumission de candidature. [#729](https://github.com/betagouv/csplab/issues/729)
- Ajout d'une page de connexion avec l'interface utilisateur. [#752](https://github.com/betagouv/csplab/issues/752)
- Ajout de la possibilité de récupérer le nom d'utilisateur actuel dans l'ATS. [#741](https://github.com/betagouv/csplab/issues/741)
- Ajout de la gestion de l'authentification par email/mot de passe. [#639](https://github.com/betagouv/csplab/issues/639)
- Ajout d'un endpoint pour lister les métiers. [#569](https://github.com/betagouv/csplab/issues/569)

### Évolutions techniques
- Simplification de l'interface des événements de domaine (DDD). [#811](https://github.com/betagouv/csplab/issues/811)
- Ajout d'un tag `robots.txt` contrôlé par une variable d'environnement. [#810](https://github.com/betagouv/csplab/issues/810)
- Séparation du traitement des webhooks d'ingestion par type d'action. [#805](https://github.com/betagouv/csplab/issues/805)
- Traduction des erreurs de domaine en français. [#807](https://github.com/betagouv/csplab/issues/807)
- Amélioration de la cohérence du schéma OpenAPI entre Typescript et DRF. [#804](https://github.com/betagouv/csplab/issues/804)
- Suppression de la commande `make lint` lors du commit. [#803](https://github.com/betagouv/csplab/issues/803)
- Correction d'un bug lié à la suppression de `lint-internal-schema` dans le tooling CI. [#816](https://github.com/betagouv/csplab/issues/816)
- Mise à jour des dépendances frontend vers les dernières versions majeures. [#796](https://github.com/betagouv/csplab/issues/796)
- Correction d'un bug empêchant l'exécution des tâches Celery en raison d'une boucle d'événements fermée et ajout d'un timeout. [#797](https://github.com/betagouv/csplab/issues/797)
- Amélioration de la gestion des versions et ajout d'une vérification de la version de `pyproject.toml` lors des changements de librairies. [#801](https://github.com/betagouv/csplab/issues/801)
- Correction d'un bug dans l'ingestion web qui cachait l'ID source dans la sérialisation des offres. [#800](https://github.com/betagouv/csplab/issues/800)
- Correction d'un bug lié à l'envoi de l'ID source par offre lors de la mise à jour vers le web. [#802](https://github.com/betagouv/csplab/issues/802)
- Refactorisation de l'architecture pour utiliser Celery pour le traitement asynchrone des webhooks. [#737](https://github.com/betagouv/csplab/issues/737)
- Mise en place d'un scheduler Huey unique. [#782](https://github.com/betagouv/csplab/issues/782)
- Amélioration de la gestion des index dans la base de données. [#786](https://github.com/betagouv/csplab/issues/786), [#789](https://github.com/betagouv/csplab/issues/789)
- Refactorisation des tests et ajout de fixtures pour une meilleure lisibilité. [#726](https://github.com/betagouv/csplab/issues/726), [#783](https://github.com/betagouv/csplab/issues/783)
- Utilisation de `include` au lieu de `autodiscover` pour l'enregistrement des tâches Celery. [#783](https://github.com/betagouv/csplab/issues/783)
- Mise à jour des dépendances (OCR, web, ingestion, notebook). [#793](https://github.com/betagouv/csplab/issues/793), [#792](https://github.com/betagouv/csplab/issues/792), [#791](https://github.com/betagouv/csplab/issues/791), [#677](https://github.com/betagouv/csplab/issues/677), [#678](https://github.com/betagouv/csplab/issues/678), [#676](https://github.com/betagouv/csplab/issues/676), [#675](https://github.com/betagouv/csplab/issues/675)
- Migration vers un modèle utilisateur personnalisé. [#614](https://github.com/betagouv/csplab/issues/614), [#616](https://github.com/betagouv/csplab/issues/616), [#630](https://github.com/betagouv/csplab/issues/630), [#632](https://github.com/betagouv/csplab/issues/632)

### Autres changements
- Ajout de la documentation pour les scripts d'abonnement et de suppression des webhooks Talentsoft. [#721](https://github.com/betagouv/csplab/issues/721)
- Mise à jour du CHANGELOG pour la version 0.1.11. [#648](https://github.com/betagouv/csplab/issues/648)
- Ajout d'un fichier `security.txt`. [#695](https://github.com/betagouv/csplab/issues/695)
- Ajout d'un workflow pour la publication de Storybook. [#724](https://github.com/betagouv/csplab/issues/724), [#647](https://github.com/betagouv/csplab/issues/647)
- Documentation de l'architecture et des conventions frontend. [#595](https://github.com/betagouv/csplab/issues/595)
- Traduction du template de PR en français. [#619](https://github.com/betagouv/csplab/issues/619)
- Ajout d'un workflow pour l'assignation automatique des PR. [#606](https://github.com/betagouv/csplab/issues/606)
- Ajout d'un workflow pour la publication de Storybook. [#647](https://github.com/betagouv/csplab/issues/647)
- Suppression de la configuration `npm sass` pour le MVP CV. [#622](https://github.com/betagouv/csplab/issues/622)
- Ajout de tests d'accessibilité pour le flow CV. [#622](https://github.com/betagouv/csplab/issues/622)
