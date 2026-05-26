## Changelog : rdv-service-public (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment en matière de connexion et de gestion des comptes, ainsi que sur la robustesse du service avec des corrections de bugs et des améliorations de la synchronisation des calendriers. Des efforts ont également été faits pour faciliter l'intégration avec d'autres services et pour améliorer la gestion des erreurs.

### Évolutions fonctionnelles
- **Connexion et comptes :**
    - Possibilité pour les administrateurs d'organisation de désactiver la connexion par email lors de la prise de rendez-vous en ligne. [#6381](https://github.com/betagouv/rdv-service-public/issues/6381)
    - Simplification de la création de comptes. [#6363](https://github.com/betagouv/rdv-service-public/issues/6363)
    - Permettre l'ouverture de comptes aux services de l'état détectés via le fournisseur d'identité ProConnect. [#6370](https://github.com/betagouv/rdv-service-public/issues/6370)
- **Expérience utilisateur :**
    - Affichage des noms des jours fériés. [#6379](https://github.com/betagouv/rdv-service-public/issues/6379)
    - Amélioration de l'affichage des listes de RDV avec plusieurs agents. [#6371](https://github.com/betagouv/rdv-service-public/issues/6371)
    - Ajout d'un texte pour inciter les agents à utiliser la fonctionnalité de RDV non notifiés au niveau des motifs. [#6372](https://github.com/betagouv/rdv-service-public/issues/6372)
    - Remplacement des pictos sur la page d'accueil de RDVSP, avec un focus sur la sécurité. [#6374](https://github.com/betagouv/rdv-service-public/issues/6374)
    - Ne plus afficher des numéros de téléphone vides. [#6386](https://github.com/betagouv/rdv-service-public/issues/6386)
- **Intégrations :**
    - Ajout de `kmeet.infomaniak.com` aux domaines autorisés pour la visio custom. [#6357](https://github.com/betagouv/rdv-service-public/issues/6357)
- **Synchronisation Caldav :**
    - Affichage des informations de l’usager dans la synchronisation Caldav. [#6351](https://github.com/betagouv/rdv-service-public/issues/6351)

### Évolutions techniques
- **Sécurité :**
    - Demande d'un code de vérification pour l'accès aux comptes sensibles. [#6319](https://github.com/betagouv/rdv-service-public/issues/6319)
    - Mise à jour de la version de JWT. [#6385](https://github.com/betagouv/rdv-service-public/issues/6385)
    - Mise à jour du DSFR View Components (version 5.0). [#6334](https://github.com/betagouv/rdv-service-public/issues/6334)
    - Mise à jour d'Omniauth-Microsoft_Graph. [#6384](https://github.com/betagouv/rdv-service-public/issues/6384)
- **Architecture et infrastructure :**
    - Utilisation de refresh tokens lors de la migration d'instance. [#6389](https://github.com/betagouv/rdv-service-public/issues/6389)
    - Passage des informations opérateur depuis l’API ANCT en session plutôt qu'en paramètres. [#6362](https://github.com/betagouv/rdv-service-public/issues/6362)
    - Retour à la gem Devise officielle. [#6345](https://github.com/betagouv/rdv-service-public/issues/6345)
- **Corrections et améliorations :**
    - Correction du job de synchronisation des nouveautés. [#6378](https://github.com/betagouv/rdv-service-public/issues/6378)
    - Correction d'un bug où deux éléments du menu étaient actifs en même temps. [#6330](https://github.com/betagouv/rdv-service-public/issues/6330)
    - Correction des tokens d'invitation en minuscule dans les liens. [#6338](https://github.com/betagouv/rdv-service-public/issues/6338)
    - Correction d'un problème où la page retournait à la page 1 après adaptation de la taille de page. [#6354](https://github.com/betagouv/rdv-service-public/issues/6354)
    - Ne plus lever d’avertissement Sentry lorsque plusieurs potentialOperators ANCT correspondent. [#6391](https://github.com/betagouv/rdv-service-public/issues/6391)

### Autres changements
- Mise à jour des règles de refus d’ouverture d’espace. [#6368](https://github.com/betagouv/rdv-service-public/issues/6368)
- Le service "secrétariat" devient le rôle "agent d’accueil". [#6285](https://github.com/betagouv/rdv-service-public/issues/6285)
- Ajout d'un lien vers l’annuaire des entreprises pour les espaces dans le SuperAdmin. [#6352](https://github.com/betagouv/rdv-service-public/issues/6352)
- Carto ANCT: renvoyer uniquement les espaces avec un SIRET. [#6373](https://github.com/betagouv/rdv-service-public/issues/6373)
- Mise à jour de premailer. [#6375](https://github.com/betagouv/rdv-service-public/issues/6375)
