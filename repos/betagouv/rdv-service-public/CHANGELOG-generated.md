## Changelog : rdv-service-public (30 derniers jours, au 17 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment pour les agents et les usagers lors de la prise de rendez-vous en ligne. Des corrections de bugs et des améliorations de la synchronisation CalDAV ont également été apportées. La migration vers le nouveau nom de domaine `rdv.numerique.gouv.fr` continue d'être prise en charge et améliorée.

### Évolutions fonctionnelles
- **Prise de rendez-vous :**
    - Amélioration de l'affichage des motifs de rendez-vous avec des cartes DSFR pour une meilleure lisibilité, tant pour les agents que pour les usagers. [#6437](https://github.com/betagouv/rdv-service-public/issues/6437) et [#6448](https://github.com/betagouv/rdv-service-public/issues/6448)
    - Ajout d'une flèche sur les cartes de motifs pour faciliter leur découverte. [#6429](https://github.com/betagouv/rdv-service-public/issues/6429)
    - Possibilité pour les administrateurs d'organisation de désactiver la connexion par email lors de la prise de rendez-vous en ligne. [#6381](https://github.com/betagouv/rdv-service-public/issues/6381)
    - Ajout d'instructions pour les usagers lors de la réservation en ligne. [#6431](https://github.com/betagouv/rdv-service-public/issues/6431)
- **Synchronisation CalDAV :**
    - Correction de la synchronisation CalDAV avec Zimbra. [#6417](https://github.com/betagouv/rdv-service-public/issues/6417)
    - Amélioration de l'affichage des informations de l'usager dans la synchronisation CalDAV. [#6351](https://github.com/betagouv/rdv-service-public/issues/6351)
    - Correction de l'activation des données personnelles synchronisées CalDAV. [#6416](https://github.com/betagouv/rdv-service-public/issues/6416)
    - Ajout d'une étape de sélection d'agenda pour la synchronisation CalDAV. [#6172](https://github.com/betagouv/rdv-service-public/issues/6172)
- **Autres :**
    - Affichage du nom de l'usager connecté. [#6452](https://github.com/betagouv/rdv-service-public/issues/6452)
    - Redirection automatique des agents de l’État vers le nouveau domaine. [#6422](https://github.com/betagouv/rdv-service-public/issues/6422)
    - Connexion ProConnect automatique. [#6420](https://github.com/betagouv/rdv-service-public/issues/6420)
    - Mise à jour des mentions légales pour le nom de domaine de la dinum. [#6442](https://github.com/betagouv/rdv-service-public/issues/6442)

### Évolutions techniques
- **Infrastructure :**
    - Utilisation de la stack `scalingo-24` dans les review apps. [#6439](https://github.com/betagouv/rdv-service-public/issues/6439)
- **Refactoring et amélioration du code :**
    - Suppression de commentaires RuboCop obsolètes. [#6445](https://github.com/betagouv/rdv-service-public/issues/6445)
    - Nettoyage de code inutilisé. [#6423](https://github.com/betagouv/rdv-service-public/issues/6423)
    - Refactor préalable aux intervalles après les RDV. [#6396](https://github.com/betagouv/rdv-service-public/issues/6396)
    - Correction de flaky specs des connections ActionCable. [#6426](https://github.com/betagouv/rdv-service-public/issues/6426)
    - Correction de flaky specs liées aux prénoms aléatoires. [#6411](https://github.com/betagouv/rdv-service-public/issues/6411)
- **Dépendances :**
    - Mise à jour de plusieurs dépendances : esbuild, net-imap, puma, view_component, omniauth-microsoft_graph, JWT.

### Autres changements
- Suppression de la contrainte d'unicité sur `Service#short_name`. [#6446](https://github.com/betagouv/rdv-service-public/issues/6446)
- Limitation de la longueur des noms de service. [#6430](https://github.com/betagouv/rdv-service-public/issues/6430)
- Création des 29 motifs France Service en un clic dans le super-admin. [#6406](https://github.com/betagouv/rdv-service-public/issues/6406)
- Ajout de min/max_public_booking_delay au blueprint des motifs. [#6432](https://github.com/betagouv/rdv-service-public/issues/6432)
- Correction de l'envoi d'emails de réinitialisation de mot de passe en cas d'absence d'adresse email. [#6447](https://github.com/betagouv/rdv-service-public/issues/6447)
- Ignorer les valeurs invalides injectées dans le formulaire de contact. [#6451](https://github.com/betagouv/rdv-service-public/issues/6451)
- Ajout d'un espace manquant dans le titre de page sur un motif. [#6365](https://github.com/betagouv/rdv-service-public/issues/6365)
- Ajout de doc pour debugger les réponses de l’API Espace Opérateur ANCT. [#6390](https://github.com/betagouv/rdv-service-public/issues/6390)
- Remplacement acronyme Mon Suivi Social. [#6419](https://github.com/betagouv/rdv-service-public/issues/6419)
- Ajout du nouveau Domain rdv.numerique.gouv.fr. [#6397](https://github.com/betagouv/rdv-service-public/issues/6397)
- Correction de l’effet du bouton « Annuler » lors d’une annulation. [#6409](https://github.com/betagouv/rdv-service-public/issues/6409)
- Correction de la demande d’ouverture de compte État. [#6407](https://github.com/betagouv/rdv-service-public/issues/6407)
- Correction des absences récurrentes sur plusieurs jours. [#6404](https://github.com/betagouv/rdv-service-public/issues/6404)
- Amélioration du message d'erreur pour les numéros de téléphone étrangers. [#6403](https://github.com/betagouv/rdv-service-public/issues/6403)
- Améliorations de la documentation et de l'environnement d'exemple pour ProConnect. [#6405](https://github.com/betagouv/rdv-service-public/issues/6405)
- Permettre d'utiliser des FS FranceConnect différents par domaine. [#6401](https://github.com/betagouv/rdv-service-public/issues/6401)
- Mise à jour du DSFR View Components (5.0). [#6334](https://github.com/betagouv/rdv-service-public/issues/6334)
- Ajout d’une étape de sélection agenda sync CalDAV. [#6172](https://github.com/betagouv/rdv-service-public/issues/6172)
- Correction de l'envoi de debug à Sentry lors d'erreurs Caldav au setup initial. [#6424](https://github.com/betagouv/rdv-service-public/issues/6424)
- Correction de l'usage de cleanup_preserved_jobs_before_seconds_ago (GoodJob). [#6408](https://github.com/betagouv/rdv-service-public/issues/6408)
- Fixer par hash les versions des GH Actions. [#6412](https://github.com/betagouv/rdv-service-public/issues/6412)
- Ne plus polluer le namespace global (Tod::TimeOfDay). [#6410](https://github.com/betagouv/rdv-service-public/issues/6410)
- Ajout d’une demande de code de vérification pour l’accès aux comptes sensibles. [#6319](https://github.com/betagouv/rdv-service-public/issues/6319)
- Correction du job de synchronisation des nouveautés. [#6378](https://github.com/betagouv/rdv-service-public/issues/6378)
- Correction de la bannière de prescription externe. [#6398](https://github.com/betagouv/rdv-service-public/issues/6398)
- Ignorer les erreurs permanentes sur la synchro outlook. [#6395](https://github.com/betagouv/rdv-service-public/issues/6395)
- Ne plus lever d’avertissement Sentry lorsque plusieurs potentialOperators ANCT correspondent. [#6391](https://github.com/betagouv/rdv-service-public/issues/6391)
- Mise à jour de la feuille de route. [#6415](https://github.com/betagouv/rdv-service-public/issues/6415)
- Permettre les numéros de téléphone des DROM pour les organisations. [#6400](https://github.com/betagouv/rdv-service-public/issues/6400)
- Utiliser des refresh tokens lors de la migration d'instance. [#6389](https://github.com/betagouv/rdv-service-public/issues/6389)
- Arrêter d'encourager les agents de RDV Aide Numérique à passer sur RDV Service Public. [#6388](https://github.com/betagouv/rdv-service-public/issues/6388)
- Ne pas afficher des numéros de téléphone vides. [#6386](https://github.com/betagouv/rdv-service-public/issues/6386)
- Clarifications de la page de détails des motifs. [#6433](https://github.com/betagouv/rdv-service-public/issues/6433)
- Utiliser un accordéon DSFR pour les composants d'historique de version et de notifs. [#6434](https://github.com/betagouv/rdv-service-public/issues/6434)
- Désactiver les rendez-vous d'accompagnement pour les espaces ouverts avec le compte opérateur. [#6435](https://github.com/betagouv/rdv-service-public/issues/6435)
- Temps de battement après les rendez-vous. [#6305](https://github.com/betagouv/rdv-service-public/issues/6305)
- Rendre obligatoire les champs de synchro Caldav. [#6428](https://github.com/betagouv/rdv-service-public/issues/6428)
