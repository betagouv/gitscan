## Changelog : aides-agri (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la stabilité et de la performance de la plateforme, ainsi que sur des corrections de bugs et des améliorations de l'expérience utilisateur, notamment au niveau de l'affichage des informations sur les aides et des notifications administratives. Une attention particulière a été portée à la préparation et à l'automatisation du déploiement.

### Évolutions fonctionnelles
- Amélioration de la lisibilité de la page de statistiques [#585](https://github.com/betagouv/aides-agri/issues/585).
- Ajout d'une information sur les aides réservées aux groupements de producteurs [#538](https://github.com/betagouv/aides-agri/issues/538).
- Ajout de l'Occitanie à la liste statique des régions couvertes [#561](https://github.com/betagouv/aides-agri/issues/561).
- Correction de l'affichage du commentaire de base juridique sur la fiche d'aide [#569](https://github.com/betagouv/aides-agri/issues/569).
- Correction d'un bug sur le fil d'Ariane [#541](https://github.com/betagouv/aides-agri/issues/541).
- Améliorations mineures de la page d'aide [#543](https://github.com/betagouv/aides-agri/issues/543).
- Correction de deux erreurs sur les notifications admin des aides [#576](https://github.com/betagouv/aides-agri/issues/576).
- Correction des envois de résultats par e-mail [#542](https://github.com/betagouv/aides-agri/issues/542).
- Nouvelle icône pour le thème Transmission [#573](https://github.com/betagouv/aides-agri/issues/573).

### Évolutions techniques
- Mise à jour de l'architecture technique et des ADR (Architecture Decision Records) [#594](https://github.com/betagouv/aides-agri/issues/594).
- Mise à jour de la librairie de composants d'interface utilisateur `@gouvfr/dsfr-chart` vers la version 2.1.1 [#589](https://github.com/betagouv/aides-agri/issues/589).
- Tentative de résolution des latences en dynamisant le nombre maximal de requêtes de Gunicorn [#578](https://github.com/betagouv/aides-agri/issues/578).
- Mise en place d'un script de stress-test de performance de l'infrastructure [#544](https://github.com/betagouv/aides-agri/issues/544).
- Automatisation du déploiement (avec plusieurs itérations de corrections) [#548](https://github.com/betagouv/aides-agri/issues/548), [#550](https://github.com/betagouv/aides-agri/issues/550), [#551](https://github.com/betagouv/aides-agri/issues/551), [#552](https://github.com/betagouv/aides-agri/issues/552), [#553](https://github.com/betagouv/aides-agri/issues/553), [#554](https://github.com/betagouv/aides-agri/issues/554).
- Mise à jour de `uv` avec un lockfile [#583](https://github.com/betagouv/aides-agri/issues/583) et [#588](https://github.com/betagouv/aides-agri/issues/588).

### Autres changements
- Mises à jour de dépendances : `sentry-sdk[django]`, `ruff`, `docling`, `@sentry/browser`, `requests`, `django-admin-extra-buttons`, `easymde`, `@testing-library/cypress`, `systeminformation`, `urllib3`, `gunicorn`, `psycopg`, `coverage`, `types-pyyaml`, `idna`, `faker`, `django-formtools`, `django-reversion`, `pymdown-extensions`.
