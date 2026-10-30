## Changelog : cdata (30 derniers jours, au 29 octobre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape majeure avec l'introduction d'un nouveau système de création de pages basé sur des "blocs" (images, cartes, grilles), offrant une plus grande flexibilité de mise en page. L'expérience utilisateur a été enrichie par de nouvelles fonctionnalités de notification, une meilleure gestion des publications et des améliorations notables de l'explorateur de données. En parallèle, les processus de déploiement et de tests ont été considérablement optimisés pour gagner en rapidité et en fiabilité.

### Évolutions fonctionnelles
- **Nouveau système de mise en page (Blocs) :** Introduction d'une approche modulaire pour construire des pages via des blocs de colonnes, d'images, de cartes ou de grilles [#1308](https://github.com/datagouv/cdata/issues/1308), [#1303](https://github.com/datagouv/cdata/issues/1303), [#1292](https://github.com/datagouv/cdata/issues/1292).
- **Gestion du contenu et des publications :** 
    - Amélioration de l'édition des articles (choix de l'URL/slug, menus latéraux de navigation, gestion des images de couverture) [#1285](https://github.com/datagouv/cdata/issues/1285), [#1274](https://github.com/datagouv/cdata/issues/1274), [#1282](https://github.com/datagouv/cdata/issues/1282).
    - Ajout d'une page de paramètres de notification et d'un menu de suivi pour les discussions [#1265](https://github.com/datagouv/cdata/issues/1265).
    - Possibilité pour les administrateurs de forcer l'analyse d'une ressource depuis l'interface d'édition [#1289](https://github.com/datagouv/cdata/issues/1289).
- **Exploration et données :** 
    - Amélioration de l'explorateur de données (persistance des filtres et tris dans l'URL, interface plus fluide) [#1254](https://github.com/datagouv/cdata/issues/1254), [#1251](https://github.com/datagouv/cdata/issues/1251), [#1290](https://github.com/datagouv/cdata/issues/1290).
    - Support des identifiants DOI pour les jeux de données [#1238](https://github.com/datagouv/cdata/issues/1238).
    - Synchronisation et amélioration de la gestion des données GEOPF [#1178](https://github.com/datagouv/cdata/issues/1178), [#1269](https://github.com/datagouv/cdata/issues/1269).
- **Interface et expérience utilisateur :** 
    - Ajout de bannières pour les organisations [#1268](https://github.com/datagouv/cdata/issues/1268) et amélioration de l'interface pour les éditeurs partiels [#1250](https://github.com/datagouv/cdata/issues/1250), [#1257](https://github.com/datagouv/cdata/issues/1257).
    - Corrections diverses : traductions françaises de l'interface [#1259](https://github.com/datagouv/cdata/issues/1259), gestion des pages d'erreur (404/410) [#1260](https://github.com/datagouv/cdata/issues/1260), et redirection après connexion [#1261](https://github.com/datagouv/cdata/issues/1261).

### Évolutions techniques
- **Optimisation de la CI/CD et des tests :** 
    - Accélération significative des tests de bout en bout (E2E) grâce au découpage en plusieurs flux (sharding) et correction de tests instables [#1253](https://github.com/datagouv/cdata/issues/1253), [#1296](https://github.com/datagouv/cdata/issues/1296).
    - Amélioration de la fiabilité de la CI (gestion des erreurs de passerelle API, injection d'IDs de débogage Sentry) [#1299](https://github.com/datagouv/cdata/issues/1299), [#1213](https://github.com/datagouv/cdata/issues/1213).
- **Architecture et Performance :** 
    - Mise à jour vers Nuxt 4.5 [#1193](https://github.com/datagouv/cdata/issues/1193).
    - Optimisation de la gestion du cache des blocs de site et des redirections serveur [#1295](https://github.com/datagouv/cdata/issues/1295), [#1300](https://github.com/datagouv/cdata/issues/1300).
- **Environnement de développement :** Résolution d'un problème de consommation mémoire du serveur de développement [#1305](https://github.com/datagouv/cdata/issues/1305).

### Autres changements
- **Maintenance du code :** Mise en place de `CODEOWNERS` [#1309](https://github.com/datagouv/cdata/issues/1309), nettoyage ESLint [#1293](https://github.com/datagouv/cdata/issues/1293) et filtrage des erreurs Sentry non pertinentes [#1276](https://github.com/datagouv/cdata/issues/1276).
