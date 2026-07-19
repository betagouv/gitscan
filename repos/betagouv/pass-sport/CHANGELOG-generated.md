## Changelog : pass-sport (30 derniers jours, au 17 juillet 2026)

### Résumé
Ce changelog présente les récentes améliorations apportées à Pass'Sport, axées sur la préparation du déploiement en production et la correction de problèmes liés au port d'écoute de l'application. Ces modifications visent à assurer une meilleure disponibilité et un fonctionnement optimal du service.

### Évolutions fonctionnelles
- Correction de problèmes liés au port d'écoute de l'application pour garantir son bon fonctionnement. [#507](https://github.com/betagouv/pass-sport/issues/507), [#508](https://github.com/betagouv/pass-sport/issues/508), [#509](https://github.com/betagouv/pass-sport/issues/509), [#510](https://github.com/betagouv/pass-sport/issues/510), [#511](https://github.com/betagouv/pass-sport/issues/511)
- Préparation du déploiement en production avec des mises à jour spécifiques. [#512](https://github.com/betagouv/pass-sport/issues/512)

### Évolutions techniques
- Modification du `Procfile` pour lancer deux processus afin de minimiser les interruptions de service lors des déploiements. [#508](https://github.com/betagouv/pass-sport/issues/508)
- Configuration de l'application pour qu'elle écoute sur toutes les interfaces réseau. [#507](https://github.com/betagouv/pass-sport/issues/507)
