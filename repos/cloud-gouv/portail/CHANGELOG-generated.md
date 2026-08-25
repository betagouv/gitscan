## Changelog : portail (30 derniers jours, au 14 août 2026)

### Résumé
Cette période a été marquée par un travail intensif sur la robustesse, la sécurité et l'observabilité du proxy. Les évolutions majeures concernent l'amélioration de la gestion des journaux (logs), l'optimisation de la résolution DNS et le durcissement des mécanismes de sécurité pour garantir un service plus stable et plus facile à administrer.

### Évolutions fonctionnelles
- **Gestion des logs** : Ajout d'une commande CLI `set-log-level` permettant de modifier dynamiquement le niveau de verbosité sans redémarrer le service.
- **Performance DNS** : Amélioration de la réactivité de la résolution DNS via l'implémentation de l'algorithme "Happy Eyeballs v2" et l'ajout de la résolution DNS en interne.
- **Fiabilité des connexions** : Introduction de timeouts pour les phases de handshake et mise en place d'une limite de connexions simultanées pour prévenir la saturation.
- **Sécurité des protocoles** : Renforcement de la validation des requêtes HTTP (normalisation des ports et rejet des formats CONNECT non conformes) et extension de la détection de protocole au TLS.

### Évolutions techniques
- **Observabilité & Logs** : 
    - Support du rechargement dynamique des fichiers de logs (via SIGHUP).
    - Intégration du support `logrotate` pour les modules NixOS.
    - Sécurisation des permissions des fichiers de logs (mode 0600).
- **Architecture & Routage** : Refactorisation et initialisation de la logique de routage vers les backends pour les protocoles HTTP et SOCKS5.
- **Sécurité & Robustesse** :
    - Durcissement de l'évaluateur d'ACL pour prévenir les comportements pathologiques.
    - Amélioration de la gestion des erreurs pour éliminer les risques de panique (crash) du processus.
    - Sécurisation de la gestion des descripteurs de fichiers (FD) via systemd et utilisation de RAII.
- **Build & Infrastructure** : 
    - Définition de la version minimale de Rust supportée (MSRV) et optimisation du profil de release.
    - Amélioration de la résilience des modules Nix.

### Autres changements
- **Documentation** : Ajout de commentaires de sécurité (`SAFETY`) sur les blocs de code critiques et nettoyage des blocs `unsafe`.
- **Tests** : Correction des tests de connexion SOCKS5 pour les scénarios multi-backends.
