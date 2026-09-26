## Changelog : OpenGateLLM (30 derniers jours, au 24 septembre 2026)

### Résumé
Ce mois-ci, OpenGateLLM a franchi une étape importante avec la migration de plusieurs composants clés vers une architecture plus robuste ("Clean Architecture"). Les évolutions se concentrent sur une gestion plus fine des clés API, un contrôle accru de la consommation des modèles (rate limiting) et une meilleure visibilité sur l'usage via l'intégration de Langfuse.

### Évolutions fonctionnelles
- **Gestion des clés API** : Possibilité de révoquer, renommer et filtrer les clés par statut ([#1152](https://github.com/etalab-ia/OpenGateLLM/issues/1152), [#1076](https://github.com/etalab-ia/OpenGateLLM/issues/1076)) et correction de conflits de nommage ([#1134](https://github.com/etalab-ia/OpenGateLLM/issues/1134)).
- **Organisation et Utilisateurs** : L'appartenance à une organisation est désormais obligatoire pour les utilisateurs ([#1137](https://github.com/etalab-ia/OpenGateLLM/issues/1137)) et les utilisateurs authentifiés peuvent désormais consulter les détails de leur organisation ([#1149](https://github.com/etalab-ia/OpenGateLLM/issues/1149)).
- **Contrôle de consommation (Rate Limiting)** : Amélioration du calcul des limites (TPM/TPD) incluant les tokens de sortie ([#1077](https://github.com/etalab-ia/OpenGateLLM/issues/1077)) et rejet automatique des requêtes trop volumineuses avant l'appel au fournisseur ([#1088](https://github.com/etalab-ia/OpenGateLLM/issues/1088)).
- **Suivi de l'usage** : Ajout de la possibilité de récupérer les données de consommation par tranches journalières ([#1107](https://github.com/etalab-ia/OpenGateLLM/issues/1107)).
- **Interface Playground** : Amélioration du design visuel ([#1094](https://github.com/etalab-ia/OpenGateLLM/issues/1094)) et de la pagination ([#983](https://github.com/etalab-ia/OpenGateLLM/issues/983)).
- **Corrections et Schémas** : Validation plus stricte des emails (conversion en minuscules) et des types de modèles ([#1126](https://github.com/etalab-ia/OpenGateLLM/issues/1126)), ainsi que des corrections sur les endpoints d'administration ([#1048](https://github.com/etalab-ia/OpenGateLLM/issues/1048), [#1053](https://github.com/etalab-ia/OpenGateLLM/issues/1053)).

### Évolutions techniques
- **Migration vers la "Clean Architecture"** : Refonte structurelle majeure des endpoints de Chat completions ([#1138](https://github.com/etalab-ia/OpenGateLLM/issues/1138)), de la gestion des organisations ([#1080](https://github.com/etalab-ia/OpenGateLLM/issues/1080), [#1057](https://github.com/etalab-ia/OpenGateLLM/issues/1057)) et de l'intégration de Langfuse ([#1142](https://github.com/etalab-ia/OpenGateLLM/issues/1142)).
- **Observabilité** : Intégration de Langfuse comme source alternative de données d'usage ([#1168](https://github.com/etalab-ia/OpenGateLLM/issues/1168)) et amélioration de la précision du suivi (latence et échecs) ([#1165](https://github.com/etalab-ia/OpenGateLLM/issues/1165)).
- **Optimisation et Refactoring** : Suppression du code hérité (legacy) ([#1159](https://github.com/etalab-ia/OpenGateLLM/issues/1159)), simplification de la gestion de la QoS ([#1131](https://github.com/etalab-ia/OpenGateLLM/issues/1131)), optimisation de la couche de base de données PostgreSQL ([#1072](https://github.com/etalab-ia/OpenGateLLM/issues/1072), [#1067](https://github.com/etalab-ia/OpenGateLLM/issues/1067)) et adoption de la syntaxe Pydantic v3 ([#1070](https://github.com/etalab-ia/OpenGateLLM/issues/1070)).
- **Standardisation** : Harmonisation de la gestion des dates à travers l'API, le domaine et le Playground ([#1062](https://github.com/etalab-ia/OpenGateLLM/issues/1062)).

### Autres changements
- Mise à jour de la documentation technique et du guide de démarrage rapide ([#1116](https://github.com/etalab-ia/OpenGateLLM/issues/1116)).
- Nettoyage de divers marqueurs de code ([#1169](https://github.com/etalab-ia/OpenGateLLM/issues/1169)).
