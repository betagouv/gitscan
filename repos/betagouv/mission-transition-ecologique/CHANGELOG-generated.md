## Changelog : mission-transition-ecologique (30 derniers jours, au 26 octobre 2026)

### Résumé
Les récentes mises à jour renforcent la fiabilité de l'envoi des données vers la plateforme "Place des Entreprises" et améliorent les outils de surveillance technique pour permettre une détection et une résolution plus rapides des erreurs.

### Évolutions fonctionnelles
- Amélioration de la transmission des données vers "Place des Entreprises" : inclusion de l'identifiant de thématique des demandes [#2686](https://github.com/betagouv/mission-transition-ecologique/issues/2686) et ajustement du délai d'envoi pour garantir la stabilité des échanges [#2690](https://github.com/betagouv/mission-transition-ecologique/issues/2690).

### Évolutions techniques
- Observabilité et débogage : mise en place du suivi des échecs de transmission vers "Place des Entreprises" dans Sentry [#2687](https://github.com/betagouv/mission-transition-ecologique/issues/2687) et correction de l'envoi des source maps serveur pour faciliter l'analyse des erreurs [#2689](https://github.com/betagouv/mission-transition-ecologique/issues/2689).
- API : exposition de la documentation OpenAPI sur l'environnement de préproduction [#2685](https://github.com/betagouv/mission-transition-ecologique/issues/2685).
