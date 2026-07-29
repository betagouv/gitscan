## Changelog : pass-sport (30 derniers jours, au 27 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilisation de l'infrastructure de production et la correction de bugs. Des ajustements ont été apportés à la configuration du serveur Nginx pour améliorer la sécurité et la disponibilité du service. Un correctif a également été implémenté pour résoudre un problème d'analyse JSON dans la gestion des contacts.

### Évolutions fonctionnelles
- Correction d'un bug empêchant l'analyse correcte des données JSON pour les contacts [#518](https://github.com/betagouv/pass-sport/issues/518).

### Évolutions techniques
- Activation de la configuration WAF (Web Application Firewall) sur le proxy Nginx en production [#516](https://github.com/betagouv/pass-sport/issues/516), [#514](https://github.com/betagouv/pass-sport/issues/514).
- Ajustements de la configuration du port pour la production [#513](https://github.com/betagouv/pass-sport/issues/513), [#512](https://github.com/betagouv/pass-sport/issues/512), [#510](https://github.com/betagouv/pass-sport/issues/510), [#509](https://github.com/betagouv/pass-sport/issues/509).
- Modification du Procfile pour lancer deux processus afin de minimiser les interruptions de service lors des déploiements [#508](https://github.com/betagouv/pass-sport/issues/508).
- Configuration du Procfile pour écouter sur toutes les interfaces réseau [#507](https://github.com/betagouv/pass-sport/issues/507).
