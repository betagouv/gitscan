## Changelog : dossierfacile-backend (30 derniers jours, au 30 juillet 2026)

### Résumé
Cette version apporte des améliorations à la gestion des avis d'imposition, notamment la possibilité de téléverser des avis plus récents. Des corrections ont également été apportées pour une meilleure gestion des erreurs ADEME et des validations concernant les informations des locataires et garants. Enfin, la sécurité a été renforcée avec l'ajout du protocole SSL pour les logs.

### Évolutions fonctionnelles
- Possibilité de téléverser des avis d'imposition plus récents pour l'analyse du dossier. [#1281](https://github.com/MTES-MCT/dossierfacile-backend/issues/1281)
- L'email du bénéficiaire est désormais obligatoire lors de la création d'un locataire. [#1277](https://github.com/MTES-MCT/dossierfacile-backend/issues/1277)
- L'email du co-locataire est désormais obligatoire. [#1274](https://github.com/MTES-MCT/dossierfacile-backend/issues/1274)
- Ajout du champ email pour le garant personnel (locataire et interface administrateur). [#1273](https://github.com/MTES-MCT/dossierfacile-backend/issues/1273)
- Amélioration de la gestion des erreurs génériques et inconnues provenant d'ADEME. [#1280](https://github.com/MTES-MCT/dossierfacile-backend/issues/1280)

### Évolutions techniques
- Ajout du protocole SSL pour la transmission des logs vers Logstash, améliorant ainsi la sécurité. [#1271](https://github.com/MTES-MCT/dossierfacile-backend/issues/1271)
- Mise à jour des dépendances du projet. [#1272](https://github.com/MTES-MCT/dossierfacile-backend/issues/1272)
- Correction d'un problème empêchant l'affichage des logs en SSL. [#1276](https://github.com/MTES-MCT/dossierfacile-backend/issues/1276)

### Autres changements
- Publication de la version 3.5.13.
