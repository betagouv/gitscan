## Changelog : meet (30 derniers jours, au 18 septembre 2026)

### Résumé
Cette période a été marquée par une amélioration significative de l'expérience utilisateur, notamment grâce à l'ajout de la langue espagnole, une interface mobile optimisée et l'introduction de la résolution vidéo 1080p. Le projet a également renforcé sa robustesse technique avec des optimisations de performance (Redis, gestion des caches) et un durcissement des processus de déploiement et de sécurité.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités** :
    - Ajout du support de la langue espagnole.
    - Introduction d'une option de résolution d'envoi en 1080p.
    - Support du moteur d'inférence Voxtral en temps réel pour les agents.
    - Possibilité pour les utilisateurs authentifiés de gérer le lobby dans les salles de confiance.
- **Améliorations de l'expérience utilisateur** :
    - Optimisation de l'interface mobile (boutons empilés, barre de contrôle repliée, meilleure réactivité des écrans de feedback).
    - Amélioration de l'accessibilité : fermeture des panneaux latéraux avec la touche Échap et annonces sonores pour les arrivées en salle d'attente.
    - Clarification de la terminologie concernant l'enregistrement vidéo.
    - Tri des participants en salle d'attente par heure d'arrivée.
- **Corrections** :
    - Résolution de problèmes liés à l'utilisation des périphériques (caméra/micro) sur Chrome et Firefox.
    - Correction du comportement du champ de texte dans le chat.
    - Correction de l'affichage des initiales des avatars.

### Évolutions techniques
- **Performance et optimisation** :
    - Remplacement des requêtes Redis bloquantes par l'utilisation de `SCAN`.
    - Refactorisation des caches de présence et du stockage du lobby pour limiter les recherches par salle.
    - Chargement différé (lazy loading) du script Crisp pour améliorer le temps de chargement initial.
- **Sécurité et stabilité** :
    - Durcissement de la CI/CD : verrouillage des actions sur des hashs de commit complets et utilisation de `uv` pour la gestion des dépendances Python.
    - Correction de vulnérabilités critiques (CVE) dans les images de base.
    - Amélioration de la gestion des webhooks LiveKit pour éviter les erreurs 422.
    - Rejet des utilisateurs inactifs au niveau du serveur de ressources.
- **Expérience de développement (DevX) et Infrastructure** :
    - Support de Podman en mode "rootless" (sans privilèges root).
    - Ajout d'un environnement de développement basé sur Nix.
    - Mise en place d'outils de diagnostic WebRTC et de limitation de bande passante pour les tests locaux.
    - Support de Traefik pour l'authentification des médias.
    - Configuration d'un serveur TURN pour les environnements de développement locaux.

### Autres changements
- **Documentation** : Mise à jour du fichier `UPGRADE.md` pour documenter la version 1.30.0.
- **Internationalisation** : Amélioration et nettoyage des fichiers de traduction backend.
