## Changelog : acceslibre (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des détails des ERP, notamment avec l'implémentation d'une fonctionnalité de génération de PDF et l'ajout de drapeaux de fonctionnalités pour un déploiement progressif. Des améliorations ont également été apportées à l'API et à la cartographie, ainsi que des corrections de bugs et des optimisations de sécurité.

### Évolutions fonctionnelles
- Possibilité de demander l'API du widget par `asp_id` [#2580](https://github.com/MTES-MCT/acceslibre/issues/2580).
- Implémentation de la génération de PDF pour les détails des ERP [#2546](https://github.com/MTES-MCT/acceslibre/issues/2546) et [#2575](https://github.com/MTES-MCT/acceslibre/issues/2575).
- Amélioration de la gestion des droits d'édition du type d'utilisateur pour les propriétaires d'ERP [#2576](https://github.com/MTES-MCT/acceslibre/issues/2576).
- Utilisation des tuiles IGN pour la cartographie, avec repli sur Carto si hors métropole française [#2566](https://github.com/MTES-MCT/acceslibre/issues/2566).
- Export du code du widget [#2565](https://github.com/MTES-MCT/acceslibre/issues/2565).

### Évolutions techniques
- Utilisation de `django-waffle` pour gérer les drapeaux de fonctionnalités (feature flags) pour le RPA [#2578](https://github.com/MTES-MCT/acceslibre/issues/2578).
- Correction d'une erreur Sentry lors de la génération de l'URL RPA [#2583](https://github.com/MTES-MCT/acceslibre/issues/2583).
- Amélioration de la gestion des connexions à la base de données pour éviter les fuites [#2579](https://github.com/MTES-MCT/acceslibre/issues/2579).
- Correction d'un bug lié à la question de la pente [#2600](https://github.com/MTES-MCT/acceslibre/issues/2600).
- Correction d'un bug lié aux détails de l'ERP [#2599](https://github.com/MTES-MCT/acceslibre/issues/2599).

### Autres changements
- Mise à jour de la documentation et du code pour améliorer la lisibilité et la maintenabilité.
- Diverses corrections de bugs mineurs et améliorations de la performance.
- Mises à jour de dépendances (voir commits dependabot).
