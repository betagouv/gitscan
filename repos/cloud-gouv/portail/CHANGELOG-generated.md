## Changelog : portail (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion dynamique des backends, permettant une configuration plus flexible et réactive du portail.  De nouvelles fonctionnalités RPC ont été ajoutées pour lister et mettre à jour ces backends, et des corrections ont été apportées pour améliorer la robustesse et la clarté des messages d'erreur.

### Évolutions fonctionnelles
- Ajout de la possibilité de mettre à jour dynamiquement les backends via l'API RPC.
- Introduction d'une nouvelle API RPC `ListBackends` pour lister les backends configurés.
- Amélioration du message d'erreur "permission denied" pour une meilleure clarté.
- Possibilité de définir un backend par défaut nul via l'API RPC `SetDefaultBackend`.
- Ajout d'une option `route.local` dans la configuration du proxy ACL.

### Évolutions techniques
- Support des backends dynamiques au niveau du proxy.
- Refonte de la gestion des backends pour permettre leur affichage dynamique dans l'état du système.
- Mise à jour des tests d'intégration et tests E2E pour couvrir les nouvelles fonctionnalités RPC.
- Correction de typos dans les messages d'erreur RPC.
- Amélioration de la compatibilité multi-plateforme en ajustant le type de pointeur.
- Mise à jour de plusieurs dépendances : `insta`, `rand`, `toml`, `rustls-pki-types`, `zlink`.

### Autres changements
- Documentation mise à jour pour refléter les nouvelles fonctionnalités.
- Simplification des contraintes de version des dépendances pour une meilleure flexibilité.
