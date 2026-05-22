## Changelog : aides-agri (30 derniers jours, au 2026-05-21)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment sur la page d'accueil et la gestion des aides, ainsi que sur la préparation et le déploiement de la version 2 du parcours agri. Des corrections de bugs et des optimisations de performance ont également été apportées pour une meilleure stabilité et réactivité de l'application.

### Évolutions fonctionnelles
- Amélioration de la page d'accueil : possibilité de sélectionner toutes les filières. [#531](https://github.com/betagouv/aides-agri/pull/531)
- Ajout d'une information sur les aides réservées aux groupements de producteurs. [#538](https://github.com/betagouv/aides-agri/pull/538)
- Correction de l'affichage des couleurs sur la page de résultats. [#511](https://github.com/betagouv/aides-agri/pull/511)
- Correction d'un bug sur le fil d'Ariane. [#541](https://github.com/betagouv/aides-agri/pull/541)
- Correction de l'affichage du commentaire de base juridique sur la fiche d'aide. [#569](https://github.com/betagouv/aides-agri/pull/569)
- Ajout de la raison de désactivation à l'export CSV de l'admin. [#532](https://github.com/betagouv/aides-agri/pull/532)
- Ajout de l'Occitanie à la liste des régions couvertes. [#561](https://github.com/betagouv/aides-agri/pull/561)
- Déploiement de la version 2 du parcours agri. [#418](https://github.com/betagouv/aides-agri/pull/418)
- Améliorations de l'outil d'édition des aides. [#498](https://github.com/betagouv/aides-agri/pull/498)
- Correction de l'impression PDF. [#525](https://github.com/betagouv/aides-agri/pull/525)
- Correction du crash de l'historique dans l'admin. [#524](https://github.com/betagouv/aides-agri/pull/524)

### Évolutions techniques
- Mise à jour de plusieurs dépendances : psycopg, coverage, types-pyyaml, idna, gunicorn, htmx.org, @sentry/browser, urllib3, faker, packaging, tzdata, django, django-admin-extra-buttons.
- Améliorations des notifications internes. [#547](https://github.com/betagouv/aides-agri/pull/547)
- Script de stress-test de performance de l'infrastructure. [#544](https://github.com/betagouv/aides-agri/pull/544)
- Tentative de réduction des latences de l'application. [#523](https://github.com/betagouv/aides-agri/pull/523)
- Limitation de la fuite mémoire via Gunicorn. [#537](https://github.com/betagouv/aides-agri/pull/537)
- Correctif sur le réglage de connexion persistante à la BDD. [#536](https://github.com/betagouv/aides-agri/pull/536)
- Facilitation du déploiement en cas de changement de schéma de BDD. [#501](https://github.com/betagouv/aides-agri/pull/501)
- Ajout d'un lockfile uv. [#562](https://github.com/betagouv/aides-agri/pull/562) et [#522](https://github.com/betagouv/aides-agri/pull/522)

### Autres changements
- Mise à jour des statistiques publiques pour avril 2026. [#533](https://github.com/betagouv/aides-agri/pull/533)
- Mise à jour de la date de validité du security.txt. [#505](https://github.com/betagouv/aides-agri/pull/505)
- Ajout de scripts pour la création/association des logos des DDT(M). [#493](https://github.com/betagouv/aides-agri/pull/493) et [#507](https://github.com/betagouv/aides-agri/pull/507)
- Nouvel icône pour le thème Transmission. [#573](https://github.com/betagouv/aides-agri/pull/573)
- Améliorations de l'accessibilité de la validation de formulaire côté client. [#530](https://github.com/betagouv/aides-agri/pull/530)
- Consolidation de la notion de base juridique des aides. [#495](https://github.com/betagouv/aides-agri/pull/495) et [#500](https://github.com/betagouv/aides-agri/pull/500)
- Correction de plusieurs bugs liés au déploiement automatisé. [#550](https://github.com/betagouv/aides-agri/pull/550), [#551](https://github.com/betagouv/aides-agri/pull/551), [#552](https://github.com/betagouv/aides-agri/pull/552), [#553](https://github.com/betagouv/aides-agri/pull/553), [#554](https://github.com/betagouv/aides-agri/pull/554) et [#548](https://github.com/betagouv/aides-agri/pull/548)
- Tracking d'événement de clic sur lien externe pour le mode minimal. [#535](https://github.com/betagouv/aides-agri/pull/535)
- Correctif sur le slug des aides. [#497](https://github.com/betagouv/aides-agri/pull/497)
