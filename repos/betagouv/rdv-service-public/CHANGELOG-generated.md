## Changelog : rdv-service-public (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse de la plateforme, la correction de bugs impactant l'expérience utilisateur (notamment sur l'agenda et la recherche d'usagers), et l'ajout de fonctionnalités pour faciliter l'administration et la gestion des comptes, en particulier pour les opérateurs de services publics (OPSN). Des améliorations de sécurité ont également été apportées avec le renforcement de l'authentification à deux facteurs pour certains comptes.

### Évolutions fonctionnelles
- **Gestion des comptes OPSN :** Création automatique d'espace lors de l'activation de RDV-SP par un OPSN [#6304](https://github.com/betagouv/rdv-service-public/issues/6304).
- **Authentification :** Renforcement de l'authentification à deux facteurs (2FA) pour certains comptes sensibles et IDP ProConnect [#6310](https://github.com/betagouv/rdv-service-public/issues/6310), [#6335](https://github.com/betagouv/rdv-service-public/issues/6335).
- **Recherche d'usagers :** Possibilité de rechercher un usager dans une nouvelle organisation pour un territoire ayant déjà des usagers [#6327](https://github.com/betagouv/rdv-service-public/issues/6327).
- **Interface utilisateur :**
    - Amélioration de l'affichage de la sélection de date et heure pour les plages de rendez-vous [#6292](https://github.com/betagouv/rdv-service-public/issues/6292).
    - Passage des formulaires de création/édition d'agent au Design System Français (DSFR) [#6309](https://github.com/betagouv/rdv-service-public/issues/6309).
    - Ajout du SIRET sur l'espace d'administration [#6302](https://github.com/betagouv/rdv-service-public/issues/6302).
    - Simplification de la désinscription de la liste d'attente [#6288](https://github.com/betagouv/rdv-service-public/issues/6288).
- **Notifications :** Envoi d'un email en cas de refus de demande d'ouverture de compte [#6278](https://github.com/betagouv/rdv-service-public/issues/6278).
- **API :** Ajout du champ `time_zone` dans l'API `rdvs` [#6340](https://github.com/betagouv/rdv-service-public/issues/6340) et des champs de géocodage dans le blueprint users pour l'API V1 [#6337](https://github.com/betagouv/rdv-service-public/issues/6337).

### Évolutions techniques
- **Sécurité :** Mise à jour de Node.js en version 24 pour corriger des vulnérabilités [#6296](https://github.com/betagouv/rdv-service-public/issues/6296), [#6299](https://github.com/betagouv/rdv-service-public/issues/6299).
- **Performance :** Limitation de l'usage mémoire de `FileAttenteJob` en le séparant en plusieurs jobs [#6324](https://github.com/betagouv/rdv-service-public/issues/6324).
- **Infrastructure :** Amélioration de la robustesse de `FileAttenteJob` [#6322](https://github.com/betagouv/rdv-service-public/issues/6322).
- **Tests :** Correction de tests instables (flaky tests) grâce à l'utilisation de `travel_to` dans Playwright [#6312](https://github.com/betagouv/rdv-service-public/issues/6312) et correction d'un test instable lié aux jours fériés [#6315](https://github.com/betagouv/rdv-service-public/issues/6315).
- **Dépendances :** Mises à jour de plusieurs dépendances : `rack-session` (2.1.1 -> 2.1.2), `rack` (3.2.5 -> 3.2.6), `addressable`, `erb` et `phonelib`.

### Autres changements
- **Documentation :** Documentation des cas d'erreur pour visioplainte [#6293](https://github.com/betagouv/rdv-service-public/issues/6293).
- **Code :** Suppression du code de l'ancien calculateur de créneaux [#6295](https://github.com/betagouv/rdv-service-public/issues/6295) et nettoyage du champ `notification_email` [#6281](https://github.com/betagouv/rdv-service-public/issues/6281).
- **Correction de bugs :** Correction de l'affichage de la seconde période d'une plage [#6326](https://github.com/betagouv/rdv-service-public/issues/6326), correction de l'affichage des jours fériés pour l'agenda multi-agent [#6325](https://github.com/betagouv/rdv-service-public/issues/6325), correction d'un bug où deux éléments du menu étaient actifs en même temps [#6330](https://github.com/betagouv/rdv-service-public/issues/6330) et correction des tokens d'invitation en minuscule [#6338](https://github.com/betagouv/rdv-service-public/issues/6338).
- **Revert :** Annulation d'une modification concernant la distinction des erreurs Caldav sur Sentry [#6350](https://github.com/betagouv/rdv-service-public/issues/6350).
