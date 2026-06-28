## Changelog : espace-membre-next (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des fonctionnalités de recherche et d'affichage des informations relatives aux startups et aux membres. Des modifications ont également été apportées aux formulaires et à la gestion des comptes utilisateurs, notamment pour intégrer de nouvelles données et simplifier les processus.

### Évolutions fonctionnelles
- **Recherche de startups:** Ajout de la possibilité de rechercher des startups par suivi [#1423](https://github.com/betagouv/espace-membre-next/issues/1423).
- **Informations membres:** Affichage de l'identifiant Matrix des membres [#1411](https://github.com/betagouv/espace-membre-next/issues/1411).
- **Informations startups:** Ajout des champs `contact_dinum` et `contact_incubator` pour les startups [#1410](https://github.com/betagouv/espace-membre-next/issues/1410).
- **Formulaire Demandes d'OPS:** Intégration d'un formulaire pour les demandes d'OPS vers Grist [#1406](https://github.com/betagouv/espace-membre-next/issues/1406).
- **Formulaire général:** Modifications diverses du formulaire [#1425](https://github.com/betagouv/espace-membre-next/issues/1425) et modifications liées aux jours travaillés par semaine [#1395](https://github.com/betagouv/espace-membre-next/issues/1395).
- **Gestion des comptes:** Modification du statut des comptes utilisateurs, passage à "Outils" et suppression des emails en bounce [#1421](https://github.com/betagouv/espace-membre-next/issues/1421).
- **Correction Matrix:** Correction pour vérifier également les comptes `.ext` dans Matrix [#1424](https://github.com/betagouv/espace-membre-next/issues/1424).
- **Événement Startup:** Ajout d'un événement "EIG" pour les startups [#805085e](https://github.com/betagouv/espace-membre-next/commit/805085e).

### Évolutions techniques
- **Suppression de champs inutilisés:** Suppression du champ `tjm` des utilisateurs [#1403](https://github.com/betagouv/espace-membre-next/issues/1403) et du code lié au parrainage [#1404](https://github.com/betagouv/espace-membre-next/issues/1404).
- **Suppression de code obsolète:** Suppression de la fonction `unblockEmailsThatAreActive` [#1412](https://github.com/betagouv/espace-membre-next/issues/1412).
