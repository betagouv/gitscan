## Changelog : recoco-plugins-mi-depafi (30 derniers jours, au 8 juin 2026)

### Résumé
Ce plugin a connu une évolution significative au cours du dernier mois, avec l'ajout de la gestion des "Réalisations" (Realisation). Cette nouvelle fonctionnalité permet aux utilisateurs de documenter et de partager les actions menées dans le cadre de la transition écologique, avec des options de visualisation sur une carte, de vote, et d'intégration avec le CRM. Des améliorations ont également été apportées à l'interface utilisateur et à l'export de données.

### Évolutions fonctionnelles
- Ajout de la fonctionnalité "Réalisations" permettant de créer, modifier, supprimer et visualiser des actions concrètes. [#US-01](https://github.com/betagouv/recoco-plugins-mi-depafi/issues/US-01) et [#US-02](https://github.com/betagouv/recoco-plugins-mi-depafi/issues/US-02)
- Possibilité de créer une "Réalisation" directement depuis une page de "Ressource".
- Intégration d'un système de vote pour les "Réalisations", limité à un vote par utilisateur.
- Affichage des "Réalisations" sur une carte interactive, avec une API dédiée.
- Ajout d'une page listant les "Réalisations" accessible depuis le CRM, avec un comptage des "Réalisations" par projet.
- Export des "Réalisations" au format CSV depuis le CRM.
- Possibilité d'éditer une "Réalisation" même après sa publication.
- Ajout d'une modale pour confirmer la finalisation d'une tâche dans une conversation.
- Ajout d'une trace privée dans le CRM lors de la publication d'une "Réalisation".

### Évolutions techniques
- Implémentation de l'API REST pour les "Réalisations" en utilisant les nouveaux hooks et mécanismes de plugins du cœur de Recoco.
- Utilisation de HTMX pour les modales d'édition et de suppression des "Réalisations", ainsi que pour la prévisualisation du contenu.
- Refonte de l'interface utilisateur de la page "Réalisations" avec des améliorations de style.
- Ajout de tests unitaires pour la création et la liste des "Réalisations".

### Autres changements
- Initialisation de la structure du projet.
- Ajout de modèles pour les "Réalisations" et les photos associées.
- Correction du nom d'une dépendance.
- Ajout d'un lien htmx pour la suppression et la visualisation des éléments.
- Ajout d'un nœud de conversation pour étendre la conversation avec un nœud "Réalisation".
- Ajout d'un template de carte de "Réalisation" manquant.
- Filtrage des "Réalisations" en mode brouillon.
