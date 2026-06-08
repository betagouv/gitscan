## Changelog : rdv-service-public (30 derniers jours, au 4 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la synchronisation CalDAV, la gestion des comptes utilisateurs (agents et usagers), la sécurité et la correction de bugs. Des améliorations ont également été apportées à l'intégration avec ProConnect et l'espace opérateur ANCT, ainsi qu'à l'expérience utilisateur globale, notamment pour les numéros de téléphone et les motifs de rendez-vous.

### Évolutions fonctionnelles
- **Synchronisation CalDAV :** Ajout d'une étape de sélection d'agenda pour la synchronisation CalDAV [#6172](https://github.com/betagouv/rdv-service-public/issues/6172). Correction de l'activation de la synchronisation des données personnelles CalDAV [#6416](https://github.com/betagouv/rdv-service-public/issues/6416). Affichage des informations de l’usager dans la synchro Caldav [#6351](https://github.com/betagouv/rdv-service-public/issues/6351).
- **Comptes utilisateurs :**
    - Permet aux administrateurs d'organisation de désactiver la connexion par email lors de la prise de rendez-vous en ligne [#6381](https://github.com/betagouv/rdv-service-public/issues/6381).
    - Simplification de la création de comptes [#6363](https://github.com/betagouv/rdv-service-public/issues/6363).
    - Permet d'ouvrir des comptes aux services de l'état détectés via le fournisseur d'identité ProConnect [#6370](https://github.com/betagouv/rdv-service-public/issues/6370).
    - Correction de la demande d’ouverture de compte État [#6407](https://github.com/betagouv/rdv-service-public/issues/6407).
    - Possibilité de supprimer les comptes d'agents et d'usagers, avec traçabilité [#6399](https://github.com/betagouv/rdv-service-public/issues/6399).
- **ProConnect & Espace Opérateur ANCT :**
    - Permet d'utiliser des FS FranceConnect différents par domaine [#6401](https://github.com/betagouv/rdv-service-public/issues/6401).
    - Ajout de documentation pour debugger les réponses de l’API Espace Opérateur ANCT [#6390](https://github.com/betagouv/rdv-service-public/issues/6390).
    - L'espace opérateur ANCT renvoie uniquement les espaces avec un SIRET [#6373](https://github.com/betagouv/rdv-service-public/issues/6373).
- **Expérience utilisateur :**
    - Amélioration du message d'erreur pour les numéros de téléphone étrangers [#6403](https://github.com/betagouv/rdv-service-public/issues/6403).
    - Correctif pour éviter les absences récurrentes sur plusieurs jours [#6404](https://github.com/betagouv/rdv-service-public/issues/6404).
    - Ajout d'un texte pour inciter les agents à utiliser la fonctionnalité de rdv non notifiés au niveau des motifs [#6372](https://github.com/betagouv/rdv-service-public/issues/6372).
    - Remplacement des pictos sur la page d'accueil de RDVSP (gratuit devient sécurisé) [#6374](https://github.com/betagouv/rdv-service-public/issues/6374).
    - Ne pas afficher des numéros de téléphone vides [#6386](https://github.com/betagouv/rdv-service-public/issues/6386).
- **Divers :**
    - Le service "secrétariat" devient le rôle "agent d'accueil" [#6285](https://github.com/betagouv/rdv-service-public/issues/6285).
    - Arrêt d'encouragement des agents de RDV Aide Numérique à passer sur RDV Service Public [#6388](https://github.com/betagouv/rdv-service-public/issues/6388).

### Évolutions techniques
- **Sécurité :**
    - Fixer par hash les versions des GitHub Actions [#6412](https://github.com/betagouv/rdv-service-public/issues/6412).
    - Demande un code de vérification pour l’accès aux comptes sensibles [#6319](https://github.com/betagouv/rdv-service-public/issues/6319).
- **Infrastructure & Déploiement :**
    - Utilisation de refresh tokens lors de la migration d'instance [#6389](https://github.com/betagouv/rdv-service-public/issues/6389).
    - Mise à jour de Bundler (4.0.12) [#6402](https://github.com/betagouv/rdv-service-public/issues/6402).
- **Refactoring & Optimisations :**
    - Refactor préalable aux intervalles après les RDV [#6396](https://github.com/betagouv/rdv-service-public/issues/6396).
    - Ne plus polluer le namespace global (Tod::TimeOfDay) [#6410](https://github.com/betagouv/rdv-service-public/issues/6410).
    - Correction de l'usage de cleanup_preserved_jobs_before_seconds_ago (GoodJob) [#6408](https://github.com/betagouv/rdv-service-public/issues/6408).
- **Mises à jour de librairies :**
    - Mise à jour du DSFR View Components (5.0) [#6334](https://github.com/betagouv/rdv-service-public/issues/6334).
    - Mise à jour de JWT [#6385](https://github.com/betagouv/rdv-service-public/issues/6385).
    - Mise à jour d'omniauth-microsoft_graph [#6384](https://github.com/betagouv/rdv-service-public/issues/6384).
    - Mise à jour de premailer [#6375](https://github.com/betagouv/rdv-service-public/issues/6375).

### Autres changements
- Changement du lien de la feuille de route [#6415](https://github.com/betagouv/rdv-service-public/issues/6415).
- Correction d'une flaky spec liée aux prénoms aléatoires [#6411](https://github.com/betagouv/rdv-service-public/issues/6411).
- Correction de l’effet du bouton « Annuler » lors d’une annulation [#6409](https://github.com/betagouv/rdv-service-public/issues/6409).
- Ajout du nouveau domaine rdv.numerique.gouv.fr [#6397](https://github.com/betagouv/rdv-service-public/issues/6397).
- Correction de la bannière de prescription externe [#6398](https://github.com/betagouv/rdv-service-public/issues/6398).
- Ignorer les erreurs permanentes sur la synchro outlook [#6395](https://github.com/betagouv/rdv-service-public/issues/6395).
- Ne plus lever d’avertissement Sentry lorsque plusieurs potentialOperators ANCT correspondent [#6391](https://github.com/betagouv/rdv-service-public/issues/6391).
- Correction de la cohérence des listes de RDV avec plusieurs agents [#6371](https://github.com/betagouv/rdv-service-public/issues/6371).
- Afficher les noms des jours fériés [#6379](https://github.com/betagouv/rdv-service-public/issues/6379).
- Correction du job de synchronisation des nouveautés [#6378](https://github.com/betagouv/rdv-service-public/issues/6378).
- Liste des RDV : revenir à la page 1 quand on adapte la taille de page [#6354](https://github.com/betagouv/rdv-service-public/issues/6354).
- Débugger nos appels à l'espace opérateur et le doc de changelog [#6359](https://github.com/betagouv/rdv-service-public/issues/6359).
- Éviter `Notion::Api::Errors::TooManyRequests` [#6355](https://github.com/betagouv/rdv-service-public/issues/6355).
- Garder les mêmes ajustements d'interface entre les deux nouveaux noms de domaine [#6414](https://github.com/betagouv/rdv-service-public/issues/6414).
- Permettre d'envoyer des mails avec le nouveau nom de domaine [#6413](https://github.com/betagouv/rdv-service-public/issues/6413).
