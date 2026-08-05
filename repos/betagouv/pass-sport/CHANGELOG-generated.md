## Changelog : pass-sport (30 derniers jours, au 04/08/2026)

### Résumé
Les récentes évolutions se sont concentrées sur le renforcement de la sécurité et de la stabilité de la plateforme. L'intégration d'un pare-feu applicatif (WAF) permet de mieux protéger le service contre les robots, tandis que des améliorations de l'infrastructure garantissent des mises à jour sans interruption de service pour les utilisateurs.

### Évolutions fonctionnelles
- Correction d'un bug lié à l'analyse (parsing) des données JSON dans le formulaire de contact [#518](https://github.com/betagouv/pass-sport/issues/518).

### Évolutions techniques
- **Sécurité (WAF) :** Activation du pare-feu applicatif (WAF) sur le proxy de production [#514](https://github.com/betagouv/pass-sport/issues/514), [#516](https://github.com/betagouv/pass-sport/issues/516) et ajout de règles pour filtrer le trafic des bots et les requêtes PHP non sollicitées.
- **Infrastructure et Déploiement :**
    - Mise en place de déploiements sans interruption de service (zero downtime) via l'optimisation du `Procfile` [#508](https://github.com/betagouv/pass-sport/issues/508).
    - Ajustements techniques sur la gestion des interfaces réseau [#507](https://github.com/betagouv/pass-sport/issues/507) et mises à jour des configurations de ports et d'environnements [#509](https://github.com/betagouv/pass-sport/issues/509), [#510](https://github.com/betagouv/pass-sport/issues/510), [#511](https://github.com/betagouv/pass-sport/issues/511), [#512](https://github.com/betagouv/pass-sport/issues/512), [#513](https://github.com/betagouv/pass-sport/issues/513).
- **Routage et Performance :** Refactorisation du routeur pour une meilleure indépendance vis-à-vis des environnements et ajustement des limites de requêtes (rate limiting) pour stabiliser la navigation.
- **CI/CD :** Mise à jour des tests de configuration pour Nginx et les règles du WAF.
