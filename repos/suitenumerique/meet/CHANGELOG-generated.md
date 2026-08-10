## Changelog : meet (30 derniers jours, au 06 août 2026)

### Résumé
Ce mois-ci, Meet a franchi une étape importante dans la gestion des réunions en permettant aux organisateurs de modifier les rôles des participants en temps réel et en offrant une personnalisation accrue des paramètres de réunion par défaut. Une part majeure des développements a également été consacrée à l'optimisation des performances de l'interface utilisateur et à la stabilisation des services de transcription et de résumé.

### Évolutions fonctionnelles
- **Gestion des rôles** : Possibilité de promouvoir ou de rétrograder des participants en cours de réunion, avec notification automatique des changements de rôle.
- **Tests de connexion** : Ajout d'une fonctionnalité de diagnostic permettant de tester la qualité de la connexion et de vérifier les paramètres WebRTC.
- **Personnalisation des réunions** : Les utilisateurs peuvent désormais définir des préférences de configuration par défaut pour leurs liens de réunion générés.
- **Améliorations du SDK** : Introduction d'une fenêtre de configuration de réunion lors de la création et possibilité de personnaliser la couleur de fond de l'iframe calendrier.
- **Identification** : Ajout d'un badge pour identifier les participants non authentifiés.

### Évolutions techniques
- **Optimisation des performances** : Réduction massive des re-renders de l'interface via la mémoïsation de composants clés (Avatars, ParticipantTiles, boutons) et la virtualisation des messages du chat pour améliorer la fluidité.
- **Stabilité MediaPipe** : Amélioration de la gestion des assets MediaPipe (WASM) et du cache pour prévenir les crashs liés aux versions et optimiser le chargement.
- **Refactoring majeur** : Restructuration profonde du module de chat et de la gestion des composants de la liste de participants pour une meilleure maintenabilité.
- **Fiabilité des services** : Amélioration de la robustesse des services de transcription et de résumé (summary) grâce à une meilleure gestion des erreurs et des mécanismes de tentatives de reconnexion (retries).
- **Accessibilité** : Amélioration de la gestion du focus lors de l'ouverture et de la navigation dans les panneaux latéraux.

### Autres changements
- **Légal et conformité** : Mise à jour des conditions d'utilisation et ajout du fichier de métadonnées `publiccode.yml`.
- **Qualité de code** : Nettoyage de la dette technique (SonarCloud, linting) et optimisation de la configuration de la CI.
