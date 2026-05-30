## Changelog : rdv-service-public (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des comptes utilisateurs et des organisations, ainsi que sur la stabilisation et le débogage de certaines fonctionnalités existantes, notamment la synchronisation des calendriers et l'intégration avec l'API Espace Opérateur ANCT. Des améliorations de sécurité ont également été apportées, notamment avec l'ajout d'une vérification à deux facteurs pour l'accès aux comptes sensibles.

### Évolutions fonctionnelles
- Les agents de RDV Aide Numérique sont désormais encouragés à migrer vers RDV Service Public. [#6388](https://github.com/betagouv/rdv-service-public/issues/6388)
- Les administrateurs d'organisation peuvent désormais désactiver la connexion par email lors de la prise de rendez-vous en ligne, renforçant ainsi la sécurité. [#6381](https://github.com/betagouv/rdv-service-public/issues/6381)
- Possibilité de créer des catégories de motifs automatiquement lors de l'activation d'ANTS Connectable dans la super admin. [#6394](https://github.com/betagouv/rdv-service-public/issues/6394)
- Ajout d'un texte d'incitation pour l'utilisation de la fonctionnalité de rendez-vous non notifiés au niveau des motifs. [#6372](https://github.com/betagouv/rdv-service-public/issues/6372)
- Les informations de l'usager sont désormais affichées lors de la synchronisation Caldav. [#6351](https://github.com/betagouv/rdv-service-public/issues/6351)
- Affichage des noms des jours fériés dans l'application. [#6379](https://github.com/betagouv/rdv-service-public/issues/6379)
- Amélioration de l'interface utilisateur sur la page d'accueil, avec remplacement des pictos et modification du texte "gratuit" par "sécurisé". [#6374](https://github.com/betagouv/rdv-service-public/issues/6374)
- Possibilité d'ouvrir des comptes aux services de l'état détectés via le fournisseur d'identité ProConnect. [#6370](https://github.com/betagouv/rdv-service-public/issues/6370)

### Évolutions techniques
- Mise à jour de la gem JWT. [#6385](https://github.com/betagouv/rdv-service-public/issues/6385)
- Mise à jour du DSFR View Components vers la version 5.0. [#6334](https://github.com/betagouv/rdv-service-public/issues/6334)
- Mise à jour de la gem omniauth-microsoft_graph. [#6384](https://github.com/betagouv/rdv-service-public/issues/6384)
- Refactor préalable aux intervalles après les RDV pour faciliter les développements futurs. [#6396](https://github.com/betagouv/rdv-service-public/issues/6396)
- Utilisation de refresh tokens lors de la migration d'instance pour une meilleure sécurité et fiabilité. [#6389](https://github.com/betagouv/rdv-service-public/issues/6389)
- Retour à la gem Devise officielle pour une meilleure stabilité et compatibilité. [#6345](https://github.com/betagouv/rdv-service-public/issues/6345)
- Correction d'un problème de pagination dans la liste des RDV. [#6354](https://github.com/betagouv/rdv-service-public/issues/6354)

### Autres changements
- Ajout de documentation pour le débogage des réponses de l’API Espace Opérateur ANCT. [#6390](https://github.com/betagouv/rdv-service-public/issues/6390)
- Ajout du nouveau domaine rdv.numerique.gouv.fr. [#6397](https://github.com/betagouv/rdv-service-public/issues/6397)
- Correction d'une bannière de prescription externe. [#6398](https://github.com/betagouv/rdv-service-public/issues/6398)
- Suppression des comptes d'agents et d'usagers est maintenant traçable. [#6399](https://github.com/betagouv/rdv-service-public/issues/6399)
- Autorisation des numéros de téléphone des DROM pour les organisations. [#6400](https://github.com/betagouv/rdv-service-public/issues/6400)
- Mise à jour de la gem Bundler vers la version 4.0.12. [#6402](https://github.com/betagouv/rdv-service-public/issues/6402)
- Ajout d'une vérification à deux facteurs pour l'accès aux comptes sensibles. [#6319](https://github.com/betagouv/rdv-service-public/issues/6319)
- Correction du job de synchronisation des nouveautés. [#6378](https://github.com/betagouv/rdv-service-public/issues/6378)
- Mise à jour de premailer. [#6375](https://github.com/betagouv/rdv-service-public/issues/6375)
- Carto ANCT: renvoie uniquement les espaces avec un SIRET. [#6373](https://github.com/betagouv/rdv-service-public/issues/6373)
- Le service secretariat devient le rôle agent d’accueil. [#6285](https://github.com/betagouv/rdv-service-public/issues/6285)
- Correction de la cohérence des listes de RDV avec plusieurs agents. [#6371](https://github.com/betagouv/rdv-service-public/issues/6371)
- Simplification de la création de comptes. [#6363](https://github.com/betagouv/rdv-service-public/issues/6363)
- Ajout de `kmeet.infomaniak.com` aux domaines autorisés en visio custom. [#6357](https://github.com/betagouv/rdv-service-public/issues/6357)
- Indiquer le statut des synchros de calendrier. [#6353](https://github.com/betagouv/rdv-service-public/issues/6353)
- Passage des infos opérateur depuis l’API ANCT en session plutôt qu'en params. [#6362](https://github.com/betagouv/rdv-service-public/issues/6362)
- Ignorer les erreurs permanentes sur la synchro outlook. [#6395](https://github.com/betagouv/rdv-service-public/issues/6395)
- Ne plus lever d’avertissement Sentry lorsque plusieurs potentialOperators ANCT correspondent. [#6391](https://github.com/betagouv/rdv-service-public/issues/6391)
- Ne pas afficher des numéros de téléphone vides. [#6386](https://github.com/betagouv/rdv-service-public/issues/6386)
