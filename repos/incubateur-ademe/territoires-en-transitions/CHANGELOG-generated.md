## Changelog : territoires-en-transitions (30 derniers jours, au 19 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur, notamment au niveau de la gestion des référentiels et des fiches action. Des corrections ont été apportées pour améliorer la stabilité et la performance de la plateforme, ainsi que des fonctionnalités pour la personnalisation et l'édition des données. L'accent a également été mis sur la migration vers de nouvelles technologies (trpc) pour une meilleure maintenabilité et performance du backend.

### Évolutions fonctionnelles
- Ajout d'une modale "demander un audit" pour les référentiels [#1234](https://github.com/incubateur-ademe/territoires-en-transitions/issues/1234).
- Possibilité d'éditer les référentiels via une vue tabulaire.
- Amélioration de l'interface utilisateur pour la gestion des sous-mesures et des tâches.
- Les contributeurs pilotes peuvent désormais créer, modifier et supprimer des sous-actions.
- Ajout de la possibilité d'ajouter la dernière note dans les rapports.
- Amélioration de la page "Plateforme" du site avec une nouvelle structure, une section FAQ et des informations mises à jour.
- Les utilisateurs peuvent désormais importer des plans plus facilement grâce à des améliorations de la gestion des fichiers et des données.
- Possibilité de personnaliser l'affichage des mesures et sous-mesures en fonction des questions de personnalisation.
- Ajout d'une matrice d'impact publique.
- Amélioration de l'édition en ligne des champs, notamment avec un sélecteur plus flexible.

### Évolutions techniques
- Migration de plusieurs endpoints SQL vers tRPC pour améliorer la performance et la maintenabilité.
- Refactor de la gestion des imports de plans pour une meilleure efficacité et sécurité.
- Amélioration de la synchronisation Calendly Airtable.
- Optimisation des requêtes et des index de la base de données.
- Mise à jour des dépendances et des configurations pour assurer la stabilité et la sécurité de la plateforme.
- Utilisation de boutons du Design System (DS) au lieu de composants personnalisés.
- Amélioration de la gestion des tests et de l'intégration continue.
- Suppression de code obsolète et nettoyage de la base de code.
- Migration vers un nouveau système de sauvegarde et de restauration de la base de données.

### Autres changements
- Mise à jour de la documentation et des commentaires du code.
- Correction de typos et amélioration de la lisibilité du code.
- Amélioration des stories pour les composants de l'interface utilisateur.
- Ajout de métriques et de logs pour faciliter le suivi et le débogage.
- Mise à jour des adresses d'envoi d'emails.
- Amélioration de la configuration de Tailwind CSS.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
