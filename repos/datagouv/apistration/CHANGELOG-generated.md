## Changelog : apistration (30 derniers jours, au 27 août 2026)

### Résumé
Ce mois-ci, Apistration a franchi une étape importante avec l'introduction de l'API "Fondations" (MI/SIAF) et la mise à jour de ses SDK (v0.3.0). Le projet a également bénéficié d'une refonte majeure de la gestion des identifiants pour renforcer la sécurité, ainsi que d'une automatisation accrue de la synchronisation des fiches avec data.gouv.fr.

### Évolutions fonctionnelles
- **Nouveaux services** : Ajout de l'API Fondations (MI/SIAF) en mode "prochainement disponible" et mise à jour de la documentation OpenAPI associée.
- **Amélioration de l'expérience utilisateur** : 
    - Clarification des libellés de civilité et passage de "nom de naissance" à "nom de famille" pour FranceConnect [#362](https://github.com/datagouv/apistration/pull/362), [#358](https://github.com/datagouv/apistration/pull/358).
    - Clarification des modalités d'appel et des accès éditeurs [#331](https://github.com/datagouv/apistration/pull/331).
- **Mises à jour métier** :
    - Actualisation des données pour le service Pass Sport (civilité, âge et quotient familial CNAF) [#342](https://github.com/datagouv/apistration/pull/342), [#320](https://github.com/datagouv/apistration/pull/320).
    - Support de l'année de campagne pour les services CNOUS [#360](https://github.com/datagouv/apistration/pull/360).
    - Ajout d'un avertissement concernant la disponibilité de la base élèves durant le mois d'août.

### Évolutions techniques
- **Synchronisation data.gouv.fr** : Implémentation d'un nouveau service de synchronisation des fiches, incluant une exécution automatique au démarrage du système et une meilleure gestion des redirections HTTP [#264](https://github.com/datagouv/apistration/pull/264).
- **Sécurité et Identifiants** : 
    - Migration massive de tous les identifiants clients (HubEE, INSEE, Mailjet, etc.) vers une nouvelle source centralisée et sécurisée [#311](https://github.com/datagouv/apistration/pull/311).
    - Renforcement de la sécurité des accès éditeurs via la restriction des adresses IP autorisées [#307](https://github.com/datagouv/apistration/pull/307).
    - Correction d'une vulnérabilité (CVE) sur la gestion des fichiers (ActiveStorage) [#312](https://github.com/datagouv/apistration/pull/312).
- **Fiabilité et Robustesse** :
    - Optimisation de la gestion des erreurs réseau (TLS/SSL) et meilleure classification des erreurs de la CNAV [#321](https://github.com/datagouv/apistration/pull/321).
    - Amélioration de la gestion des jetons (tokens) pour DataSubvention (mise en cache et tentatives de renouvellement automatique) [#357](https://github.com/datagouv/apistration/pull/357).
    - Durcissement de la validation des prénoms et de la civilité pour éviter les données erronées.
- **Infrastructure et CI/CD** : Extension de la suite de tests (mocks) pour inclure l'exécution automatique sur les pull requests, y compris celles provenant de forks [#329](https://github.com/datagouv/apistration/pull/329).

### Autres changements
- **Documentation** : Mise à jour des listes d'API FranceConnect et nettoyage des descriptions Swagger.
- **Maintenance** : Nettoyage des données de test obsolètes et optimisation des logs de synchronisation.
