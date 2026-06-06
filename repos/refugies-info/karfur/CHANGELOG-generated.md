## Changelog : karfur (30 derniers jours, au 4 juin 2026)

### Résumé
Ce mois-ci, les évolutions de karfur se sont concentrées sur la correction de bugs et l'amélioration de la stabilité de la plateforme, notamment en production. Des améliorations ont été apportées à la recherche, à l'affichage des données et à la gestion des doublons. L'équipe a également travaillé sur l'amélioration de l'expérience utilisateur sur mobile et la gestion des erreurs.

### Évolutions fonctionnelles
- Correction d'un problème d'affichage des accents dans le moteur de recherche [#3769](https://github.com/refugies-info/karfur/issues/3769).
- Amélioration de l'affichage sur mobile : correction du comportement du bouton "retour en haut" [#3773](https://github.com/refugies-info/karfur/issues/3773).
- Correction de l'affichage des labels de département qui se superposaient aux pop-ups [#3766](https://github.com/refugies-info/karfur/issues/3766).
- Correction d'un bug empêchant l'affichage des fiches sur le site en production [#3770](https://github.com/refugies-info/karfur/issues/3770).
- Correction d'une coquille sur la page "mission" [#3746](https://github.com/refugies-info/karfur/issues/3746).
- Correction d'un problème de sauvegarde automatique sur la fiche OPFRA [#3762](https://github.com/refugies-info/karfur/issues/3762).
- Ajout d'un endpoint pour la détection de doublons d'agents [#3754](https://github.com/refugies-info/karfur/issues/3754) et amélioration du scoring des doublons.

### Évolutions techniques
- Refactorisation du code pour gérer correctement les valeurs nulles dans le calcul du nombre de CDA [#3770](https://github.com/refugies-info/karfur/issues/3770).
- Correction de la gestion des caractères encodés et de l'affichage des villes sélectionnées lors d'un rafraîchissement de la page.
- Amélioration de la gestion des erreurs et ajout de logs plus précis.
- Stabilisation des tests Jest sur mobile après des mises à jour de dépendances.
- Mise à jour des dépendances pour corriger des failles de sécurité.
- Amélioration de la gestion des dates et des timestamps pour éviter les erreurs.
- Correction de la gestion des utilisateurs SSO avec un prénom potentiellement nul.

### Autres changements
- Ajout d'un nouveau membre à l'équipe.
- Ajout du nom de l'équipe au fichier README.
- Ajout d'un hook GitLeaks pour la détection de secrets dans le code.
- Suppression de configurations obsolètes et nettoyage du code.
- Mise à jour de la documentation.
- Publication de la version 2.8.0.
