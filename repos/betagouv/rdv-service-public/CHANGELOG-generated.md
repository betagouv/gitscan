## Changelog : rdv-service-public (30 derniers jours, au 27 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité avec le renforcement de l'authentification à deux facteurs pour certains comptes, la correction de failles potentielles et la mise à jour des dépendances. Des améliorations ont également été apportées à l'expérience utilisateur, notamment dans la gestion des plages horaires, la recherche d'usagers et l'interface d'administration. Enfin, des corrections de bugs et des optimisations de performance ont été réalisées.

### Évolutions fonctionnelles
- **Authentification :** Mise en place de l'authentification à deux facteurs (2FA) pour les comptes sensibles ProConnect [#6335](https://github.com/betagouv/rdv-service-public/issues/6335) et pour certains IDP ProConnect [#6310](https://github.com/betagouv/rdv-service-public/issues/6310).
- **Gestion des espaces :** Correction de la création d'espaces via les OPSN [#6336](https://github.com/betagouv/rdv-service-public/issues/6336) et création automatique d'espace lors de l'activation de RDV-SP par un OPSN [#6304](https://github.com/betagouv/rdv-service-public/issues/6304).
- **Recherche d'usagers :** Possibilité de rechercher un usager dans une nouvelle organisation pour un territoire ayant déjà des usagers [#6327](https://github.com/betagouv/rdv-service-public/issues/6327).
- **Plages horaires :** Correction de l'affichage de la seconde période d'une plage [#6326](https://github.com/betagouv/rdv-service-public/issues/6326) et correction pour les récurrences sur les plages d'ouverture [#6329](https://github.com/betagouv/rdv-service-public/issues/6329).
- **Interface utilisateur :**
    - Passage des formulaires de création/édition d'agent au Design System Français (DSFR) [#6309](https://github.com/betagouv/rdv-service-public/issues/6309).
    - Amélioration de l'affichage de la sélection d'organisation avec un retour à l'accueil contextuel [#6301](https://github.com/betagouv/rdv-service-public/issues/6301).
    - Mise en valeur du choix de date et heure d'une plage [#6292](https://github.com/betagouv/rdv-service-public/issues/6292).
- **Notifications :** Envoi d'un email en cas de refus de demande d’ouverture de compte [#6278](https://github.com/betagouv/rdv-service-public/issues/6278) et information des agents de la mise en place de la double authentification [#6314](https://github.com/betagouv/rdv-service-public/issues/6314).
- **Informations espace :** Ajout du SIRET sur l’espace [#6302](https://github.com/betagouv/rdv-service-public/issues/6302) et du nombre d’habitants de la commune dans la demande d’ouverture de compte [#6321](https://github.com/betagouv/rdv-service-public/issues/6321).
- **Liste d'attente :** Possibilité de se désinscrire de la liste d’attente en un clic [#6288](https://github.com/betagouv/rdv-service-public/issues/6288).

### Évolutions techniques
- **Sécurité :** Mise à jour de Node en version 24 pour corriger des vulnérabilités [#6296](https://github.com/betagouv/rdv-service-public/issues/6296) et [#6299](https://github.com/betagouv/rdv-service-public/issues/6299).
- **API :** Ajout des champs de geocoding dans le blueprint users pour l'API V1 [#6337](https://github.com/betagouv/rdv-service-public/issues/6337) et ajout du champ `time_zone` dans l'API `rdvs` [#6340](https://github.com/betagouv/rdv-service-public/issues/6340).
- **Performance :** Limitation de l'usage mémoire par `FileAttenteJob` en le séparant en plusieurs jobs [#6324](https://github.com/betagouv/rdv-service-public/issues/6324) et rendu plus robuste de `FileAttenteJob` [#6322](https://github.com/betagouv/rdv-service-public/issues/6322).
- **Dépendances :** MAJ de `connection_pool` en v3.0 [#6333](https://github.com/betagouv/rdv-service-public/issues/6333) et de la gem `addressable` [#6318](https://github.com/betagouv/rdv-service-public/issues/6318).
- **Tests :** Correction de flaky specs avec l'utilisation de `travel_to` de Playwright [#6312](https://github.com/betagouv/rdv-service-public/issues/6312) et correction d'une flaky spec à cause d’un jour férié [#6323](https://github.com/betagouv/rdv-service-public/issues/6323) et [#6390](https://github.com/betagouv/rdv-service-public/issues/6390).

### Autres changements
- Suppression du markup Stimulus sur `_recurrence.html.slim` [#6291](https://github.com/betagouv/rdv-service-public/issues/6291).
- Suppression du feature flag `new planning` et des bandeaux de nouveautés [#6316](https://github.com/betagouv/rdv-service-public/issues/6316).
- Nettoyage du champ `notification_email` et suppression de la rétrocompatibilité API [#6281](https://github.com/betagouv/rdv-service-public/issues/6281).
- Documentation des cas d'erreur pour visioplainte [#6293](https://github.com/betagouv/rdv-service-public/issues/6293).
- Suppression du code de l'ancien calculateur de créneaux [#6295](https://github.com/betagouv/rdv-service-public/issues/6295).
- Correction d'une flaky spec à la maj Phonelib [#6308](https://github.com/betagouv/rdv-service-public/issues/6308).
- Mise à jour de phonelib pour prendre en compte les numéros récents, nouvelles données, indicatifs... [#6303](https://github.com/betagouv/rdv-service-public/issues/6303).
- Correction LAPINS-6SF [#6300](https://github.com/betagouv/rdv-service-public/issues/6300).
- Eviter `Notion::Api::Errors::TooManyRequests` [#6342](https://github.com/betagouv/rdv-service-public/issues/6342).
- Automatiquement sélectionner la barre de recherche usager [#6332](https://github.com/betagouv/rdv-service-public/issues/6332).
