## Changelog : Aidants_Connect (30 derniers jours, au 15 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration significative de l'accessibilité de l'application, notamment en corrigeant des problèmes identifiés lors d'un pré-audit. Des améliorations ont également été apportées à la structure sémantique du code et des templates, ainsi qu'à l'export des données pour les Organismes de Formation (OF). Une préparation à la mise à jour vers Django 5.2 a été initiée avec la mise à jour des dépendances.

### Évolutions fonctionnelles
- Suppression de la rubrique "à distance" dans le formulaire de nouveau mandat, rendant ce dernier plus accessible. [#1780](https://github.com/betagouv/Aidants_Connect/issues/1780)
- Amélioration de l'export des inscrits pour les Organismes de Formation (OF). [#1778](https://github.com/betagouv/Aidants_Connect/issues/1778)
- Ajout d'un score Pix pour évaluer la qualité des données. [#1782](https://github.com/betagouv/Aidants_Connect/issues/1782)
- Les emails de formation ne sont plus envoyés aux référents inactifs. [#1784](https://github.com/betagouv/Aidants_Connect/issues/1784)

### Évolutions techniques
- Refactor important de nombreux templates HTML pour améliorer la structure sémantique et l'accessibilité, notamment en utilisant des listes et des balises HTML appropriées (h1, h2, h3, etc.).
- Ajout d'attributs ARIA pour améliorer l'accessibilité pour les utilisateurs de technologies d'assistance.
- Mise à jour des dépendances pour préparer la migration vers Django 5.2.
- Suppression de code HTML obsolète et non utilisé.
- Amélioration de la gestion du focus pour le cookie banner afin d'améliorer l'accessibilité.

### Autres changements
- Ajout de templates d'erreur DSFR (400, 403, 404, 408, 500) pour une meilleure expérience utilisateur en cas d'erreur.
- Correction de la visibilité des tuiles de formation pour les aidants et responsables en fonction de leurs droits de mandat.
- Amélioration de la structure des accordéons dans les templates.
- Suppression de balises meta inutilisées.
