## Changelog : mirai-mesreunions (30 derniers jours, au 29 août 2026)

### Résumé
Ce mois-ci, le projet s'est concentré sur la stabilisation de l'expérience utilisateur de la version bêta et sur une modernisation majeure de l'infrastructure de déploiement. Les utilisateurs bénéficieront d'une interface plus cohérente et d'une meilleure fiabilité lors des imports de contenus, tandis que l'équipe technique a optimisé les processus de construction pour une intégration plus fluide au sein du cluster.

### Évolutions fonctionnelles
- **Amélioration de l'interface utilisateur** : Intégration d'un menu commun pour la version bêta, incluant la gestion du profil utilisateur et la fonction de déconnexion.
- **Fiabilisation des imports YouTube** : Les détections anti-bot ne bloquent plus l'importation ; le système tente désormais automatiquement de nouvelles tentatives (retry) pour assurer la continuité du processus.
- **Correction de l'authentification** : Résolution d'un problème de boucle de connexion lié à la gestion des jetons OIDC dans les cookies.

### Évolutions techniques
- **Modernisation de la CI/CD** : Migration du processus de construction (build) directement dans le cluster via BuildKit rootless, supprimant la dépendance aux machines virtuelles (VM) externes.
- **Optimisation de la robustesse du service** : Amélioration de la gestion du démarrage du service web pour éviter les conflits lors de l'initialisation de la base de données entre plusieurs instances (replicas).
- **Maintenance de la chaîne de build** : Correction de plusieurs bugs dans les scripts de construction (gestion des destinations d'images, des variables et de la détection du cluster).
- **Optimisation des logs** : Réduction du bruit dans les journaux du composant "bridge" en limitant les messages répétitifs liés aux connexions AMQP.
