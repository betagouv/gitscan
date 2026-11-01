## Changelog : cdata (30 derniers jours, au 29 octobre 2026)

### Résumé
Ce mois-ci, cdata a franchi une étape importante dans la gestion de son contenu avec l'introduction d'un nouveau système de construction de pages basé sur des blocs et des sections. Le projet a également enrichi l'expérience utilisateur avec de nouvelles options de notification, une meilleure visibilité des données (DOI, synchronisation géographique) et des outils d'administration plus complets.

### Évolutions fonctionnelles
- **Nouveau système de mise en page** : Introduction d'une approche modulaire pour composer les pages en utilisant des sections, des grilles et divers types de blocs (images, cartes, etc.) [#1292](https://github.com/datagouv/cdata/issues/1292), [#1303](https://github.com/datagouv/cdata/issues/1303), [#1308](https://github.com/datagouv/cdata/issues/1308).
- **Navigation et affichage** : 
    - Ajout de menus latéraux pour naviguer dans les titres des articles [#1285](https://github.com/datagouv/cdata/issues/1285).
    - Mise en place de fils d'Ariane pour les pages édito [#1275](https://github.com/datagouv/cdata/issues/1275).
    - Ajout de bannières pour les organisations [#1268](https://github.com/datagouv/cdata/issues/1268).
- **Données et Géospatial** : 
    - Intégration de la synchronisation GeoPF [#1178](https://github.com/datagouv/cdata/issues/1178).
    - Affichage des identifiants DOI pour les jeux de données, avec possibilité de les demander [#1238](https://github.com/datagouv/cdata/issues/1238).
- **Notifications** : Création d'une page de gestion des paramètres de notification et d'un menu de suivi pour les discussions [#1265](https://github.com/datagouv/cdata/issues/1265).
- **Administration** : 
    - Possibilité de personnaliser les slugs des articles [#1274](https://github.com/datagouv/cdata/issues/1274).
    - Forçage de l'analyse des ressources depuis l'interface d'édition [#1289](https://github.com/datagouv/cdata/issues/1289).
    - Amélioration de la gestion des demandes d'adhésion [#1277](https://github.com/datagouv/cdata/issues/1277).
- **Corrections d'interface** : 
    - Finalisation de la traduction de l'interface en français [#1259](https://github.com/datagouv/cdata/issues/1259).
    - Correction de l'affichage des erreurs (pages 404/410) [#1260](https://github.com/datagouv/cdata/issues/1260).
    - Diverses corrections de mise en page et de comportement des formulaires [#1263](https://github.com/datagouv/cdata/issues/1263), [#1290](https://github.com/datagouv/cdata/issues/1290).

### Évolutions techniques
- **Optimisation de la CI/CD** : Accélération des tests de bout en bout (E2E) via le partitionnement des tests (sharding) [#1253](https://github.com/datagouv/cdata/issues/1253), [#1296](https://github.com/datagouv/cdata/issues/1296).
- **Performance et Résilience** : 
    - Amélioration de la gestion du cache (Nginx et SSR) pour garantir la fraîcheur des données [#1273](https://github.com/datagouv/cdata/issues/1273), [#1295](https://github.com/datagouv/cdata/issues/1295).
    - Mise en place de tentatives automatiques sur les requêtes API en cas d'erreur de passerelle [#1299](https://github.com/datagouv/cdata/issues/1299).
- **Expérience de développement** : Résolution d'un problème de consommation mémoire du serveur de développement [#1305](https://github.com/datagouv/cdata/issues/1305).

### Autres changements
- Maintenance du code via ESLint [#1293](https://github.com/datagouv/cdata/issues/1293).
- Mise en place du fichier `CODEOWNERS` pour la gestion des responsabilités du dépôt [#1309](https://github.com/datagouv/cdata/issues/1309).
