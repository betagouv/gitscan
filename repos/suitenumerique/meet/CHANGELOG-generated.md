## Changelog : meet (30 derniers jours, au 4 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des fichiers, notamment un accès sécurisé et une administration dédiée. L'expérience utilisateur est également améliorée avec l'ajout de fonctionnalités de picture-in-picture, de réactions et d'optimisations de performance, en particulier au niveau du chargement initial de l'application. Des corrections de sécurité et des mises à jour de dépendances ont également été intégrées.

### Évolutions fonctionnelles
- Ajout d'une administration dédiée pour les fichiers [#1387](https://github.com/suitenumerique/meet/issues/1387).
- Implémentation de la fonctionnalité Picture-in-Picture (PiP) pour les réunions, incluant une barre de contrôle et des notifications.
- Amélioration de la gestion des réactions avec une meilleure accessibilité et compatibilité mobile.
- Support étendu des formats vidéo et audio pour les résumés de réunion [#1358](https://github.com/suitenumerique/meet/issues/1358).
- Possibilité de configurer l'accès et le niveau de permission des salles de réunion via l'API externe [#1260](https://github.com/suitenumerique/meet/issues/1260).
- Ajout d'une commande de gestion pour fusionner les utilisateurs en double.
- Support de la configuration de la salle de réunion (configuration et niveau d'accès) via l'API externe.

### Évolutions techniques
- Refactorisation de l'API pour remplacer les options de salle obsolètes.
- Mise à jour de plusieurs dépendances, incluant `aiohttp`, `urllib3`, `eslint-plugin-react-hooks`, `webpack-dev-server`, `django` et `core-js` pour corriger des failles de sécurité et améliorer la stabilité.
- Utilisation de `uv` pour la gestion des dépendances dans les agents.
- Optimisation du chargement initial de l'application en utilisant le code splitting et le lazy loading des routes.
- Amélioration de la robustesse du processus de suppression des fichiers.
- Refactorisation de la logique de gestion des utilisateurs pour éviter les conditions de concurrence.
- Utilisation de `uv.lock` pour la gestion des dépendances dans le PaaS.
- Amélioration de la synchronisation de la configuration de la salle de réunion.
- Préfixage des routes Swagger avec `/api`.

### Autres changements
- Mise à jour de la documentation pour refléter le support de la configuration de la salle de réunion.
- Amélioration des logs pour le speaker assignment.
- Correction de la documentation des valeurs du chart Helm.
- Suppression de dépendances inutiles dans le frontend.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Ajout de tests pour la couverture du code.
- Correction de la position des tooltips dans la fenêtre PiP.
- Amélioration de la gestion des erreurs et des exceptions.
- Correction de la génération des ID de salle pour renforcer la sécurité.
- Mise à jour du changelog.
