## Changelog : aigle-api (30 derniers jours, au 28 mai 2026)

### Résumé
Les dernières mises à jour d'aigle-api améliorent la gestion des droits d'administration, la manipulation des zones personnalisées, et la performance globale de l'API. Des corrections ont été apportées pour assurer le bon fonctionnement des tests et des routes d'administration, ainsi qu'une amélioration du processus de déploiement. Une modification du type de données des tilesets a également été effectuée.

### Évolutions fonctionnelles
- **Administration :** Amélioration de la gestion des groupes d'utilisateurs pour les super-administrateurs, permettant de modifier facilement les groupes [#62](https://github.com/MTES-MCT/aigle-api/pull/62).
- **Zones personnalisées :** Correction de bugs dans la gestion des zones personnalisées par les administrateurs [#63](https://github.com/MTES-MCT/aigle-api/pull/63).
- **Géocodage :** Restriction de la recherche du géocodage [#65](https://github.com/MTES-MCT/aigle-api/pull/65).
- **Import/Export :** Amélioration de l'import et de l'export en masse [#66](https://github.com/MTES-MCT/aigle-api/pull/66).

### Évolutions techniques
- **Tileset :** Le champ de date des tilesets est maintenant de type `date` au lieu de `datetime` [#60](https://github.com/MTES-MCT/aigle-api/pull/60).
- **Performance :** Diverses optimisations de performance ont été implémentées [#64](https://github.com/MTES-MCT/aigle-api/pull/64).
- **CI/CD :** La configuration du CI a été mise à jour pour ne déployer que si les tests réussissent [#61](https://github.com/MTES-MCT/aigle-api/pull/61).
- **Logs :** Ajout de logs pour les routes d'administration super-administrateur [#62](https://github.com/MTES-MCT/aigle-api/pull/62).
- **Configuration locale :** Amélioration de la configuration locale pour faciliter le développement [#64](https://github.com/MTES-MCT/aigle-api/pull/64).

### Autres changements
- **Tests :** Correction de la suite de tests [#65](https://github.com/MTES-MCT/aigle-api/pull/65).
- **Droits Super-Admin :** Correction des droits pour les super-administrateurs [#64](https://github.com/MTES-MCT/aigle-api/pull/64).
