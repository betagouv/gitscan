## Changelog : monstagedeseconde (30 derniers jours)

### Résumé
Les dernières semaines ont été marquées par des corrections de bugs et des améliorations de la plateforme, notamment au niveau de la gestion des stages, de l'importation de données et de l'interface utilisateur. Des améliorations ont également été apportées à la recherche d'offres de stage et à la signature électronique des conventions. Enfin, des mises à jour techniques ont été effectuées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Correction d'un bug empêchant l'affichage correct des demandes de stage manquantes [#777](https://github.com/betagouv/monstagedeseconde/issues/777).
- Amélioration de la gestion des erreurs lors de l'analyse JSON des données des entreprises [#776](https://github.com/betagouv/monstagedeseconde/issues/776).
- Correction d'une erreur liée à un attribut manquant dans la gestion des utilisateurs des établissements scolaires [#778](https://github.com/betagouv/monstagedeseconde/issues/778).
- Amélioration de l'importation des classes des élèves depuis Sygne [#827d7549].
- Correction de la recherche mobile d'offres de stage [#6f41f3b6].
- Amélioration de la fonction "offres inappropriées" [#770](https://github.com/betagouv/monstagedeseconde/issues/770).
- Correction de l'affichage des accords multiples pour les gestionnaires d'établissement [#752](https://github.com/betagouv/monstagedeseconde/issues/752).
- Amélioration de l'envoi d'emails pour les signatures d'accords [#771](https://github.com/betagouv/monstagedeseconde/issues/771).
- Correction de l'affichage des secteurs dans la recherche d'offres [#0cae47f4].
- Correction de l'attribution du `group_id` lors de la mise à jour des offres [#f6a84085].
- Correction de l'affichage des PNG pour les signatures [#116d2abf].
- Amélioration de la gestion des établissements scolaires dans l'interface d'administration [#23cda3bb, #0ad19aa3].
- Correction de bugs et améliorations de l'interface de recherche d'offres [#748, #754].
- Amélioration de la gestion des places disponibles pour les offres de stage [#756](https://github.com/betagouv/monstagedeseconde/issues/756).
- Ajout d'une nouvelle gem `letter_thief` pour la gestion des emails [#750](https://github.com/betagouv/monstagedeseconde/issues/750).

### Évolutions techniques
- Mise à jour des dépendances `faraday` et `qs` vers leurs dernières versions [#767, #769].
- Mise en place d'un système de versionnement des fichiers de configuration traditionnels [#9d5bb3dd].
- Amélioration du script de synchronisation des données [#9d5bb3dd].
- Mise à jour de la configuration Ruby LSP [#d31e3aec].
- Suppression de l'objet `InternshipOfferInfo` [#82a0a0b2].

### Autres changements
- Amélioration de la documentation et des tests unitaires.
- Corrections de typographie et d'erreurs de formulation dans l'interface utilisateur.
- Nettoyage du code et refactoring de certaines parties de l'application.
- Mise à jour des paramètres de production dans la base de données [#94b5f376].
- Ajout de contraintes à la base de données pour le secteur [#2980f59e].
- Amélioration de la gestion des tests KPI [#8d07816a, #6d9022c6].
- Suppression d'assignations vides dans le code [#1f94238b, #8d4c21d8].
