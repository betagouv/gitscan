## Changelog : rdv-service-public (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité avec le renforcement de l'authentification à deux facteurs (2FA) pour certains comptes, des corrections de bugs concernant la gestion des rendez-vous (plages, récurrences, jours fériés) et l'interface utilisateur, ainsi que des améliorations de la robustesse et de la performance du service. Des modifications ont également été apportées à l'API pour inclure des informations supplémentaires sur les usagers et les rendez-vous.

### Évolutions fonctionnelles
- **Sécurité :** Mise en place du 2FA pour les comptes sensibles ProConnect [#6310](https://github.com/betagouv/rdv-service-public/issues/6310) et pour certains IDP ProConnect.
- **Gestion des rendez-vous :**
    - Correction d'un bug empêchant l'affichage correct de la seconde période d'une plage horaire [#6326](https://github.com/betagouv/rdv-service-public/issues/6326).
    - Correction de l'affichage des jours fériés dans l'agenda multi-agent [#6325](https://github.com/betagouv/rdv-service-public/issues/6325).
    - Correction d'un bug lié aux récurrences sur les plages d'ouverture [#6329](https://github.com/betagouv/rdv-service-public/issues/6329).
    - Gestion améliorée des événements Caldav externes déjà supprimés [#6348](https://github.com/betagouv/rdv-service-public/issues/6348).
- **Interface utilisateur :**
    - Correction d'un bug où deux éléments du menu pouvaient être actifs simultanément [#6330](https://github.com/betagouv/rdv-service-public/issues/6330).
    - Sélection automatique de la barre de recherche usager [#6332](https://github.com/betagouv/rdv-service-public/issues/6332).
    - Mise en valeur du choix de date et heure d'une plage [#6292](https://github.com/betagouv/rdv-service-public/issues/6292).
    - Passage des formulaires de création/édition d'agent au Design System Français (DSFR) [#6309](https://github.com/betagouv/rdv-service-public/issues/6309).
- **API :**
    - Ajout des champs de géocodage dans le blueprint users pour l'API V1 [#6337](https://github.com/betagouv/rdv-service-public/issues/6337).
    - Ajout du champ `time_zone` dans l'API `rdvs` [#6340](https://github.com/betagouv/rdv-service-public/issues/6340).

### Évolutions techniques
- Mise à jour de Node vers la version 24 dans les jobs GitHub Actions [#6331](https://github.com/betagouv/rdv-service-public/issues/6331).
- Mise à jour de la librairie `connection_pool` en v3.0 [#6333](https://github.com/betagouv/rdv-service-public/issues/6333).
- Amélioration de la robustesse de `FileAttenteJob` en limitant l'usage mémoire et en le séparant en plusieurs jobs [#6324](https://github.com/betagouv/rdv-service-public/issues/6324) et [#6322](https://github.com/betagouv/rdv-service-public/issues/6322).
- Correction des tokens d'invitation en minuscule dans les liens [#6338](https://github.com/betagouv/rdv-service-public/issues/6338).
- Suppression de la rétrocompatibilité du champ `notification_email` dans l'API [#6281](https://github.com/betagouv/rdv-service-public/issues/6281).
- Mise à jour de la gem `addressable` [#6318](https://github.com/betagouv/rdv-service-public/issues/6318).

### Autres changements
- Ajout d'un lien vers l'annuaire des entreprises pour les espaces dans le SuperAdmin [#6352](https://github.com/betagouv/rdv-service-public/issues/6352).
- Ajout du nombre d'habitants de la commune dans la demande d'ouverture de compte [#6321](https://github.com/betagouv/rdv-service-public/issues/6321).
- Information des agents de la mise en place de la double authentification [#6314](https://github.com/betagouv/rdv-service-public/issues/6314).
- Suppression du feature flag `new planning` et des bandeaux de nouveautés [#6316](https://github.com/betagouv/rdv-service-public/issues/6316).
- Correction d'une flaky spec à cause du lundi férié [#6315](https://github.com/betagouv/rdv-service-public/issues/6315).
- Correction de la création d’espace via les OPSN [#6336](https://github.com/betagouv/rdv-service-public/issues/6336).
- Revert d'une modification concernant la distinction des erreurs Caldav sur Sentry [#6350](https://github.com/betagouv/rdv-service-public/issues/6350).
- Éviter `Notion::Api::Errors::TooManyRequests` [#6342](https://github.com/betagouv/rdv-service-public/issues/6342).
