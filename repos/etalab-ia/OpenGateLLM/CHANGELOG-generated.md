## Changelog : OpenGateLLM (30 derniers jours, au 17 août 2026)

### Résumé
Ce mois a été marqué par un effort important de restructuration interne pour améliorer la maintenabilité du projet via l'adoption d'une "Clean Architecture". Les utilisateurs bénéficieront également d'une sécurité renforcée lors de l'authentification et de corrections sur l'interface du Playground.

### Évolutions fonctionnelles
- **Sécurité** : Amélioration de la protection contre l'énumération d'utilisateurs en retournant des messages d'erreur génériques lors des échecs d'authentification ([#963](https://github.com/etalab-ia/OpenGateLLM/issues/963)).
- **Interface (Playground)** : Correction du formulaire d'authentification dans le Playground via l'utilisation de Reflex ([#981](https://github.com/etalab-ia/OpenGateLLM/issues/981)).
- **Données** : Amélioration de la précision de l'affichage des impacts environnementaux en privilégiant la valeur `0.0` au lieu de `None` ([#990](https://github.com/etalab-ia/OpenGateLLM/issues/990)).

### Évolutions techniques
- **Refactoring (Clean Architecture)** : Migration de plusieurs points de terminaison critiques vers une architecture propre pour faciliter l'évolution du code :
    - Endpoint OCR ([#984](https://github.com/etalab-ia/OpenGateLLM/issues/984))
    - Gestion des utilisateurs administrateurs ([#962](https://github.com/etalab-ia/OpenGateLLM/issues/962))
    - Gestion des tokens d'administration ([#947](https://github.com/etalab-ia/OpenGateLLM/issues/947))
- **CI/CD et Tests** : 
    - Stabilisation de la pipeline CI/CD avec l'installation des dépendances manquantes pour les tests de bout en bout (E2E) ([#968](https://github.com/etalab-ia/OpenGateLLM/issues/968), [#964](https://github.com/etalab-ia/OpenGateLLM/issues/964)).
    - Résolution de blocages de scans de sécurité (Trivy) liés à des vulnérabilités CVE sur `perl-base` ([#969](https://github.com/etalab-ia/OpenGateLLM/issues/969)).
    - Intégration de tests de configuration héritée ([#991](https://github.com/etalab-ia/OpenGateLLM/issues/991)).
- **Monitoring et Modèles** :
    - Amélioration du suivi dans Langfuse pour inclure les requêtes non-streaming ([#987](https://github.com/etalab-ia/OpenGateLLM/issues/987)).
    - Optimisation de la construction du corps des requêtes de modèles ([#977](https://github.com/etalab-ia/OpenGateLLM/issues/977)).
    - Suppression du composant `ModelProviderGateway` pour simplifier l'architecture ([#972](https://github.com/etalab-ia/OpenGateLLM/issues/972)).

### Autres changements
- **Documentation** : 
    - Mise à jour de la documentation générée et des versions de release ([#975](https://github.com/etalab-ia/OpenGateLLM/issues/975)).
    - Ajout d'une décision d'architecture (ADR) concernant la segmentation du RAG ([#971](https://github.com/etalab-ia/OpenGateLLM/issues/971)).
- **Configuration** : Mise à jour des variables d'environnement par défaut dans l'exemple de configuration ([#974](https://github.com/etalab-ia/OpenGateLLM/issues/974)).
