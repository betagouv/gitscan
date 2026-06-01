## Changelog : meet (30 derniers jours, au 31 mai 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration des performances frontend, notamment en optimisant le chargement des ressources et en réduisant la taille des bundles JavaScript. Des améliorations significatives ont également été apportées à la gestion des configurations de salle et à la synchronisation des états, permettant une plus grande flexibilité et un meilleur contrôle pour les administrateurs. Enfin, des fonctionnalités de picture-in-picture et de réactions ont été ajoutées, enrichissant l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout du support pour tous les types de fichiers audio et vidéo. [#1358](https://github.com/suitenumerique/meet/issues/1358)
- Implémentation d'une fonctionnalité Picture-in-Picture (PiP) pour les réunions, incluant une barre de contrôle basique et des notifications d'état de connexion.
- Ajout de réactions pendant les réunions, avec une interface accessible et responsive.
- Possibilité pour les administrateurs de configurer le droit de muter les autres participants en fonction de la configuration de la salle.
- Amélioration de l'attribution des locuteurs grâce à l'analyse VAD (Voice Activity Detection).
- Support de la configuration et du niveau d'accès des salles via l'API externe. [#1260](https://github.com/suitenumerique/meet/issues/1260)
- Ajout d'un lien direct vers l'enregistrement dans l'email de notification de fin d'enregistrement.
- Amélioration du logging de l'attribution des locuteurs.

### Évolutions techniques
- Optimisation du chargement des ressources frontend via le code splitting et le lazy loading des routes.
- Utilisation de Rollup pour la visualisation des bundles et l'optimisation de la taille du code.
- Remplacement des imports de styles LiveKit par un chargement dynamique.
- Refactorisation du code frontend pour améliorer la modularité et la maintenabilité.
- Utilisation de `uv` pour la gestion des dépendances dans les agents.
- Validation de la configuration des salles avec un schéma Pydantic.
- Amélioration de la robustesse du processus de démarrage de l'enregistrement.
- Mise à jour des dépendances, incluant des correctifs de sécurité pour `webpack-dev-server`, `postcss`, `pytest` et `urllib3`.
- Refactorisation de la gestion des variables d'environnement backend pour une meilleure organisation et cohérence.
- Utilisation de fichiers YAML pour la configuration des composants communs.
- Amélioration de la synchronisation des états de la configuration des salles.

### Autres changements
- Mise à jour de la documentation de l'API externe pour refléter le support de la configuration des salles.
- Correction de bugs mineurs liés à l'interface utilisateur, notamment le positionnement des tooltips et le recentrage de la barre de réactions.
- Suppression des buildpacks obsolètes et utilisation de `uv` pour la gestion des dépendances.
- Amélioration de la terminologie des rôles dans les localisations.
- Correction de problèmes liés aux URLs de la documentation Swagger et Redoc.
- Mise à jour de la version de la release à 1.17.0.
- Correction de la génération des IDs de salle pour une meilleure sécurité.
- Amélioration de la gestion des fontes pour l'accessibilité.
- Correction de bugs liés au support du format WebM.
- Correction de problèmes de boucle de reconnexion.
- Amélioration de la gestion des erreurs et de la robustesse du système.
- Correction de problèmes liés à l'affichage des enregistrements dans les emails.
- Ajout de tests pour le support du format WebM.
- Amélioration de la gestion des événements de transcription.
- Correction de problèmes liés à l'authentification des add-ons.
- Suppression de code inutile et amélioration de la lisibilité du code.
- Mise à jour de la documentation du changelog.
