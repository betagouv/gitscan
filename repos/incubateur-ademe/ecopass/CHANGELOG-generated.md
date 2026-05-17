## Changelog : ecopass (30 derniers jours, au 13 mai 2026)

### Résumé
Cette version apporte des améliorations significatives en termes de performance, notamment lors de l'export de grandes quantités de données, et corrige des bugs liés à la gestion des prix et des exports en batch. De nouvelles fonctionnalités ont été ajoutées pour faciliter l'accès aux données pour les utilisateurs Bercy et pour la création de produits anonymisés.

### Évolutions fonctionnelles
- Les utilisateurs de Bercy peuvent désormais accéder aux données. [#147](https://github.com/incubateur-ademe/ecopass/issues/147)
- Amélioration des performances lors de la création de produits anonymisés.
- Correction d'un bug empêchant l'export correct de produits en batch. [#143](https://github.com/incubateur-ademe/ecopass/issues/143)
- Correction d'un bug lié à la gestion des prix inférieurs à 1 pour les produits importés en batch. [#142](https://github.com/incubateur-ademe/ecopass/issues/142)
- Amélioration de la documentation concernant le score environnemental. [#142](https://github.com/incubateur-ademe/ecopass/issues/142)

### Évolutions techniques
- Optimisation du streaming des produits lors des exports volumineux. [#146](https://github.com/incubateur-ademe/ecopass/issues/146)
- Mise à jour de la configuration pnpm pour assurer la compatibilité avec la version 10.
- Amélioration de la performance de la création de produits anonymisés.

### Autres changements
- Mise à jour de la documentation README.
- Ajustement du timeout de Matomo.
- Ajout d'un rôle "Bercy" pour la gestion des permissions. [#144](https://github.com/incubateur-ademe/ecopass/issues/144)
