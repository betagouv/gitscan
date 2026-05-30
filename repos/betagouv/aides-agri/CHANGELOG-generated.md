## Changelog : aides-agri (30 derniers jours, au 29 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la performance et de la stabilité de l'application, ainsi que sur des corrections de bugs et des améliorations de l'expérience utilisateur, notamment au niveau de l'administration des aides et de la homepage. Des mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la compatibilité du système.

### Évolutions fonctionnelles
- Ajout de la région Occitanie à la liste des régions couvertes par le catalogue d'aides. [#561](https://github.com/betagouv/aides-agri/issues/561)
- Amélioration de la homepage : possibilité de sélectionner toutes les filières. [#531](https://github.com/betagouv/aides-agri/issues/531)
- Ajout d'une information sur les aides réservées aux groupements de producteurs. [#538](https://github.com/betagouv/aides-agri/issues/538)
- Ajout de la raison de désactivation à l'export CSV de l'administration. [#532](https://github.com/betagouv/aides-agri/issues/532)
- Amélioration de l'accessibilité de la validation de formulaire côté client. [#530](https://github.com/betagouv/aides-agri/issues/530)
- Correction de l'impression PDF. [#525](https://github.com/betagouv/aides-agri/issues/525)
- Correction du crash de l'historique dans l'administration. [#524](https://github.com/betagouv/aides-agri/issues/524)
- Correction d'un bug sur le fil d'Ariane. [#541](https://github.com/betagouv/aides-agri/issues/541)
- Correction de deux erreurs sur les notifications admin des aides. [#576](https://github.com/betagouv/aides-agri/issues/576)
- Correction sur la fiche d'aide : le commentaire de base juridique n'était pas affiché. [#569](https://github.com/betagouv/aides-agri/issues/569)
- Améliorations mineures de la page d'aide. [#543](https://github.com/betagouv/aides-agri/issues/543)

### Évolutions techniques
- Tentative de résolution des latences : dynamisation du nombre maximal de requêtes de Gunicorn. [#578](https://github.com/betagouv/aides-agri/issues/578)
- Tentative de réduction des latences de l'application. [#523](https://github.com/betagouv/aides-agri/issues/523)
- Tentative de limitation de la fuite mémoire via Gunicorn. [#537](https://github.com/betagouv/aides-agri/issues/537)
- Correctif sur le réglage de connexion persistante à la BDD. [#536](https://github.com/betagouv/aides-agri/issues/536)
- Mise à jour de plusieurs dépendances : Django, psycopg, certifi, idna, requests, sentry-sdk, django-formtools, faker, django-reversion, urllib3, tzdata, packaging, etc.
- Mise à jour de dépendances de développement : ruff, @testing-library/cypress, systeminformation.
- Script de stress-test de performance de l'infrastructure. [#544](https://github.com/betagouv/aides-agri/issues/544)
- Ajout de tracking d'événement de clic sur lien externe pour le mode minimal. [#535](https://github.com/betagouv/aides-agri/issues/535)

### Autres changements
- Nouvel icône pour le thème Transmission. [#573](https://github.com/betagouv/aides-agri/issues/573)
- Mise à jour des statistiques publiques pour avril 2026. [#533](https://github.com/betagouv/aides-agri/issues/533)
- Déploiement automatisé : plusieurs correctifs et ajustements ont été apportés au processus de déploiement. [#548](https://github.com/betagouv/aides-agri/issues/548), [#550](https://github.com/betagouv/aides-agri/issues/550), [#551](https://github.com/betagouv/aides-agri/issues/551), [#552](https://github.com/betagouv/aides-agri/issues/552), [#553](https://github.com/betagouv/aides-agri/issues/553), [#554](https://github.com/betagouv/aides-agri/issues/554)
- UV lock pour sécuriser les dépendances. [#562](https://github.com/betagouv/aides-agri/issues/562), [#583](https://github.com/betagouv/aides-agri/issues/583)
