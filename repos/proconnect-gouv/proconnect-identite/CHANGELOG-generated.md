## Changelog : proconnect-identite (30 derniers jours)

### Résumé
Ce mois-ci, les évolutions de ProConnect Identité se concentrent sur l'amélioration de l'expérience utilisateur, notamment en simplifiant l'authentification via FranceConnect, en améliorant la gestion des organisations et des modérations, et en optimisant la performance de certaines requêtes. Des corrections de bugs et des mises à jour techniques ont également été apportées pour assurer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- Simplification du processus d'authentification avec FranceConnect, notamment en permettant de choisir entre plusieurs mairies (#1728).
- Amélioration de l'algorithme pour déterminer si une entreprise est unipersonnelle (#1746).
- Possibilité de choisir entre plusieurs mairies lors de l'authentification (#1728).
- Ajout d'un statut "reouvert" aux modérations (#1701).
- Amélioration de la gestion des organisations avec l'ajout d'un responsable d'organisation aux exports (#1766).
- Correction d'un bug empêchant la perte de session lors du rechargement de l'application (#1778).
- Amélioration de la version responsive de la nouvelle interface utilisateur (#1777).
- Suppression du flag de fonctionnalité pour la certification des utilisateurs, simplifiant ainsi le processus (#1705).
- Ajout d'une alerte en cas d'indisponibilité de l'API Sirene (#1724).
- Amélioration de la performance de la recherche d'organisations suggérées (#1780).

### Évolutions techniques
- Migration de tous les fichiers de migration vers TypeScript (#1712).
- Refactorisation majeure des "guards" (vérifications) pour une meilleure maintenabilité (#1716).
- Migration de la vérification de petite association vers le domaine lorsque l'email est vérifié (#1760).
- Ajout du champ `status` à la table `franceconnect_userinfo` pour l'anonymisation (#1757).
- Mise à jour des types de vérification faibles (#1722).
- Suppression de la variable d'environnement FranceConnect obsolète (#1708).
- Correction d'un problème où les liens de domaine non vérifiés étaient écrasés après modération (#1763).
- Ajout de tests unitaires et E2E pour la vérification des types d'utilisateur (#1759).
- Mise à jour des dépendances : `axios` (1.13.3 -> 1.13.5), `ejs` (3.1.10 -> 4.0.1), `lodash` (4.17.21 -> 4.17.23), `nodemailer`, `qs` (6.14.1 -> 6.14.2), `sentry` et `cypress-io/github-action`.

### Autres changements
- Ajout d'un avertissement sur l'environnement de test lors de la connexion et de l'inscription (#1754).
- Collecte des données `sp_name` et `user_ip_address` pour le suivi (#1703).
- Amélioration de la documentation et du code.
- Corrections mineures et refactoring du code.
- Mise à jour des fichiers de verrouillage des dépendances.
- Ajout de tests pour les types de vérification d'assignation d'utilisateur (#1759).
- Ajout d'un test E2E pour la certification d'un dirigeant avec un flux de suggestion (#1750).
- Mise à jour de l'icône de la section d'aide (#1773).
- Ajout d'un barrel file dans le dossier adapter (#1767).
- Suppression d'une contrainte de type de lien faible (#1764).
- Ajout d'un type `verified_by_coop_mediation_numerique` pour les liens organisation utilisateur (#1736).
- Simplification du logger d'événements de débogage (#1747).
