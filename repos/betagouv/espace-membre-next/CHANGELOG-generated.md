## Changelog : espace-membre-next (30 derniers jours, au 01 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des informations disponibles sur les startups et les membres, ainsi que sur des ajustements de formulaires et de gestion des comptes. Des fonctionnalités de recherche et d'affichage de données spécifiques ont été ajoutées, notamment concernant le suivi des startups et les identifiants Matrix des membres.

### Évolutions fonctionnelles
- Ajout d'un champ pour le choix de Scalingo lors de la création/modification des startups [#1434](https://github.com/betagouv/espace-membre-next/issues/1434).
- Possibilité de rechercher des startups par suivi [#1423](https://github.com/betagouv/espace-membre-next/issues/1423).
- Affichage de l'identifiant Matrix des membres [#1411](https://github.com/betagouv/espace-membre-next/issues/1411).
- Ajout des champs `contact_dinum` et `contact_incubator` pour les startups [#1410](https://github.com/betagouv/espace-membre-next/issues/1410).
- Modification du formulaire pour les jours travaillés par semaine [#1395](https://github.com/betagouv/espace-membre-next/issues/1395).
- Ajout d'un événement "EIG" pour les startups.
- Modification du statut des comptes pour passer à "Outils" et suppression des emails de type bounce [#1421](https://github.com/betagouv/espace-membre-next/issues/1421).
- Correction : Vérification des comptes `.ext` dans Matrix [#1424](https://github.com/betagouv/espace-membre-next/issues/1424).

### Évolutions techniques
- Suppression du champ `tjm` de la table `users` [#1403](https://github.com/betagouv/espace-membre-next/issues/1403).
- Suppression de la logique liée au parrainage [#1404](https://github.com/betagouv/espace-membre-next/issues/1404).
- Suppression de la fonction `unblockEmailsThatAreActive` [#1412](https://github.com/betagouv/espace-membre-next/issues/1412).
- Implémentation d'un formulaire pour les demandes d'OPS vers Grist [#1406](https://github.com/betagouv/espace-membre-next/issues/1406).
- Modifications diverses du formulaire [#1425](https://github.com/betagouv/espace-membre-next/issues/1425).
