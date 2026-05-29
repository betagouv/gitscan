## Changelog : hyyypertool (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur avec l'ajout du mode sombre, l'amélioration de la gestion des modérations (ajout de raisons de refus, tri des colonnes) et une sécurité renforcée grâce à la limitation du débit par adresse IP. Des corrections de bugs et des mises à jour de dépendances ont également été effectuées.

### Évolutions fonctionnelles
- Ajout d'un champ "raison du refus" pour les modérations, permettant de donner un contexte plus clair aux utilisateurs.
- Possibilité de trier les colonnes dans la liste des modérations.
- Ajout de la possibilité de supprimer des modèles de réponse.
- Amélioration de l'interface utilisateur avec l'implémentation du mode sombre, incluant l'adaptation des boutons et des listes déroulantes.
- Ajout d'un interrupteur pour autoriser ou non la modification de la demande par l'utilisateur.

### Évolutions techniques
- Implémentation d'une limitation du débit par adresse IP pour renforcer la sécurité.
- Remplacement des mocks de certains services externes par des routes de développement locales pour une meilleure isolation et flexibilité.
- Mise à jour de plusieurs dépendances pour bénéficier des dernières corrections et améliorations de sécurité.
- Refactorisation du code pour améliorer la maintenabilité et la performance.
- Ajout d'une colonne `end_user_reason` à la table `response_templates`.

### Autres changements
- Mise à jour de la documentation.
- Corrections de bugs mineurs liés à l'affichage en mode sombre et à la gestion du cache.
- Amélioration des messages d'erreur et de l'expérience utilisateur globale.
- Mise à jour des dépendances de développement (Cypress, Prettier, etc.).
- Publication de nouvelles versions : 2026.5.1, 2026.5.2, 2026.5.3, 2026.5.4, 2026.5.5, 2026.5.6, 2026.5.7, 2026.5.8, 2026.5.9, 2026.5.10, 2026.5.11, 2026.5.12.
