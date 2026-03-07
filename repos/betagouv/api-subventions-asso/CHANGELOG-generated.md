## Changelog : api-subventions-asso (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à l'API au cours du dernier mois. Les principales évolutions concernent l'amélioration des performances de l'importation des données Chorus, l'ajout d'informations administratives dans les journaux de données, ainsi que des refactorings internes pour une meilleure maintenabilité et une plus grande clarté du code. Des corrections de bugs et des ajustements de l'interface utilisateur ont également été effectués.

### Évolutions fonctionnelles
- Amélioration de la formulation du processus de dépôt de fichiers sur l'interface utilisateur. [#3836](https://github.com/betagouv/api-subventions-asso/issues/3836)
- Ajout d'informations sur l'administrateur dans les données enregistrées (datalog). [#3756](https://github.com/betagouv/api-subventions-asso/issues/3756)

### Évolutions techniques
- Refactorisation de l'interface `port` de l'API, incluant l'introduction de `mapper` et `adapter`. [#3803](https://github.com/betagouv/api-subventions-asso/issues/3803) [#3828](https://github.com/betagouv/api-subventions-asso/issues/3828)
- Amélioration des performances de l'importation des données Chorus. [#3808](https://github.com/betagouv/api-subventions-asso/issues/3808) [#3809](https://github.com/betagouv/api-subventions-asso/issues/3809)
- Refactorisation des services plats pour une meilleure homogénéité. [#3663](https://github.com/betagouv/api-subventions-asso/issues/3663) [#3815](https://github.com/betagouv/api-subventions-asso/issues/3815)
- Ajout de statistiques détaillées sur les consommateurs de l'API. [#3733](https://github.com/betagouv/api-subventions-asso/issues/3733) [#3826](https://github.com/betagouv/api-subventions-asso/issues/3826)
- Mise à jour de la configuration TypeScript. [#3799](https://github.com/betagouv/api-subventions-asso/issues/3799)

### Autres changements
- Correction d'un bug concernant le renommage d'un mapper. [#0000](https://github.com/betagouv/api-subventions-asso/issues/0000)
- Renommage de l'adaptateur en mapper dans les tests.
- Publication des versions 0.81.0, 0.80.1, 0.80.0 et 0.79.0.
