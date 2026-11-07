## Changelog : resorption-bidonvilles (30 derniers jours, au 28 octobre 2026)

### Résumé
Ce mois-ci, la plateforme a bénéficié d'améliorations significatives pour la gestion des erreurs de données et l'expérience utilisateur. Les utilisateurs disposent désormais d'une meilleure visibilité sur les erreurs d'indicateurs et d'un indicateur clair pour identifier l'environnement de préproduction. L'interface a également été épurée avec la suppression de certains bandeaux d'alerte et l'ajout d'une annonce pour la Journée de la Résorption.

### Évolutions fonctionnelles
- Ajout d'une fenêtre contextuelle (popup) pour annoncer les nouveautés liées à la Journée de la Résorption [#2792](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2792).
- Amélioration de la gestion des erreurs d'indicateurs : regroupement par année, ajout de préfixes pour les messages scolaires et amélioration de la gestion du focus sur les erreurs [#2781](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2781).
- Mise en place d'un signalement visuel pour identifier l'environnement de préproduction [#2782](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2782).
- Retrait du bandeau d'alerte "canicule" sur l'ensemble de l'interface (tableau de bord, liste des sites et fiches sites).

### Évolutions techniques
- Refactorisation du système de style : passage de l'utilisation de styles "scoped" vers Tailwind CSS.
- Optimisation du composant `ErrorSummary` pour rendre la propriété de message optionnelle et permettre l'émission d'un événement `select` [#2781](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2781).
- Simplification de la gestion des favicons en supprimant la distinction spécifique pour l'environnement de préproduction [#2782](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2782).
