## Changelog : aides-agri (30 derniers jours, au 4 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la performance et de la stabilité de la plateforme, notamment en corrigeant des problèmes de déploiement et en optimisant la gestion des ressources serveur. Des améliorations fonctionnelles ont également été apportées, comme l'ajout de la région Occitanie, des informations sur les aides pour les groupements de producteurs et des correctifs sur l'interface utilisateur pour une meilleure expérience.

### Évolutions fonctionnelles
- Ajout de la région Occitanie à la liste des régions couvertes. [#561](https://github.com/betagouv/aides-agri/pull/561)
- Ajout d'une information sur les aides réservées aux groupements de producteurs. [#538](https://github.com/betagouv/aides-agri/pull/538)
- Amélioration de la page d'aide avec des correctifs mineurs. [#543](https://github.com/betagouv/aides-agri/pull/543)
- Possibilité de sélectionner toutes les filières sur la page d'accueil. [#531](https://github.com/betagouv/aides-agri/pull/531)
- Ajout de la raison de désactivation à l'export CSV de l'administration. [#532](https://github.com/betagouv/aides-agri/pull/532)
- Correction de bugs sur le fil d'Ariane et l'affichage du commentaire de base juridique sur la fiche d'aide. [#541](https://github.com/betagouv/aides-agri/pull/541), [#569](https://github.com/betagouv/aides-agri/pull/569)
- Amélioration des notifications internes. [#547](https://github.com/betagouv/aides-agri/pull/547)
- Correction de deux erreurs sur les notifications admin des aides. [#576](https://github.com/betagouv/aides-agri/pull/576)

### Évolutions techniques
- Tentative de résolution des latences en dynamisant le `max-requests` de Gunicorn. [#578](https://github.com/betagouv/aides-agri/pull/578)
- Script de stress-test de performance de l'infrastructure ajouté. [#544](https://github.com/betagouv/aides-agri/pull/544)
- Correctif sur le réglage de connexion persistante à la BDD. [#536](https://github.com/betagouv/aides-agri/pull/536)
- Tentative de limitation de la fuite mémoire via Gunicorn. [#537](https://github.com/betagouv/aides-agri/pull/537)
- Mises à jour de plusieurs dépendances : Django, psycopg, coverage, requests, urllib3, idna, faker, django-formtools, django-reversion, gunicorn, sentry-sdk, etc.
- Amélioration de l'accessibilité de la validation de formulaire côté client. [#530](https://github.com/betagouv/aides-agri/pull/530)
- Rendre la page de statistiques plus lisible. [#585](https://github.com/betagouv/aides-agri/pull/585)

### Autres changements
- Mise à jour des statistiques publiques pour avril 2026. [#533](https://github.com/betagouv/aides-agri/pull/533)
- Ajout d'un nouvel icône pour le thème Transmission. [#573](https://github.com/betagouv/aides-agri/pull/573)
- Plusieurs correctifs et tentatives de résolution de problèmes liés au déploiement automatisé. [#548](https://github.com/betagouv/aides-agri/pull/548), [#550](https://github.com/betagouv/aides-agri/pull/550), [#551](https://github.com/betagouv/aides-agri/pull/552), [#553](https://github.com/betagouv/aides-agri/pull/553), [#554](https://github.com/betagouv/aides-agri/pull/554)
- Tracking d'événement de clic sur lien externe pour le mode minimal. [#535](https://github.com/betagouv/aides-agri/pull/535)
- uv lock (plusieurs occurrences). [#583](https://github.com/betagouv/aides-agri/pull/583), [#588](https://github.com/betagouv/aides-agri/pull/588), [#562](https://github.com/betagouv/aides-agri/pull/562)
