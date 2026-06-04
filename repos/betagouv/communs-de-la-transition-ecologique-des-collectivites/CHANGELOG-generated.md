## Changelog : communs-de-la-transition-ecologique-des-collectivites (30 derniers jours, au 03 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration du tableau de bord de la transition écologique (Dashboard TE) avec de nouvelles fonctionnalités de filtrage, de tri et d'agrégation de données. L'API des aides a également été enrichie avec des fonctionnalités de feedback, de pondération et de matching plus précis. Plusieurs corrections et améliorations ont été apportées à l'API et aux tests pour une meilleure stabilité et performance.

### Évolutions fonctionnelles
- **Dashboard TE :** Ajout de filtres multi-valeurs pour les sites, interventions et thématiques, avec options "match all" ou "match any". [#9d6df4b](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/9d6df4b)
- **Dashboard TE :** Possibilité de trier la liste des projets. [#c4f6d12](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/c4f6d12)
- **Dashboard TE :** Ajout d'un endpoint `/projets/summary` pour obtenir un résumé des projets. [#9d6df4b](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/9d6df4b)
- **Dashboard TE :**  Exposition de la probabilité de transition écologique (TE) par projet. [#50072aa](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/50072aa)
- **Dashboard TE :** Agrégation des fiches action TE avec un flag `inclure_tet`. [#963ac30](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/963ac30)
- **API Aides :** Ajout d'un endpoint `/aides/feedback` pour permettre aux utilisateurs de signaler une aide non pertinente pour un projet. [#fd753e2](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/fd753e2)
- **API Aides :** Possibilité de rechercher des aides par classification et par communes. [#dd81e6b](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/dd81e6b)
- **API Aides :** Ajout de paramètres `cutoff` et `seuils de confiance` sur l'endpoint `/aides`. [#954785a](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/954785a)
- **API Aides :**  Alignement de l'endpoint `GET /aides` sur l'utilisation de `projetId` (camelCase) avec une dépréciation progressive de `projet_id`. [#c80923d](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/c80923d)
- **Data MEC :** Ajout d'une page dispositifs sur `data_mec` et classification via LLM. [#843a001](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/843a001)

### Évolutions techniques
- **API :** Amélioration du typage OpenAPI sur les endpoints `/aides/feedback`. [#cdccc82](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/cdccc82)
- **CI/CD :** Séparation des jobs de release et de déploiement en production pour une meilleure résilience. [#cecc2b4](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/cecc2b4)
- **Matching Aides :** Amélioration du matching combiné des aides vers le thématique. [#583486d](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/583486d)
- **Matching Aides :** Implémentation d'un matching textuel lexical (BM25) en complément du matching thématique. [#b43e3f2](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/b43e3f2)
- **Dashboard TE :** Correction du filtre montantMin/Max sur le budget du projet. [#3d5def1](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/3d5def1)
- **Dashboard TE :** Liaison des financements et projets via une table de jointure. [#f3d35e3](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/f3d35e3)

### Autres changements
- **Documentation :** Masquage des détails d'implémentation dans le Swagger de l'API des aides. [#80e08b5](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/80e08b5)
- **Tests :** Alignement des mocks des tests sur `findOneWithSource` et verrouillage du routing par source pour les tests des aides. [#9c9b4a5](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/9c9b4a5)
- **Scripts :** Ajout de scripts de diagnostic pour la qualité des données géo, thématique et textuelle des aides. [#c01532d](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/c01532d)
- **Scripts :** Ajout d'un script de requalification du catalogue d'aides. [#0246da4](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/0246da4)
- **Swagger :** Exposition du Swagger du Dashboard TE sur le hub public `/api`. [#05242c0](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/05242c0)
