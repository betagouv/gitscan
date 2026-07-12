## Changelog : bal (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations concernant l'ingestion de données DECA, la gestion des identifiants, et la sécurité des secrets. Des migrations d'infrastructure ont également été réalisées pour les environnements de production et de recette.

### Évolutions fonctionnelles
- Mise à jour de l'ingestion des données DECA, dans le cadre de la tâche LBA-4953. [#527](https://github.com/mission-apprentissage/bal/issues/527)
- Mise à jour des identifiants DECA. [#528](https://github.com/mission-apprentissage/bal/issues/528)
- Correction de la conversion du code motif de rupture. [#529](https://github.com/mission-apprentissage/bal/issues/529)

### Évolutions techniques
- Migration du serveur BAL de production. [#525](https://github.com/mission-apprentissage/bal/issues/525)
- Migration du serveur BAL de recette. [#523](https://github.com/mission-apprentissage/bal/issues/523)
- Rotation du secret principal SOPS pour renforcer la sécurité. [#526](https://github.com/mission-apprentissage/bal/issues/526)
- Suppression des sous-modules `.infra/authorizations` et `.infra/inventories`. [#522](https://github.com/mission-apprentissage/bal/issues/522)

### Autres changements
- Correction de quelques fautes de frappe. [#524](https://github.com/mission-apprentissage/bal/issues/524)
