## Changelog : Aidants_Connect (30 derniers jours, au 15 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'accessibilité de l'application, notamment via l'utilisation de balises sémantiques plus appropriées et l'ajout d'attributs ARIA. Des améliorations ont également été apportées à la gestion des mandats, à l'export des données pour les organismes de formation et à la préparation de la mise à jour vers Django 5.2.

### Évolutions fonctionnelles
- Suppression de la rubrique "à distance" dans le formulaire de création de mandat, rendant ce dernier plus accessible. [#1780](https://github.com/betagouv/Aidants_Connect/issues/1780)
- Amélioration de l'export des inscrits pour les Organismes de Formation (OF). [#1778](https://github.com/betagouv/Aidants_Connect/issues/1778)
- Ajout d'un score PIX pour évaluer la performance de l'application. [#1782](https://github.com/betagouv/Aidants_Connect/issues/1782)
- Ajout d'une option pour activer/désactiver le consentement SMS pour les tests.
- Les emails de formation ne sont plus envoyés aux référents inactifs. [#1784](https://github.com/betagouv/Aidants_Connect/issues/1784)

### Évolutions techniques
- Refactoring important du formulaire de mandat pour supprimer les options de signature à distance et améliorer la clarté du code.
- Amélioration de la structure sémantique et de l'accessibilité générale de l'application en utilisant des balises HTML plus appropriées (listes, titres, etc.) et des attributs ARIA.
- Mise à jour des dépendances en préparation de la migration vers Django 5.2.
- Suppression de code obsolète et de templates inutilisés pour simplifier la base de code.
- Implémentation de templates d'erreur DSFR (400, 403, 404, 408, 500).
- Ajout de gestion du focus pour le cookie banner afin d'améliorer l'accessibilité.

### Autres changements
- Ajout de notes suite au test PIX.
- Amélioration de la documentation et des tests.
- Correction de problèmes de visibilité des tuiles de formation pour les aidants et responsables en fonction des droits de mandat.
- Suppression de l'iframe BREVO de la page d'accueil pour améliorer l'accessibilité et la réactivité.
- Mise à jour des titres et des structures de sections pour améliorer la sémantique et l'accessibilité.
