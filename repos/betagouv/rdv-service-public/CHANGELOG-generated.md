## Changelog : rdv-service-public (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment pour les agents et les usagers. On note l'ajout de nouvelles fonctionnalités comme la création simplifiée de services et de motifs, l'amélioration de la synchronisation CalDAV, et des corrections de bugs pour une meilleure stabilité et fiabilité du service. La migration vers un nouveau nom de domaine a également été préparée et implémentée.

### Évolutions fonctionnelles
- **Gestion des services :** Les administrateurs d'espace peuvent désormais créer un nouveau service directement depuis l'interface. [#6455](https://github.com/betagouv/rdv-service-public/issues/6455)
- **Recherche de créneaux :** L'interface de recherche de créneaux pour les agents a été améliorée avec l'utilisation de cartes DSFR pour une meilleure présentation. [#6437](https://github.com/betagouv/rdv-service-public/issues/6437)
- **Motifs de rendez-vous :**
    - Ajout d'une flèche sur les cartes de motifs pour faciliter leur découverte. [#6429](https://github.com/betagouv/rdv-service-public/issues/6429)
    - Utilisation de cartes DSFR pour le choix des motifs lors de la création d'un nouveau rendez-vous collectif. [#6448](https://github.com/betagouv/rdv-service-public/issues/6448)
    - Clarification de la page de détails des motifs. [#6433](https://github.com/betagouv/rdv-service-public/issues/6433)
    - Possibilité de créer 29 motifs France Service en un seul clic dans l'interface super-admin. [#6406](https://github.com/betagouv/rdv-service-public/issues/6406)
- **Synchronisation CalDAV :** Amélioration de la synchronisation CalDAV avec Zimbra et correction de bugs liés à l'activation des données personnelles et à l'effet du bouton "Annuler". [#6416](https://github.com/betagouv/rdv-service-public/issues/6416), [#6407](https://github.com/betagouv/rdv-service-public/issues/6407), [#6417](https://github.com/betagouv/rdv-service-public/issues/6417)
- **Nom de domaine :** Préparation et implémentation du nouveau nom de domaine rdv.numerique.gouv.fr. [#6397](https://github.com/betagouv/rdv-service-public/issues/6397)
- **Informations usager :** Affichage du nom de l'usager connecté. [#6452](https://github.com/betagouv/rdv-service-public/issues/6452)
- **Instructions de réservation :** Ajout d'instructions pour les usagers lors de la réservation en ligne. [#6431](https://github.com/betagouv/rdv-service-public/issues/6431)
- **Numéros de téléphone :** Amélioration du message d'erreur pour les numéros de téléphone étrangers. [#6403](https://github.com/betagouv/rdv-service-public/issues/6403)

### Évolutions techniques
- **Authentification :**
    - Connexion automatique via ProConnect. [#6420](https://github.com/betagouv/rdv-service-public/issues/6420)
    - Redirection automatique des agents de l’État vers le nouveau domaine. [#6422](https://github.com/betagouv/rdv-service-public/issues/6422)
    - Possibilité d'utiliser différents fournisseurs FranceConnect par domaine. [#6401](https://github.com/betagouv/rdv-service-public/issues/6401)
- **Infrastructure :** Utilisation de la stack `scalingo-24` pour les review apps. [#6439](https://github.com/betagouv/rdv-service-public/issues/6439)
- **Tests :** Correction de flaky specs liées aux connections ActionCable et aux prénoms aléatoires. [#6426](https://github.com/betagouv/rdv-service-public/issues/6426), [#6411](https://github.com/betagouv/rdv-service-public/issues/6411)
- **Sécurité :** Fixation par hash des versions des GitHub Actions pour renforcer la sécurité. [#6412](https://github.com/betagouv/rdv-service-public/issues/6412)
- **Refactoring :** Refactor préalable aux intervalles après les RDV. [#6396](https://github.com/betagouv/rdv-service-public/issues/6396)
- **Suppression de code obsolète :** Nettoyage d'un peu de code inutilisé. [#6423](https://github.com/betagouv/rdv-service-public/issues/6423)

### Autres changements
- **Documentation :** Ajout de documentation pour debugger les réponses de l’API Espace Opérateur ANCT. [#6390](https://github.com/betagouv/rdv-service-public/issues/6390)
- **Configuration :** Mise à jour des mentions légales pour le nouveau nom de domaine de la dinum. [#6442](https://github.com/betagouv/rdv-service-public/issues/6442)
- **Corrections mineures :**
    - Ajout d'un espace manquant dans le titre de page sur un motif. [#6365](https://github.com/betagouv/rdv-service-public/issues/6365)
    - Suppression de commentaires Rubocop dépréciés. [#6445](https://github.com/betagouv/rdv-service-public/issues/6445)
    - Remplacement de l'acronyme "Mon Suivi Social". [#6419](https://github.com/betagouv/rdv-service-public/issues/6419)
    - Correction d'un bug empêchant l'envoi d'emails de réinitialisation de mot de passe sans adresse email. [#6447](https://github.com/betagouv/rdv-service-public/issues/6447)
    - Ignorer les valeurs invalides injectées dans le formulaire de contact. [#6451](https://github.com/betagouv/rdv-service-public/issues/6451)
    - Ignorer les benign errors lors de la création d'une plage par API. [#6461](https://github.com/betagouv/rdv-service-public/issues/6461)
    - Remplacer les ACR custom ProConnect par des ACR standards. [#6462](https://github.com/betagouv/rdv-service-public/issues/6462)
    - Désactiver les rendez-vous d'accompagnement pour les espaces ouverts avec le compte opérateur. [#6435](https://github.com/betagouv/rdv-service-public/issues/6435)
    - Retirer la contrainte d'unicité sur Service#short_name. [#6446](https://github.com/betagouv/rdv-service-public/issues/6446)
    - Limiter la longueur des noms de service. [#6430](https://github.com/betagouv/rdv-service-public/issues/6430)
    - Désactiver toutes les règles Metrics de rubocop. [#6392](https://github.com/betagouv/rdv-service-public/issues/6392)
    - Corriger les flaky spec des connections ActionCable. [#6426](https://github.com/betagouv/rdv-service-public/issues/6426)
    - Corriger l'usage de cleanup_preserved_jobs_before_seconds_ago (GoodJob). [#6408](https://github.com/betagouv/rdv-service-public/issues/6408)
    - Ne plus polluer le namespace global (Tod::TimeOfDay). [#6410](https://github.com/betagouv/rdv-service-public/issues/6410)
    - Correctif pour éviter les absences récurrentes sur plusieurs jours. [#6404](https://github.com/betagouv/rdv-service-public/issues/6404)
    - Ignorer les erreurs permanentes sur la synchro outlook. [#6395](https://github.com/betagouv/rdv-service-public/issues/6395)
    - Bannière de prescription externe corrigée. [#6398](https://github.com/betagouv/rdv-service-public/issues/6398)
