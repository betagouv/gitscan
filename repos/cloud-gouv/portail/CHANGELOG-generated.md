## Changelog : portail (30 derniers jours, au 07 septembre 2026)

### Résumé
Cette période a été marquée par une amélioration significative de la maturité du projet, notamment grâce à la mise en place d'une documentation complète et multilingue. Les capacités de surveillance ont été renforcées avec l'introduction d'un système d'événements, et la gestion des journaux (logs) est devenue plus flexible et robuste.

### Évolutions fonctionnelles
- **Gestion des logs** : Ajout d'une commande CLI permettant de modifier dynamiquement le niveau de verbosité des logs.
- **Surveillance et événements** : Possibilité de s'abonner aux événements du système via la ligne de commande (CLI) et le protocole RPC.
- **Sécurité** : Émission de notifications automatiques en cas d'échec de la négociation TLS (handshake).

### Évolutions techniques
- **Système d'événements** : Implémentation d'un bus d'événements et de nouvelles interfaces RPC (Varlink/Control) pour la gestion des notifications.
- **Réseau et Proxy** : Refonte de la détection de protocole (incluant l'extension au TLS) et refactorisation de la logique de routage pour les flux HTTP et SOCKS5.
- **Gestion des journaux** : Amélioration de la gestion des fichiers de logs avec support de la réouverture automatique via SIGHUP et intégration de `logrotate` pour les modules NixOS.
- **Infrastructure et Build** : Mise en place de `mdbook` pour la documentation, ajout du packaging Nix et de fichiers `shell.nix` pour l'environnement de développement.
- **Tests** : Augmentation des délais d'attente (timeouts) dans les tests de protocoles pour améliorer la stabilité.

### Autres changements
- **Documentation** : Création d'une documentation exhaustive (guide de démarrage rapide, référence API, roadmap et guide de contribution) disponible en anglais et en français.
- **Internationalisation (i18n)** : Initialisation du support multilingue et ajout des premières traductions françaises.
- **Nettoyage** : Suppression de code mort dans le module de l'analyse syntaxique (AST) des ACL.
