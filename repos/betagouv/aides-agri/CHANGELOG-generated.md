## Changelog : aides-agri (30 derniers jours, au 19 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la stabilité et de la performance de l'application, notamment en préparation du déploiement de la version 2. Des corrections de bugs ont été apportées pour améliorer l'expérience utilisateur, en particulier sur la page de résultats et l'administration des aides. L'ajout de la région Occitanie au catalogue des régions couvertes est également une évolution notable.

### Évolutions fonctionnelles
- Ajout de la région Occitanie à la liste des régions couvertes. [#561](https://github.com/betagouv/aides-agri/pull/561)
- Possibilité de sélectionner toutes les filières sur la page d'accueil. [#531](https://github.com/betagouv/aides-agri/pull/531)
- Ajout d'une information sur les aides réservées aux groupements de producteurs. [#538](https://github.com/betagouv/aides-agri/pull/538)
- Amélioration de la page d'aide avec des ajustements mineurs. [#543](https://github.com/betagouv/aides-agri/pull/543)
- Ajout de la raison de désactivation à l'export CSV de l'administration. [#532](https://github.com/betagouv/aides-agri/pull/532)
- Consolidation de la notion de base juridique des aides, avec plusieurs itérations d'amélioration. [#495](https://github.com/betagouv/aides-agri/pull/495), [#499](https://github.com/betagouv/aides-agri/pull/499)
- Améliorations de l'outil d'édition des aides. [#498](https://github.com/betagouv/aides-agri/pull/498)
- Correction d'un bug d'affichage de couleur sur la page de résultats. [#511](https://github.com/betagouv/aides-agri/pull/511)
- Correction d'un bug sur le fil d'Ariane. [#541](https://github.com/betagouv/aides-agri/pull/541)
- Correction d'un bug sur l'envoi de résultats par e-mail. [#542](https://github.com/betagouv/aides-agri/pull/542)
- Correction du crash de l'historique dans l'administration. [#524](https://github.com/betagouv/aides-agri/pull/524)
- Correction de l'impression PDF. [#525](https://github.com/betagouv/aides-agri/pull/525)
- Correction du slug des aides. [#497](https://github.com/betagouv/aides-agri/pull/497)

### Évolutions techniques
- Préparation et déploiement de la version 2 du parcours agri. [#418](https://github.com/betagouv/aides-agri/pull/418)
- Mise en place d'un script de stress-test de performance de l'infrastructure. [#544](https://github.com/betagouv/aides-agri/pull/544)
- Améliorations des notifications internes. [#547](https://github.com/betagouv/aides-agri/pull/547)
- Tentative de limitation de la fuite mémoire via Gunicorn. [#537](https://github.com/betagouv/aides-agri/pull/537)
- Correctif sur le réglage de connexion persistante à la BDD. [#536](https://github.com/betagouv/aides-agri/pull/536)
- Tentative de réduction des latences de l'application. [#523](https://github.com/betagouv/aides-agri/pull/523)
- Mise à jour de plusieurs dépendances : `psycopg`, `coverage`, `types-pyyaml`, `idna`, `gunicorn`, `sentry-sdk[django]`, `urllib3`, `faker`, `django-dsfr`, `mjml-python`, `packaging`, `certifi`, `tzdata`.
- Mise à jour des outils de développement : `ruff`, `@testing-library/cypress`, `systeminformation`.
- Verrouillage des dépendances avec `uv lock`. [#562](https://github.com/betagouv/aides-agri/pull/562), [#522](https://github.com/betagouv/aides-agri/pull/522), [#491](https://github.com/betagouv/aides-agri/pull/491)

### Autres changements
- Mise à jour des statistiques publiques pour avril 2026. [#533](https://github.com/betagouv/aides-agri/pull/533)
- Mise à jour de la date de validité du security.txt. [#505](https://github.com/betagouv/aides-agri/pull/505)
- Ajout de scripts pour la création et l'association des logos des DDT(M). [#493](https://github.com/betagouv/aides-agri/pull/493)
- Tracking d'événement de clic sur lien externe pour le mode minimal. [#535](https://github.com/betagouv/aides-agri/pull/535)
- Améliorations de l'accessibilité de la validation de formulaire côté client. [#530](https://github.com/betagouv/aides-agri/pull/530)
