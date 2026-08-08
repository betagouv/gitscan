## Changelog : portail (30 derniers jours, au 07 août 2026)

### Résumé
Cette période a été marquée par un effort important de sécurisation et de stabilisation du proxy. Les développements se sont concentrés sur le renforcement de la robustesse du moteur de règles (ACL), l'amélioration des performances de connexion réseau et la fiabilisation de l'infrastructure de déploiement.

### Évolutions fonctionnelles
- Ajout de la résolution DNS interne pour améliorer la réactivité du service.

### Évolutions techniques
- **Sécurité et Robustesse** :
    - Renforcement de l'évaluateur d'ACL pour prévenir les comportements anormaux.
    - Sécurisation des permissions des fichiers de logs (mode 0600).
    - Réduction de la surface d'attaque par la suppression et la sécurisation des blocs de code non sécurisés (*unsafe*).
    - Injection du contexte d'authentification client dans l'évaluation des ACL pour distinguer le trafic TLS du trafic en clair.
- **Réseau et Performance** :
    - Implémentation de l'algorithme *Happy Eyeballs v2* pour optimiser la résolution DNS.
    - Ajout de timeouts pour les phases de handshake et renommage des timeouts de requête pour plus de clarté.
    - Amélioration de la gestion des connexions : ajout d'un plafond de connexions et gestion des erreurs de connexion transitoires.
    - Normalisation des ports et rejet des formats de requêtes HTTP CONNECT non conformes.
- **Infrastructure et Système** :
    - Amélioration de la résilience des modules Nix.
    - Optimisation de la gestion des sockets via systemd et utilisation de RAII pour la gestion des descripteurs de fichiers.
    - Mise à jour de la configuration de build (MSRV, profils de release et gestion des fonctionnalités).

### Autres changements
- **Documentation** : Ajout de commentaires de sécurité obligatoires sur tous les blocs de code critiques.
- **Tests** : Correction de tests de connexion SOCKS5.
- **CI/CD** : Initialisation de la gestion automatisée des dépendances via Renovate.
