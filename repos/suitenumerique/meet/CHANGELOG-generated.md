## Changelog : meet (30 derniers jours, au 13 septembre 2026)

### Résumé
Ce mois-ci, meet a franchi une étape importante en améliorant l'expérience utilisateur, notamment via une meilleure ergonomie sur mobile et l'ajout du support de la langue espagnole. Les utilisateurs bénéficient désormais d'une option de haute qualité vidéo (1080p) et d'une gestion plus intuitive des salles. En parallèle, une attention particulière a été portée à la performance et à la sécurité, avec une optimisation de la gestion des participants et un renforcement des processus de déploiement.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités** :
  - Ajout d'une option de résolution d'envoi en 1080p [#1660].
  - Support de la langue espagnole.
  - Possibilité pour les utilisateurs authentifiés de gérer la salle (lobby) dans les salles de confiance.
  - Support du moteur d'inférence Voxtral en temps réel pour les agents.
- **Expérience utilisateur & Interface** :
  - **Optimisation mobile** : Amélioration de la réactivité des écrans de feedback et adaptation de la barre de contrôle et des boutons de modales pour les petits écrans.
  - **Accessibilité** : Possibilité de fermer les panneaux latéraux avec la touche Échap.
  - **Améliorations visuelles** : Ajustement de l'intensité du flou d'arrière-plan, centrage amélioré des initiales des avatars et alignement des boutons de feedback.
  - **Clarté** : Clarification de la terminologie concernant l'enregistrement vidéo.
- **Corrections** :
  - Résolution de bugs sur le champ de texte du chat.
  - Correction de la gestion des erreurs lors du partage d'écran et de l'utilisation des périphériques (Chrome/Windows/Firefox).
  - Correction de l'affichage des notifications de connexion.

### Évolutions techniques
- **Performance & Optimisation** :
  - Refonte de la gestion du cache de présence et du stockage du lobby pour limiter les recherches de clés par salle.
  - Remplacement des commandes Redis bloquantes (`KEYS`) par des scans basés sur un curseur (`SCAN`).
  - Ajustement des intervalles de rafraîchissement (polling) du lobby pour optimiser les ressources.
- **Sécurité & Robustesse** :
  - Correction de vulnérabilités critiques (CVE) dans les images de base.
  - Durcissement de la CI/CD : utilisation de `uv` pour l'installation des dépendances Python et verrouillage des versions des actions GitHub par hash de commit.
  - Renforcement de la sécurité du serveur de ressources avec le rejet des utilisateurs inactifs.
- **Infrastructure & Développement** :
  - Mise à jour du serveur LiveKit vers la version v1.13.6.
  - Ajout du support du reverse proxy Traefik pour l'authentification média [#1649].
  - Introduction de nouveaux outils de développement (DevX) : statistiques WebRTC et outil de limitation de bande passante réseau.
  - Configuration d'un serveur TURN pour l'environnement de développement local.
- **Observabilité** :
  - Amélioration du traçage et des logs (échantillonnage des traces, logs de durée des requêtes Gunicorn, enrichissement des événements analytics).

### Autres changements
- **Documentation** : Mise à jour de la documentation de montée de version (`UPGRADE.md`) et corrections de typos.
- **Internationalisation** : Amélioration globale des traductions du backend.
