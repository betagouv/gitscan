## Changelog : st-ansible (30 derniers jours, au 22 octobre 2026)

### Résumé
Cette période a été marquée par l'intégration de nouveaux services de gestion de fichiers et de transferts, ainsi que par l'introduction du rôle "conversations". Les capacités de messagerie ont été modernisées et la robustesse de l'infrastructure a été renforcée par l'ajout de nouveaux mécanismes de contrôle de santé des services.

### Évolutions fonctionnelles
- **Nouveaux services** : Ajout des applications `file-scanner` et `transfers`, incluant leur intégration complète avec les services d'antivirus.
- **Communication** : Introduction du nouveau rôle `conversations` et mise à jour de l'outil CLI pour supporter son déploiement.
- **Messagerie** : 
    - Modernisation du composant de messagerie avec l'ajout de `pymta` (remplaçant `mta-in`).
    - Possibilité d'utiliser `exav` comme moteur d'antivirus au sein de l'application MPA.

### Évolutions techniques
- **CLI & Déploiement** : 
    - Amélioration de la gestion des groupes d'hôtes hérités (legacy) et automatisation de la réparation du proxy SOCKS lors des montées de version.
    - Découplage des tests de réparation du proxy SOCKS pour une meilleure isolation.
- **Infrastructure & Réseau** : 
    - Support de Caddy en tant que façade (front-end) pour l'image `messages-keycloak`.
    - Optimisation du filtrage des messages via le déploiement de la configuration du classificateur Bayes pour Rspamd.
- **Observabilité** : Mise en place de tests de santé (healthchecks) pour les workers `file-scanner` (via Dramatiq) et pour les conteneurs Podman (exécution sans shell).

### Autres changements
- **Documentation** : Mise à jour de la documentation pour accompagner l'arrivée du rôle `conversations`.
