## Changelog : menshen (30 derniers jours, au 01 juillet 2026)

### Résumé
Ce mois-ci, le projet Menshen a connu des avancées significatives en termes de déploiement et de performance. L'ajout d'un chart Helm et de workflows de publication Docker simplifie le déploiement en Kubernetes. Des optimisations ont été apportées à la gestion des connexions PostgreSQL et à la génération de jetons, améliorant ainsi la réactivité et l'efficacité du serveur d'autorisation.

### Évolutions fonctionnelles
- Ajout des "grants" à la réponse de l'échange de jetons, offrant plus de flexibilité et d'informations aux clients.
- Suppression du "feature flag" `TOKEN_EXCHANGE_ENABLED`, activant définitivement la fonctionnalité d'échange de jetons.

### Évolutions techniques
- **Déploiement :**
    - Ajout d'un chart Helm pour faciliter le déploiement sur Kubernetes [#6f1dddc](https://github.com/suitenumerique/menshen/commit/6f1dddc).
    - Automatisation et documentation du développement basé sur Kubernetes [#7b027c6](https://github.com/suitenumerique/menshen/commit/7b027c6).
    - Ajout d'un workflow pour la publication des images Docker [#e6246c2](https://github.com/suitenumerique/menshen/commit/e6246c2).
- **Performance et Infrastructure :**
    - Support du pool de connexions PostgreSQL pour une meilleure gestion des ressources [#5840f47](https://github.com/suitenumerique/menshen/commit/5840f47).
    - Utilisation d'Uvicorn pour exécuter l'application en production, améliorant les performances [#9414c22](https://github.com/suitenumerique/menshen/commit/9414c22).
- **Architecture :**
    - Refactorisation de la gestion de la requête d'échange de jeton vers un service dédié [#c25b12a](https://github.com/suitenumerique/menshen/commit/c25b12a).
    - Déplacement du module de génération de jetons vers `services.token` [#80bf387](https://github.com/suitenumerique/menshen/commit/80bf387).
    - Conversion des sérializers en structures `msgspec` pour une meilleure performance [#dac2ee9](https://github.com/suitenumerique/menshen/commit/dac2ee9).
    - Héritage des structures de `msgspec.Struc` pour une meilleure organisation du code [#60bf50a](https://github.com/suitenumerique/menshen/commit/60bf50a).
- **Dépendances :**
    - Mise à jour de la version de Python à 3.14.6 [#ab12175](https://github.com/suitenumerique/menshen/commit/ab12175).

### Autres changements
- Ajout de tests pour les modèles `token_exchange` [#ca2fb77](https://github.com/suitenumerique/menshen/commit/ca2fb77).
- Ajout de tests pour le service de requête d'échange de jetons [#adf3c38](https://github.com/suitenumerique/menshen/commit/adf3c38).
- Suppression des dépendances `drf-standardized-errors` et `annotated-types` pour simplifier le projet [#5add6ac](https://github.com/suitenumerique/menshen/commit/5add6ac), [#60fa40c](https://github.com/suitenumerique/menshen/commit/60fa40c).
- Correction d'une erreur de copier/coller dans le playground [#f76e461](https://github.com/suitenumerique/menshen/commit/f76e461).
- Ajout de la dépendance `uvicorn` [#c8816ac](https://github.com/suitenumerique/menshen/commit/c8816ac).
- Bundle des fichiers statiques dans l'image Docker [#af7fd64](https://github.com/suitenumerique/menshen/commit/af7fd64).
- Ajout des paramètres OIDC manquants [#5e30abc](https://github.com/suitenumerique/menshen/commit/5e30abc).
