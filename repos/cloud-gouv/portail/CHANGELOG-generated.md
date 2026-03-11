## Changelog : portail (30 derniers jours)

### Résumé
Ce mois-ci, le portail a bénéficié d'améliorations significatives en matière de connectivité et de sécurité. L'ajout du support mTLS et de la connexion HTTP permet une plus grande flexibilité et une meilleure protection des accès. Des bases pour les tests end-to-end ont également été posées.

### Évolutions fonctionnelles
- Ajout du support pour les connexions HTTP via `http connect` [#30](https://github.com/cloud-gouv/portail/issues/30).
- Activation du support mTLS (mutual TLS) côté serveur pour une sécurité renforcée [#27](https://github.com/cloud-gouv/portail/issues/27).

### Évolutions techniques
- Initialisation des tests end-to-end (E2E) via le proxy.
- Le démon peut maintenant créer optionnellement les sockets proxy et RPC.
- Passage du backend par défaut depuis les paramètres de configuration.

### Autres changements
- Ajout du fichier de configuration Renovate pour la gestion automatique des dépendances.
- Mise à jour de l'action `samueldr/lix-gha-installer-action`.
