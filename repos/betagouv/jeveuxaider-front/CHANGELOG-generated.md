## Changelog : jeveuxaider-front (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience d'inscription des organisations et des missions, notamment en simplifiant les formulaires et en ajoutant de nouvelles fonctionnalités de gestion des tags et des ressources. Des corrections et des améliorations ont également été apportées à la navigation, aux notifications et à l'intégration des événements canicule et tournées d'été.

### Évolutions fonctionnelles
- **Inscription des organisations :** Refonte des formulaires d'inscription des organisations avec une amélioration de la gestion des adresses, de la sélection des départements et de la validation des données. Ajout d'une description template pour faciliter la saisie de l'adresse. [#346](https://github.com/betagouv/jeveuxaider-front/issues/346)
- **Gestion des tags :** Implémentation d'un nouveau formulaire pour la gestion des tags des structures, avec validation et soumission améliorées.
- **Partage de missions :** Amélioration du partage de missions, notamment pour les utilisateurs non-managers. [#353](https://github.com/betagouv/jeveuxaider-front/issues/353)
- **Navigation :** Renommage de "Associations" en "Annuaire" dans l'en-tête et les liens de page pour une meilleure cohérence.
- **Campagne d'été :** Mise à jour des composants MissionInfos et Section pour la campagne d'été.
- **Événement Canicule :** Mise à jour des dates de l'événement canicule de juin à août.
- **Fermeture des inscriptions :** Modification du libellé "Fermer les inscriptions" en "Mettre en pause les inscriptions" pour plus de clarté.
- **Ajout d'un lien Canicule :** Ajout d'un lien "Canicule" dans la navigation secondaire.
- **Filtre de localisation :** Mise à jour des options de rayon et de la logique de valeur par défaut du filtre de localisation. [#342](https://github.com/betagouv/jeveuxaider-front/issues/342)
- **Invitation Soft Gate :** Ajout de paramètres UTM pour le suivi des invitations et correction de problèmes de comportement sur certains appareils mobiles.
- **Statistiques Plausible :** Mise à jour de l'API Plausible et suppression d'un filtre de date défectueux. [#344](https://github.com/betagouv/jeveuxaider-front/issues/344)

### Évolutions techniques
- **Refactoring :** Refactorisation de plusieurs composants liés à l'inscription des organisations et à la gestion des états.
- **Architecture :** Amélioration de la gestion de l'état des organisations et de la logique des badges.
- **README :** Mise à jour de la description du projet et de la pile technique dans le fichier README.
- **Typescript :** Utilisation de `v-bind` pour les attributs aria afin d'éviter les exigences d'attributs avec tiret. [#349](https://github.com/betagouv/jeveuxaider-front/issues/349)
- **Quiz :** Ajout de `redirectParams` pour la gestion dynamique des requêtes dans les composants de quiz.

### Autres changements
- **Mise à jour des labels Rolables :** Mise à jour des labels des rôles. [#348](https://github.com/betagouv/jeveuxaider-front/issues/348)
- **Suppression du filtre adulte :** Suppression du filtre adulte du marché inversé et ajout d'une redirection. [#352](https://github.com/betagouv/jeveuxaider-front/issues/352)
- **Correction de validation de date de naissance :** Correction d'une validation de date de naissance non sécurisée. [#350](https://github.com/betagouv/jeveuxaider-front/issues/350)
- **Suppression du composant d'upload de logo :** Suppression du composant d'upload de logo du formulaire Territoire pour simplifier la mise en page.
- **Amélioration du Drawer :** Ajout de `overflow-x-hidden` pour éviter le défilement horizontal.
