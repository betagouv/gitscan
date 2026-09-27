## Changelog : autometa-jobs (30 derniers jours, au 25 septembre 2026)

### Résumé
Ce mois-ci, le projet a renforcé sa sécurité et automatisé ses processus de déploiement pour garantir une plus grande stabilité et une gestion des accès plus granulaire.

### Évolutions fonctionnelles
- Amélioration de la gestion des accès avec le support de clés d'authentification (bearer keys) spécifiques par client via la configuration `PIPOMETA_EXTRA_API_KEYS` [#79](https://github.com/gip-inclusion/autometa-jobs/pull/79).

### Évolutions techniques
- Automatisation du pipeline CI/CD : le build, le push et le redéploiement sont désormais déclenchés automatiquement sur la branche principale dès que les tests sont validés [#81](https://github.com/gip-inclusion/autometa-jobs/pull/81).
- Fiabilisation des environnements de build grâce à l'adoption de `uv` pour le verrouillage des dépendances [#80](https://github.com/gip-inclusion/autometa-jobs/pull/80).
