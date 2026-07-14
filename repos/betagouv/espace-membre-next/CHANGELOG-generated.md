## Changelog : espace-membre-next (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations de l'interface utilisateur, notamment l'ajout d'informations sur les startups et les membres, ainsi que des corrections de bugs pour améliorer la stabilité et l'expérience utilisateur. Des changements ont également été apportés à la gestion des outils (Sentry, Matomo) et des comptes utilisateurs.

### Évolutions fonctionnelles

- Ajout de la possibilité de rechercher des startups par suivi [#1423](https://github.com/betagouv/espace-membre-next/issues/1423).
- Affichage de l'identifiant Matrix des membres [#1411](https://github.com/betagouv/espace-membre-next/issues/1411).
- Ajout des champs `contact_dinum` et `contact_incubator` pour les startups [#1410](https://github.com/betagouv/espace-membre-next/issues/1410).
- Ajout d'un champ pour le choix de scalingo lors de la création d'une demande d'OPS [#1434](https://github.com/betagouv/espace-membre-next/issues/1434).
- Modification du formulaire de demande d'OPS [#1425](https://github.com/betagouv/espace-membre-next/issues/1425).
- Ajout d'un événement "EIG" pour les startups [#805085e](https://github.com/betagouv/espace-membre-next/commit/805085e).
- Amélioration des informations Tchap affichées [#1437](https://github.com/betagouv/espace-membre-next/issues/1437).
- Correction d'un bug empêchant l'affichage des formations sans description [#1438](https://github.com/betagouv/espace-membre-next/issues/1438).
- Correction pour vérifier les comptes `.ext` Matrix [#1424](https://github.com/betagouv/espace-membre-next/issues/1424).

### Évolutions techniques

- Changement de la configuration de Sentry et Matomo pour utiliser les demandes-OPS [#1436](https://github.com/betagouv/espace-membre-next/issues/1436).
- Correction d'un problème avec Sentry [#1426](https://github.com/betagouv/espace-membre-next/issues/1426).
- Modification du statut des comptes utilisateurs pour passer à "Outils" et suppression des emails de bounce [#1421](https://github.com/betagouv/espace-membre-next/issues/1421).
- Suppression du champ `tjm` des utilisateurs [#1403](https://github.com/betagouv/espace-membre-next/issues/1403).
- Suppression de tout code lié au parrainage [#1404](https://github.com/betagouv/espace-membre-next/issues/1404).
- Mise en place d'un formulaire pour les demandes d'OPS vers Grist [#1406](https://github.com/betagouv/espace-membre-next/issues/1406).

### Autres changements

- Masquage des anciennes informations de compte Matomo/Sentry [#1440](https://github.com/betagouv/espace-membre-next/issues/1440).
- Suppression de la fonction `unblockEmailsThatAreActive` [#1412](https://github.com/betagouv/espace-membre-next/issues/1412).
