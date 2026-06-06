## Changelog : rdv-service-public (30 derniers jours, au 4 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la synchronisation CalDAV, la gestion des comptes utilisateurs (notamment pour les agents de l'État et via ProConnect), et la correction de plusieurs bugs affectant l'expérience utilisateur et la stabilité de la plateforme. Des améliorations de sécurité ont également été apportées, notamment concernant l'authentification et la gestion des versions des dépendances.

### Évolutions fonctionnelles
- **Synchronisation CalDAV :** Amélioration de la synchronisation CalDAV avec ajout d'une étape de sélection d'agenda et affichage des informations de l'usager. Correction d'un bug empêchant l'activation de la synchronisation des données personnelles. [#6172](https://github.com/betagouv/rdv-service-public/issues/6172), [#6416](https://github.com/betagouv/rdv-service-public/issues/6416), [#6351](https://github.com/betagouv/rdv-service-public/issues/6351)
- **Comptes utilisateurs :**
    - Simplification de la création de comptes. [#6363](https://github.com/betagouv/rdv-service-public/issues/6363)
    - Possibilité pour les administrateurs d'organisation de désactiver la connexion par email lors de la prise de rendez-vous en ligne. [#6381](https://github.com/betagouv/rdv-service-public/issues/6381)
    - Ouverture de comptes aux services de l'État détectés via le fournisseur d'identité ProConnect. [#6370](https://github.com/betagouv/rdv-service-public/issues/6370)
    - Correction de la demande d’ouverture de compte État. [#6407](https://github.com/betagouv/rdv-service-public/issues/6407)
- **Espace Opérateur ANCT :** Ajout de documentation pour le débogage des réponses de l’API Espace Opérateur ANCT. [#6390](https://github.com/betagouv/rdv-service-public/issues/6390)
- **Notifications :** Possibilité d'envoyer des mails avec le nouveau nom de domaine. [#6413](https://github.com/betagouv/rdv-service-public/issues/6413)
- **Interface utilisateur :**
    - Amélioration du message d'erreur pour les numéros de téléphone étrangers. [#6403](https://github.com/betagouv/rdv-service-public/issues/6403)
    - Remplacement des pictos sur la page d'accueil de RDVSP (gratuit devient sécurisé). [#6374](https://github.com/betagouv/rdv-service-public/issues/6374)
    - Ajout d'un texte pour inciter les agents à utiliser la fonctionnalité de rdv non notifiés au niveau des motifs. [#6372](https://github.com/betagouv/rdv-service-public/issues/6372)

### Évolutions techniques
- **Sécurité :**
    - Fixer par hash les versions des GitHub Actions pour renforcer la sécurité. [#6412](https://github.com/betagouv/rdv-service-public/issues/6412)
    - Demande d’un code de vérification pour l’accès aux comptes sensibles. [#6319](https://github.com/betagouv/rdv-service-public/issues/6319)
- **Infrastructure :** Utilisation de refresh tokens lors de la migration d'instance. [#6389](https://github.com/betagouv/rdv-service-public/issues/6389)
- **Refactoring :** Refactor préalable aux intervalles après les RDV. [#6396](https://github.com/betagouv/rdv-service-public/issues/6396)
- **Dépendances :** Mise à jour de plusieurs dépendances : View Component (4.6.0 -> 4.9.0), Bundler (4.0.12), Faraday (2.14.1 -> 2.14.2), Nokogiri (1.19.1 -> 1.19.3), JWT, DSFR View Components (5.0), omniauth-microsoft_graph.
- **GoodJob :** Correction de l'usage de `cleanup_preserved_jobs_before_seconds_ago`. [#6408](https://github.com/betagouv/rdv-service-public/issues/6408)

### Autres changements
- Changement du lien de la feuille de route. [#6415](https://github.com/betagouv/rdv-service-public/issues/6415)
- Correction d'une flaky spec liée aux prénoms aléatoires. [#6411](https://github.com/betagouv/rdv-service-public/issues/6411)
- Suppression des pollutions du namespace global (Tod::TimeOfDay). [#6410](https://github.com/betagouv/rdv-service-public/issues/6410)
- Correction d'un bug sur la bannière de prescription externe. [#6398](https://github.com/betagouv/rdv-service-public/issues/6398)
- Ajout de catégories de motifs lorsque `ants_connectable` est activé dans la super admin. [#6394](https://github.com/betagouv/rdv-service-public/issues/6394)
- Ignorer les erreurs permanentes sur la synchro outlook. [#6395](https://github.com/betagouv/rdv-service-public/issues/6395)
- Ne plus lever d’avertissement Sentry lorsque plusieurs potentialOperators ANCT correspondent. [#6391](https://github.com/betagouv/rdv-service-public/issues/6391)
- Arrêter d'encourager les agents de RDV Aide Numérique à passer sur RDV Service Public. [#6388](https://github.com/betagouv/rdv-service-public/issues/6388)
- Ne pas afficher des numéros de téléphone vides. [#6386](https://github.com/betagouv/rdv-service-public/issues/6386)
- Correction sur les absences récurrentes sur plusieurs jours. [#6404](https://github.com/betagouv/rdv-service-public/issues/6404)
- Correction d'une incohérence dans les listes de RDV avec plusieurs agents. [#6371](https://github.com/betagouv/rdv-service-public/issues/6371)
- Correction de l'effet du bouton « Annuler » lors d’une annulation. [#6409](https://github.com/betagouv/rdv-service-public/issues/6409)
- Afficher les noms des jours fériés. [#6379](https://github.com/betagouv/rdv-service-public/issues/6379)
- Correction du job de synchronisation des nouveautés. [#6378](https://github.com/betagouv/rdv-service-public/issues/6378)
- Le service secretariat devient le rôle agent d’accueil. [#6285](https://github.com/betagouv/rdv-service-public/issues/6285)
- Liste des RDV : revenir à la page 1 quand on adapte la taille de page. [#6354](https://github.com/betagouv/rdv-service-public/issues/6354)
- Débugger nos appels à l'espace opérateur et le doc de changelog. [#6359](https://github.com/betagouv/rdv-service-public/issues/6359)
- Carto ANCT: renvoyer uniquement les espaces avec un SIRET. [#6373](https://github.com/betagouv/rdv-service-public/issues/6373)
