## Changelog : rdv-service-public (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la synchronisation CalDAV, la gestion des comptes utilisateurs (simplification de la création, suppression traçable, accès via ProConnect), et la correction de plusieurs bugs affectant l'interface utilisateur et la stabilité du service. Des améliorations de sécurité ont également été apportées, notamment concernant les accès aux comptes sensibles et la fixation des versions des dépendances.

### Évolutions fonctionnelles
- **Comptes utilisateurs :**
  - Simplification du processus de création de compte. [#6363](https://github.com/betagouv/rdv-service-public/issues/6363)
  - Possibilité pour les administrateurs d'organisation de désactiver la connexion par email lors de la prise de rendez-vous en ligne. [#6381](https://github.com/betagouv/rdv-service-public/issues/6381)
  - Les suppressions de comptes d'agents et d'usagers sont désormais traçables. [#6399](https://github.com/betagouv/rdv-service-public/issues/6399)
  - Prise en charge des numéros de téléphone des DROM pour les organisations. [#6400](https://github.com/betagouv/rdv-service-public/issues/6400)
  - Possibilité d'ouvrir des comptes pour les services de l'état détectés via ProConnect. [#6370](https://github.com/betagouv/rdv-service-public/issues/6370)
- **Synchronisation CalDAV :**
  - Correction de la synchronisation CalDAV avec Zimbra. [#6417](https://github.com/betagouv/rdv-service-public/issues/6417)
  - Ajout d’une étape de sélection d’agenda pour la synchronisation CalDAV. [#6172](https://github.com/betagouv/rdv-service-public/issues/6172)
  - Correction de l’activation des données personnelles synchronisées CalDAV. [#6416](https://github.com/betagouv/rdv-service-public/issues/6416)
  - Affichage des informations de l’usager dans la synchronisation Caldav. [#6351](https://github.com/betagouv/rdv-service-public/issues/6351)
- **Interface utilisateur :**
  - Amélioration du message d'erreur pour les numéros de téléphone étrangers. [#6403](https://github.com/betagouv/rdv-service-public/issues/6403)
  - Remplacement de l'acronyme "Mon Suivi Social". [#6419](https://github.com/betagouv/rdv-service-public/issues/6419)
  - Mise à jour des pictos sur la page d'accueil (gratuit devient sécurisé). [#6374](https://github.com/betagouv/rdv-service-public/issues/6374)
  - Ajout d'un texte pour inciter les agents à utiliser la fonctionnalité de rdv non notifiés au niveau des motifs. [#6372](https://github.com/betagouv/rdv-service-public/issues/6372)
- **Autres:**
  - Temps de battement configurable après les rendez-vous. [#6305](https://github.com/betagouv/rdv-service-public/issues/6305)
  - Correction de l'effet du bouton « Annuler » lors d’une annulation. [#6409](https://github.com/betagouv/rdv-service-public/issues/6409)
  - Correction pour éviter les absences récurrentes sur plusieurs jours. [#6404](https://github.com/betagouv/rdv-service-public/issues/6404)

### Évolutions techniques
- **Sécurité :**
  - Fixation par hash des versions des GitHub Actions. [#6412](https://github.com/betagouv/rdv-service-public/issues/6412)
  - Demande d'un code de vérification pour l'accès aux comptes sensibles. [#6319](https://github.com/betagouv/rdv-service-public/issues/6319)
- **Infrastructure & Dépendances :**
  - Mise à jour de la version de bundler. [#6402](https://github.com/betagouv/rdv-service-public/issues/6402)
  - Mise à jour de la version de DSFR Form Builder. [#6356](https://github.com/betagouv/rdv-service-public/issues/6356)
  - Mise à jour des versions de JWT, Omniauth-Microsoft Graph et Premailer. [#6385](https://github.com/betagouv/rdv-service-public/issues/6385), [#6375](https://github.com/betagouv/rdv-service-public/issues/6375), [#6383](https://github.com/betagouv/rdv-service-public/issues/6383)
  - Mise à jour du DSFR View Components (5.0). [#6334](https://github.com/betagouv/rdv-service-public/issues/6334)
- **Architecture & Performance :**
  - Refactor préalable aux intervalles après les rendez-vous. [#6396](https://github.com/betagouv/rdv-service-public/issues/6396)
  - Correction d'une flaky spec liée aux prénoms aléatoires. [#6411](https://github.com/betagouv/rdv-service-public/issues/6411)
  - Correction de l'usage de cleanup_preserved_jobs_before_seconds_ago (GoodJob). [#6408](https://github.com/betagouv/rdv-service-public/issues/6408)
  - Ne plus polluer le namespace global (Tod::TimeOfDay). [#6410](https://github.com/betagouv/rdv-service-public/issues/6410)
  - Désactivation des règles Metrics de Rubocop. [#6392](https://github.com/betagouv/rdv-service-public/issues/6392)
- **Intégrations:**
  - Ajout du nouveau domaine rdv.numerique.gouv.fr. [#6397](https://github.com/betagouv/rdv-service-public/issues/6397)
  - Permettre d'utiliser des FS FranceConnect différents par domaine. [#6401](https://github.com/betagouv/rdv-service-public/issues/6401)

### Autres changements
- Envoi de debug à Sentry lors d'erreurs Caldav au setup initial. [#6424](https://github.com/betagouv/rdv-service-public/issues/6424)
- Ajout de documentation pour debugger les réponses de l’API Espace Opérateur ANCT. [#6390](https://github.com/betagouv/rdv-service-public/issues/6390)
- Correction demande d’ouverture de compte État. [#6407](https://github.com/betagouv/rdv-service-public/issues/6407)
- Mise à jour du lien de la feuille de route. [#6415](https://github.com/betagouv/rdv-service-public/issues/6415)
- Nettoyage de code inutilisé. [#6423](https://github.com/betagouv/rdv-service-public/issues/6423)
- Correction de la cohérence des listes de RDV avec plusieurs agents. [#6371](https://github.com/betagouv/rdv-service-public/issues/6371)
- Correction de la synchro outlook pour ignorer les erreurs permanentes. [#6395](https://github.com/betagouv/rdv-service-public/issues/6395)
- Correction du job de synchronisation des nouveautés. [#6378](https://github.com/betagouv/rdv-service-public/issues/6378)
- Correction d'un bug où Sentry levait un avertissement lorsque plusieurs potentialOperators ANCT correspondaient. [#6391](https://github.com/betagouv/rdv-service-public/issues/6391)
- Correction d'un bug lié à la liste des RDV et à l'adaptation de la taille de page. [#6354](https://github.com/betagouv/rdv-service-public/issues/6354)
- Le service "secrétariat" devient le rôle "agent d'accueil". [#6285](https://github.com/betagouv/rdv-service-public/issues/6285)
- Carto ANCT: renvoyer uniquement les espaces avec un SIRET. [#6373](https://github.com/betagouv/rdv-service-public/issues/6373)
- Utiliser des refresh tokens lors de la migration d'instance. [#6389](https://github.com/betagouv/rdv-service-public/issues/6389)
- Arrêter d'encourager les agents de RDV Aide Numérique à passer sur RDV Service Public. [#6388](https://github.com/betagouv/rdv-service-public/issues/6388)
- Bannière de prescription externe corrigée. [#6398](https://github.com/betagouv/rdv-service-public/issues/6398)
- Améliorations de la documentation et de l'environnement sample pour ProConnect. [#6405](https://github.com/betagouv/rdv-service-public/issues/6405)
