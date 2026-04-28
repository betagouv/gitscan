## Changelog : conversations (30 derniers jours, au 27 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout de nouvelles fonctionnalités pour l'authentification, la gestion des documents et l'expérience utilisateur globale. L'ajout d'un outil de documentation automatique et l'amélioration de l'interface utilisateur pour les projets sont particulièrement notables. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance.

### Évolutions fonctionnelles
- Ajout de l'authentification OIDC silencieuse [#1234](https://github.com/suitenumerique/conversations/issues/1234).
- Prise en charge de l'analyse des fichiers ODT et amélioration du routage des documents.
- Possibilité de copier le contenu formaté dans Word/Docs depuis l'interface.
- Ajout d'un outil de documentation automatique pour le backend.
- Possibilité de taper pendant que le LLM génère une réponse.
- Amélioration de l'interface utilisateur pour la gestion des projets (UI et correction de bugs).
- Nouvelle interface utilisateur pour l'en-tête.
- Ajout d'un mode débogage pour le développement local.

### Évolutions techniques
- Prise en charge des modèles open source.
- Refactorisation des tests backend pour une meilleure organisation.
- Mise à jour des dépendances backend et frontend pour corriger des vulnérabilités de sécurité (CVEs).
- Récupération des données carbone depuis l'API Albert.
- Ajout de linting supplémentaire sur le frontend.
- Suppression des outils de recherche legacy de la configuration du modèle.

### Autres changements
- Correction de bugs mineurs d'interface utilisateur (taille du bouton "nouvelle conversation", liens sources ouvrant dans un nouvel onglet, marges, couleurs).
- Mise à jour des chaînes de traduction (i18n).
- Ajout d'une blague pour le 1er avril (désactivée).
- Correction de problèmes de rendu Markdown en streaming.
- Correction de bugs liés au thème sombre.
- Correction de problèmes liés aux tests E2E (langue forcée à l'anglais).
