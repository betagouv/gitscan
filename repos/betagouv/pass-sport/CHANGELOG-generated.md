## Changelog : pass-sport (30 derniers jours, au 04 août 2026)

### Résumé
Les récentes évolutions se sont concentrées sur le renforcement de la sécurité de la plateforme et l'amélioration de sa stabilité technique. L'accent a été mis sur la protection contre les accès automatisés malveillants et la garantie d'un service disponible en permanence, sans interruption lors des mises à jour.

### Évolutions fonctionnelles
- Correction d'un bug lors de l'analyse des données du formulaire de contact [#518](https://github.com/betagouv/pass-sport/pull/518).

### Évolutions techniques
- **Sécurité (WAF)** : Activation et configuration du pare-feu applicatif (WAF) sur l'infrastructure de production pour filtrer les robots et bloquer le trafic non pertinent [#514](https://github.com/betagouv/pass-sport/pull/514), [#516](https://github.com/betagouv/pass-sport/pull/516).
- **Disponibilité et Infrastructure** : 
    - Optimisation du déploiement pour assurer une continuité de service sans interruption (zéro downtime) [#508](https://github.com/betagouv/pass-sport/pull/508).
    - Ajustements des configurations réseau (ports et interfaces) pour améliorer la connectivité [#507](https://github.com/betagouv/pass-sport/pull/507), [#513](https://github.com/betagouv/pass-sport/pull/513).
- **Routage et Performance** : 
    - Amélioration de la gestion du trafic via le routeur, incluant une meilleure gestion des pics de requêtes (burst limit) et une refactorisation de la configuration.
- **CI/CD** : Mise à jour des tests de configuration Nginx et des variables d'environnement pour fiabiliser les processus de déploiement.
