## Changelog : portail (30 derniers jours, au 14 août 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante en matière de robustesse et de sécurité. Les efforts se sont concentrés sur la fiabilisation du moteur de routage, l'optimisation de la résolution DNS et l'amélioration des outils d'administration, notamment pour la gestion simplifiée des journaux d'activité (logs).

### Évolutions fonctionnelles
- **Gestion des logs :** Ajout d'une commande CLI `set-log-level` permettant de modifier le niveau de verbosité des logs en temps réel sans redémarrer le service.
- **Administration :** Support de la rotation des fichiers de logs (logrotate) via le module NixOS et possibilité de recharger les fichiers de logs via un signal SIGHUP.

### Évolutions techniques
- **Routage et Protocoles :** 
    - Refonte majeure de la détection des protocoles, incluant désormais une extension au support TLS.
    - Factorisation et réorganisation de la logique de routage vers un nouveau composant dédié pour les flux HTTP et SOCKS5.
- **Sécurité et Résilience :**
    - Renforcement de l'évaluateur d'ACL pour prévenir les comportements anormaux ou malveillants.
    - Sécurisation des permissions des fichiers de logs (mode 0600).
    - Amélioration de la conformité du protocole HTTP (normalisation des ports et validation des requêtes CONNECT).
    - Réduction de la surface d'attaque par la suppression de blocs de code `unsafe` et une meilleure gestion des erreurs pour éviter les plantages (panics).
- **Performance et Stabilité :**
    - Implémentation de l'algorithme "Happy Eyeballs v2" et de la résolution DNS interne pour accélérer l'établissement des connexions.
    - Introduction de timeouts pour les phases de handshake et de requêtes, ainsi que de limites de connexions pour protéger le système contre la saturation.
- **Infrastructure :** Amélioration de la résilience des modules Nix/Systemd, notamment sur la gestion des sockets et des descripteurs de fichiers.

### Autres changements
- **Documentation :** Ajout de commentaires de sécurité sur l'utilisation des blocs `unsafe` dans le code Rust.
- **Build et CI :** Optimisation du processus de compilation (définition du MSRV, ajout de profils de release) et nettoyage des fonctionnalités de build.
- **Tests :** Corrections de tests sur les connexions SOCKS5 multi-backends.
