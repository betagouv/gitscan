## Changelog : resorption-bidonvilles (30 derniers jours, au 28 octobre 2026)

### Résumé
Ce mois-ci, la plateforme a bénéficié d'améliorations visant à clarifier l'information pour les utilisateurs, notamment grâce à une meilleure gestion de l'affichage des erreurs d'indicateurs et l'introduction de nouveaux éléments visuels (popup de nouveautés, identification de l'environnement de préproduction). Plusieurs ajustements d'interface ont également été effectués pour épurer l'expérience utilisateur.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités et interface** :
    - Ajout d'une fenêtre contextuelle (popup) pour présenter les nouveautés liées à la Journée de la Résorption [#2792](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2792).
    - Mise en place d'un signalement visuel permettant d'identifier immédiatement l'environnement de préproduction [#2782](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2782).
- **Améliorations et corrections** :
    - Optimisation de la gestion des erreurs d'indicateurs : les erreurs sont désormais regroupées par année et les messages sont plus explicites [#2781](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2781).
    - Retrait du bandeau d'alerte "canicule" sur le tableau de bord, la liste des sites et les fiches sites.
    - Correction du libellé concernant le mode public des commentaires d'action [#2778](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2778).

### Évolutions techniques
- **Refactorisation et styles** :
    - Migration des styles vers Tailwind CSS pour remplacer l'utilisation des styles "scoped".
    - Simplification de la gestion du favicon pour l'environnement de préproduction [#2782](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2782).
- **Composants UI** :
    - Amélioration du composant `ErrorSummary` pour le rendre plus flexible (propriété de message optionnelle et émission d'événements de sélection) [#2781](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2781).

### Autres changements
- Publication des versions v2.60.2, v2.60.3 et v2.60.4.
