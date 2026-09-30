## Changelog : portail (30 derniers jours, au 07/09/2026)

### Résumé
Cette période a été marquée par un effort majeur sur la documentation, l'internationalisation et l'observabilité du système. Le portail permet désormais de suivre en temps réel certains événements système, facilitant ainsi le diagnostic des erreurs de connexion sécurisée.

### Évolutions fonctionnelles
- Ajout de la possibilité de s'abonner aux événements via l'interface en ligne de commande (CLI).
- Notification des échecs de handshake TLS pour améliorer la visibilité sur les erreurs de connexion sécurisée.

### Évolutions techniques
- Implémentation de l'interface RPC `SubscribeEvents` via Varlink et le module de contrôle.
- Refactorisation de l'Eventbus vers le `ProxyRuntime`.
- Mise en place de l'infrastructure de documentation avec `mdbook` et intégration du packaging Nix.
- Ajustement des délais d'attente (timeouts) pour les tests de protocoles.

### Autres changements
- **Documentation** : Création d'un corpus complet incluant un guide de démarrage rapide, la référence de l'API, la configuration, une roadmap et un guide de contribution.
- **Internationalisation** : Initialisation du système de traduction et ajout du support pour la langue française.
- **Développement** : Ajout d'un environnement de développement via `shell.nix` et automatisation des workflows de documentation.
