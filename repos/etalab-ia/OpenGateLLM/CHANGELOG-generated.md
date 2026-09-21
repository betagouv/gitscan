## Changelog : OpenGateLLM (30 derniers jours, au 18/09/2026)

### Résumé
Ce mois-ci, OpenGateLLM a franchi une étape majeure avec une refonte profonde de son architecture vers le modèle "Clean Architecture" pour améliorer la maintenabilité et la robustesse du système. Parallèlement, l'expérience utilisateur a été enrichie par de meilleures capacités de suivi de consommation, un Playground amélioré et un contrôle plus fin de la limitation de débit (rate-limiting).

### Évolutions fonctionnelles
- **Amélioration du Playground** : Refonte du design, correction de la pagination via le champ `total` de l'API et résolution de problèmes de liens URL ([#1094](https://github.com/etalab-ia/OpenGateLLM/issues/1094), [#983](https://github.com/etalab-ia/OpenGateLLM/issues/983), [#1096](https://github.com/etalab-ia/OpenGateLLM/issues/1096)).
- **Suivi et Monitoring** : Ajout de buckets de consommation quotidienne dans l'API d'usage ([#1107](https://github.com/etalab-ia/OpenGateLLM/issues/1107)) et mise à disposition de nouveaux templates Grafana pour le monitoring du trafic et de l'inférence ([#903](https://github.com/etalab-ia/OpenGateLLM/issues/903)).
- **Contrôle d'accès et limites** : L'appartenance à une organisation est désormais obligatoire pour les utilisateurs ([#1137](https://github.com/etalab-ia/OpenGateLLM/issues/1137)). Le système de rate-limiting est plus précis en comptabilisant les tokens de sortie ([#1077](https://github.com/etalab-ia/OpenGateLLM/issues/1077)) et en rejetant les prompts trop volumineux avant l'appel au fournisseur ([#1088](https://github.com/etalab-ia/OpenGateLLM/issues/1088)).
- **Simplification de l'API** : Renommage des endpoints pour une meilleure clarté (ex: `/v1/me/info` devient `/v1/me`) ([#1033](https://github.com/etalab-ia/OpenGateLLM/issues/1033)).
- **Administration** : Renforcement de la validation des champs lors des mises à jour via l'interface d'administration ([#1053](https://github.com/etalab-ia/OpenGateLLM/issues/1053)).

### Évolutions techniques
- **Migration vers la Clean Architecture** : Refonte massive de la structure interne pour isoler la logique métier, touchant les endpoints de chat ([#1138](https://github.com/etalab-ia/OpenGateLLM/issues/1138), [#1140](https://github.com/etalab-ia/OpenGateLLM/issues/1140)), la gestion des organisations ([#1041](https://github.com/etalab-ia/OpenGateLLM/issues/1041), [#1050](https://github.com/etalab-ia/OpenGateLLM/issues/1050), [#1057](https://github.com/etalab-ia/OpenGateLLM/issues/1057), [#1080](https://github.com/etalab-ia/OpenGateLLM/issues/1080)), la gestion des clés/utilisateurs ([#1024](https://github.com/etalab-ia/OpenGateLLM/issues/1024), [#1038](https://github.com/etalab-ia/OpenGateLLM/issues/1038), [#1039](https://github.com/etalab-ia/OpenGateLLM/issues/1039)) et l'usage ([#1045](https://github.com/etalab-ia/OpenGateLLM/issues/1045)).
- **Simplification de l'infrastructure** : Suppression de la gestion de la QoS via Celery et RabbitMQ pour réduire la complexité opérationnelle ([#1131](https://github.com/etalab-ia/OpenGateLLM/issues/1131)).
- **Optimisations de la couche de données** : Adoption de la syntaxe Pydantic v3 ([#1070](https://github.com/etalab-ia/OpenGateLLM/issues/1070)), refactorisation de la couche PostgreSQL pour plus de performance ([#1072](https://github.com/etalab-ia/OpenGateLLM/issues/1072)) et standardisation de la gestion des dates dans toute l'application ([#1062](https://github.com/etalab-ia/OpenGateLLM/issues/1062)).
- **CI/CD et Sécurité** : Amélioration de l'exécution des tests en CI et mise à jour des scans de sécurité ([#1043](https://github.com/etalab-ia/OpenGateLLM/issues/1043), [#1078](https://github.com/etalab-ia/OpenGateLLM/issues/1078)).

### Autres changements
- **Documentation** : Mise à jour du guide de démarrage rapide (support ARM64 et dépendances CLI) ([#1116](https://github.com/etalab-ia/OpenGateLLM/issues/1116)) et ajout de documents d'architecture (ADR) concernant la nouvelle stratégie de QoS ([#1123](https://github.com/etalab-ia/OpenGateLLM/issues/1123)).
- **Configuration** : Ajout de Jinja2 aux dépendances du projet ([#1122](https://github.com/etalab-ia/OpenGateLLM/issues/1122)).
