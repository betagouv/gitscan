## Changelog : territoires-en-transitions (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, l'équipe a continué à moderniser l'architecture de la plateforme en migrant des fonctionnalités vers tRPC pour une meilleure performance et maintenabilité. Des améliorations significatives ont été apportées à la gestion des plans, des fiches actions et des indicateurs, notamment en termes de permissions et d'expérience utilisateur. L'ajout d'une page publique "matrice d'impact" permet une meilleure communication sur les résultats des actions.

### Évolutions fonctionnelles
- Ajout d'une page publique "matrice d'impact" pour visualiser les impacts des actions. [#58db5f8](https://github.com/incubateur-ademe/territoires-en-transitions/issues/58db5f8)
- Amélioration de la gestion des permissions pour les contributeurs sur les fiches actions : ils peuvent désormais créer, modifier et supprimer des sous-actions. [#e2e6673](https://github.com/incubateur-ademe/territoires-en-transitions/issues/e2e6673)
- Possibilité d'ajouter la dernière note d'une fiche action dans les rapports. [#6f4471d](https://github.com/incubateur-ademe/territoires-en-transitions/issues/6f4471d)
- Amélioration de l'interface utilisateur pour la gestion des sous-mesures et des tâches associées.
- Correction de bugs et améliorations de l'expérience utilisateur sur la page des collectivités et du programme.
- Amélioration de la synchronisation Calendly/Airtable. [#e110cf0](https://github.com/incubateur-ademe/territoires-en-transitions/issues/e110cf0)
- Ajout d'une fonctionnalité de personnalisation des fiches actions avec des questions/réponses et un bandeau intégré. [#c5a5e91](https://github.com/incubateur-ademe/territoires-en-transitions/issues/c5a5e91)

### Évolutions techniques
- Migration de plusieurs endpoints vers tRPC : départements, régions, types de plans, ressources, claims, tags, mutations de fiches actions.
- Refactoring du code pour améliorer la performance et la maintenabilité, notamment dans la gestion des imports de plans et des accès aux données.
- Amélioration de la gestion des tests, avec une meilleure isolation et parallélisation.
- Mise à jour de l'infrastructure de backup et restore de la base de données.
- Suppression de code legacy et de feature flags obsolètes.
- Optimisation de l'import de plans et sécurisation de la création de fiches actions.
- Ajout d'index sur les tables d'historique pour améliorer les performances.
- Utilisation d'une bannière personnalisée à la place de Stonly pour les messages d'information.
- Décorrélation du scroll entre le contenu principal et le side panel.

### Autres changements
- Mise à jour de la documentation et des labels dans le catalogue.
- Correction de typos et amélioration de la qualité du code.
- Ajout d'événements Posthog pour le suivi des imports de plans.
- Amélioration de la configuration de Tailwind CSS.
- Mise à jour de l'adresse d'envoi d'emails.
- Modification de la description des rôles des membres.
- Remplacement des statistiques d'usage par des statistiques d'impacts et de résultats.
- Amélioration de l'isolation des tests et ajout de tests unitaires.
