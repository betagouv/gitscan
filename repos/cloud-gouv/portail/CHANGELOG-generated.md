## Changelog : portail (30 derniers jours)

### Résumé
Ce mois-ci, le portail a bénéficié d'améliorations significatives en matière de sécurité et de fonctionnalités réseau. L'ajout du support mTLS et de la redirection HTTP CONNECT renforce la sécurité et la flexibilité du proxy, permettant une meilleure intégration avec différents environnements.

### Évolutions fonctionnelles
- Ajout du support pour la redirection HTTP CONNECT, permettant de proxyfier des connexions HTTP standards [#30](https://github.com/cloud-gouv/portail/issues/30).
- Activation du support mTLS (mutual TLS) côté serveur pour une communication plus sécurisée [#27](https://github.com/cloud-gouv/portail/issues/27).

### Évolutions techniques
- Initialisation des tests E2E pour la connexion via le proxy.
- Passage de la configuration du backend par défaut via les paramètres.

### Autres changements
- Ajout du fichier de configuration Renovate (`renovate.json`).
- Mise à jour de l'action `samueldr/lix-gha-installer-action`.
