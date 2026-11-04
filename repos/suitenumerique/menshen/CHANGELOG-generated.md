## Changelog : menshen (30 derniers jours, au 03/11/2026)

### Résumé
Cette période a été marquée par un renforcement majeur de la sécurité (correction de nombreuses vulnérabilités et hachage des jetons) et une modernisation de la bibliothèque client Python pour supporter l'asynchrone. Le projet a également amélioré sa robustesse grâce à l'ajout de tests de bout en bout (E2E) et une meilleure gestion des erreurs de sécurité.

### Évolutions fonctionnelles
- **Nouveau format de permissions** : Adoption d'un nouveau pattern pour les scopes de jetons suivant le modèle `service:resource:action`.
- **Améliorations du client Python** :
  - Ajout du support asynchrone avec `TokenExchangeAsyncClient`.
  - Possibilité d'utiliser le client comme gestionnaire de contexte (context manager).
  - Ajout d'un timeout par défaut pour les requêtes POST.
- **Configuration de l'API** : Possibilité de configurer les URLs de la documentation API et de contrôler l'activation/désactivation du schéma OpenAPI.
- **Logging** : Ajout de la configuration du logger `lasuite` directement dans les paramètres du projet.

### Évolutions techniques
- **Sécurité** :
  - Correction de 42 vulnérabilités (CVE) via la mise à jour des dépendances.
  - Hachage des jetons échangés au repos avec l'algorithme HMAC-SHA256.
  - Suppression de certificats racines non sécurisés (emSign) des dépendances.
- **Refactorisation du client** :
  - Migration de la bibliothèque de transport de `requests` vers `httpx`.
  - Extraction de la logique métier indépendante du transport dans un client de base.
  - Renommage du module `client` en `clients` pour une meilleure clarté.
- **Backend & Architecture** :
  - Amélioration de la gestion des utilisateurs inactifs et des tentatives d'introspection suspectes.
  - Mise à jour de `django-lasuite` vers la version 1.0.0.
  - Optimisation de la signature des méthodes des services de base.
  - Correction de la migration des données de jetons hachés.
- **Tests & CI/CD** :
  - Ajout de tests de bout en bout (E2E) pour le playground et Keycloak.
  - Intégration de linters et de configurations de tests plus strictes.
  - Mise à jour des workflows GitHub Actions.

### Autres changements
- **Documentation** : Simplification de la documentation d'intégration avec `lasuite` et mise à jour des notes sur la migration du mocking HTTP.
- **Maintenance** : Nettoyage du code (correction de fautes de frappe et de warnings de typage).
