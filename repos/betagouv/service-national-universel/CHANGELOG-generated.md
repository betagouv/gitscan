## Changelog : service-national-universel (30 derniers jours)

### Résumé
Les dernières mises à jour du Service National Universel se concentrent sur l'amélioration de la gestion des emails, notamment en réponse à des problèmes de délivrabilité avec Microsoft. Des corrections ont également été apportées pour gérer correctement les statuts des référents et les suppressions d'utilisateurs, ainsi que l'ajout d'informations sur la date d'envoi du passeport.

### Évolutions fonctionnelles
- Ajout de la date d'envoi du passeport aux informations du jeune via l'API. [#5255](https://github.com/betagouv/service-national-universel/issues/5255)
- Les super-modérateurs sont désormais les seuls autorisés à supprimer des utilisateurs. [#5241](https://github.com/betagouv/service-national-universel/issues/5241)
- Une alerte est maintenant affichée sur les pages de connexion et d'accueil de l'administration en cas de problèmes d'envoi d'emails. [#5247](https://github.com/betagouv/service-national-universel/issues/5247)
- Correction de la gestion des statuts des référents inactifs. [#5250](https://github.com/betagouv/service-national-universel/issues/5250)

### Évolutions techniques
- Mise en place d'un filtre pour les domaines email Microsoft afin de pallier des problèmes de délivrabilité (puis retiré). [#5251](https://github.com/betagouv/service-national-universel/issues/5251), [#5252](https://github.com/betagouv/service-national-universel/issues/5252), [#5253](https://github.com/betagouv/service-national-universel/issues/5253)
- Mise à jour des librairies spécifiques. [#5245](https://github.com/betagouv/service-national-universel/issues/5245)
