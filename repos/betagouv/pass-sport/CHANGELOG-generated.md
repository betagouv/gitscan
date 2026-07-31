## Changelog : pass-sport (30 derniers jours, au 27 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité et la performance de l'application en production. Des corrections ont été apportées pour assurer un fonctionnement fluide, notamment concernant la configuration du serveur web et la gestion des processus. Une correction de bug a également été implémentée pour le parsing des données de contact.

### Évolutions fonctionnelles
- Correction d'un bug empêchant l'analyse correcte des données de contact [#518](https://github.com/betagouv/pass-sport/issues/518).

### Évolutions techniques
- Activation de la configuration WAF (Web Application Firewall) sur le proxy Nginx en production [#516](https://github.com/betagouv/pass-sport/issues/516) et [#514](https://github.com/betagouv/pass-sport/issues/514).
- Correction et stabilisation de la configuration du port d'écoute de l'application [#513](https://github.com/betagouv/pass-sport/issues/513), [#511](https://github.com/betagouv/pass-sport/issues/511), [#512](https://github.com/betagouv/pass-sport/issues/512), [#510](https://github.com/betagouv/pass-sport/issues/510), [#509](https://github.com/betagouv/pass-sport/issues/509).
- Modification du Procfile pour lancer 2 processus afin de minimiser les interruptions de service lors des déploiements [#508](https://github.com/betagouv/pass-sport/issues/508).
- Configuration du Procfile pour écouter sur toutes les interfaces réseau [#507](https://github.com/betagouv/pass-sport/issues/507).
