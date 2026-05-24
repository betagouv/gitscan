## Changelog : aides-agri (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec le déploiement de la version 2 du parcours agri, des corrections de bugs d'affichage et de fonctionnement, et l'ajout de nouvelles fonctionnalités comme la sélection de toutes les filières sur la page d'accueil. Des efforts ont également été faits pour optimiser les performances et la sécurité de l'application.

### Évolutions fonctionnelles
- Ajout de la possibilité de sélectionner toutes les filières sur la page d'accueil [#531](https://github.com/betagouv/aides-agri/issues/531).
- Ajout d'une information sur les aides réservées aux groupements de producteurs [#538](https://github.com/betagouv/aides-agri/issues/538).
- Ajout de la raison de désactivation à l'export CSV de l'admin [#532](https://github.com/betagouv/aides-agri/issues/532).
- Correction de l'affichage du commentaire de base juridique sur la fiche d'aide [#569](https://github.com/betagouv/aides-agri/issues/569).
- Correction d'un bug d'affichage de couleur sur la page de résultats [#511](https://github.com/betagouv/aides-agri/issues/511).
- Correction d'un bug sur le fil d'Ariane [#541](https://github.com/betagouv/aides-agri/issues/541).
- Correction de l'impression PDF [#525](https://github.com/betagouv/aides-agri/issues/525).
- Correction du crash de l'historique dans l'admin [#524](https://github.com/betagouv/aides-agri/issues/524).
- Ajout de l'Occitanie à la liste statique des régions couvertes [#561](https://github.com/betagouv/aides-agri/issues/561).
- Déploiement de la version 2 du parcours agri [#418](https://github.com/betagouv/aides-agri/issues/418).
- Améliorations mineures de la page d'aide [#543](https://github.com/betagouv/aides-agri/issues/543).

### Évolutions techniques
- Mise à jour de plusieurs dépendances : Django, psycopg, coverage, types-pyyaml, idna, urllib3, htmx.org, @sentry/browser, faker, django-anymail, packaging, certifi, tzdata, requests, django-reversion, pymdown-extensions, gunicorn, easymde, @testing-library/cypress, systeminformation, ruff.
- Mise en place d'un script de stress-test de performance de l'infrastructure [#544](https://github.com/betagouv/aides-agri/issues/544).
- Améliorations des notifications internes [#547](https://github.com/betagouv/aides-agri/issues/547).
- Tentative de limitation de la fuite mémoire via Gunicorn [#537](https://github.com/betagouv/aides-agri/issues/537).
- Correctif sur le réglage de connexion persistante à la BDD [#536](https://github.com/betagouv/aides-agri/issues/536).
- Tentative de réduction des latences de l'application [#523](https://github.com/betagouv/aides-agri/issues/523).
- Facilitation du déploiement en cas de changement de schéma de BDD [#501](https://github.com/betagouv/aides-agri/issues/501).
- Ajout d'un nouveau logo (pour le thème Transmission) [#573](https://github.com/betagouv/aides-agri/issues/573).
- Mise à jour des statistiques publiques pour avril 2026 [#533](https://github.com/betagouv/aides-agri/issues/533).
- Mise à jour de la date de validité du security.txt [#505](https://github.com/betagouv/aides-agri/issues/505).
- Ajout de scripts pour les services déconcentrés et logos [#507](https://github.com/betagouv/aides-agri/issues/507).
- Utilisation de `uv lock` pour verrouiller les dépendances [#562](https://github.com/betagouv/aides-agri/issues/562) et [#522](https://github.com/betagouv/aides-agri/issues/522).

### Autres changements
- Tracking d'événement de clic sur lien externe pour le mode minimal [#535](https://github.com/betagouv/aides-agri/issues/535).
- Améliorations de l'accessibilité de la validation de formulaire côté client [#530](https://github.com/betagouv/aides-agri/issues/530).
- Plusieurs correctifs liés au déploiement automatisé [#554](https://github.com/betagouv/aides-agri/issues/554), [#553](https://github.com/betagouv/aides-agri/issues/553), [#552](https://github.com/betagouv/aides-agri/issues/552), [#551](https://github.com/betagouv/aides-agri/issues/551), [#550](https://github.com/betagouv/aides-agri/issues/550), [#548](https://github.com/betagouv/aides-agri/issues/548).
