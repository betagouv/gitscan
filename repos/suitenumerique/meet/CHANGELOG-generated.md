## Changelog : meet (30 derniers jours, au 16 septembre 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de l'expérience utilisateur (nouvelle résolution vidéo, support de l'espagnol et ergonomie mobile) et sur un renforcement significatif de la sécurité et de la stabilité de l'infrastructure (optimisation des performances backend et durcissement des pipelines CI/CD).

### Évolutions fonctionnelles
- **Qualité vidéo et média** : Ajout de l'option de résolution 1080p [#1660](https://github.com/suitenumerique/meet/pull/1660), meilleure gestion des erreurs lors de l'utilisation des caméras et clarification des textes liés à l'enregistrement vidéo.
- **Gestion des réunions** : Les utilisateurs authentifiés peuvent désormais gérer le lobby dans les salles de confiance ; les participants en attente sont désormais triés par ordre d'arrivée.
- **Internationalisation et UX** : Ajout du support de la langue espagnole, interface plus naturelle et amélioration de la réactivité des écrans de feedback sur mobile.
- **Accessibilité** : Possibilité de fermer les panneaux latéraux avec la touche Échap et annonces vocales pour les indices de fermeture.

### Évolutions techniques
- **Performances et optimisation** : Refactoring du cache de présence et du stockage du lobby pour limiter les recherches de clés ; remplacement des commandes Redis bloquantes par des scans basés sur curseur.
- **Sécurité** : Renforcement de la validation des utilisateurs (rejet des utilisateurs inactifs, contrôle du nom d'affichage) et correction de vulnérabilités critiques dans `libexpat`.
- **Infrastructure et CI/CD** : Durcissement des workflows GitHub Actions (utilisation de `uv`, verrouillage des versions des actions, sécurisation des téléchargements) et migration des images MinIO vers `quay.io`.
- **Observabilité** : Amélioration du suivi des erreurs d'enregistrement, intégration des SIDs LiveKit dans l'analytics et meilleure gestion de la configuration Sentry.
- **Architecture** : Ajout du support de Traefik pour l'authentification média et support de l'agent Voxtral realtime.

### Autres changements
- **Documentation** : Mise à jour du guide de montée de version pour la v1.30.0.
- **Maintenance** : Nettoyage des logs pour réduire le bruit et optimisation de la configuration des outils de développement (WebRTC stats, TURN server local).
