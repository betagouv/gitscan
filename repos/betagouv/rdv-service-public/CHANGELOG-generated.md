## Changelog : rdv-service-public (30 derniers jours, au 5 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des calendriers, la sécurité (notamment avec l'authentification à deux facteurs), et l'expérience utilisateur, avec des corrections de bugs et des améliorations de l'interface. Des optimisations ont également été apportées pour gérer plus efficacement les tâches en arrière-plan et l'utilisation de la mémoire.

### Évolutions fonctionnelles
- **Calendrier :** Indication du statut des synchronisations de calendrier pour une meilleure visibilité. [#6353](https://github.com/betagouv/rdv-service-public/issues/6353)
- **Recherche d'usagers :** Possibilité de rechercher des usagers dans une nouvelle organisation pour un territoire ayant déjà des usagers. [#6327](https://github.com/betagouv/rdv-service-public/issues/6327)
- **API :** Ajout du champ `time_zone` à l'API `rdvs` pour une gestion plus précise des fuseaux horaires. [#6340](https://github.com/betagouv/rdv-service-public/issues/6340)
- **API :** Ajout des champs de géocodage dans le blueprint users pour l'API V1. [#6337](https://github.com/betagouv/rdv-service-public/issues/6337)
- **Visio-conférence :** Ajout de `kmeet.infomaniak.com` aux domaines autorisés pour les visio-conférences personnalisées. [#6357](https://github.com/betagouv/rdv-service-public/issues/6357)
- **SuperAdmin :** Ajout d'un lien vers l'annuaire des entreprises pour les espaces. [#6352](https://github.com/betagouv/rdv-service-public/issues/6352)
- **Onboarding :** Correction du redirect lors de l'onboarding. [#6323](https://github.com/betagouv/rdv-service-public/issues/6323)
- **Formulaires Agent :** Passage des formulaires de création/édition d'agent au DSFR (Design System FR). [#6309](https://github.com/betagouv/rdv-service-public/issues/6309)

### Évolutions techniques
- **Authentification :** Mise en place du 2FA (authentification à deux facteurs) pour certains IDP ProConnect et comptes sensibles. [#6310](https://github.com/betagouv/rdv-service-public/issues/6310), [#6335](https://github.com/betagouv/rdv-service-public/issues/6335)
- **Infrastructure :** Passage à Node24 dans les jobs GitHub Actions pour bénéficier des dernières versions et correctifs de sécurité. [#6331](https://github.com/betagouv/rdv-service-public/issues/6331)
- **Performance :** Limitation de l'usage mémoire par `FileAttenteJob` en le séparant en plusieurs jobs. [#6324](https://github.com/betagouv/rdv-service-public/issues/6324)
- **Robustesse :** Amélioration de la robustesse de `FileAttenteJob`. [#6322](https://github.com/betagouv/rdv-service-public/issues/6322)
- **Dépendances :** Mise à jour de la gem `connection_pool` en v3.0. [#6333](https://github.com/betagouv/rdv-service-public/issues/6333) et de la gem `addressable`. [#6318](https://github.com/betagouv/rdv-service-public/issues/6318)
- **Devise :** Retour à la gem Devise officielle. [#6345](https://github.com/betagouv/rdv-service-public/issues/6345)

### Autres changements
- **Documentation :** Suppression du feature flag `new planning` et des bandeaux de nouveautés associés. [#6316](https://github.com/betagouv/rdv-service-public/issues/6316)
- **Nettoyage :** Nettoyage du champ `notification_email` et suppression de la rétrocompatibilité API. [#6281](https://github.com/betagouv/rdv-service-public/issues/6281)
- **Divers :** Correction de bugs mineurs concernant l'affichage des plages horaires, des jours fériés, et la sélection de la barre de recherche. [#6326](https://github.com/betagouv/rdv-service-public/issues/6326), [#6325](https://github.com/betagouv/rdv-service-public/issues/6325), [#6332](https://github.com/betagouv/rdv-service-public/issues/6332), [#6330](https://github.com/betagouv/rdv-service-public/issues/6330)
- **Correction :** Correction des tokens d'invitation en minuscule dans les liens. [#6338](https://github.com/betagouv/rdv-service-public/issues/6338)
- **Correction :** Correction d’une flaky spec à cause du lundi férié. [#6315](https://github.com/betagouv/rdv-service-public/issues/6315)
- **Information :** Ajout du nombre d’habitants de la commune dans la demande d’ouverture de compte. [#6321](https://github.com/betagouv/rdv-service-public/issues/6321)
- **Information :** Mise en valeur du choix de date et heure d'une plage. [#6292](https://github.com/betagouv/rdv-service-public/issues/6292)
