## Changelog : portail (30 derniers jours, au 2026-06-10)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout de fonctionnalités au serveur RPC et au proxy, permettant une gestion plus flexible des backends et des routes. Ces changements visent à améliorer la configuration et l'utilisation du portail dans différents environnements.

### Évolutions fonctionnelles
- Ajout de la fonctionnalité `ListBackends` au serveur RPC, permettant de lister les backends disponibles.
- Possibilité de définir un backend par défaut nul via `SetDefaultBackend` dans l'interface RPC/Varlink.
- Introduction de l'option `route.local` dans la configuration du proxy ACL, offrant un contrôle plus précis sur le routage.

### Évolutions techniques
- Refonte des dépendances pour utiliser `rustls-pki-types` et `toml` avec des contraintes de version plus larges, améliorant la compatibilité et la flexibilité.
- Simplification de la gestion des dépendances en supprimant `peekable`.

### Autres changements
- Aucune information supplémentaire disponible.
