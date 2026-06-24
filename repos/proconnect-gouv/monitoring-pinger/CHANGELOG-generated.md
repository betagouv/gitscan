## Changelog : monitoring-pinger (30 derniers jours, au 22 juin 2026)

### Résumé
Cette mise à jour améliore la gestion des alertes envoyées par le service de monitoring.  Le système évite désormais de renvoyer des notifications déjà traitées et ne transmet les messages que si l'incident est considéré comme une urgence, réduisant ainsi le bruit et améliorant la pertinence des alertes reçues par l'équipe ProConnect.

### Évolutions fonctionnelles
- Le service ne renvoie plus les mêmes notifications une seconde fois [#95e9841](https://github.com/proconnect-gouv/monitoring-pinger/commit/95e9841).
- Seules les alertes d'urgence sont désormais transmises [#44d810e](https://github.com/proconnect-gouv/monitoring-pinger/commit/44d810e).

### Évolutions techniques
- Initialisation du projet [#a80a686](https://github.com/proconnect-gouv/monitoring-pinger/commit/a80a686).
