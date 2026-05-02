## Changelog : stage-direct (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives en termes d'authentification, de tests et de performance. L'ajout de pages d'authentification avec le bouton Proconnect, ainsi que la mise en place de tests end-to-end et d'intégration, renforcent la qualité et la fiabilité de la plateforme. Une refonte de la configuration TRPC et de la gestion des routes a également été effectuée pour optimiser l'architecture.

### Évolutions fonctionnelles
- Ajout de pages d'authentification avec intégration du bouton Proconnect pour une expérience utilisateur simplifiée. [#1](https://github.com/betagouv/stage-direct/pull/1)
- Création d'une page FAQ pour répondre aux questions fréquentes des utilisateurs.
- Amélioration de la gestion des erreurs dans les formulaires.
- Implémentation d'un système de session côté client pour une meilleure gestion de l'état de l'utilisateur.

### Évolutions techniques
- Mise en place d'une suite de tests end-to-end (e2e) et d'intégration avec Playwright pour garantir la qualité du code et la couverture des fonctionnalités.
- Refonte de la configuration TRPC pour une meilleure séparation des routes authentifiées et non authentifiées.
- Initialisation et réinitialisation des migrations Prisma pour une gestion optimisée de la base de données.
- Amélioration de la configuration de l'environnement avec la gestion des variables d'environnement (.dotenv).
- Optimisation de la performance en supprimant les index inutiles.
- Mise à jour des dépendances du projet.

### Autres changements
- Améliorations de l'UX/UI et corrections de style CSS.
- Utilisation du bouton Proconnect de la DSFR pour une cohérence visuelle.
- Préchargement des données pour une meilleure réactivité de l'application.
- Initialisation du stack de l'application.
- Corrections mineures et revue du code.
