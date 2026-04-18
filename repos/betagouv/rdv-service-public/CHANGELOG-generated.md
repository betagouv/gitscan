## Changelog : rdv-service-public (30 derniers jours, au 16 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des comptes utilisateurs, notamment pour les opérateurs et les administrateurs, avec un renforcement de la sécurité via l'authentification à deux facteurs. Des corrections et améliorations ont également été apportées à la gestion des agendas, des plages de rendez-vous et des exports de données. Enfin, des optimisations ont été réalisées pour améliorer la robustesse et la performance de l'application.

### Évolutions fonctionnelles
- **Sécurité :** Mise en place de l'authentification à deux facteurs (2FA) pour les comptes sensibles et certains fournisseurs d'identité ProConnect [#6335](https://github.com/betagouv/rdv-service-public/issues/6335).
- **Gestion des comptes :**
    - Ajout du numéro SIRET lors de la création d'un espace [#6302](https://github.com/betagouv/rdv-service-public/issues/6302).
    - Possibilité de saisir des adresses à l'étranger [#6275](https://github.com/betagouv/rdv-service-public/issues/6275).
    - Amélioration de l'affichage des usagers ayant le même email [#6282](https://github.com/betagouv/rdv-service-public/issues/6282).
    - Simplification de la désinscription des listes d'attente [#6288](https://github.com/betagouv/rdv-service-public/issues/6288).
- **Agendas et plages :**
    - Correction de l'affichage des jours fériés dans l'agenda multi-agent [#6325](https://github.com/betagouv/rdv-service-public/issues/6325).
    - Correction des récurrences sur les plages d'ouverture [#6329](https://github.com/betagouv/rdv-service-public/issues/6329).
    - Amélioration de la gestion des plages d'ouverture exceptionnelles (renommées "Ponctuelles") [#6307](https://github.com/betagouv/rdv-service-public/issues/6307).
    - Possibilité de configurer la couleur d'une plage [#6261](https://github.com/betagouv/rdv-service-public/issues/6261).
- **Export de données :** Ajout de la possibilité de télécharger la liste des participants à un rendez-vous collectif au format CSV [#6263](https://github.com/betagouv/rdv-service-public/issues/6263).
- **Notifications :** Clarification du SMS d'annulation de participation à un rendez-vous [#6283](https://github.com/betagouv/rdv-service-public/issues/6283).
- **Interface utilisateur :**
    - Amélioration de la sélection de l'organisation dans l'interface de connexion usager [#6332](https://github.com/betagouv/rdv-service-public/issues/6332).
    - Passage des formulaires de création/édition d'agent au Design System Français (DSFR) [#6309](https://github.com/betagouv/rdv-service-public/issues/6309).

### Évolutions techniques
- **Infrastructure :** Mise à jour de Node.js en version 24 dans les jobs GitHub Actions [#6331](https://github.com/betagouv/rdv-service-public/issues/6331) et [#6296](https://github.com/betagouv/rdv-service-public/issues/6296).
- **Performance :** Limitation de l'usage mémoire de `FileAttenteJob` en le divisant en plusieurs jobs [#6324](https://github.com/betagouv/rdv-service-public/issues/6324).
- **Robustesse :** Amélioration de la robustesse de `FileAttenteJob` [#6322](https://github.com/betagouv/rdv-service-public/issues/6322).
- **Tests :** Correction de flaky specs grâce à l'utilisation de `travel_to` dans Playwright [#6312](https://github.com/betagouv/rdv-service-public/issues/6312) et [#6290](https://github.com/betagouv/rdv-service-public/issues/6290).
- **Dépendances :** Mises à jour de plusieurs dépendances (rack, bcrypt, icalendar, brace-expansion, connection_pool, addressable)

### Autres changements
- **Documentation :** Documentation des cas d'erreur pour visioplainte [#6293](https://github.com/betagouv/rdv-service-public/issues/6293).
- **Nettoyage de code :** Suppression du code de l'ancien calculateur de créneaux [#6295](https://github.com/betagouv/rdv-service-public/issues/6295).
- Suppression du champ `notification_email` [#6281](https://github.com/betagouv/rdv-service-public/issues/6281).
- Suppression du markup Stimulus sur `_recurrence.html.slim` [#6291](https://github.com/betagouv/rdv-service-public/issues/6291).
