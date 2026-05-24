## Changelog : communs-de-la-transition-ecologique-des-collectivites (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent principalement sur l'amélioration du tableau de bord de la transition écologique (dashboard-te) avec de nouvelles fonctionnalités de filtrage, de tri et d'agrégation des données. Des améliorations significatives ont également été apportées à la gestion des aides, notamment en termes de matching, de classification et de feedback utilisateur. Enfin, l'intégration des données du référentiel MEC (Mesures d'Accompagnement des Collectivités) progresse avec de nouveaux endpoints et une classification par LLM.

### Évolutions fonctionnelles
- Ajout d'un indicateur pour inclure les fiches action TE (Transition Écologique) dans les statistiques nationales du dashboard-te. [#963ac30](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/963ac30)
- Possibilité de filtrer et synthétiser les projets du dashboard-te par probabilité de transition écologique. [#6dafb99](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/6dafb99)
- Amélioration des filtres du dashboard-te avec des alias de tri plus intuitifs (budget, etc.). [#d07f1e3](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/d07f1e3)
- Filtrage des projets du dashboard-te par financement et montant. [#8e71a3e](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/8e71a3e)
- Ajout d'un endpoint pour obtenir un résumé des projets du dashboard-te. [#9d6df4b](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/9d6df4b)
- Possibilité de filtrer les projets du dashboard-te par site, intervention et thématique, avec un score minimum. [#b14b0b2](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/b14b0b2)
- Ajout d'un endpoint pour exporter les projets du dashboard-te. [#a95497c](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/a95497c)
- Nouveau endpoint pour permettre aux utilisateurs de signaler une aide non pertinente pour un projet. [#fd753e2](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/fd753e2)
- Exposition de l'API Swagger du dashboard-te sur le hub public. [#05242c0](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/05242c0)
- Page "Dispositifs" sur data_mec avec classification LLM. [#843a001](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/843a001)
- Endpoint dédié pour les projets MEC. [#30353a1](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/30353a1)

### Évolutions techniques
- Refactorisation du code pour séparer les dispositifs du référentiel vers le dashboard-te. [#02dc6fa](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/02dc6fa)
- Mise en place d'un système de pondération des axes pour le matching aides/projets. [#f60ece9](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/f60ece9)
- Amélioration du matching combiné pour le thématique des aides. [#583486d](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/583486d)
- Implémentation d'un matching textuel lexical (BM25) en complément du matching thématique pour les aides. [#b43e3f2](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/b43e3f2)
- Utilisation de Drizzle pour les migrations de schéma data_mec. [#7a86d84](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/7a86d84)
- Séparation des jobs de release et de déploiement en deux jobs ré-exécutables. [#cecc2b4](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/cecc2b4)

### Autres changements
- Documentation : Masquage des détails d'implémentation dans le Swagger des aides. [#80e08b5](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/80e08b5)
- Ajout de scripts de diagnostic pour les données géo, thématique et textuelles des aides. [#c01532d](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/c01532d)
- Ajout d'un script de requalification du catalogue d'aides. [#0246da4](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/0246da4)
- Correction de plusieurs tests E2E et tests unitaires. [#ec89065](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/ec89065), [#2f5475e](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/2f5475e), [#9c9b4a5](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/9c9b4a5)
