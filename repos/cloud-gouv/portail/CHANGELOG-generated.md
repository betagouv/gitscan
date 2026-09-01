## Changelog : portail (30 derniers jours, au 14 août 2026)

### Résumé
Cette période a été marquée par un effort important de renforcement de la fiabilité et de la gestion opérationnelle du portail. Les évolutions se concentrent sur une meilleure gestion des journaux (logs), une résolution DNS plus rapide et une robustesse accrue du proxy face aux erreurs de connexion et aux configurations de sécurité complexes.

### Évolutions fonctionnelles
- **Gestion dynamique des logs** : Ajout d'une commande CLI `set-log-level` permettant de modifier le niveau de verbosité des journaux sans redémarrer le service.
- **Amélioration de la connectivité** : Implémentation de la résolution DNS interne et de l'algorithme "Happy Eyeballs v2" pour accélérer et fiabiliser l'établissement des connexions.
- **Maintenance simplifiée** : Support du rechargement des fichiers de logs via un signal SIGHUP, facilitant la rotation des fichiers sans interruption de service.

### Évolutions techniques
- **Routage et Protocoles** : 
    - Refactorisation majeure de la logique de routage backend pour les protocoles HTTP et SOCKS5.
    - Amélioration de la détection des protocoles, incluant désormais une extension pour le support TLS.
- **Sécurité et Résilience** :
    - Renforcement de l'évaluateur d'ACL pour prévenir les comportements anormaux liés à des règles complexes.
    - Durcissement de la gestion des connexions : ajout de timeouts pour les handshakes, gestion des erreurs de connexion transitoires et mise en place d'une limite de connexions simultanées.
    - Sécurisation des permissions des fichiers de logs (mode 0600) et validation stricte des sockets via systemd.
- **Optimisation du système de logging** : Création d'un nouveau composant de gestion des écritures de logs et intégration du support `logrotate` pour les utilisateurs NixOS.

### Autres changements
- **Documentation et Qualité du code** : Ajout de commentaires de sécurité sur les blocs `unsafe` et nettoyage du code pour supprimer les blocs non utilisés.
- **Build et Infrastructure** : 
    - Définition de la version minimale de Rust supportée (MSRV) et optimisation des profils de compilation pour la production.
    - Amélioration de la résilience des modules Nix/NixOS.
    - Nettoyage des fonctionnalités (features) disponibles.
