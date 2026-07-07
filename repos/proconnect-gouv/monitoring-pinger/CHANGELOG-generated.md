## Changelog : monitoring-pinger (30 derniers jours, au 03 juillet 2026)

### Résumé
Ce mois-ci, l'application de monitoring a été améliorée pour éviter les notifications répétitives en cas d'incident, et pour ne notifier que les incidents critiques. Des mécanismes de relance ont été ajoutés pour garantir l'envoi des notifications, et la configuration du seuil de minutes pour les alertes est désormais plus flexible.

### Évolutions fonctionnelles
- Les notifications ne sont plus renvoyées si elles ont déjà été envoyées une fois [#95e9841](https://github.com/proconnect-gouv/monitoring-pinger/commit/95e9841).
- Seules les urgences sont désormais notifiées [#44d810e](https://github.com/proconnect-gouv/monitoring-pinger/commit/44d810e).
- Ajout d'une tentative de renvoi des notifications en cas d'échec initial [#e83bd67](https://github.com/proconnect-gouv/monitoring-pinger/commit/e83bd67).

### Évolutions techniques
- Le seuil de minutes pour les alertes est désormais configurable via une variable d'environnement [#837a246](https://github.com/proconnect-gouv/monitoring-pinger/commit/837a246).
- Ajout de logs pour faciliter le débogage [#837a246](https://github.com/proconnect-gouv/monitoring-pinger/commit/837a246).

### Autres changements
- Initialisation du projet [#a80a686](https://github.com/proconnect-gouv/monitoring-pinger/commit/a80a686).
