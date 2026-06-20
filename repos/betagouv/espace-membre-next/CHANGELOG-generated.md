## Changelog : espace-membre-next (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'enrichissement des données des membres et des startups, ainsi que sur des corrections et des simplifications de certaines fonctionnalités. Des améliorations ont été apportées au formulaire de demande d'OPS et à la gestion des événements. Des éléments liés au parrainage ont été supprimés.

### Évolutions fonctionnelles
- Ajout de l'affichage de l'identifiant Matrix des membres [#1411](https://github.com/betagouv/espace-membre-next/issues/1411).
- Ajout des champs `contact_dinum` et `contact_incubator` pour les startups [#1410](https://github.com/betagouv/espace-membre-next/issues/1410).
- Amélioration du formulaire de demande d'OPS avec intégration vers Grist [#1406](https://github.com/betagouv/espace-membre-next/issues/1406).
- Modification du formulaire pour les jours travaillés par semaine [#1395](https://github.com/betagouv/espace-membre-next/issues/1395).
- Correction du nom de la phase "perennisation" qui est maintenant "consolidation" [#1392](https://github.com/betagouv/espace-membre-next/issues/1392).
- Correction des noms des événements dans la sélection pour les startups [#1385](https://github.com/betagouv/espace-membre-next/issues/1385).
- Amélioration de la détection de Tchap, avec un court-circuit lorsque possible [#1393](https://github.com/betagouv/espace-membre-next/issues/1393).

### Évolutions techniques
- Ajout d'une table `matrix_accounts` et script de synchronisation associé [#1373](https://github.com/betagouv/espace-membre-next/issues/1373).
- Suppression du champ `tjm` de la table `users` [#1403](https://github.com/betagouv/espace-membre-next/issues/1403).
- Suppression de toutes les fonctionnalités liées au parrainage [#1404](https://github.com/betagouv/espace-membre-next/issues/1404).

### Autres changements
- Suppression d'un script bloquant l'envoi d'emails actifs [#1412](https://github.com/betagouv/espace-membre-next/issues/1412).
