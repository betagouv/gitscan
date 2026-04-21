## Changelog : acceslibre (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'accès aux données via l'API, notamment pour les widgets, et sur l'implémentation de nouvelles fonctionnalités liées aux détails des ERP (Établissements Recevant du Public), comme la génération de PDF. Des corrections et améliorations de sécurité ont également été apportées, ainsi que des optimisations techniques et des mises à jour de dépendances.

### Évolutions fonctionnelles
- Possibilité de demander l'API des widgets par `asp_id` [#2580](https://github.com/MTES-MCT/acceslibre/issues/2580).
- Implémentation de la génération de PDF pour les détails des ERP [#2546](https://github.com/MTES-MCT/acceslibre/issues/2546) et [#2575](https://github.com/MTES-MCT/acceslibre/issues/2575).
- Amélioration de l'affichage des détails des ERP avec un nouveau layout, contrôlé par un *feature flag* [#2575](https://github.com/MTES-MCT/acceslibre/issues/2575).
- Restriction de la modification du type d'utilisateur aux propriétaires des ERP [#2576](https://github.com/MTES-MCT/acceslibre/issues/2576).
- Changement de la tuile de carte pour utiliser IGN, avec repli sur Carto si hors zone métropolitaine française [#2566](https://github.com/MTES-MCT/acceslibre/issues/2566).
- Export quotidien des données au format XML [#2536](https://github.com/MTES-MCT/acceslibre/issues/2536).

### Évolutions techniques
- Utilisation d'un *feature flag* Waffle pour contrôler l'activation de la fonctionnalité RPA [#2578](https://github.com/MTES-MCT/acceslibre/issues/2578).
- Correction d'une erreur dans la génération de l'URL RPA [#2583](https://github.com/MTES-MCT/acceslibre/issues/2583).
- Amélioration de la gestion des connexions à la base de données pour éviter les fuites [#2579](https://github.com/MTES-MCT/acceslibre/issues/2579).
- Correction d'un bug lié à la vérification de `source_id` [#2581](https://github.com/MTES-MCT/acceslibre/issues/2581).

### Autres changements
- Export du code du widget [#2565](https://github.com/MTES-MCT/acceslibre/issues/2565).
- Plusieurs mises à jour de dépendances ont été effectuées pour assurer la sécurité et la stabilité du projet.
