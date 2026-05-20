## Changelog : rdv-service-public (30 derniers jours, au 19 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité, l'expérience utilisateur et l'intégration avec des services tiers. Des améliorations ont été apportées à l'authentification, à la gestion des comptes et à la synchronisation des calendriers. Des corrections de bugs et des optimisations ont également été réalisées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- **Authentification renforcée:** Une demande de code de vérification est désormais exigée pour accéder aux comptes sensibles, améliorant ainsi la sécurité. [#6319](https://github.com/betagouv/rdv-service-public/issues/6319)
- **Ouverture de comptes simplifiée:** Les agents de l'état peuvent désormais ouvrir des comptes via le fournisseur d'identité ProConnect. [#6370](https://github.com/betagouv/rdv-service-public/issues/6370)
- **Gestion des organisations:** Les administrateurs d'organisation peuvent désactiver la connexion par email lors de la prise de rendez-vous en ligne. [#6381](https://github.com/betagouv/rdv-service-public/issues/6381)
- **Informations utilisateur synchronisées Caldav:** Les informations de l’usager sont maintenant affichées lors de la synchronisation Caldav. [#6351](https://github.com/betagouv/rdv-service-public/issues/6351)
- **Affichage des jours fériés:** Les noms des jours fériés sont désormais affichés dans l'application. [#6379](https://github.com/betagouv/rdv-service-public/issues/6379)
- **Amélioration de la création de comptes:** Simplification du processus de création de comptes. [#6363](https://github.com/betagouv/rdv-service-public/issues/6363)
- **Rôle "agent d'accueil":** Le service "secrétariat" a été renommé "agent d’accueil". [#6285](https://github.com/betagouv/rdv-service-public/issues/6285)
- **API : Champs de géocodage:** Ajout des champs de géocodage dans le blueprint users pour l'API V1. [#6337](https://github.com/betagouv/rdv-service-public/issues/6337)
- **API : Champ time_zone:** Ajout du champ `time_zone` dans l'API `rdvs`. [#6340](https://github.com/betagouv/rdv-service-public/issues/6340)

### Évolutions techniques
- **Mise à jour des dépendances:**
    - Mise à jour de la version JWT. [#6385](https://github.com/betagouv/rdv-service-public/issues/6385)
    - Mise à jour des composants DSFR (version 5.0). [#6334](https://github.com/betagouv/rdv-service-public/issues/6334)
    - Mise à jour d'omniauth-microsoft_graph. [#6384](https://github.com/betagouv/rdv-service-public/issues/6384)
    - Mise à jour de premailer. [#6375](https://github.com/betagouv/rdv-service-public/issues/6375)
- **Synchronisation Caldav:** Correction du job de synchronisation des nouveautés Caldav. [#6378](https://github.com/betagouv/rdv-service-public/issues/6378)
- **Correction d'un bug de menu:** Correction d'un bug où deux éléments du menu pouvaient être actifs simultanément. [#6330](https://github.com/betagouv/rdv-service-public/issues/6330)
- **Retour à Devise officielle:** Reversion à la gem Devise officielle. [#6345](https://github.com/betagouv/rdv-service-public/issues/6345)

### Autres changements
- **Correction d'affichage:** Ne pas afficher les numéros de téléphone vides. [#6386](https://github.com/betagouv/rdv-service-public/issues/6386)
- **Amélioration de l'API ANCT:** Passage des informations opérateur depuis l’API ANCT en session plutôt qu'en paramètres. [#6362](https://github.com/betagouv/rdv-service-public/issues/6362)
- **Carto ANCT:** La carto ANCT renvoie désormais uniquement les espaces avec un SIRET. [#6373](https://github.com/betagouv/rdv-service-public/issues/6373)
- **Ajout d'une incitation:** Ajout d'un texte pour inciter les agents à utiliser la fonctionnalité de rdv non notifiés au niveau des motifs. [#6372](https://github.com/betagouv/rdv-service-public/issues/6372)
- **Correction de la liste des RDV:** Correction de la cohérence des listes de RDV avec plusieurs agents. [#6371](https://github.com/betagouv/rdv-service-public/issues/6371)
- **Correction des tokens d'invitation:** Les tokens d'invitation sont désormais en minuscule dans les liens. [#6338](https://github.com/betagouv/rdv-service-public/issues/6338)
- **Ajout d'un domaine autorisé:** Ajout de `kmeet.infomaniak.com` aux domaines autorisés en visio custom. [#6357](https://github.com/betagouv/rdv-service-public/issues/6357)
- **Amélioration du statut des synchros:** Indiquer le statut des synchros de calendrier. [#6353](https://github.com/betagouv/rdv-service-public/issues/6353)
- **Correction d'une erreur Caldav:** Correction d'une erreur liée à la suppression d'événements Caldav externes. [#6348](https://github.com/betagouv/rdv-service-public/issues/6348)
- **Revert d'une correction Caldav:** Annulation d'une correction précédente concernant les erreurs Caldav sur Sentry. [#6350](https://github.com/betagouv/rdv-service-public/issues/6350)
- **Correction de la pagination:** Correction d'un bug de pagination dans la liste des RDV. [#6354](https://github.com/betagouv/rdv-service-public/issues/6354)
- **Débug des appels API:** Débug des appels à l'espace opérateur et mise à jour de la documentation du changelog. [#6359](https://github.com/betagouv/rdv-service-public/issues/6359)
