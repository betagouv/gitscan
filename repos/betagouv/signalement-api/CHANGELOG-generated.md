## Changelog : signalement-api (30 derniers jours)

### Résumé
Ce changelog présente les récentes améliorations apportées à l'API SignalConso. Les modifications concernent principalement l'optimisation de la gestion de la mémoire, la correction de bugs liés à la taille des fichiers uploadés et à l'export de données, ainsi que des ajustements pour améliorer la robustesse et la surveillance du système.

### Évolutions fonctionnelles
- Correction d'un problème où la limite de taille du corps de la requête était trop courte, empêchant l'envoi de certaines données. [#2011](https://github.com/betagouv/signalement-api/pull/2011)
- Correction du nom des fichiers exportés. [#2017](https://github.com/betagouv/signalement-api/pull/2017)
- Ajustement du seuil d'alerte pour les uploads de fichiers afin d'éviter des alertes intempestives. [#2012](https://github.com/betagouv/signalement-api/pull/2012)

### Évolutions techniques
- Limitation de la taille de la mémoire directe (direct memory) pour améliorer la stabilité et la performance de l'application. [#2023](https://github.com/betagouv/signalement-api/pull/2023), [#2015](https://github.com/betagouv/signalement-api/pull/2015), [#2019](https://github.com/betagouv/signalement-api/pull/2019)
- Ajout de la possibilité de configurer les options `-Xmx` et `-Xms` (taille maximale et initiale du heap) en production. [#2015](https://github.com/betagouv/signalement-api/pull/2015)
- Correction de problèmes de linting. [#2017](https://github.com/betagouv/signalement-api/pull/2017)
- Suppression des logs d'erreur inutiles en cas de non-paiement pour Social Blade. [#2013](https://github.com/betagouv/signalement-api/pull/2013)

### Autres changements
- Ignorer les alertes Albert lorsque la limite d'utilisation est atteinte. [#2011](https://github.com/betagouv/signalement-api/pull/2011)
- Limitation des arenas directes. [#2025](https://github.com/betagouv/signalement-api/pull/2025)
