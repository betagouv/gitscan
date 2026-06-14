## Changelog : territoires-en-transitions (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité, la gestion des documents et l'import de plans d'action, notamment via l'ajout d'une fonctionnalité d'importation de fichiers Excel et la gestion des erreurs associées. Des améliorations significatives ont également été apportées à l'interface utilisateur, en particulier pour la gestion des référentiels et des actions, avec une attention particulière portée à la duplication de plans et à la personnalisation.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité de duplication de plan d'action, incluant la copie des budgets, des preuves et des notes associées [#26f13d9](https://github.com/incubateur-ademe/territoires-en-transitions/issues/26f13d9).
- Possibilité de demander un audit directement depuis l'interface [#cd04de5](https://github.com/incubateur-ademe/territoires-en-transitions/issues/cd04de5).
- Amélioration de l'interface pour la gestion des actions, avec une vue tabulaire éditable et des options de filtrage plus précises [#a464ae6](https://github.com/incubateur-ademe/territoires-en-transitions/issues/a464ae6).
- Ajout de la possibilité de télécharger des documents [#0937de9](https://github.com/incubateur-ademe/territoires-en-transitions/issues/0937de9).
- Amélioration de la gestion des invitations et des erreurs associées.
- Ajout d'une modale pour détailler une action à la tâche.

### Évolutions techniques
- Renforcement de la sécurité en bloquant des potentielles failles de type IDOR (Insecure Direct Object Reference) et SSRF (Server-Side Request Forgery) [#0420172](https://github.com/incubateur-ademe/territoires-en-transitions/issues/0420172), [#2930c8b](https://github.com/incubateur-ademe/territoires-en-transitions/issues/2930c8b).
- Refactor de l'import de plans d'action avec une validation plus robuste et une meilleure gestion des erreurs, incluant l'utilisation de Zod pour la validation des formulaires et une gestion améliorée des jobs asynchrones [#f9348bb](https://github.com/incubateur-ademe/territoires-en-transitions/issues/f9348bb).
- Migration vers Next.js 16.2.7 et mise à jour des dépendances ESLint [#b54924a](https://github.com/incubateur-ademe/territoires-en-transitions/issues/b54924a).
- Amélioration des performances en remplaçant Fuse.js par une recherche plein texte côté serveur pour la recherche de collectivités [#8a731f8](https://github.com/incubateur-ademe/territoires-en-transitions/issues/8a731f8).
- Refactor de la gestion des labels JSX pour une meilleure maintenabilité et réutilisation.
- Amélioration de la gestion des tests, avec la migration vers Vitest et la suppression de tests Cypress dépréciés.
- Utilisation de points TRPC pour certaines opérations (comptage de documents, modification/suppression de preuves).

### Autres changements
- Mise à jour de la documentation.
- Suppression de code et de fichiers inutilisés.
- Amélioration de la configuration CI/CD.
- Corrections de typos et améliorations de la lisibilité du code.
- Ajout de fixtures pour les tests.
- Amélioration de la gestion des erreurs et des logs.
- Mise à jour des dépendances.
- Ajout de metadata pour la nouvelle page plateforme du site.
