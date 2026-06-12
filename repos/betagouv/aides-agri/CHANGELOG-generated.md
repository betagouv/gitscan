## Changelog : aides-agri (30 derniers jours, au 10 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la documentation du projet, notamment en matière de sécurité et d'architecture technique. Des corrections ont été apportées pour améliorer la stabilité des exports CSV et des déploiements automatiques. Des mises à jour de dépendances ont également été effectuées pour maintenir la sécurité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout de la région Occitanie à la liste des régions couvertes par le service. [#561](https://github.com/betagouv/aides-agri/issues/561)
- Amélioration de la lisibilité de la page de statistiques. [#585](https://github.com/betagouv/aides-agri/issues/585)
- Ajout d'un champ pour l'export CSV dans l'interface d'administration. [#607](https://github.com/betagouv/aides-agri/issues/607)
- Correction de l'affichage du commentaire du base juridique sur la fiche d'aide. [#569](https://github.com/betagouv/aides-agri/issues/569)
- Amélioration des notifications internes pour les aides. [#576](https://github.com/betagouv/aides-agri/issues/576)
- Ajout d'un nouvel icône pour le thème Transmission. [#573](https://github.com/betagouv/aides-agri/issues/573)

### Évolutions techniques
- Mise à jour de l'architecture technique et des ADR (Architecture Decision Records). [#594](https://github.com/betagouv/aides-agri/issues/594)
- Correction d'un problème lié à l'exécution de `aides_publish_illustrations_from_db`. [#600](https://github.com/betagouv/aides-agri/issues/600)
- Tentative de résolution des latences en dynamisant le nombre maximal de requêtes de Gunicorn. [#578](https://github.com/betagouv/aides-agri/issues/578)
- Amélioration des exports CSV depuis l'administration. [#599](https://github.com/betagouv/aides-agri/issues/599)
- Correction de plusieurs problèmes liés au déploiement automatique. [#548](https://github.com/betagouv/aides-agri/issues/548), [#550](https://github.com/betagouv/aides-agri/issues/550), [#551](https://github.com/betagouv/aides-agri/issues/551), [#552](https://github.com/betagouv/aides-agri/issues/552), [#553](https://github.com/betagouv/aides-agri/issues/553), [#554](https://github.com/betagouv/aides-agri/issues/554)

### Autres changements
- Mise à jour de la documentation du projet, incluant des corrections de typos et une remise à niveau complète. [#602](https://github.com/betagouv/aides-agri/issues/602), [#603](https://github.com/betagouv/aides-agri/issues/603), [#604](https://github.com/betagouv/aides-agri/issues/604), [#605](https://github.com/betagouv/aides-agri/issues/605), [#606](https://github.com/betagouv/aides-agri/issues/606)
- Mises à jour régulières des dépendances (psycopg, coverage, idna, faker, django-formtools, types-pyyaml, django-reversion, requests, gunicorn, etc.).
- Mises à jour des dépendances de développement (ruff, @testing-library/cypress, systeminformation).
- Mise à jour des librairies `@gouvfr/dsfr-chart`, `docling`, `@sentry/browser`, `easymde`.
- Exécution régulière de `uv lock`. [#583](https://github.com/betagouv/aides-agri/issues/583), [#588](https://github.com/betagouv/aides-agri/issues/588), [#598](https://github.com/betagouv/aides-agri/issues/598)
