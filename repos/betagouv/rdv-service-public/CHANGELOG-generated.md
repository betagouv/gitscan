## Changelog : rdv-service-public (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur et la correction de bugs, notamment concernant la gestion des rendez-vous, la synchronisation des calendriers et la création d'espaces. Des améliorations ont également été apportées à la sécurité et à la gestion des accès.

### Évolutions fonctionnelles
- Les informations de l'opérateur ANCT sont désormais stockées en session plutôt qu'en paramètres d'URL, améliorant ainsi la gestion de ces données. [#6362](https://github.com/betagouv/rdv-service-public/issues/6362)
- Un texte d'incitation a été ajouté pour encourager les agents à utiliser la fonctionnalité de rendez-vous non notifiés au niveau des motifs. [#6372](https://github.com/betagouv/rdv-service-public/issues/6372)
- Simplification du processus de création de comptes. [#6363](https://github.com/betagouv/rdv-service-public/issues/6363)
- Ajout d'un lien vers l’annuaire des entreprises pour les espaces dans le SuperAdmin. [#6352](https://github.com/betagouv/rdv-service-public/issues/6352)
- Ajout des champs de géocodage dans le blueprint users pour l'API V1. [#6337](https://github.com/betagouv/rdv-service-public/issues/6337)
- Ajout du champ `time_zone` dans l'API `rdvs`. [#6340](https://github.com/betagouv/rdv-service-public/issues/6340)
- Correction de la cohérence des listes de RDV avec plusieurs agents. [#6371](https://github.com/betagouv/rdv-service-public/issues/6371)
- Remplacement des pictos sur la page d'accueil de RDVSP, avec un changement de "gratuit" à "sécurisé". [#6374](https://github.com/betagouv/rdv-service-public/issues/6374)

### Évolutions techniques
- Le service "secrétariat" a été renommé "agent d’accueil" pour une meilleure clarté des rôles. [#6285](https://github.com/betagouv/rdv-service-public/issues/6285)
- Mise à jour des règles de refus d’ouverture d’espace pour une gestion plus précise. [#6368](https://github.com/betagouv/rdv-service-public/issues/6368)
- Correction d'un bug où deux éléments du menu pouvaient être actifs simultanément. [#6330](https://github.com/betagouv/rdv-service-public/issues/6330)
- Retour à la gem Devise officielle pour une meilleure stabilité. [#6345](https://github.com/betagouv/rdv-service-public/issues/6345)
- Correction d'un problème lié aux appels à l'espace opérateur et amélioration de la documentation du changelog. [#6359](https://github.com/betagouv/rdv-service-public/issues/6359)
- Carto ANCT: renvoie uniquement les espaces avec un SIRET. [#6373](https://github.com/betagouv/rdv-service-public/issues/6373)
- Correction de la création d’espace via les OPSN. [#6336](https://github.com/betagouv/rdv-service-public/issues/6336)

### Autres changements
- Ajout de `kmeet.infomaniak.com` aux domaines autorisés pour la visio personnalisée. [#6357](https://github.com/betagouv/rdv-service-public/issues/6357)
- Indication du statut des synchronisations de calendrier. [#6353](https://github.com/betagouv/rdv-service-public/issues/6353)
- Mise à jour de Premailer. [#6375](https://github.com/betagouv/rdv-service-public/issues/6375)
- Correction des tokens d'invitation en minuscule dans les liens. [#6338](https://github.com/betagouv/rdv-service-public/issues/6338)
- Mise en place du 2FA ProConnect uniquement pour les comptes sensibles. [#6335](https://github.com/betagouv/rdv-service-public/issues/6335)
- Correction d'un bug lié à la suppression d'événements Caldav externes. [#6348](https://github.com/betagouv/rdv-service-public/issues/6348)
- Revert d'une modification concernant la distinction des erreurs Caldav sur Sentry. [#6350](https://github.com/betagouv/rdv-service-public/issues/6350)
- Correction d'un problème lié à la pagination de la liste des RDV. [#6354](https://github.com/betagouv/rdv-service-public/issues/6354)
- Correction d'un problème lié aux erreurs `Notion::Api::Errors::TooManyRequests`. [#6355](https://github.com/betagouv/rdv-service-public/issues/6342)
