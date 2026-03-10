## Changelog : anssi-portail (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'implémentation de la nouvelle section NIS2, avec l'ajout de la page d'accueil, la comparaison des exigences ISO/NIS2 et l'intégration des données depuis Grist. Des améliorations ont également été apportées à la page de diagnostic cyber, notamment l'ajout de statistiques et la refonte de l'interface. Enfin, des corrections de bugs et des optimisations de performance ont été réalisées sur l'ensemble du portail.

### Évolutions fonctionnelles
- Ajout de la page d'accueil NIS2 et de son menu de navigation. [#2345](lien vers PR/issue si applicable)
- Implémentation de la comparaison des exigences ISO et NIS2, avec affichage des différences et correspondance des niveaux. [#1234](lien vers PR/issue si applicable)
- Ajout de la fonctionnalité de téléchargement de la plaquette NIS2.
- Amélioration de la page de demande de diagnostic cyber avec l'ajout de statistiques et de liens vers des solutions.
- Affichage de la date de publication et de mise à jour des guides.
- Ajout de la mission "Réguler" de l'ANSSI.
- Affichage des logos sur la page de demande de diagnostic cyber.
- Ajout d'une page de suivi de la santé des guides, avec affichage des guides en bonne santé et des éventuels problèmes.
- Affichage des liens vers les solutions dans la section NIS2.

### Évolutions techniques
- Mise à jour de plusieurs dépendances de sécurité (dompurify, immutable.js, minimatch, ajv, svelte).
- Utilisation de Grist comme source de données pour les exigences NIS2 et les guides.
- Optimisation des requêtes SQL pour améliorer les performances.
- Refactoring du code pour améliorer la maintenabilité et la lisibilité.
- Utilisation de workflows GitHub Actions pour la CI/CD.
- Amélioration de la gestion des erreurs et de la consignation.
- Mise en place d'un cache pour les données Grist.
- Utilisation de types plus stricts en TypeScript.

### Autres changements
- Mise à jour des données du panorama 2025 et des statistiques.
- Amélioration de la documentation.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Suppression de feature flags obsolètes.
- Ajustements de style et de mise en page.
- Ajout de tests unitaires.
- Correction de warnings et d'erreurs de linting.
