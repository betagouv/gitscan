## Changelog : autometa-jobs (30 derniers jours, au 21/09/2026)

### Résumé
Cette période a été marquée par un renforcement de la sécurité des accès et une optimisation des processus de déploiement automatique pour garantir une meilleure fiabilité et une gestion plus fine des clients.

### Évolutions fonctionnelles
- Sécurisation de l'orchestrateur par l'introduction de clés d'accès (bearer keys) spécifiques à chaque client via la configuration `PIPOMETA_EXTRA_API_KEYS` [#79](https://github.com/gip-inclusion/autometa-jobs/pull/79).

### Évolutions techniques
- Automatisation du pipeline CI/CD incluant le build, le push et le redéploiement automatique lors des mises à jour de la branche principale [#81](https://github.com/gip-inclusion/autometa-jobs/pull/81).
- Optimisation de la gestion des dépendances et de la construction du projet grâce à l'adoption de `uv` pour le verrouillage des environnements [#80](https://github.com/gip-inclusion/autometa-jobs/pull/80).
