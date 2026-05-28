## Changelog : rdv-service-public (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'intégration avec l'ANCT, la gestion des erreurs et la synchronisation des calendriers, ainsi que sur des corrections de bugs et des améliorations de l'expérience utilisateur, notamment au niveau de la création de comptes et de l'affichage d'informations. Des mises à jour de sécurité et de dépendances ont également été effectuées.

### Évolutions fonctionnelles
- **ANCT :** Amélioration de l'intégration avec l'API Espace Opérateur ANCT, incluant l'ajout de documentation pour le débogage des réponses ([#6390](https://github.com/betagouv/rdv-service-public/issues/6390)) et le passage des informations de l'opérateur en session pour une meilleure gestion ([#6362](https://github.com/betagouv/rdv-service-public/issues/6362)).
- **Authentification :** Possibilité pour les administrateurs d'organisation de désactiver la connexion par email lors de la prise de rendez-vous en ligne ([#6381](https://github.com/betagouv/rdv-service-public/issues/6381)). Ajout d'une demande de code de vérification pour l'accès aux comptes sensibles ([#6319](https://github.com/betagouv/rdv-service-public/issues/6319)).
- **Synchronisation Calendrier :** Affichage des informations de l’usager lors de la synchronisation Caldav ([#6351](https://github.com/betagouv/rdv-service-public/issues/6351)). Amélioration de la gestion des erreurs Caldav et distinction des statuts HTTP pour un meilleur suivi sur Sentry ([#6347](https://github.com/betagouv/rdv-service-public/issues/6347)).
- **Interface Utilisateur :** Remplacement des pictos sur la page d'accueil, avec un changement de "gratuit" à "sécurisé" ([#6374](https://github.com/betagouv/rdv-service-public/issues/6374)). Ajout d'un texte pour inciter les agents à utiliser la fonctionnalité de rendez-vous non notifiés ([#6372](https://github.com/betagouv/rdv-service-public/issues/6372)). Affichage des noms des jours fériés ([#6379](https://github.com/betagouv/rdv-service-public/issues/6379)).
- **Ouverture de comptes :** Permettre les ouvertures de comptes aux services de l'état détectés via le fournisseur d'identité ProConnect ([#6370](https://github.com/betagouv/rdv-service-public/issues/6370)). Simplification de la création de comptes ([#6363](https://github.com/betagouv/rdv-service-public/issues/6363)).

### Évolutions techniques
- **Mise à jour des dépendances :** Mise à jour de plusieurs dépendances, notamment `view_component`, `JWT`, `omniauth-microsoft_graph`, `DSFR View Components`, `nokogiri`, `net-imap`, `faraday` et `brace-expansion`.
- **Refactoring :** Refactor préalable aux intervalles après les RDV ([#6396](https://github.com/betagouv/rdv-service-public/issues/6396)).
- **Correction d'erreurs :** Correction d'une erreur sur la bannière de prescription externe ([#6398](https://github.com/betagouv/rdv-service-public/issues/6398)). Correction d'une incohérence dans les listes de RDV avec plusieurs agents ([#6371](https://github.com/betagouv/rdv-service-public/issues/6371)).
- **Synchronisation :** Utilisation de refresh tokens lors de la migration d'instance ([#6389](https://github.com/betagouv/rdv-service-public/issues/6389)). Correction du job de synchronisation des nouveautés ([#6378](https://github.com/betagouv/rdv-service-public/issues/6378)).
- **Sécurité :** Mise à jour de la gem Devise vers la version officielle ([#6345](https://github.com/betagouv/rdv-service-public/issues/6345)).

### Autres changements
- Ajout du nouveau domaine `rdv.numerique.gouv.fr` ([#6397](https://github.com/betagouv/rdv-service-public/issues/6397)).
- Le rôle "secrétariat" a été renommé "agent d'accueil" ([#6285](https://github.com/betagouv/rdv-service-public/issues/6285)).
- Correction des tokens d'invitation en minuscule dans les liens ([#6338](https://github.com/betagouv/rdv-service-public/issues/6338)).
- Ajout de `kmeet.infomaniak.com` aux domaines autorisés pour la visio custom ([#6357](https://github.com/betagouv/rdv-service-public/issues/6357)).
- Suppression d'un encouragement à utiliser RDV Service Public pour les agents RDV Aide Numérique ([#6388](https://github.com/betagouv/rdv-service-public/issues/6388)).
- Ne plus lever d’avertissement Sentry lorsque plusieurs potentialOperators ANCT correspondent ([#6391](https://github.com/betagouv/rdv-service-public/issues/6391)).
- Ignorer les erreurs permanentes sur la synchro outlook ([#6395](https://github.com/betagouv/rdv-service-public/issues/6395)).
- Correction d'un bug où deux éléments du menu étaient actifs en même temps ([#6330](https://github.com/betagouv/rdv-service-public/issues/6330)).
- Ajout d'un lien vers l’annuaire des entreprises pour les espaces dans le SuperAdmin ([#6352](https://github.com/betagouv/rdv-service-public/issues/6352)).
- Carto ANCT: renvoyer uniquement les espaces avec un SIRET ([#6373](https://github.com/betagouv/rdv-service-public/issues/6373)).
