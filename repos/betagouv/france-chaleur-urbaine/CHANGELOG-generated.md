## Changelog : france-chaleur-urbaine (30 derniers jours, au 09 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'administration du site, la gestion des données et des réseaux de chaleur, ainsi que des corrections de bugs et des optimisations de performance. Des améliorations significatives ont été apportées à l'interface d'administration, notamment avec un nouveau méga-menu et une réorganisation du dashboard. Des corrections ont également été apportées pour améliorer la gestion des utilisateurs et des données en base de données.

### Évolutions fonctionnelles
- Ajout de la gestion du maître d'ouvrage pour les réseaux en construction. [#1260](https://github.com/betagouv/france-chaleur-urbaine/pull/1260)
- Amélioration de la gestion des statuts des demandes, avec une simplification autour du statut "recontacté". [#1257](https://github.com/betagouv/france-chaleur-urbaine/pull/1257)
- Ajout d'une modale de confirmation avant l'envoi d'emails depuis l'administration. [#1244](https://github.com/betagouv/france-chaleur-urbaine/pull/1244)
- Les administrateurs peuvent désormais mettre à jour le statut des demandes.
- Les boutons de modification/suppression sont maintenant affichés pour toutes les relances.
- Possibilité de lister les organisations dans la gestion des réseaux. [#1259](https://github.com/betagouv/france-chaleur-urbaine/pull/1259)
- Affichage de l'éligibilité sur les iframes legacy restauré.
- Amélioration de la performance du tableau des demandes. [#1256](https://github.com/betagouv/france-chaleur-urbaine/pull/1256)
- Amélioration de l'affichage des accès aux demandes dans l'administration.
- Ajout du tracking custom des événements iframes et formulaires. [#1254](https://github.com/betagouv/france-chaleur-urbaine/pull/1254)

### Évolutions techniques
- Refactorisation de l'API PAC et initialisation de l'API IFPEN (renommée PAC).
- Mise à jour du package `publicodes`.
- Amélioration de la gestion des limites de `MapConfiguration` pour éviter les surcharges.
- Simplification de la mise à jour en masse des géométries. [#1252](https://github.com/betagouv/france-chaleur-urbaine/pull/1252)
- Correction d'un problème de duplication d'utilisateurs administrateurs. [#1251](https://github.com/betagouv/france-chaleur-urbaine/pull/1251)
- Nettoyage du code legacy lié aux tags. [#1242](https://github.com/betagouv/france-chaleur-urbaine/pull/1242)
- Déplacement de la page `api-gestionnaire` dans le module `partner-api`. [#1258](https://github.com/betagouv/france-chaleur-urbaine/pull/1258)
- Suppression de l'intégration Pipedrive et des notifications emails de l'équipe FCU.
- Correction d'un test unitaire lié au coup de pouce chauffage.
- Correction de bugs et améliorations diverses de l'API.
- Amélioration de la gestion des cookies de grande taille (> 4096kb).

### Autres changements
- Ajout de tracking pour les host des demandes.
- Ajout de la distinction des suppressions automatiques de demandes dans les événements. [#1255](https://github.com/betagouv/france-chaleur-urbaine/pull/1255)
- Correction de données de demandes corrompues en base de données.
- Ajout d'une commande CLI pour identifier les fichiers tracés.
- Mise à jour de la documentation et des tests.
- Diverses corrections de bugs et améliorations de la qualité du code.
- Ajout du logo ADEME et FCU sur la carte.
