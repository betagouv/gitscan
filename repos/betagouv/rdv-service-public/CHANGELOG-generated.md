## Changelog : rdv-service-public (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment en simplifiant la création de comptes et en affichant des informations plus claires sur les synchronisations de calendriers. Des corrections ont également été apportées pour améliorer la stabilité et la fiabilité du service, en particulier concernant la gestion des rendez-vous et des erreurs Caldav. Des améliorations techniques ont été réalisées pour optimiser l'intégration avec l'annuaire des entreprises et les opérateurs de services publics.

### Évolutions fonctionnelles
- Simplification du processus de création de compte pour les agents. [#6363](https://github.com/betagouv/rdv-service-public/pull/6363)
- Ajout d'un texte d'incitation pour encourager l'utilisation de la fonctionnalité de rendez-vous non notifiés au niveau des motifs. [#6372](https://github.com/betagouv/rdv-service-public/pull/6372)
- Amélioration de la cohérence de l'affichage des listes de rendez-vous avec plusieurs agents. [#6371](https://github.com/betagouv/rdv-service-public/pull/6371)
- Remplacement des pictos sur la page d'accueil, avec un changement de "gratuit" à "sécurisé". [#6374](https://github.com/betagouv/rdv-service-public/pull/6374)
- Ajout d'un lien vers l'annuaire des entreprises pour les espaces dans le SuperAdmin. [#6352](https://github.com/betagouv/rdv-service-public/pull/6352)
- Indication du statut des synchronisations de calendrier pour une meilleure visibilité. [#6353](https://github.com/betagouv/rdv-service-public/pull/6353)
- Possibilité de rechercher des usagers dans une nouvelle organisation pour un territoire ayant déjà des usagers. [#6327](https://github.com/betagouv/rdv-service-public/pull/6327)
- Ajout du champ `time_zone` dans l'API `rdvs`. [#6340](https://github.com/betagouv/rdv-service-public/pull/6340)
- Correction des tokens d'invitation qui sont maintenant en minuscule dans les liens. [#6338](https://github.com/betagouv/rdv-service-public/pull/6338)

### Évolutions techniques
- Passage des informations opérateur depuis l’API ANCT en session plutôt qu'en paramètres. [#6362](https://github.com/betagouv/rdv-service-public/pull/6362)
- Mise à jour des règles de refus d’ouverture d’espace. [#6368](https://github.com/betagouv/rdv-service-public/pull/6368)
- Le rôle "secrétariat" est maintenant "agent d’accueil". [#6285](https://github.com/betagouv/rdv-service-public/pull/6285)
- Retour à la gem Devise officielle. [#6345](https://github.com/betagouv/rdv-service-public/pull/6345)
- Mise à jour de `connection_pool` en v3.0. [#6333](https://github.com/betagouv/rdv-service-public/pull/6333)
- Passage à Node24 dans les jobs GitHub Actions. [#6331](https://github.com/betagouv/rdv-service-public/pull/6331)
- Correction de la création d’espace via les OPSN. [#6336](https://github.com/betagouv/rdv-service-public/pull/6336)
- Correction des récurrences sur les plages d'ouverture. [#6329](https://github.com/betagouv/rdv-service-public/pull/6329)
- Ajout des champs de geocoding dans le blueprint users pour l'API V1. [#6337](https://github.com/betagouv/rdv-service-public/pull/6337)

### Autres changements
- Mise à jour de premailer. [#6375](https://github.com/betagouv/rdv-service-public/pull/6375)
- Carto ANCT: renvoi uniquement des espaces avec un SIRET. [#6373](https://github.com/betagouv/rdv-service-public/pull/6373)
- Ajout de `kmeet.infomaniak.com` aux domaines autorisés en visio custom. [#6357](https://github.com/betagouv/rdv-service-public/pull/6357)
- Correction d'un bug où deux éléments du menu étaient actifs en même temps. [#6330](https://github.com/betagouv/rdv-service-public/pull/6330)
- Suppression d'un revert concernant les erreurs Caldav. [#6350](https://github.com/betagouv/rdv-service-public/pull/6350)
- Correction d'un problème où la page retournait à la page 1 lors de l'adaptation de la taille de page. [#6354](https://github.com/betagouv/rdv-service-public/pull/6354)
- Correction d'un bug lié aux appels à l'espace opérateur et mise à jour du changelog. [#6359](https://github.com/betagouv/rdv-service-public/pull/6359)
- Implémentation de la 2FA ProConnect uniquement pour les comptes sensibles. [#6310](https://github.com/betagouv/rdv-service-public/pull/6310)
- Correction d'un problème lié à `Notion::Api::Errors::TooManyRequests`. [#6355](https://github.com/betagouv/rdv-service-public/pull/6355) et [#6342](https://github.com/betagouv/rdv-service-public/pull/6342)
- Sélection automatique de la barre de recherche usager. [#6332](https://github.com/betagouv/rdv-service-public/pull/6332)
