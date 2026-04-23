## Changelog : b3desk (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la correction de bugs et l'ajout de fonctionnalités liées à la délégation de réunions et à l'expérience utilisateur lors de la participation à une visioconférence. Des mises à jour de dépendances ont également été effectuées pour maintenir la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- Correction d'un bug permettant à un utilisateur authentifié de modifier son nom sur la page de participation à une réunion. [#318](https://github.com/numerique-gouv/b3desk/issues/318)
- Amélioration de l'interface utilisateur pour éviter que le logo ne soit masqué par le titre de la réunion. [#319](https://github.com/numerique-gouv/b3desk/issues/319)
- Implémentation de la délégation de réunions, permettant à un utilisateur de déléguer sa participation à une autre personne. [#241](https://github.com/numerique-gouv/b3desk/pulls/241) (via #226)

### Évolutions techniques
- Correction de la compatibilité avec Keycloak dans le pipeline CI. [#317](https://github.com/numerique-gouv/b3desk/issues/317)
- Mise à jour vers la version 1.6.1dev et 1.5.9dev.
- Mises à jour de plusieurs dépendances : `lxml`, `python-dotenv`, `authlib`, `mako`, `pytest`, `uv`, `cryptography`, `pygments`, `requests`.

### Autres changements
- Aucune information supplémentaire disponible.
