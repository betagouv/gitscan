## Changelog : conversations (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, l'équipe a apporté des améliorations significatives à la sécurité, à la compatibilité des documents et à l'expérience utilisateur de l'application. L'ajout de l'authentification OIDC silencieuse, la prise en charge de nouveaux formats de documents (ODT) et l'optimisation de l'interface utilisateur sont les points forts de cette version. Des corrections de bugs ont également été implémentées pour améliorer la stabilité et la fiabilité de l'application.

### Évolutions fonctionnelles
- Ajout de l'authentification OIDC silencieuse pour une connexion plus fluide [#1234](https://github.com/suitenumerique/conversations/issues/1234).
- Prise en charge de l'analyse des documents ODT, permettant aux utilisateurs de charger et d'interagir avec ce format de fichier.
- Amélioration de l'interface utilisateur avec un nouveau header.
- Possibilité de taper pendant que le LLM génère une réponse, améliorant l'interactivité.
- Ajout d'un outil d'auto-documentation pour faciliter la compréhension et l'utilisation de l'application.
- Ajout d'un mode débogage pour le développement local, facilitant l'identification et la résolution des problèmes.
- Amélioration de l'interface utilisateur pour les projets, avec des corrections de style et de mise en page.
- Les liens sources s'ouvrent désormais dans un nouvel onglet.
- Correction d'un bug qui empêchait la création de nouvelles conversations dans un projet.
- Correction d'un bug qui provoquait un crash en streaming avec les APIs compatibles OpenAI.

### Évolutions techniques
- Refactorisation des tests pour améliorer leur organisation et leur maintenabilité.
- Mise à jour des dépendances pour corriger des vulnérabilités de sécurité (CVE).
- Mise à jour de `lxml` et `pypdf`.
- Mise à jour de `pydantic-ai-slim` et d'autres packages.
- Ajout de support pour les modèles open source.
- Intégration des données carbone depuis l'API Albert.
- Amélioration du routage des documents.
- Ajout de tests unitaires pour le composant `SourceItem`.
- Ajout de linting supplémentaire sur le frontend.
- Mise à jour des dépendances frontend et backend.
- Force de la langue anglaise avant les tests du panneau gauche pour éviter des problèmes d'i18n.

### Autres changements
- Mise à jour des chaînes de traduction (i18n).
- Bump de la version à 0.0.15.
- Mise à jour des descriptions des outils.
- Correction d'un bug lié à un prank d'avril.
- Correction de problèmes de style CSS pour les boutons et le sélecteur de modèle.
