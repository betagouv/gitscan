## Changelog : mission-transition-ecologique (30 derniers jours, au 02 novembre 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de la fiabilité des échanges de données avec la plateforme "Place des Entreprises" et sur le renforcement du suivi technique pour garantir une meilleure stabilité et une meilleure visibilité des erreurs du service.

### Évolutions fonctionnelles
- Mise à jour des données relatives aux programmes et aux projets [#2684](https://github.com/betagouv/mission-transition-ecologique/issues/2684), [#2683](https://github.com/betagouv/mission-transition-ecologique/issues/2683).
- Amélioration de la précision des données transmises en incluant l'identifiant de thématique des demandes [#2686](https://github.com/betagouv/mission-transition-ecologique/issues/2686).

### Évolutions techniques
- **API & Documentation** : Exposition de la documentation OpenAPI sur l'environnement de préproduction pour faciliter l'intégration [#2685](https://github.com/betagouv/mission-transition-ecologique/issues/2685).
- **Observabilité & Monitoring** :
    - Mise en place du suivi des échecs de transmission vers "Place des Entreprises" via Sentry [#2687](https://github.com/betagouv/mission-transition-ecologique/issues/2687).
    - Optimisation de la remontée des *source maps* serveur pour améliorer la précision du débogage [#2689](https://github.com/betagouv/mission-transition-ecologique/issues/2689).
- **Fiabilité des échanges** : Ajustement du délai d'envoi vers "Place des Entreprises" à 10 secondes pour stabiliser les processus de transmission [#2690](https://github.com/betagouv/mission-transition-ecologique/issues/2690).
