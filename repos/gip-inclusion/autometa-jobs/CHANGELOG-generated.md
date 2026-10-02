## Changelog : autometa-jobs (30 derniers jours, au 25 septembre 2026)

### Résumé
Les récentes évolutions se concentrent sur le renforcement de la sécurité et de la fiabilité du système. L'accent a été mis sur l'automatisation des processus de déploiement et une meilleure gestion des accès pour les clients, garantissant ainsi un environnement plus stable et sécurisé.

### Évolutions fonctionnelles
- Amélioration de la gestion de la sécurité avec la possibilité d'utiliser des clés Bearer spécifiques par client via la configuration `PIPOMETA_EXTRA_API_KEYS` ([#79](https://github.com/gip-inclusion/autometa-jobs/pull/79)).

### Évolutions techniques
- **CI/CD** : Automatisation complète du cycle de déploiement (build, push et redeployment) lors des mises à jour de la branche principale ([#81](https://github.com/gip-inclusion/autometa-jobs/pull/81)).
- **Build** : Optimisation de la gestion des dépendances et de la reproductibilité des environnements grâce à l'adoption de `uv` pour le verrouillage des dépendances ([#80](https://github.com/gip-inclusion/autometa-jobs/pull/80)).
