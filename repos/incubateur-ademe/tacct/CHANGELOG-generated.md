## Changelog : tacct (30 derniers jours, au 7 mai 2026)

### Résumé
Ce changelog présente les améliorations apportées à tacct au cours du dernier mois. Les principales évolutions concernent l'enrichissement des données disponibles (agriculture biologique, feux de forêt, âge du bâti), l'amélioration de l'interface utilisateur (nouvelles images, boutons, correction de bugs d'affichage) et l'ajout de nouvelles fonctionnalités pour la gestion des ressources et la navigation.

### Évolutions fonctionnelles
- Amélioration de la navigation et des boutons du slider pour les articles et collections.
- Ajout d'un design patch pour la gestion des DROM (Départements et Régions d'Outre-Mer).
- Implémentation d'une barre de recherche, d'une section ressources, d'une FAQ et de guides méthodologiques.
- Correction de l'affichage de la modale du slider des collections.
- Ajout d'une fonctionnalité d'export/partage (correction d'un bug lié au bouton).
- Mise à jour des données relatives aux surfaces en agriculture biologique [#1234](https://github.com/incubateur-ademe/tacct/issues/1234).
- Mise à jour des données relatives aux incendies de forêt.
- Ajout de données sur l'âge du bâti.
- Ajout d'une notice sur la page d'accueil.

### Évolutions techniques
- Import corrigé.
- Refactoring : remplacement d'anciennes images et suppression de fichiers inutilisés.
- Mise à jour de la base de données pour l'agriculture biologique.
- Correction du `z-index` de la modale cookie.

### Autres changements
- Amélioration de la couleur du bandeau de la page d'accueil.
- Merge de branches pour intégrer les modifications de `facili-tacct`.
- Mise à jour de la base de données pour les sources d'incendies de forêt.
