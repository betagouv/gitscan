## Changelog : apistration (30 derniers jours, au 10 août 2026)

### Résumé
Ce mois a été marqué par une évolution majeure de l'expérience "Éditeur", qui dispose désormais d'un espace dédié pour gérer ses propres accès, prolonger ses jetons (tokens) et configurer ses paramètres de sécurité en autonomie. Parallèlement, plusieurs API clés (CNOUS, Pass-Sport, Démarche numérique) ont été enrichies de nouvelles données ou fonctionnalités, tandis que la gestion interne des secrets et la précision des limitations de débit (throttling) ont été renforcées pour plus de robustesse.

### Évolutions fonctionnelles
- **Autonomie des Éditeurs** : 
    - Création d'un espace éditeur avec une page de paramètres dédiée et une navigation simplifiée.
    - Mise en place du self-service pour la prolongation des jetons d'accès [#252](https://github.com/datagouv/apistration/pull/252).
    - Possibilité pour les éditeurs de restreindre l'usage de leurs jetons à des plages d'adresses IP spécifiques [#307](https://github.com/datagouv/apistration/pull/307).
    - Meilleure visibilité sur les habilitations et les délégations de ressources.
- **Évolutions des API** :
    - **CNOUS** : Passage à la version 5 de l'API étudiant boursier, incluant désormais l'explication et l'exposition du numéro INE [#285](https://github.com/datagouv/apistration/pull/285).
    - **Pass-Sport** : Mise à jour des données concernant la civilité et le quotient familial (CNAF) pour les services CNAV [#320](https://github.com/datagouv/apistration/pull/320).
    - **Démarche numérique** : Ajout d'un nouveau webhook pour l'API Particulier [#266](https://github.com/datagouv/apistration/pull/266).
    - **DGFIP** : Clarification du titre de l'endpoint TVA pour préciser son périmètre intra-communautaire.
- **Amélioration de l'expérience utilisateur** :
    - Reclassification des erreurs CNAV (passage de 404 à 502) pour une meilleure interprétation technique [#321](https://github.com/datagouv/apistration/pull/321).
    - Ajout de points de terminaison (endpoints) "ping" dans les SDK Ruby et Node.js pour faciliter le diagnostic de connectivité.

### Évolutions techniques
- **Gestion des secrets et sécurité** :
    - Migration massive de l'utilisation des identifiants (HubEE, Mailjet, INSEE, etc.) vers une nouvelle source de gestion centralisée et sécurisée [#311](https://github.com/datagouv/apistration/pull/311).
    - Correction d'une vulnérabilité (CVE) sur la gestion des fichiers via ActiveStorage [#312](https://github.com/datagouv/apistration/pull/312).
- **Contrôle de flux (Throttling)** :
    - Implémentation d'un système de limitation de débit granulaire permettant de définir des dépassements (overrides) par endpoint ou par utilisateur/habilitation [#294](https://github.com/datagouv/apistration/pull/294).
- **Infrastructure et CI/CD** :
    - Amélioration du workflow de tests : les tests de mocks sont désormais exécutés sur les pull requests provenant de forks [#329](https://github.com/datagouv/apistration/pull/329).
    - Alignement du workflow de déploiement de l'environnement de staging avec celui du sandbox.

### Autres changements
- **Documentation** :
    - Enrichissement de la documentation sur l'intégration des éditeurs et sur la gestion des délégations.
    - Ajout d'une entrée FAQ concernant la typologie des numéros de TVA pour la DGFIP.
- **Maintenance** :
    - Régénération régulière des spécifications OpenAPI (Swagger) et des SDK pour intégrer les nouveaux paramètres (notamment le `delegation_id`).
    - Nettoyage du code via Rubocop.
