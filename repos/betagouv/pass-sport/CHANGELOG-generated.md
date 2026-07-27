## Changelog : pass-sport (30 derniers jours, au 23 juillet 2026)

### Résumé
Ce changelog fait état d'améliorations significatives concernant le déploiement et la configuration de l'application en production. Les modifications se concentrent sur l'optimisation de la disponibilité et de la sécurité de l'application, notamment via l'ajout d'un Web Application Firewall (WAF) et l'amélioration de la gestion des processus.

### Évolutions fonctionnelles
Aucune évolution fonctionnelle visible pour les utilisateurs n'a été apportée durant cette période.

### Évolutions techniques
- **Déploiement & Infrastructure:** Configuration du Web Application Firewall (WAF) en production pour renforcer la sécurité de l'application. [#516](https://github.com/betagouv/pass-sport/issues/516) et [#514](https://github.com/betagouv/pass-sport/issues/514)
- **Procfile:** Modification du `Procfile` pour lancer deux processus afin de minimiser les interruptions de service lors des déploiements. [#508](https://github.com/betagouv/pass-sport/issues/508)
- **Procfile:** Configuration de l'application pour écouter sur toutes les interfaces réseau. [#507](https://github.com/betagouv/pass-sport/issues/507)
- **Port:** Correction de la configuration du port d'écoute de l'application. [#513](https://github.com/betagouv/pass-sport/issues/513), [#511](https://github.com/betagouv/pass-sport/issues/511), [#510](https://github.com/betagouv/pass-sport/issues/510), [#509](https://github.com/betagouv/pass-sport/issues/509)
- **Production:** Diverses mises à jour de configuration pour l'environnement de production. [#512](https://github.com/betagouv/pass-sport/issues/512)
