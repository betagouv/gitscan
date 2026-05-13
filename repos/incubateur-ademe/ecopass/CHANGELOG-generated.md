## Changelog : ecopass (30 derniers jours, au 12 mai 2026)

### Résumé
Cette version apporte des améliorations de performance lors de la création de produits anonymisés, ainsi qu'un nouveau rôle "Bercy" pour la gestion des accès. Des corrections ont été apportées pour améliorer la fiabilité des exports en batch et la gestion des prix des produits lors de l'importation massive. La documentation concernant le score environnemental a également été clarifiée.

### Évolutions fonctionnelles
- Ajout d'un rôle "Bercy" pour une gestion des accès spécifique.  [#144](https://github.com/incubateur-ademe/ecopass/issues/144)
- Correction d'un bug empêchant l'export en batch des données administratives. [#143](https://github.com/incubateur-ademe/ecopass/issues/143)
- Correction de la gestion des prix inférieurs à 1 lors de l'importation massive de produits. [#142](https://github.com/incubateur-ademe/ecopass/issues/142)
- Amélioration des performances lors de la création de produits anonymisés.

### Évolutions techniques
- Mise à jour de la configuration de pnpm pour assurer la compatibilité avec la version 10.
- Mise à jour du timeout de Matomo.

### Autres changements
- Mise à jour de la documentation README.
- Clarification de la documentation sur le calcul du score environnemental.
