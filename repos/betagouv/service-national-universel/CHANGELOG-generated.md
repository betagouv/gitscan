## Changelog : service-national-universel (30 derniers jours)

### Résumé
Les dernières mises à jour du Service National Universel se concentrent sur l'amélioration de la gestion des emails, notamment en réponse à des problèmes de délivrabilité avec Microsoft, et sur la sécurisation de certaines actions administratives. Des informations supplémentaires sur la date du passeport sont désormais disponibles via l'API.

### Évolutions fonctionnelles
- L'API permet désormais d'ajouter des informations sur la date de délivrance du passeport des jeunes. [#5259](https://github.com/betagouv/service-national-universel/issues/5259)
- Une alerte est maintenant affichée sur les pages de connexion et d'accueil de l'interface d'administration en cas de problèmes d'envoi d'emails. [#5247](https://github.com/betagouv/service-national-universel/issues/5247)
- Seuls les super-modérateurs peuvent désormais supprimer des utilisateurs. [#5241](https://github.com/betagouv/service-national-universel/issues/5241)

### Évolutions techniques
- Mise à jour des versions de certaines librairies spécifiques. [#5245](https://github.com/betagouv/service-national-universel/issues/5245)
- Amélioration de la gestion des statuts des référents dans l'API. [#5250](https://github.com/betagouv/service-national-universel/issues/5250)
- Implémentation d'un mécanisme de filtrage des domaines email Microsoft pour atténuer les problèmes de délivrabilité (puis désactivé et réactivé). [#5251](https://github.com/betagouv/service-national-universel/issues/5251), [#5252](https://github.com/betagouv/service-national-universel/issues/5252), [#5253](https://github.com/betagouv/service-national-universel/issues/5253), [#5254](https://github.com/betagouv/service-national-universel/issues/5254), [#5255](https://github.com/betagouv/service-national-universel/issues/5255)
