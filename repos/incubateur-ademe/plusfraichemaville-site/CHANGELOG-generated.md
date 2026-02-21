## Changelog : plusfraichemaville-site (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des projets, des estimations et des collectivités. Des corrections de bugs ont été apportées pour améliorer la stabilité et l'expérience utilisateur, notamment lors de la navigation entre les projets et l'ouverture des modales. Des mises à jour techniques ont également été effectuées pour maintenir la sécurité et la performance de la plateforme.

### Évolutions fonctionnelles
- Possibilité de voir tous les projets pour une EPCI ou une commune. (#469)
- Amélioration de l'ouverture de la modale de création d'estimation. (#460, #461)
- Ajout d'un script pour peupler les nouvelles tables `epci` et `commune`. (#468)
- Affichage du Climadiag pour la commune ou l'EPCI de l'utilisateur. (#464)
- Gestion des collectivités : ajout d'une alerte Mattermost si l'utilisateur n'a pas de SIREN. (#465)
- Possibilité d'ajouter des fiches solutions à une estimation. (#467)
- Suppression du champ `fiches_solutions_id` dans la table `estimation` et ajout d'un bouton de suppression pour les fiches solutions dans une estimation.
- Modification de l'ordre des boutons dans la modale d'estimation. (#462)
- Correction de l'index de la fiche solution dans l'ouverture de la modale d'estimation.
- Correction de l'affichage des options de maturité (z-index).

### Évolutions techniques
- Mise à jour de Next.js et de jspdf pour corriger des problèmes de sécurité. (#466, #463)
- Changement de l'URL de l'API Adresse. (#464)
- Suppression de la liaison collectivite <> User, simplification du code.
- Refactoring du code et nettoyage pour améliorer la lisibilité et la maintenabilité.
- Correction de plusieurs erreurs et avertissements TypeScript.
- Suppression de l'utilisation de `UserWithCollectivite` lorsque ce n'est pas nécessaire.

### Autres changements
- Ajustement de la marge pour correspondre au design.
- Ajout d'une icône au premier label du fil d'Ariane.
- Correction de problèmes de build.
- Merge de la branche `prod` en `main`.
