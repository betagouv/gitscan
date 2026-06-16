## Changelog : OpenGateLLM (30 derniers jours, au 15 juin 2026)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'améliorations significatives en termes de gestion des modèles (santé des modèles, gestion des erreurs API), d'architecture interne pour une meilleure maintenabilité et de corrections de bugs pour améliorer l'expérience utilisateur. Des améliorations ont également été apportées à la gestion des documents et à la sécurité.

### Évolutions fonctionnelles
- Possibilité de rechercher des utilisateurs par adresse email. [#909](https://github.com/etalab-ia/OpenGateLLM/issues/909)
- Ajout d'un bouton de copie pour les clés API dans l'interface utilisateur. [#896](https://github.com/etalab-ia/OpenGateLLM/issues/896)
- Gestion des réponses non-string de l'API Mistral. [#892](https://github.com/etalab-ia/OpenGateLLM/issues/892)
- Ajout d'une limite de stockage pour les documents (20MB par document). [#902](https://github.com/etalab-ia/OpenGateLLM/issues/902)
- Implémentation d'un endpoint de vérification de la santé des modèles via `/metrics`. [#911](https://github.com/etalab-ia/OpenGateLLM/issues/911)

### Évolutions techniques
- Refactorisation importante de l'endpoint de rerank pour une architecture plus propre. [#905](https://github.com/etalab-ia/OpenGateLLM/issues/905)
- Refactorisation de plusieurs endpoints administratifs (utilisateurs, suppression d'utilisateurs) vers une architecture plus propre. [#898](https://github.com/etalab-ia/OpenGateLLM/issues/898), [#893](https://github.com/etalab-ia/OpenGateLLM/issues/893), [#867](https://github.com/etalab-ia/OpenGateLLM/issues/867)
- Séparation des use cases liés à la gestion des modèles. [#890](https://github.com/etalab-ia/OpenGateLLM/issues/890)
- Variable la fréquence de rafraîchissement d'Elasticsearch pour améliorer les performances. [#904](https://github.com/etalab-ia/OpenGateLLM/issues/904)
- Injection du contexte dans Langfuse pour le monitoring. [#889](https://github.com/etalab-ia/OpenGateLLM/issues/889)
- Déplacement des schémas d'administration dans un dossier dédié. [#928](https://github.com/etalab-ia/OpenGateLLM/issues/928)

### Autres changements
- Mise à jour de la documentation générée. [#915](https://github.com/etalab-ia/OpenGateLLM/issues/915), [#891](https://github.com/etalab-ia/OpenGateLLM/issues/891)
- Amélioration du CI/CD : ajout d'un fichier `.dockerignore` et optimisation de la construction des images Docker. [#901](https://github.com/etalab-ia/OpenGateLLM/issues/901), [#900](https://github.com/etalab-ia/OpenGateLLM/issues/900)
- Ignorer certaines vulnérabilités (CVE) dans les analyses de sécurité Trivy. [#874](https://github.com/etalab-ia/OpenGateLLM/issues/874), [#873](https://github.com/etalab-ia/OpenGateLLM/issues/873), [#872](https://github.com/etalab-ia/OpenGateLLM/issues/872)
- Mise à jour de dépendances : python-multipart et devalue. [#863](https://github.com/etalab-ia/OpenGateLLM/issues/863), [#869](https://github.com/etalab-ia/OpenGateLLM/issues/869)
