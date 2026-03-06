## Changelog : monprojetsup (30 derniers jours)

### Résumé
Ce changelog présente les évolutions récentes de Mon Projet Sup, avec un focus sur l'amélioration des suggestions de formations, la gestion des indicateurs et des corrections pour stabiliser l'application. Des améliorations techniques ont également été apportées pour optimiser les performances et faciliter le développement.

### Évolutions fonctionnelles
- Amélioration de l'affichage et de la gestion des indicateurs, suite aux demandes de Laura. [#1061](https://github.com/betagouv/monprojetsup/issues/1061)
- Ajout d'un mode expert avec affichage d'informations détaillées sur les JWT. [#1064](https://github.com/betagouv/monprojetsup/issues/1064) et [#1059](https://github.com/betagouv/monprojetsup/issues/1059)
- Restauration du service de progression. [#1047](https://github.com/betagouv/monprojetsup/issues/1047)
- Mise à jour de l'API front-end. [#1048](https://github.com/betagouv/monprojetsup/issues/1048)
- Amélioration du chargement initial des modèles pour les suggestions2, optimisant ainsi la performance. [#1051](https://github.com/betagouv/monprojetsup/issues/1051)

### Évolutions techniques
- Mise à jour des versions de Spring Boot et d'autres dépendances, corrigeant des problèmes et améliorant la stabilité. [#1053](https://github.com/betagouv/monprojetsup/issues/1053)
- Optimisation du calcul des villes-voeux. [#1050](https://github.com/betagouv/monprojetsup/issues/1050)
- Réduction de l'utilisation de la mémoire pour les suggestions2. [#1040](https://github.com/betagouv/monprojetsup/issues/1040)
- Ajout de tests pour la CI pour les suggestions2. [#1058](https://github.com/betagouv/monprojetsup/issues/1058)
- Simplification du code pour le calcul des villes-voeux.
- Correction de tests et suppression de logs inutiles.
- Rebase de la branche `prod` sur `demo`. [#1070](https://github.com/betagouv/monprojetsup/issues/1070)

### Autres changements
- Modification du niveau de log d'une erreur en information pour un comportement nominal. [#1069](https://github.com/betagouv/monprojetsup/issues/1069)
- Suppression de valeurs codées en dur pour l'année. [#1066](https://github.com/betagouv/monprojetsup/issues/1066)
- Ajout de logs pour le mode expert.
- Ajout de fichiers manquants.
- Correction de bugs divers et amélioration de la qualité du code.
