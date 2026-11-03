## Changelog : conversations (30 derniers jours, au 02/11/2026)

### Résumé
Ce mois-ci, les développements se sont concentrés sur la robustesse de l'expérience utilisateur, notamment pour rendre les échanges avec l'IA plus fluides lors de rechargements de page ou d'interruptions. Un effort majeur a également été porté sur la sécurité du système (correction de vulnérabilités) et la protection de la vie privée, tout en renforçant les outils de surveillance technique pour garantir la stabilité du service.

### Évolutions fonctionnelles
- **Amélioration de la continuité du chat** : l'interface gère désormais mieux les interruptions de réponse et les rechargements de page, permettant de conserver le contexte et d'afficher des notifications claires sur l'état des réponses.
- **Contrôle de l'IA** : ajout d'une limite de jetons (tokens) de sortie par message et amélioration de la gestion des contenus de type "liste" pour les appels non-streaming.
- **Gestion documentaire** : amélioration de la conservation des fichiers originaux lors de l'ajout de documents à une conversation.
- **Expérience utilisateur (UX)** : 
    - Clarification des messages lors du traitement de fichiers de projet.
    - Amélioration de la gestion de l'authentification pour les utilisateurs partageant une même adresse e-mail.
    - Meilleure compatibilité avec les navigateurs plus anciens.
    - Messages d'alerte affinés en cas de forte affluence.

### Évolutions techniques
- **Sécurité et Confidentialité** : 
    - Correction de nombreuses vulnérabilités (CVE) sur les dépendances critiques (authlib, pypdf, undici, zod, djangorestframework, etc.).
    - Renforcement de la protection des données : garantie qu'aucun prompt utilisateur n'est enregistré dans les logs ou la télémétrie.
- **Observabilité et Monitoring** : 
    - Mise en place de métriques Prometheus pour suivre l'utilisation des modèles, les flux de chat et les appels sortants.
    - Intégration de nouveaux moniteurs (ServiceMonitor/PodMonitor) via Helm.
    - Configuration ajustable du taux d'échantillonnage des traces Sentry.
- **Stabilité et Performance** : 
    - Ajout de timeouts pour les clients Redis et Celery.
    - Amélioration de l'intégrité des données en nettoyant les caractères spéciaux (NUL) avant la sauvegarde des conversations.
    - Migration des tâches périodiques vers Celery Beat.
- **Infrastructure et CI/CD** : 
    - Optimisation du cache Playwright dans les pipelines CI.
    - Mise à jour des configurations Helm (gestion du fichier robots.txt).
    - Amélioration de l'environnement de développement Docker (utilisation de mailcatcher et restriction des ports en localhost).

### Autres changements
- **Documentation** : ajout de la politique d'utilisation de l'IA, de la politique de contribution (PR) et des procédures de déploiement.
- **Internationalisation** : mise à jour des chaînes de traduction.
