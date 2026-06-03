## Changelog : meet (30 derniers jours, au 2026-06-02)

### Résumé
Les dernières mises à jour de Meet se concentrent sur l'amélioration de la gestion des utilisateurs, la correction de bugs et l'optimisation des performances, notamment au niveau du chargement des ressources frontend. De nouvelles fonctionnalités sont également introduites, comme la gestion du mutisme des participants basée sur la configuration de la salle et l'amélioration de la reconnaissance vocale avec l'assignation des intervenants.

### Évolutions fonctionnelles
- Ajout de la possibilité de configurer le mutisme des participants en fonction de la configuration de la salle.
- Amélioration de la reconnaissance vocale avec l'assignation des intervenants (speaker diarization).
- Prise en charge de tous les formats de fichiers audio/vidéo.
- Introduction d'une fonctionnalité Picture-in-Picture (PiP) pour les réunions, avec contrôle du volume, de la mise en sourdine et des options.
- Amélioration de l'accessibilité avec l'ajout d'options de personnalisation de la police.
- Ajout d'une synchronisation pour les mises à jour de la configuration de la salle.
- Possibilité de configurer l'encodage des enregistrements LiveKit Egress.
- Support de l'assignation des intervenants dans les résumés de réunion.

### Évolutions techniques
- Refactorisation du code frontend pour améliorer le code splitting et réduire la taille des bundles JavaScript.
- Optimisation du chargement des dépendances frontend (lazy loading, isolation des composants).
- Utilisation de `uv` pour la gestion des dépendances dans les agents et le backend.
- Amélioration de la gestion des erreurs et de la robustesse du processus d'enregistrement.
- Refactorisation de la gestion des variables d'environnement pour une meilleure organisation et cohérence.
- Mise à jour des dépendances (webpack-dev-server, postcss, pytest, django, urllib3) pour corriger des failles de sécurité et bénéficier des dernières améliorations.
- Ajout de tests pour la couverture du code backend.
- Correction de problèmes de concurrence lors de la création d'utilisateurs.
- Ajout d'une commande de gestion pour fusionner les utilisateurs en double.
- Amélioration de la validation de la configuration des salles avec Pydantic.
- Ajout de la gestion des logs.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et configurations.
- Amélioration des messages de log pour faciliter le débogage.
- Correction de la documentation des URLs Swagger et Redoc.
- Ajout d'une commande Kubernetes pour la fusion des utilisateurs en double.
- Mise à jour du chart Helm pour la version 0.0.22.
- Amélioration de la gestion des variables d'environnement pour le développement.
- Correction de la génération des IDs de salle pour plus de sécurité.
- Ajout d'une gestion des erreurs pour l'échange de tokens d'application.
- Suppression de buildpack requirements.txt pour utiliser uv.lock.
- Amélioration de la gestion des erreurs lors de l'enregistrement.
- Correction de l'affichage des titres de page dans la fenêtre PiP.
- Correction de bugs d'affichage et de positionnement dans l'interface utilisateur.
- Correction de bugs liés à la barre d'outils de réaction.
- Correction de bugs liés à la barre de contrôle mobile.
- Amélioration de la terminologie des rôles dans les localisations.
- Ajout de la gestion des fichiers SVG optimisés.
- Ajout d'une synchronisation pour les mises à jour du niveau d'accès au lobby.
