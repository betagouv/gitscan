## Changelog : espace-membre-next (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des startups et des membres, avec l'ajout de nouvelles informations et de fonctionnalités de recherche. Des modifications ont également été apportées aux formulaires et à la gestion des comptes utilisateurs.

### Évolutions fonctionnelles
- **Startups :** Ajout de la possibilité de rechercher des startups par suivi [#1423](https://github.com/betagouv/espace-membre-next/issues/1423).
- **Startups :** Ajout des champs `contact_dinum` et `contact_incubator` pour les startups [#1410](https://github.com/betagouv/espace-membre-next/issues/1410).
- **Membres :** Affichage de l'identifiant Matrix des membres [#1411](https://github.com/betagouv/espace-membre-next/issues/1411).
- **Formulaire Demandes d'OPS :** Modification du formulaire pour intégrer Grist [#1406](https://github.com/betagouv/espace-membre-next/issues/1406).
- **Formulaire général :** Modifications diverses du formulaire [#1425](https://github.com/betagouv/espace-membre-next/issues/1425).
- **Jours travaillés :** Modification du formulaire pour gérer le nombre de jours travaillés par semaine [#1395](https://github.com/betagouv/espace-membre-next/issues/1395).
- **Statut des comptes :** Le statut des comptes peut maintenant être mis à "Outils" et la suppression des emails en bounce a été implémentée [#1421](https://github.com/betagouv/espace-membre-next/issues/1421).
- **Événements Startup :** Ajout d'un événement "EIG" pour les startups.

### Évolutions techniques
- **Base de données :** Suppression du champ `tjm` de la table `users` [#1403](https://github.com/betagouv/espace-membre-next/issues/1403).
- **Base de données :** Suppression des fonctionnalités liées au parrainage [#1404](https://github.com/betagouv/espace-membre-next/issues/1404).
- **Matrix :** Correction pour vérifier également les comptes `.ext` [#1424](https://github.com/betagouv/espace-membre-next/issues/1424).
- **Code :** Suppression de la fonction `unblockEmailsThatAreActive` [#1412](https://github.com/betagouv/espace-membre-next/issues/1412).

### Autres changements
- Nettoyage et simplification du code.
