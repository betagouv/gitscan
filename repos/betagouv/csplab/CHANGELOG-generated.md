## Changelog : csplab (30 derniers jours, au 2026-06-19)

### Résumé
Ce mois-ci, l'équipe a continué à développer et améliorer les fonctionnalités de CSPLab, en se concentrant sur l'ingestion des offres d'emploi, l'interface utilisateur et l'infrastructure. Des améliorations significatives ont été apportées à la gestion des sources d'offres, à l'authentification, et à l'expérience utilisateur, notamment avec l'ajout de composants d'interface et l'amélioration de la gestion des erreurs.

### Évolutions fonctionnelles
- Ajout de la pagination pour la présentation des offres ATS. [#812](https://github.com/betagouv/csplab/issues/812)
- Possibilité de persister des champs additionnels pour les offres d'emploi. [#809](https://github.com/betagouv/csplab/issues/809)
- Ajout d'un tag meta "robots" contrôlable par une variable d'environnement pour l'indexation par les moteurs de recherche. [#810](https://github.com/betagouv/csplab/issues/810)
- Initialisation des interfaces Organisme et Étape de Recrutement d'un Organisme pour la présentation recruteur. [#798](https://github.com/betagouv/csplab/issues/798)
- Ajout de la possibilité de modifier plusieurs champs lors de la mise à jour d'une offre. [#808](https://github.com/betagouv/csplab/issues/808)
- Amélioration de l'affichage du métier dans la liste des offres pour les candidats. [#747](https://github.com/betagouv/csplab/issues/747)
- Ajout de la soumission de candidature. [#729](https://github.com/betagouv/csplab/issues/729)
- Ajout de la création d'utilisateurs avec un profil candidat et agent. [#744](https://github.com/betagouv/csplab/issues/744) et [#735](https://github.com/betagouv/csplab/issues/735)
- Ajout d'une page de connexion avec une interface utilisateur. [#752](https://github.com/betagouv/csplab/issues/752)
- Ajout de composants d'interface utilisateur (badges, avatars, conteneurs de contenu, onglets). [#790](https://github.com/betagouv/csplab/issues/790), [#741](https://github.com/betagouv/csplab/issues/741), [#682](https://github.com/betagouv/csplab/issues/682), [#683](https://github.com/betagouv/csplab/issues/683)
- Interception et gestion des erreurs frontend. [#629](https://github.com/betagouv/csplab/issues/629)

### Évolutions techniques
- Simplification de l'interface des événements de domaine (DDD). [#811](https://github.com/betagouv/csplab/issues/811)
- Refactorisation de la gestion des tâches asynchrones avec Celery, en les séparant par type d'action. [#805](https://github.com/betagouv/csplab/issues/805)
- Traduction des erreurs de domaine en français. [#807](https://github.com/betagouv/csplab/issues/807)
- Mise à jour des dépendances frontend vers les dernières versions majeures. [#796](https://github.com/betagouv/csplab/issues/796)
- Amélioration de la cohérence du schéma OpenAPI entre TypeScript et DRF. [#804](https://github.com/betagouv/csplab/issues/804)
- Suppression de `make lint` lors du commit. [#803](https://github.com/betagouv/csplab/issues/803)
- Correction d'une erreur de boucle d'événements et ajout d'un timeout aux tâches Celery. [#797](https://github.com/betagouv/csplab/issues/797)
- Utilisation de `include` au lieu de `autodiscover` pour l'enregistrement des tâches Celery. [#799](https://github.com/betagouv/csplab/issues/799)
- Exécution de Huey dans le conteneur web pour la compatibilité Scalingo. [#782](https://github.com/betagouv/csplab/issues/782)
- Amélioration des fixtures de tests d'intégration. [#726](https://github.com/betagouv/csplab/issues/726) et [#750](https://github.com/betagouv/csplab/issues/750)
- Refactorisation de l'architecture pour isoler les vues d'ingestion. [#662](https://github.com/betagouv/csplab/issues/662)
- Ajout d'index manquants sur les clés primaires. [#786](https://github.com/betagouv/csplab/issues/786) et [#789](https://github.com/betagouv/csplab/issues/789)
- Migration vers un modèle d'utilisateur personnalisé. [#614](https://github.com/betagouv/csplab/issues/614), [#616](https://github.com/betagouv/csplab/issues/616) et [#632](https://github.com/betagouv/csplab/issues/632)
- Refactorisation de l'organisation des tests. [#787](https://github.com/betagouv/csplab/issues/787) et [#673](https://github.com/betagouv/csplab/issues/673)
- Amélioration de la gestion des variables d'environnement pour les tests. [#785](https://github.com/betagouv/csplab/issues/785)

### Autres changements
- Ajout de documentation non technique pour l'ingestion. [#813](https://github.com/betagouv/csplab/issues/813)
- Mise à jour du CHANGELOG pour la version 0.1.11. [#648](https://github.com/betagouv/csplab/issues/648)
- Ajout d'un fichier `security.txt`. [#695](https://github.com/betagouv/csplab/issues/695)
- Ajout d'un template de PR en français. [#619](https://github.com/betagouv/csplab/issues/619)
- Configuration de GitHub Pages pour gérer un nom de domaine personnalisé. [#727](https://github.com/betagouv/csplab/issues/727)
- Ajout de tests Cypress pour le frontend. [#716](https://github.com/betagouv/csplab/issues/716)
- Ajout de documentation sur l'architecture et les conventions du frontend. [#595](https://github.com/betagouv/csplab/issues/595)
- Ajout d'un notebook pour comparer les référentiels Dila et Talentsoft. [#601](https://github.com/betagouv/csplab/issues/601)
