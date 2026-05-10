## Changelog : rdv-service-public (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des calendriers, la correction de bugs liés à l'interface utilisateur et à la synchronisation des données, ainsi que sur des optimisations de performance et de sécurité. Des améliorations ont également été apportées à l'API et à l'administration du service.

### Évolutions fonctionnelles
- Possibilité de passer les informations de l'opérateur depuis l'API ANCT en session, améliorant ainsi la gestion des données utilisateurs. [#6362](https://github.com/betagouv/rdv-service-public/pull/6362)
- Ajout du champ `time_zone` dans l'API `rdvs` pour une meilleure gestion des fuseaux horaires. [#6340](https://github.com/betagouv/rdv-service-public/pull/6340)
- Ajout d'un lien vers l'annuaire des entreprises pour les espaces dans le SuperAdmin, facilitant la recherche et l'identification des organisations. [#6352](https://github.com/betagouv/rdv-service-public/pull/6352)
- Amélioration de la recherche d'usagers dans une nouvelle organisation pour les territoires ayant déjà des usagers. [#6327](https://github.com/betagouv/rdv-service-public/pull/6327)
- Correction de l'affichage des jours fériés pour l'agenda multi-agent. [#6325](https://github.com/betagouv/rdv-service-public/pull/6325)
- Correction de l'affichage de la seconde période d'une plage horaire. [#6326](https://github.com/betagouv/rdv-service-public/pull/6326)
- Correction de la création d’espace via les OPSN. [#6336](https://github.com/betagouv/rdv-service-public/pull/6336)
- Ajout des champs de geocoding dans le blueprint users pour l'API V1. [#6337](https://github.com/betagouv/rdv-service-public/pull/6337)
- Correction des tokens d'invitation qui sont maintenant en minuscule dans les liens. [#6338](https://github.com/betagouv/rdv-service-public/pull/6338)

### Évolutions techniques
- Passage à Node24 dans les jobs GitHub Actions pour bénéficier des dernières améliorations et correctifs de sécurité. [#6331](https://github.com/betagouv/rdv-service-public/pull/6331)
- Mise à jour de la gem `connection_pool` en version 3.0. [#6333](https://github.com/betagouv/rdv-service-public/pull/6333)
- Retour à la gem Devise officielle pour assurer la stabilité et la compatibilité. [#6345](https://github.com/betagouv/rdv-service-public/pull/6345)
- Optimisation de l'utilisation de la mémoire par `FileAttenteJob` en le séparant en plusieurs jobs. [#6324](https://github.com/betagouv/rdv-service-public/pull/6324)
- Amélioration de la robustesse de `FileAttenteJob`. [#6322](https://github.com/betagouv/rdv-service-public/pull/6322)
- Ajout de `kmeet.infomaniak.com` aux domaines autorisés pour les visioconférences personnalisées. [#6357](https://github.com/betagouv/rdv-service-public/pull/6357)

### Autres changements
- Mise en place du 2FA ProConnect uniquement pour les comptes sensibles. [#6335](https://github.com/betagouv/rdv-service-public/pull/6335)
- Forçage du 2FA pour certains IDP ProConnect pour renforcer la sécurité. [#6310](https://github.com/betagouv/rdv-service-public/pull/6310)
- Correction d'un bug où deux éléments du menu pouvaient être actifs simultanément. [#6330](https://github.com/betagouv/rdv-service-public/pull/6330)
- Sélection automatique de la barre de recherche usager pour une meilleure expérience utilisateur. [#6332](https://github.com/betagouv/rdv-service-public/pull/6332)
- Gestion du cas où un événement Caldav externe est déjà supprimé. [#6348](https://github.com/betagouv/rdv-service-public/pull/6348)
- Éviter les erreurs `Notion::Api::Errors::TooManyRequests` lors de l'utilisation de l'API Notion. [#6342](https://github.com/betagouv/rdv-service-public/pull/6342)
- Correction d'une réversion de la distinction des erreurs Caldav sur Sentry par statut HTTP. [#6350](https://github.com/betagouv/rdv-service-public/pull/6350)
- Distinction des erreurs Caldav sur Sentry par statut HTTP pour un meilleur suivi des erreurs. [#6347](https://github.com/betagouv/rdv-service-public/pull/6347)
