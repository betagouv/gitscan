## Changelog : espace-membre-next (30 derniers jours, au 22 juin 2026)

### Résumé
Ce mois-ci, l'espace membre a bénéficié d'améliorations concernant la gestion des comptes utilisateurs, l'ajout d'informations sur les startups (contact Dinum et incubateur), et l'intégration de Matrix. Des ajustements ont également été faits concernant les demandes d'OPS et la gestion des phases de projet.

### Évolutions fonctionnelles
- Modification du statut des comptes utilisateurs, désormais accessible via les outils, et suppression des emails de type "bounce" [#1421](https://github.com/betagouv/espace-membre-next/issues/1421).
- Affichage de l'identifiant Matrix des membres [#1411](https://github.com/betagouv/espace-membre-next/issues/1411).
- Ajout des champs `contact_dinum` et `contact_incubator` pour les startups [#1410](https://github.com/betagouv/espace-membre-next/issues/1410).
- Modification du formulaire pour les jours travaillés par semaine [#1395](https://github.com/betagouv/espace-membre-next/issues/1395).
- Formulaire de demande d'OPS redirigé vers Grist [#1406](https://github.com/betagouv/espace-membre-next/issues/1406).
- Renommage de la phase "perennisation" en "consolidation" [#1392](https://github.com/betagouv/espace-membre-next/issues/1392).

### Évolutions techniques
- Intégration d'une table `matrix_accounts` et script de synchronisation pour Matrix [#1373](https://github.com/betagouv/espace-membre-next/issues/1373).
- Optimisation de la détection de Tchap pour éviter des traitements inutiles [#1393](https://github.com/betagouv/espace-membre-next/issues/1393).
- Suppression du champ `tjm` de la table `users` [#1403](https://github.com/betagouv/espace-membre-next/issues/1403).
- Suppression des fonctionnalités liées au parrainage [#1404](https://github.com/betagouv/espace-membre-next/issues/1404).

### Autres changements
- Suppression d'un script obsolète `unblockEmailsThatAreActive` [#1412](https://github.com/betagouv/espace-membre-next/issues/1412).
