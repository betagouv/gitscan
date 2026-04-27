## Changelog : apilos (30 derniers jours, au 22 avril 2026)

### Résumé
Ce changelog présente les améliorations apportées à apilos au cours du dernier mois. Les efforts se sont concentrés sur l'optimisation des performances, notamment lors de la récupération des logements, ainsi que sur l'ajout de nouvelles fonctionnalités d'export de données vers S3 et l'amélioration de la gestion des conventions et de leurs financements.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter les conventions départementales directement vers un bucket S3 [#2151](https://github.com/MTES-MCT/apilos/issues/2151).
- Amélioration de la gestion des champs à choix dans le mapping des propriétés de financement [#2157](https://github.com/MTES-MCT/apilos/issues/2157).
- Implémentation d'une commande d'export des conventions, accompagnée d'une mise à jour de la documentation [#2149](https://github.com/MTES-MCT/apilos/issues/2149).
- Correction de la mise en correspondance entre les logements et leurs financements [#2140](https://github.com/MTES-MCT/apilos/issues/2140).

### Évolutions techniques
- Optimisation de la récupération des logements grâce au préchargement et à la mise en cache [#2155](https://github.com/MTES-MCT/apilos/issues/2155).
- Augmentation du nombre de workers Gunicorn pour améliorer la capacité de traitement [#2154](https://github.com/MTES-MCT/apilos/issues/2154).
- Augmentation du délai d'expiration de Gunicorn de 26 à 30 secondes [#2153](https://github.com/MTES-MCT/apilos/issues/2153).
- Optimisation générale du code [#2156](https://github.com/MTES-MCT/apilos/issues/2156).

### Autres changements
- Suppression des logs d'avertissement de la classe `ConventionKPI` [#2148](https://github.com/MTES-MCT/apilos/issues/2148).
