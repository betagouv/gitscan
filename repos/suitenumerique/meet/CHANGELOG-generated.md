## Changelog : meet (30 derniers jours, au 04/10/2026)

### Résumé
Ce mois-ci, meet a franchi une étape importante avec l'introduction de fonctionnalités de zoom et de panoramique lors du partage d'écran, rendant la collaboration plus précise. La sécurité a été renforcée par une campagne massive de correction de vulnérabilités et une meilleure protection des données de réunion. Enfin, l'infrastructure et l'expérience de développement ont été modernisées pour offrir plus de stabilité et de flexibilité.

### Évolutions fonctionnelles
- **Partage d'écran amélioré** : Ajout de contrôles de zoom et de panoramique (pan) avec support de la molette de la souris, des raccourcis clavier et d'une interface dédiée.
- **Nouvelles capacités de réunion** : Les visiteurs non connectés peuvent désormais démarrer une réunion.
- **Expérience utilisateur (UX) et Interface (UI)** :
    - Ajout de notifications sonores lors de l'arrivée de participants en salle d'attente.
    - Alertes visuelles en cas de basculement de la connexion vers le protocole TURN.
    - Meilleure clarté sur l'état de l'enregistrement vidéo et les délais d'attente.
    - Tri des participants en salle d'attente par heure d'arrivée.
    - Améliorations esthétiques des boutons de feedback, des icônes de plein écran et de l'affichage des avatars.
- **Accessibilité** :
    - Exposition de l'état de chargement aux technologies d'assistance.
    - Ajout de la navigation au clavier pour les outils de zoom du partage d'écran.
- **Corrections de bugs** :
    - Correction du comportement de la fonction "main levée" en mode image-dans-image (PiP).
    - Résolution de problèmes liés aux permissions de mode d'enregistrement et à la résolution de réception.
    - Correction de la gestion des échecs d'enregistrement (egresss LiveKit).

### Évolutions techniques
- **Sécurité renforcée** :
    - Correction de nombreuses vulnérabilités critiques (CVE) affectant Django, PyJWT, libssl, libexpat et d'autres composants système.
    - Mise en œuvre de la redirection des données sensibles (redaction) de Sentry pour protéger le contenu des réunions.
    - Limitation du débit (throttling) pour la génération de liens de réunion et plafonnement quotidien de la création de salles.
    - Rejet des utilisateurs inactifs sur le serveur de ressources.
- **Infrastructure et Déploiement** :
    - Migration du stockage local de MinIO vers Garage pour le développement et les services média.
    - Améliorations des charts Helm (support de `envFrom`, gestion des sondes de santé, automatisation du nettoyage des salles inactives via cronjob).
    - Migration de la CI vers des workflows partagés et ajout de scans de vulnérabilités (Menshen).
- **Optimisations Backend** :
    - Refactorisation de la gestion du cache de présence et du stockage de la salle pour limiter la consommation de ressources.
    - Remplacement du client MinIO par `boto3` pour une meilleure compatibilité S3.
- **Expérience Développeur (DevX)** :
    - Modernisation de la stack de développement (Node 22, support de Podman en mode rootless, support des environnements Nix).
    - Optimisation des images Docker et de la gestion de Redis.

### Autres changements
- **Documentation** : Mise à jour du README et documentation de la nouvelle procédure de purge des salles inactives.
- **Nettoyage** : Suppression de vues API et de workflows (Crowdin, templates GitHub) inutilisés.
