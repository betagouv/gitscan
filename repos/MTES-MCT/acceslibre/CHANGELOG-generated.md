## Changelog : acceslibre (30 derniers jours, au 15 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'accès aux données via l'API, l'implémentation de nouvelles fonctionnalités pour la gestion des ERP (Établissements Recevant du Public) et l'optimisation de l'infrastructure. Des corrections de bugs et des améliorations de la sécurité ont également été apportées.

### Évolutions fonctionnelles
- Possibilité de demander l'API widget par `asp_id` [#2580](https://github.com/MTES-MCT/acceslibre/issues/2580).
- Amélioration de l'affichage des détails des ERP avec une implémentation en mode "feature flag" [#2575](https://github.com/MTES-MCT/acceslibre/issues/2575) et [#2546](https://github.com/MTES-MCT/acceslibre/issues/2546).
- Restriction de la modification du type d'utilisateur aux propriétaires de l'ERP [#2576](https://github.com/MTES-MCT/acceslibre/issues/2576).
- Utilisation de tuiles IGN pour la cartographie, avec repli sur Carto si l'établissement n'est pas en France métropolitaine [#2566](https://github.com/MTES-MCT/acceslibre/issues/2566).
- Export quotidien des données au format XML [#2536](https://github.com/MTES-MCT/acceslibre/issues/2536).

### Évolutions techniques
- Implémentation d'un switch Django-waffle pour activer/désactiver la fonctionnalité RPA (Robotic Process Automation) [#2578](https://github.com/MTES-MCT/acceslibre/issues/2578).
- Correction d'une erreur dans la génération de l'URL RPA [#2583](https://github.com/MTES-MCT/acceslibre/issues/2583).
- Amélioration de la gestion des connexions à la base de données pour éviter les fuites [#2579](https://github.com/MTES-MCT/acceslibre/issues/2579).
- Mise à niveau de Python et PostgreSQL [#2547](https://github.com/MTES-MCT/acceslibre/issues/2547).

### Autres changements
- Correction de bugs mineurs et améliorations de la robustesse du code.
- Mise à jour de la documentation.
- Corrections concernant l'affichage "à propos" [#2577](https://github.com/MTES-MCT/acceslibre/issues/2577).
- Export du code du widget [#2565](https://github.com/MTES-MCT/acceslibre/issues/2565).
