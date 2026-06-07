## Changelog : OpenGateLLM (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'améliorations significatives en termes de gestion des documents, de santé des modèles, de sécurité et de refactoring de l'architecture interne. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la performance de la plateforme. L'interface utilisateur a été enrichie avec l'ajout d'un bouton de copie pour les clés API.

### Évolutions fonctionnelles
- Ajout d'un bouton de copie pour faciliter la création et l'utilisation des clés API dans l'interface Playground. [#896](https://github.com/etalab-ia/OpenGateLLM/issues/896)
- Augmentation du temps de rafraîchissement d'Elasticsearch à 2 secondes pour une meilleure indexation. [#904](https://github.com/etalab-ia/OpenGateLLM/issues/904)
- Possibilité de téléverser des documents jusqu'à 20MB par document. [#902](https://github.com/etalab-ia/OpenGateLLM/issues/902)
- Ajout de limites de stockage pour les documents. [#899](https://github.com/etalab-ia/OpenGateLLM/issues/899)
- Gestion améliorée des réponses non-string de l'API Mistral. [#892](https://github.com/etalab-ia/OpenGateLLM/issues/892)

### Évolutions techniques
- Refactoring de plusieurs endpoints de l'API admin (utilisateurs, création d'utilisateurs) vers une architecture plus propre et maintenable. [#898](https://github.com/etalab-ia/OpenGateLLM/issues/898), [#893](https://github.com/etalab-ia/OpenGateLLM/issues/893), [#867](https://github.com/etalab-ia/OpenGateLLM/issues/867)
- Refactoring du code lié à la gestion des modèles, avec séparation des cas d'utilisation pour une meilleure organisation. [#890](https://github.com/etalab-ia/OpenGateLLM/issues/890)
- Implémentation d'un support de vérification de la santé des modèles. [#870](https://github.com/etalab-ia/OpenGateLLM/issues/870)
- Injection du contexte dans Langfuse pour un meilleur suivi et monitoring. [#889](https://github.com/etalab-ia/OpenGateLLM/issues/889)
- Amélioration de la configuration CI/CD avec l'ajout d'un fichier `.dockerignore` et l'optimisation du build. [#901](https://github.com/etalab-ia/OpenGateLLM/issues/901)
- Correction de problèmes liés à l'analyse de vulnérabilités avec Trivy, incluant l'ignorance de certaines CVE. [#874](https://github.com/etalab-ia/OpenGateLLM/issues/874), [#873](https://github.com/etalab-ia/OpenGateLLM/issues/873), [#872](https://github.com/etalab-ia/OpenGateLLM/issues/872)
- Renommage de certains repos et fichiers pour une meilleure cohérence. [#865](https://github.com/etalab-ia/OpenGateLLM/issues/865), [#864](https://github.com/etalab-ia/OpenGateLLM/issues/864)

### Autres changements
- Mise à jour de la documentation générée et des versions de publication. [#891](https://github.com/etalab-ia/OpenGateLLM/issues/891)
- Correction de l'URL de base pour Langfuse. [#868](https://github.com/etalab-ia/OpenGateLLM/issues/868)
