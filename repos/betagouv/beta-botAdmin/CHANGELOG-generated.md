## Changelog : beta-botAdmin (30 derniers jours, au 21 septembre 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration du processus d'invitation grâce à un nouveau mode simulation, l'ajout de la gestion des listes de membres et la résolution de problèmes de collision de mentions sur Matrix. L'intégration avec n8n a également été fiabilisée.

### Évolutions fonctionnelles
- Introduction du mode simulation (`--simuler`) pour les commandes d'invitation, permettant de tester le flux via n8n et d'identifier les invités.
- Amélioration de la commande d'invitation avec une gestion plus stricte des options (refus des options inconnues).
- Ajout de fonctionnalités liées à la gestion des listes de membres [#47](https://github.com/betagouv/beta-botAdmin/pull/47).
- Correction d'un problème de collision de mentions avec d'autres bots sur Matrix [#55](https://github.com/betagouv/beta-botAdmin/pull/55).

### Évolutions techniques
- Fiabilisation de l'intégration avec n8n : une réponse muette est désormais traitée comme un échec et non plus comme un succès.
- Application de correctifs via les pull requests [#12](https://github.com/betagouv/beta-botAdmin/pull/12) et [#54](https://github.com/betagouv/beta-botAdmin/pull/54).

### Autres changements
- Mise à jour de la documentation concernant les exemples d'utilisation de la commande `email`.
