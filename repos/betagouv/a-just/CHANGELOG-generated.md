## Changelog : a-just (30 derniers jours, au 02 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment avec l'ajout d'un système de feedback intégré, des améliorations de la gestion des dates et des corrections de bugs pour une meilleure stabilité. Des améliorations ont également été apportées à l'administration pour le suivi des avis utilisateurs.

### Évolutions fonctionnelles
- Ajout d'un système de feedback utilisateur permettant aux utilisateurs de noter et commenter l'application a-just [#89024c55](https://github.com/betagouv/a-just/commit/89024c55).
- Affichage automatique du formulaire de feedback pour les utilisateurs utilisant le produit depuis plus d'un mois [#00e867fa](https://github.com/betagouv/a-just/commit/00e867fa).
- Amélioration de la gestion des dates d'arrivée dans la section "Situation à prendre en compte", avec initialisation automatique de la date de début de statut [#b27b19f7](https://github.com/betagouv/a-just/commit/b27b19f7).
- Possibilité de dupliquer un agent [#0f3dbfdc](https://github.com/betagouv/a-just/commit/0f3dbfdc) et [#dd034c15](https://github.com/betagouv/a-just/commit/dd034c15).
- Ajout du nom de l'agent au nom d'utilisation [#cc8242bc](https://github.com/betagouv/a-just/commit/cc8242bc).
- Ajout d'une page d'administration pour visualiser les avis utilisateurs (historique, notes moyennes, commentaires, statistiques) [#f3001459](https://github.com/betagouv/a-just/commit/f3001459).
- Possibilité de saisir manuellement une date dans les composants de sélection de date (aj-date-select et aj-date-select-blue) [#761752ed](https://github.com/betagouv/a-just/commit/761752ed).

### Évolutions techniques
- Refactorisation du code lié au formulaire de feedback, incluant le déplacement du composant dans le dossier `components` [#fed005fc](https://github.com/betagouv/a-just/commit/fed005fc).
- Correction d'une requête Sequelize pour optimiser la récupération des statistiques d'avis [#06e52cb2](https://github.com/betagouv/a-just/commit/06e52cb2).
- Correction du type de validation pour les notes (utilisation de `Types.number()` au lieu de `.min` et `.max`) pour éviter les erreurs 500 [#ec31cd51](https://github.com/betagouv/a-just/commit/ec31cd51).
- Mise à jour des tests E2E pour le formulaire d'ajout d'agent afin d'utiliser la nouvelle fonctionnalité de saisie manuelle de date [#57939669](https://github.com/betagouv/a-just/commit/57939669).
- Correction d'un bug affectant l'affichage de la date "À compter du" sur la page de réaffectation [#8a832abd](https://github.com/betagouv/a-just/commit/8a832abd).

### Autres changements
- Mise à jour de la documentation et des textes de démonstration pour le panorama et le calculateur de données brutes [#41f42fc2](https://github.com/betagouv/a-just/commit/41f42fc2), [#be445df2](https://github.com/betagouv/a-just/commit/be445df2), [#3600abc2](https://github.com/betagouv/a-just/commit/3600abc2).
- Corrections de style et de typographie [#e64e5cd0](https://github.com/betagouv/a-just/commit/e64e5cd0), [#f7c74c5a](https://github.com/betagouv/a-just/commit/f7c74c5a), [#f1efb445](https://github.com/betagouv/a-just/commit/f1efb445).
- Suppression de commentaires et de logs inutiles [#a9b5435b](https://github.com/betagouv/a-just/commit/a9b5435b), [#32a0f972](https://github.com/betagouv/a-just/commit/32a0f972), [#8223a9b1](https://github.com/betagouv/a-just/commit/8223a9b1).
- Correction de bugs mineurs liés à l'affichage et au layout [#9ad62061](https://github.com/betagouv/a-just/commit/9ad62061), [#dcda241d](https://github.com/betagouv/a-just/commit/dcda241d), [#faec5186](https://github.com/betagouv/a-just/commit/faec5186).
- Correction des tooltips TMD [#6587b216](https://github.com/betagouv/a-just/commit/6587b216).
- Mise à jour de la version [#9855e2a7](https://github.com/betagouv/a-just/commit/9855e2a7).
