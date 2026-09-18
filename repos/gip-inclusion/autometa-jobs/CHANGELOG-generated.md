## Changelog : autometa-jobs (30 derniers jours, au 09/09/2026)

### Résumé
Les récentes évolutions se concentrent sur le renforcement de la sécurité des accès et l'automatisation complète du cycle de déploiement, garantissant une plateforme plus stable et une meilleure isolation des clients.

### Évolutions fonctionnelles
- Amélioration de la gestion de l'authentification permettant l'utilisation de clés "bearer" spécifiques par client via la configuration `PIPOMETA_EXTRA_API_KEYS` [#79](https://github.com/gip-inclusion/autometa-jobs/pull/79).

### Évolutions techniques
- Automatisation du pipeline CI/CD pour inclure le build, le push et le redéploiement automatique lors des mises à jour de la branche principale [#81](https://github.com/gip-inclusion/autometa-jobs/pull/81).
- Optimisation de la gestion des dépendances et de la reproductibilité des environnements grâce à l'adoption de l'outil `uv` [#80](https://github.com/gip-inclusion/autometa-jobs/pull/80).
- Mise à jour des bibliothèques critiques pour assurer la stabilité du système (alembic, uvicorn, scaleway et boto3).
