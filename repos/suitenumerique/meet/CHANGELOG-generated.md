## Changelog : meet (30 derniers jours, au 07/10/2026)

### Résumé
Cette période a été marquée par une amélioration majeure de l'expérience de partage d'écran, incluant désormais des fonctions de zoom et de panoramique. Un effort conséquent a également été déployé pour renforcer la sécurité de l'application (correction de vulnérabilités et protection des secrets) et moderniser les outils de développement pour les contributeurs.

### Évolutions fonctionnelles
- **Partage d'écran** : Ajout de contrôles de zoom et de panoramique (via souris ou clavier) et amélioration de l'interface de la barre d'outils.
- **Accessibilité** : Amélioration de la navigation au clavier pour le zoom, de la pagination des participants et de la communication des états de chargement aux technologies d'assistance.
- **Expérience utilisateur** : 
    - Possibilité pour les visiteurs non connectés de démarrer une réunion.
    - Ajout d'un signal sonore lors de l'arrivée en salle d'attente.
    - Notifications d'alerte en cas de bascule de connexion sur le protocole TURN.
    - Clarification des messages et permissions concernant l'enregistrement vidéo.

### Évolutions techniques
- **Sécurité** : 
    - Hachage des secrets d'application en SHA-256 et protection contre la modification des identifiants clients dans l'administration.
    - Correction de nombreuses vulnérabilités critiques (CVE) sur Django, PyJWT, libssl et d'autres dépendances système.
    - Mise en place de limitations (throttling) pour la génération de liens de réunion et de quotas quotidiens pour la création de salles.
- **Infrastructure & Environnement de développement** :
    - Migration de la stack de développement vers Garage (remplacement de MinIO) et support de Podman en mode rootless.
    - Modernisation de la stack locale (Node 22, support Nix) et optimisation des images Docker.
    - Amélioration des déploiements Helm (support de `envFrom` et gestion des sondes de santé).
- **Backend & Performance** :
    - Optimisation des performances en réduisant les requêtes de domaine sur l'endpoint des tokens.
    - Automatisation de la purge des salles inactives via une tâche planifiée (cronjob).
    - Amélioration de la gestion des échecs d'enregistrement (LiveKit egress).
- **CI/CD & Qualité** :
    - Migration de la CI vers des workflows partagés et ajout de scans de vulnérabilités (Menshen).
    - Introduction de tests unitaires frontend avec Vitest.
- **Observabilité** : 
    - Renforcement de la confidentialité sur Sentry (redaction du contenu des réunions) et meilleur contrôle de l'échantillonnage des traces.

### Autres changements
- **Documentation** : Mise à jour des guides de migration (Brevo) et du fichier `UPGRADE.md`.
- **Nettoyage** : Suppression de vues API inutilisées, de templates GitHub obsolètes et de workflows Crowdin non utilisés.
