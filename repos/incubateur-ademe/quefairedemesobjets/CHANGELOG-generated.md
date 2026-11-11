## Changelog : quefairedemesobjets (30 derniers jours, au 10 novembre 2026)

### Résumé
Ce mois a été marqué par une étape majeure avec le passage de l'Assistant en version 2, offrant une expérience utilisateur plus fluide, une cartographie plus rapide et un parcours de recherche amélioré. Parallèlement, le projet renforce son ouverture de données (Open Data) via une nouvelle API et modernise ses outils de gestion interne pour une meilleure qualité des données.

### Évolutions fonctionnelles
- **Lancement de l'Assistant V2** : déploiement d'une nouvelle interface incluant un parcours complet (accueil, fiches lieux, solutions et carte), une cartographie optimisée (glyphes statiques, compression des tuiles) et une meilleure gestion de la géolocalisation [#3576](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3576) [#3645](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3645).
- **Généralisation de l'Assistant** : fin de la phase bêta et bascule automatique de toutes les intégrations par iframe vers la version 2 [#3655](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3655).
- **Ouverture des données (Open Data)** : mise à disposition des lieux, des fiches produits et des consignes de tri via la nouvelle API v1 et sur stockage S3 [#3517](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3517) [#3444](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3444).

### Évolutions techniques
- **Modernisation de l'administration** : mise en place d'une nouvelle architecture (Django + React) pour la gestion des suggestions de données, incluant des actions de masse et une interface de revue optimisée [#3488](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3488) [#3493](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3493).
- **Optimisation de la CI/CD** : refonte majeure des pipelines pour gagner en rapidité et en fiabilité (parallélisation des tests avec pytest-xdist, optimisation du cache Docker, exécution différenciée selon les changements de la PR) [#3593](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3593) [#3587](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3587) [#3586](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3586).
- **Intelligence Artificielle** : introduction d'une approche par Machine Learning pour automatiser la déduplication des acteurs [#3176](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3176).
- **Infrastructure & API** : déploiement de l'instance de l'API v1 pour les requêtes géographiques et la recherche de lieux [#3509](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3509) [#3434](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3434).
- **Corrections de bugs** : résolution de problèmes de compatibilité avec Django 6.1 [#3664](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3664), correction de l'affichage mobile des iframes [#3635](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3635) et de la persistance de la géolocalisation lors des redirections [#3498](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3498).

### Autres changements
- **Documentation** : ajout de la documentation pour le nouveau système de gestion des suggestions administratives [#3494](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3494).
- **Nettoyage** : suppression des scripts d'intégration obsolètes et des notifications Mattermost [#3662](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3662) [#3558](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3558).
- **Observabilité** : rétablissement des enregistrements de sessions et des sondages via PostHog pour le suivi utilisateur [#3579](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3579).
