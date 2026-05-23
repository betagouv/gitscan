## Changelog : ecopass (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la performance et de la gestion des données, notamment pour les exports massifs et la création de produits anonymisés. Des améliorations ont également été apportées pour faciliter l'accès aux données pour les utilisateurs Bercy et pour une meilleure gestion des étiquettes complexes et des images de produits.

### Évolutions fonctionnelles
- Ajout d'un rôle spécifique pour les utilisateurs de Bercy, leur permettant d'accéder aux données. [#144](https://github.com/incubateur-ademe/ecopass/issues/144)
- Amélioration de la gestion des étiquettes complexes de produits. [#152](https://github.com/incubateur-ademe/ecopass/issues/152)
- Correction de l'affichage des images de produits avec le GTIN et la comparaison. [#153](https://github.com/incubateur-ademe/ecopass/issues/153)
- Amélioration des performances de la création de produits anonymisés.
- Correction de l'affichage des quantités avec des nombres décimaux. [#148](https://github.com/incubateur-ademe/ecopass/issues/148)

### Évolutions techniques
- Optimisation des performances lors de l'export de grands volumes de produits en utilisant le streaming. [#146](https://github.com/incubateur-ademe/ecopass/issues/146)
- Amélioration de l'ordre des éléments dans l'API pour un tri par nom. [#151](https://github.com/incubateur-ademe/ecopass/issues/151)
- Correction de problèmes liés à la compatibilité avec pnpm 10. [#93e4b74](https://github.com/incubateur-ademe/ecopass/commit/93e4b74)
- Mise à jour des paquets, de Node.js et de pnpm. [#145](https://github.com/incubateur-ademe/ecopass/issues/145)
- Amélioration de la gestion des exports en batch pour les administrateurs. [#143](https://github.com/incubateur-ademe/ecopass/issues/143)

### Autres changements
- Mise à jour de la documentation. [#150](https://github.com/incubateur-ademe/ecopass/issues/150) et [#f8dc6c2](https://github.com/incubateur-ademe/ecopass/commit/f8dc6c2)
- Mise à jour du fichier README.
- Ajustement du timeout de Matomo.
- Ajout de la possibilité de tester la connexion à la base de données. [#149](https://github.com/incubateur-ademe/ecopass/issues/149)
