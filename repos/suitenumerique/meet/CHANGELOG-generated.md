## Changelog : meet (30 derniers jours, au 19 septembre 2026)

### Résumé
Ce mois-ci a été marqué par la sortie de la version 1.31.0. Les utilisateurs bénéficient d'une qualité vidéo améliorée avec l'option 1080p, d'une interface mobile plus ergonomique et de l'ajout de la langue espagnole. Parallèlement, l'infrastructure de développement et la sécurité des pipelines ont été considérablement renforcées pour garantir une plateforme plus stable et robuste.

### Évolutions fonctionnelles
- **Qualité vidéo** : Ajout d'une option de résolution d'envoi en 1080p et meilleure gestion de la résolution lors de la désactivation de la caméra.
- **Gestion des réunions et du lobby** : 
    - Tri des participants en salle d'attente par ordre d'arrivée.
    - Ajout de notifications sonores lors de l'arrivée de nouveaux participants.
    - Possibilité pour les utilisateurs authentifiés de gérer le lobby dans les salles de confiance.
- **Interface et Accessibilité** :
    - Amélioration de la réactivité de l'interface sur mobile (boutons et barre de contrôle).
    - Support de la touche `Échap` pour fermer les panneaux latéraux.
    - Clarification de la terminologie liée à l'enregistrement vidéo.
- **Intelligence Artificielle** : Support du moteur d'inférence Voxtral en temps réel pour les agents.
- **Internationalisation** : Ajout du support complet pour la langue espagnole.

### Évolutions techniques
- **Performance et Optimisation** :
    - Refactorisation de la gestion du cache (présence et lobby) pour optimiser les recherches de clés dans Redis.
    - Chargement différé de certains scripts tiers (Crisp) pour améliorer le temps de chargement initial.
    - Optimisation de l'intervalle de rafraîchissement du lobby.
- **Sécurité et CI/CD** :
    - Durcissement des pipelines de CI (ancrage des actions sur des hashs de commit, utilisation de `uv` pour la gestion des dépendances).
    - Correction de vulnérabilités critiques (CVE) dans les images de base.
    - Mise à jour du serveur LiveKit.
- **Expérience Développeur (DevX)** :
    - Introduction d'outils de diagnostic pour WebRTC et le throttling réseau.
    - Support de Podman en mode "rootless" pour le développement local.
    - Ajout d'un environnement de développement (devenv shell) basé sur Nix.
- **Infrastructure** : Support de Traefik pour l'authentification média et mise à jour des images MinIO.

### Autres changements
- **Documentation** : Mise à jour de la documentation de montée de version (`UPGRADE.md`).
- **Localisation** : Amélioration des traductions au niveau du backend.
- **Maintenance** : Nettoyage de la configuration CI (renommage de fichiers) et suppression de wrappers de composition inutilisés.
