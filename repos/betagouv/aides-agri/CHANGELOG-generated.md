## Changelog : aides-agri (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la performance et de la stabilité de l'application, notamment en corrigeant des problèmes de latence et de déploiement. Des améliorations ont également été apportées à l'interface utilisateur, notamment sur la page d'accueil et l'affichage des aides, ainsi que des corrections de bugs concernant l'impression PDF et l'historique dans l'administration. Enfin, plusieurs dépendances ont été mises à jour pour bénéficier des dernières corrections et améliorations de sécurité.

### Évolutions fonctionnelles
- Possibilité de sélectionner toutes les filières sur la page d'accueil. [#531](https://github.com/betagouv/aides-agri/issues/531)
- Ajout d'une information sur les aides réservées aux groupements de producteurs. [#538](https://github.com/betagouv/aides-agri/issues/538)
- Ajout de la raison de désactivation à l'export CSV de l'administration. [#532](https://github.com/betagouv/aides-agri/issues/532)
- Améliorations mineures de la page d'aide. [#543](https://github.com/betagouv/aides-agri/issues/543)
- Correction d'un bug d'affichage de couleur sur la page de résultats. [#511](https://github.com/betagouv/aides-agri/issues/511)
- Correction d'un bug sur le fil d'Ariane. [#541](https://github.com/betagouv/aides-agri/issues/541)
- Correction de l'impression PDF. [#525](https://github.com/betagouv/aides-agri/issues/525)
- Correction du crash de l'historique dans l'administration. [#524](https://github.com/betagouv/aides-agri/issues/524)
- Correction de deux erreurs sur les notifications admin des aides. [#576](https://github.com/betagouv/aides-agri/issues/576)
- Correction sur la fiche d'aide : le commentaire de base juridique n'était pas affiché. [#569](https://github.com/betagouv/aides-agri/issues/569)

### Évolutions techniques
- Tentative de résolution des latences en dynamisant le nombre maximal de requêtes de Gunicorn. [#578](https://github.com/betagouv/aides-agri/issues/578)
- Tentative de réduction des latences de l'application. [#523](https://github.com/betagouv/aides-agri/issues/523)
- Ajout d'un script de stress-test de performance de l'infrastructure. [#544](https://github.com/betagouv/aides-agri/issues/544)
- Mise à jour de plusieurs dépendances : Django, psycopg, coverage, tzdata, packaging, certifi, idna, htmx.org, @sentry/browser, urllib3, ip-address et socks.
- Mise à jour de Gunicorn en version 26.0.0. [#545](https://github.com/betagouv/aides-agri/issues/545)
- Utilisation de `uv lock` pour verrouiller les dépendances. [#562](https://github.com/betagouv/aides-agri/issues/562) et [#522](https://github.com/betagouv/aides-agri/issues/522)
- Ajout de l'Occitanie à la liste statique des régions couvertes. [#561](https://github.com/betagouv/aides-agri/issues/561)

### Autres changements
- Améliorations des notifications internes. [#547](https://github.com/betagouv/aides-agri/issues/547)
- Ajout d'un nouvel icône pour le thème Transmission. [#573](https://github.com/betagouv/aides-agri/issues/573)
- Tracking d'événement de clic sur lien externe pour le mode minimal. [#535](https://github.com/betagouv/aides-agri/issues/535)
- Mise à jour des statistiques publiques pour avril 2026. [#533](https://github.com/betagouv/aides-agri/issues/533)
- Plusieurs correctifs concernant le déploiement automatisé. [#554](https://github.com/betagouv/aides-agri/issues/554), [#553](https://github.com/betagouv/aides-agri/issues/553), [#552](https://github.com/betagouv/aides-agri/issues/552), [#551](https://github.com/betagouv/aides-agri/issues/551), [#550](https://github.com/betagouv/aides-agri/issues/550), [#548](https://github.com/betagouv/aides-agri/issues/548)
- Correctifs sur l'envoi de résultats par e-mail. [#542](https://github.com/betagouv/aides-agri/issues/542)
- Amélioration de l'accessibilité de la validation de formulaire côté client. [#530](https://github.com/betagouv/aides-agri/issues/530)
- Correction du réglage de connexion persistante à la BDD. [#536](https://github.com/betagouv/aides-agri/issues/536)
