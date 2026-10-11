## Changelog : meet (30 derniers jours, au 11 octobre 2026)

### Résumé
Ce mois-ci, meet a franchi des étapes importantes pour améliorer l'expérience de partage d'écran grâce à l'ajout de fonctions de zoom et de panoramique. La sécurité a été une priorité absolue avec la correction de nombreuses vulnérabilités et le renforcement des mécanismes d'authentification. Enfin, l'accessibilité a été nettement améliorée pour offrir une meilleure expérience aux utilisateurs utilisant des technologies d'assistance.

### Évolutions fonctionnelles
- **Partage d'écran** : Ajout de fonctionnalités de zoom et de panoramique lors du partage d'écran, avec un support complet pour la molette de la souris et la navigation au clavier.
- **Accès aux réunions** : Les visiteurs non connectés peuvent désormais démarrer une réunion.
- **Enregistrements** : Possibilité de configurer l'encodage spécifiquement pour chaque enregistrement via l'API.
- **Accessibilité** : 
    - Amélioration de la navigation au clavier pour la pagination des participants et les contrôles de zoom.
    - Meilleure visibilité des états de chargement pour les technologies d'assistance.
    - Ajout de contours de focus visibles sur les éléments de menu.
- **Expérience utilisateur** : 
    - Notifications visuelles en cas de bascule de connexion vers le protocole TURN.
    - Amélioration de la gestion des sons de la salle d'attente et des infobulles.

### Évolutions techniques
- **Sécurité** : 
    - Correction massive de vulnérabilités critiques (CVE) sur diverses dépendances (Django, PyJWT, libssl, libpcre2, etc.).
    - Renforcement de la protection des données : hachage des secrets d'application en SHA-256 et limitation quotidienne de la création de salles.
    - Sécurisation du flux de la salle d'attente (lobby) en supprimant la dépendance aux cookies.
- **Authentification** : 
    - Introduction d'un point de terminaison d'échange de jetons pour faciliter l'intégration de meet dans des iframes.
    - Support de l'authentification alternative via les fragments d'URL.
- **Infrastructure & DevOps** : 
    - Migration de l'environnement de développement local vers Garage (en remplacement de MinIO).
    - Optimisation des déploiements Helm (support de `envFrom` et rendu des sondes de santé).
    - Migration de la CI vers des workflows GitHub Actions partagés et ajout de scans de vulnérabilités (Menshen).
    - Mise en place d'une tâche automatisée (cronjob) pour purger les salles inactives.
- **Performance & Tests** : 
    - Réduction des requêtes de domaine sur l'endpoint de jetons d'application.
    - Intégration de Vitest pour permettre l'exécution de tests unitaires sur le frontend.

### Autres changements
- **Documentation** : Mises à jour du README, du CHANGELOG et du guide de mise à niveau (UPGRADE.md).
- **Nettoyage** : Suppression de logs de console inutiles et de composants API obsolètes.
