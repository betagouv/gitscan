## Changelog : monitoring-pinger (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les améliorations apportées au monitoring-pinger visent à rendre les alertes plus fiables et pertinentes. Nous avons notamment ajouté une gestion des tentatives en cas d'échec d'envoi de notification, et évité l'envoi de notifications non urgentes ainsi que les envois redondants. L'application est maintenant initialisée et prête à être utilisée.

### Évolutions fonctionnelles
- Les notifications sont maintenant retentées en cas d'échec d'envoi, améliorant la fiabilité des alertes. [#N/A](https://github.com/proconnect-gouv/monitoring-pinger/commit/e83bd67)
- Seules les alertes d'urgence sont désormais envoyées, réduisant le bruit et permettant de se concentrer sur les incidents critiques. [#N/A](https://github.com/proconnect-gouv/monitoring-pinger/commit/44d810e)
- Une notification n'est envoyée qu'une seule fois pour un même incident, évitant ainsi les alertes répétées. [#N/A](https://github.com/proconnect-gouv/monitoring-pinger/commit/95e9841)

### Évolutions techniques
- Initialisation du projet. [#N/A](https://github.com/proconnect-gouv/monitoring-pinger/commit/a80a686)
