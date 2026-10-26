## Changelog : st-deploycenter (30 derniers jours, au 24 octobre 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de l'intégration avec ProConnect, offrant une meilleure visibilité sur l'état de synchronisation et les données des organisations (SIRET, fiches). Le projet a également renforcé la gestion des services via la possibilité de transférer des abonnements et a stabilisé les processus critiques liés à l'activation des domaines et à la gestion DNS.

### Évolutions fonctionnelles
- **Gestion des services** : 
    - Ajout de la fonctionnalité de transfert d'un abonnement d'un opérateur à un autre.
    - Correction des contrôles lors de la désactivation des services.
- **Amélioration de l'interface ProConnect** :
    - Ajout d'un statut "out-of-sync" pour les IDP ProConnect [#65](https://github.com/suitenumerique/st-deploycenter/issues/65).
    - Intégration des métadonnées (Fiche et SIRET) sur l'ensemble des lignes de données.
- **Sécurité et permissions** :
    - Introduction de la nouvelle permission `can_admin_operators`.
    - Extension de l'utilisation des clés d'API externes sur davantage de points de terminaison (endpoints) opérateurs.

### Évolutions techniques
- **Optimisation de ProConnect** :
    - Migration vers une API d'activation "domaine par domaine" pour plus de précision.
    - Mise en conformité avec le nouveau format YAML de prévalidation.
    - Amélioration de la résilience : gestion des timeouts d'activation, optimisation de la mémoire pour les tâches cron et mécanismes de rafraîchissement du cache DNS pour les appels API.
- **Gestion des domaines et DNS** :
    - Corrections sur le mapping des domaines et la vérification du cache DNS.
    - Amélioration des scripts de gestion des domaines.
