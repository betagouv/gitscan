## Changelog : resorption-bidonvilles (30 derniers jours, au 28/10/2026)

### Résumé
Les récentes évolutions se sont concentrées sur l'amélioration de la clarté de l'interface utilisateur et la gestion des erreurs. La plateforme bénéficie désormais d'une meilleure distinction entre les environnements de travail et d'une présentation plus structurée des erreurs d'indicateurs. Des ajustements visuels ont également été effectués pour épurer l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout d'une fenêtre contextuelle (popup) pour présenter les nouveautés liées à la Journée de la Résorption [#2792](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2792).
- Mise en place d'un signalement visuel permettant d'identifier immédiatement l'environnement de préproduction [#2782](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2782).
- Amélioration de la gestion des erreurs d'indicateurs : les messages sont désormais plus explicites et regroupés par année pour faciliter la lecture [#2781](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2781).
- Optimisation du système de focus lors de la consultation des erreurs d'indicateurs [#2781](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2781).
- Suppression du bandeau d'alerte "canicule" sur le tableau de bord, la liste des sites et les fiches sites.

### Évolutions techniques
- Refactorisation des styles pour privilégier l'utilisation de Tailwind CSS au détriment des styles "scoped".
- Optimisation du code via l'ajout d'utilitaires de regroupement des erreurs par année [#2781](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2781).
- Amélioration du composant `ErrorSummary` (rendu de la propriété message optionnelle et ajout de l'émission d'un événement `select`) [#2781](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2781).
- Simplification de la gestion du favicon pour l'environnement de préproduction [#2782](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2782).

### Autres changements
- Publication des versions v2.60.2, v2.60.3 et v2.60.4.
