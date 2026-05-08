## Changelog : rdv-service-public (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des calendriers (synchronisation, affichage, robustesse), l'expérience utilisateur lors de la recherche d'usagers et la création d'espaces, ainsi que des corrections de bugs et des mises à jour techniques pour améliorer la stabilité et la sécurité de la plateforme. Des améliorations ont également été apportées à l'intégration avec ProConnect et à l'API.

### Évolutions fonctionnelles
- **Calendrier :** Indication du statut des synchronisations de calendrier pour une meilleure visibilité. [#6353](https://github.com/betagouv/rdv-service-public/issues/6353)
- **Calendrier :** Gestion améliorée des événements Caldav externes déjà supprimés. [#6348](https://github.com/betagouv/rdv-service-public/issues/6348)
- **Recherche d'usagers :** Possibilité de rechercher des usagers dans une nouvelle organisation pour un territoire ayant déjà des usagers. [#6327](https://github.com/betagouv/rdv-service-public/issues/6327)
- **SuperAdmin :** Ajout d'un lien vers l'annuaire des entreprises pour les espaces. [#6352](https://github.com/betagouv/rdv-service-public/issues/6352)
- **API :** Ajout du champ `time_zone` à l'API `rdvs` pour une meilleure gestion des fuseaux horaires. [#6340](https://github.com/betagouv/rdv-service-public/issues/6340)
- **API :** Ajout des champs de géocodage dans le blueprint users pour l'API V1. [#6337](https://github.com/betagouv/rdv-service-public/issues/6337)
- **Onboarding :** Correction du redirect lors de l'onboarding. [#6323](https://github.com/betagouv/rdv-service-public/issues/6323)
- **Formulaires Agent :** Passage des formulaires de création/édition d'agent au DSFR (Design System FR). [#6309](https://github.com/betagouv/rdv-service-public/issues/6309)
- **Informations Territoire :** Ajout du nombre d'habitants de la commune dans la demande d'ouverture de compte. [#6321](https://github.com/betagouv/rdv-service-public/issues/6321)

### Évolutions techniques
- **Devise :** Retour à la gem Devise officielle pour une meilleure stabilité. [#6345](https://github.com/betagouv/rdv-service-public/issues/6345)
- **Node.js :** Mise à jour vers Node24 dans les jobs GitHub Actions. [#6331](https://github.com/betagouv/rdv-service-public/issues/6331)
- **Bibliothèques :** Mise à jour de la gem `connection_pool` en v3.0. [#6333](https://github.com/betagouv/rdv-service-public/issues/6333)
- **Robustesse :** Amélioration de la robustesse de `FileAttenteJob` en séparant en plusieurs jobs pour limiter l'usage mémoire. [#6324](https://github.com/betagouv/rdv-service-public/issues/6324) et [#6322](https://github.com/betagouv/rdv-service-public/issues/6322)
- **Sécurité :**  Forcer l'authentification à deux facteurs (2FA) pour certains IDP ProConnect et pour les comptes sensibles. [#6310](https://github.com/betagouv/rdv-service-public/issues/6310) et [#6335](https://github.com/betagouv/rdv-service-public/issues/6335)
- **Correction :** Correction des tokens d'invitation en minuscule dans les liens. [#6338](https://github.com/betagouv/rdv-service-public/issues/6338)
- **Correction :** Correction d'un bug où deux éléments du menu pouvaient être actifs en même temps. [#6330](https://github.com/betagouv/rdv-service-public/issues/6330)
- **Correction :** Correction de l'affichage des jours fériés pour l'agenda multi-agent. [#6325](https://github.com/betagouv/rdv-service-public/issues/6325)
- **Correction :** Correction de l'affichage de la seconde période d'une plage horaire. [#6326](https://github.com/betagouv/rdv-service-public/issues/6326)
- **Correction :** Correction de la création d’espace via les OPSN. [#6336](https://github.com/betagouv/rdv-service-public/issues/6336)
- **Correction :** Correction des récurrences sur les plages d'ouverture. [#6329](https://github.com/betagouv/rdv-service-public/issues/6329)

### Autres changements
- **Visio :** Ajout de `kmeet.infomaniak.com` aux domaines autorisés pour les visioconférences personnalisées. [#6357](https://github.com/betagouv/rdv-service-public/issues/6357)
- **Sentry :** Distinguer les erreurs Caldav sur Sentry par statut HTTP (revert d'une modification précédente). [#6350](https://github.com/betagouv/rdv-service-public/issues/6350)
- **API ANCT :** Passage des informations opérateur de l'API ANCT en session plutôt qu'en paramètres. [#6362](https://github.com/betagouv/rdv-service-public/issues/6362)
- **Nettoyage :** Nettoyage du champ `notification_email` et suppression de la rétrocompatibilité API. [#6281](https://github.com/betagouv/rdv-service-public/issues/6281)
- **Automatisation :** Sélection automatique de la barre de recherche usager. [#6332](https://github.com/betagouv/rdv-service-public/issues/6332)
- **Feature Flags :** Suppression du feature flag `new planning` et des bandeaux de nouveautés associés. [#6316](https://github.com/betagouv/rdv-service-public/issues/6316)
- **Dépendances :** Mise à jour de la gem `addressable`. [#6318](https://github.com/betagouv/rdv-service-public/issues/6318)
- **Dépendances :** Mise à jour de la gem `rack-session`. [#6317](https://github.com/betagouv/rdv-service-public/issues/6317)
- **Dépendances :** Mise à jour de la gem `erb`. [#6341](https://github.com/betagouv/rdv-service-public/issues/6341)
- **Dépendances :** Mise à jour de la gem `net-imap`. [#6358](https://github.com/betagouv/rdv-service-public/issues/6358)
