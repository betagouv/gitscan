## Changelog : aides-agri (30 derniers jours)

### Résumé
Ce changelog présente les évolutions récentes de la plateforme d'aides agricoles. Les principales nouveautés concernent l'ajout d'une page de statistiques pour le suivi des données, des améliorations de l'interface d'administration pour la gestion des aides, et des corrections et mises à jour pour assurer la stabilité et la sécurité de la plateforme. Plusieurs améliorations ont également été apportées au parcours utilisateur et à l'affichage des informations sur les aides.

### Évolutions fonctionnelles
- Ajout d'une première version de la page de statistiques, permettant un suivi des données de la plateforme. [#387](https://github.com/betagouv/aides-agri/pull/387)
- Amélioration du parcours utilisateur v1. [#363](https://github.com/betagouv/aides-agri/pull/363)
- Mise à jour de la page des fonds d'urgence DNC. [#370](https://github.com/betagouv/aides-agri/pull/370)
- Les bureaux valideurs peuvent désormais voir les aides avant leur publication. [#371](https://github.com/betagouv/aides-agri/pull/371)
- Export CSV de la base édito : ajout de l'URL de la fiche édito. [#393](https://github.com/betagouv/aides-agri/pull/393)
- Ajustement mineur de l'administration des aides. [#372](https://github.com/betagouv/aides-agri/pull/372)

### Évolutions techniques
- Amélioration du script de mises à jour. [#381](https://github.com/betagouv/aides-agri/pull/381)
- Configuration d'un "cooldown" pour les mises à jour automatiques de dépendances (dependabot) afin d'éviter des interruptions de service trop fréquentes. [#374](https://github.com/betagouv/aides-agri/pull/374)
- Mises à jour de plusieurs dépendances :
    - `gunicorn` de 25.0.1 à 25.0.3 puis à 25.1.0 [#367](https://github.com/betagouv/aides-agri/pull/367) et [#386](https://github.com/betagouv/aides-agri/pull/386)
    - `faker` de 40.1.2 à 40.4.0 [#366](https://github.com/betagouv/aides-agri/pull/366)
    - `sentry-sdk` de 2.51.0 à 2.52.0 puis à 2.53.0 [#364](https://github.com/betagouv/aides-agri/pull/364) et [#395](https://github.com/betagouv/aides-agri/pull/395)
    - `psycopg` de 3.3.2 à 3.3.3 [#398](https://github.com/betagouv/aides-agri/pull/398)
    - `django-dsfr` de 3.3.0 à 3.3.1 [#355](https://github.com/betagouv/aides-agri/pull/355)
    - `coverage` de 7.13.3 à 7.13.4 [#383](https://github.com/betagouv/aides-agri/pull/383)
    - `whitenoise` de 6.11.0 à 6.12.0 [#403](https://github.com/betagouv/aides-agri/pull/403)
    - `@sentry/browser` de 10.37.0 à 10.38.0 puis à 10.39.0 et 10.40.0 [#373](https://github.com/betagouv/aides-agri/pull/373), [#389](https://github.com/betagouv/aides-agri/pull/389), [#399](https://github.com/betagouv/aides-agri/pull/399)
    - `djade` de 1.7.0 à 1.8.0 puis à 1.9.0 [#394](https://github.com/betagouv/aides-agri/pull/394) et [#402](https://github.com/betagouv/aides-agri/pull/402)
    - `ruff` de 0.15.0 à 0.15.1, 0.15.2, 0.15.3 et 0.15.4 [#385](https://github.com/betagouv/aides-agri/pull/385), [#391](https://github.com/betagouv/aides-agri/pull/391), [#400](https://github.com/betagouv/aides-agri/pull/400) et [#401](https://github.com/betagouv/aides-agri/pull/401)

### Autres changements
- Mise à jour de la documentation.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Mises à jour de dépendances de développement (pytest-django, js-yaml, lodash-es, tar-fs, minimatch, systeminformation, esbuild).
