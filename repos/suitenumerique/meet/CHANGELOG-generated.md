## Changelog : meet (30 derniers jours, au 08/09/2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment via l'ajout de nouveaux outils de test audio, le support de la langue espagnole et une interface mobile optimisée. Parallèlement, des optimisations techniques majeures ont été apportées pour accroître les performances de la gestion des participants et renforcer la sécurité de la chaîne de déploiement.

### Évolutions fonctionnelles
- **Outils audio et vidéo** : 
    - Ajout d'une option de résolution d'envoi en 1080p [#1660](https://github.com/suitenumerique/meet/issues/1660).
    - Intégration d'une jauge de niveau pour le microphone et d'un testeur de son pour la sortie audio.
- **Interface et Accessibilité** :
    - Ajout du support de la langue espagnole.
    - Amélioration de l'ergonomie sur mobile (boutons empilés, barre de contrôle adaptative et meilleure réactivité des écrans de feedback).
    - Possibilité de fermer les panneaux latéraux avec la touche `Échap` [#1507](https://github.com/suitenumerique/meet/issues/1507).
- **Gestion des réunions** :
    - Les utilisateurs authentifiés peuvent désormais gérer la salle d'attente (lobby) dans les salles de confiance.
- **Intelligence Artificielle** :
    - Support du moteur d'inférence Voxtral en temps réel pour les agents.

### Évolutions techniques
- **Optimisations de performance** : 
    - Refactorisation de la gestion du cache de présence et du stockage de la salle d'attente pour limiter les recherches de clés par salle et optimiser les ressources.
    - Augmentation de l'intervalle de rafraîchissement (polling) du lobby.
- **Infrastructure et Sécurité** :
    - Support du proxy inverse Traefik pour l'authentification média [#1649](https://github.com/suitenumerique/meet/issues/1649).
    - Mise à jour du serveur LiveKit vers la version v1.13.6.
    - Renforcement de la sécurité de la CI/CD (utilisation de `uv` pour l'installation des dépendances et verrouillage des versions des actions GitHub).
- **Fiabilité et Observabilité** :
    - Amélioration de la télémétrie pour le suivi des erreurs de périphériques, de l'enregistrement et des diagnostics média.
    - Ajout d'outils de développement pour les statistiques WebRTC et le bridage réseau (network throttling).
- **Corrections** :
    - Résolution de nombreux bugs liés à la gestion des périphériques (caméra/micro), à l'affichage des avatars et à la synchronisation des préférences utilisateur [#1673](https://github.com/suitenumerique/meet/issues/1673).

### Autres changements
- **Documentation** : Mise à jour du guide de mise à niveau (`UPGRADE.md`) et corrections de la documentation technique.
- **Développement** : Configuration d'un serveur TURN sur la pile de développement locale LiveKit.
