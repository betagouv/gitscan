## Changelog : apistration (30 derniers jours, au 17 septembre 2026)

### Résumé
Cette période a été marquée par un renforcement majeur de la fiabilité des intégrations avec des partenaires clés (INSEE, CNAV, associations) et une amélioration de la transparence pour les administrateurs. La plateforme a également franchi une étape importante dans la gestion des attestations (EAJE) avec l'introduction de documents PDF vérifiables et sécurisés.

### Évolutions fonctionnelles
- **Gestion des attestations (EAJE) :**
    - Introduction de la génération et du rendu de PDF d'attestation vérifiables. [#296](https://github.com/datagouv/apistration/pull/296)
    - Support des preuves d'attestation via des jetons chiffrés et via des en-têtes de requête.
    - Hébergement de la page de vérification des attestations directement sur l'application web.
- **Données Associations (MI/SIAF) :**
    - Ajout des points de terminaison (endpoints) pour les associations en mode "prochainement".
    - Mise à jour des SDK (v0.4.0) incluant les ressources liées aux associations.
- **Améliorations de l'interface d'administration :**
    - Meilleure visibilité pour le diagnostic : affichage des réponses brutes des fournisseurs dans le back-office. [#376](https://github.com/datagouv/apistration/pull/376)
    - Optimisation des requêtes manuelles : utilisation de listes déroulantes pour les valeurs énumérées OpenAPI et support d'en-têtes supplémentaires. [#410](https://github.com/datagouv/apistration/pull/410)
    - Amélioration de la lisibilité des verdicts de vérification et de l'alignement des champs de saisie.
- **Services tiers :**
    - Synchronisation automatique des fiches vers data.gouv.fr. [#344](https://github.com/datagouv/apistration/pull/344)
    - Amélioration de la gestion des campagnes CNOUS (prise en compte de l'année de campagne). [#360](https://github.com/datagouv/apistration/pull/360)

### Évolutions techniques
- **Sécurité et Authentification :**
    - Mise en place d'une rotation automatique des mots de passe pour l'authentification INSEE afin de renforcer la sécurité. [#383](https://github.com/datagouv/apistration/pull/383)
    - Gestion de la révocation des habilitations en cascade sur les délégations associées. [#397](https://github.com/datagouv/apistration/pull/397)
- **Fiabilité et Observabilité :**
    - Amélioration du suivi des erreurs (CNAV, quotient familial) avec une meilleure distinction des codes d'erreur fournisseurs dans les logs et Sentry. [#401](https://github.com/datagouv/apistration/pull/401)
    - Gestion robuste des erreurs de handshake TLS (conversion en erreur 502 propre).
    - Correction de la pagination des événements Sentry. [#403](https://github.com/datagouv/apistration/pull/403)
- **Infrastructure et CI/CD :**
    - Résolution de problèmes de concurrence (race conditions) dans les pipelines de déploiement. [#412](https://github.com/datagouv/apistration/pull/412)
    - Optimisation de la gestion des fichiers `robots.txt` pour restreindre l'indexation des environnements hors production. [#399](https://github.com/datagouv/apistration/pull/399)
- **Client Data.gouv.fr :**
    - Amélioration du client pour le suivi des redirections et la préservation des méthodes HTTP lors des appels. [#354](https://github.com/datagouv/apistration/pull/354)

### Autres changements
- **Documentation :**
    - Mise à jour des mentions légales. [#386](https://github.com/datagouv/apistration/pull/386)
    - Enrichissement de la documentation technique (régimes de formation MESRI, procédures d'investigation API-SECU, dictionnaire DGFiP).
    - Mise à jour des liens vers la documentation Sirene.
- **Nettoyage :**
    - Refactorisation des payloads SIAF pour une meilleure cohérence des clés et du vocabulaire.
