## Changelog : menshen (30 derniers jours, au 05/11/2026)

### Résumé
Cette période a été marquée par un renforcement significatif de la sécurité, notamment via le hachage des jetons au repos et la correction de nombreuses vulnérabilités. Le client Python a été modernisé pour supporter l'asynchrone, et l'observabilité du système a été améliorée grâce à une meilleure intégration de Sentry.

### Évolutions fonctionnelles
- **Sécurité renforcée** : 
    - Hachage des jetons échangés au repos avec HMAC-SHA256.
    - Restriction de la révocation des jetons au seul service source.
    - Meilleure gestion des utilisateurs inactifs et des tentatives d'introspection suspectes.
- **Amélioration du client Python** :
    - Ajout d'un client asynchrone (`TokenExchangeAsyncClient`).
    - Support du gestionnaire de contexte (`with`) pour une meilleure gestion du cycle de vie du client.
    - Ajout d'un timeout par défaut pour les requêtes POST.
- **Configuration et flexibilité** :
    - Possibilité de configurer les URLs de la documentation API (OpenAPI et interactive).
    - Ajout de la configuration du logger `lasuite` dans les paramètres.
- **Modèle de données** : Évolution du pattern des scopes de jetons vers le format `service:resource:action`.
- **Environnement de test (Playground)** : Enrichissement du playground avec des tests de bout en bout (E2E) et l'intégration du client menshen.

### Évolutions techniques
- **Refonte du client Python** : Migration de la bibliothèque `requests` vers `httpx` et extraction de la logique commune dans un client de base pour plus de modularité.
- **Maintenance de sécurité** : Mise à jour massive des dépendances pour corriger 42 vulnérabilités (CVE).
- **Infrastructure et CI/CD** :
    - Mise à jour des images Docker de base vers Python 3.14.10.
    - Amélioration de la compatibilité ascendante de Python.
    - Optimisation des actions GitHub et de la configuration de l'environnement de build.
- **Observabilité** : Ajout de paramètres de configuration pour le traçage et le profilage via Sentry.
- **Backend** : Optimisation de la signature des méthodes des services de base et correction de migrations de données liées aux jetons hachés.

### Autres changements
- **Documentation** : Simplification de la documentation concernant l'intégration de `lasuite`.
- **Nettoyage** : Correction de warnings de typage, de fautes de frappe et de la structure des modules du client.
