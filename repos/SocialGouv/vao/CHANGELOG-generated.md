## Changelog : vao (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent principalement sur l'amélioration du module d'agrément, notamment en ce qui concerne la gestion des messages, le renouvellement des agréments et l'interface back-office. Des corrections et des améliorations ont également été apportées au fusager et à la gestion des utilisateurs.

### Évolutions fonctionnelles
- Ajout de la gestion des messages non lus pour les agréments côté DREETS. [#1272](https://github.com/SocialGouv/vao/issues/1272)
- Amélioration de l'affichage des informations de la personne et de son représentant légal. [#1265](https://github.com/SocialGouv/vao/issues/1265)
- Ajout de la possibilité de modifier le statut d'un agrément en "À MODIFIER" dans le back-office. [#1227](https://github.com/SocialGouv/vao/issues/1227)
- Ajout d'un bouton d'action pour confirmer la complétude d'un agrément dans le back-office. [#1236](https://github.com/SocialGouv/vao/issues/1236)
- Ajout d'un affichage des documents par onglets dans le back-office pour les agréments. [#1233](https://github.com/SocialGouv/vao/issues/1233)
- Ajout de la possibilité de refuser un agrément dans le back-office. [#1245](https://github.com/SocialGouv/vao/issues/1245)
- Ajout de la liste des JDMA dans le fusager. [#1268](https://github.com/SocialGouv/vao/issues/1268)
- Suppression des menus "Renouvellement" et "Agrément" dans le fusager. [#1269](https://github.com/SocialGouv/vao/issues/1269)
- Correction d'un bug où le nombre de femmes était indéfini dans le fusager. [#1270](https://github.com/SocialGouv/vao/issues/1270)
- Correction d'un bug où le bouton d'action disparaissait dans le fusager. [#1238](https://github.com/SocialGouv/vao/issues/1238)
- Correction d'un bug empêchant de passer à l'étape suivante dans le fusager avec une condition spécifique. [#1237](https://github.com/SocialGouv/vao/issues/1237)

### Évolutions techniques
- Refactorisation et passage en TypeScript de plusieurs composants liés aux étapes de renouvellement d'agrément (1085, 1084, 1101, 1194).
- Amélioration de la gestion des requêtes pour éviter les erreurs liées aux tableaux. [#1247](https://github.com/SocialGouv/vao/issues/1247)
- Mise à jour des pré-commits pour interdire l'utilisation de `console.log`. [#1246](https://github.com/SocialGouv/vao/issues/1246)
- Amélioration des tests E2E pour la gestion des personnes physiques et la suppression d'utilisateurs. [#1244](https://github.com/SocialGouv/vao/issues/1244) et [#1235](https://github.com/SocialGouv/vao/issues/1235)

### Autres changements
- Nettoyage du code dans `shared-ui`. [#1234](https://github.com/SocialGouv/vao/issues/1234)
- Correction de bugs mineurs et améliorations diverses de l'interface utilisateur.
