## Changelog : OpenGateLLM (30 derniers jours)

### Résumé
Ce mois-ci, OpenGateLLM a connu une importante évolution vers une architecture plus propre et plus maintenable, avec une refactorisation majeure des routes et des endpoints. De nouvelles fonctionnalités ont été ajoutées, notamment la gestion des chunks et l'amélioration des capacités de recherche, tandis que des fonctionnalités plus anciennes sont dépréciées pour simplifier le code et l'expérience utilisateur. Des corrections de bugs et des améliorations de la surveillance ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un endpoint POST `/v1/chunks` pour la gestion des chunks de documents [#660](https://github.com/etalab-ia/OpenGateLLM/issues/660).
- Amélioration de la recherche avec l'ajout d'un filtre sur les métadonnées [#700](https://github.com/etalab-ia/OpenGateLLM/issues/700).
- Possibilité d'ordonner les résultats lors de la récupération des collections et des documents via les paramètres `order_by` et `order_direction` [#709](https://github.com/etalab-ia/OpenGateLLM/issues/709).
- Intégration du support des modèles de rerank vLLM [#719](https://github.com/etalab-ia/OpenGateLLM/issues/719).
- Ajout d'une fonctionnalité de recherche intégrée dans l'interface de chat [#708](https://github.com/etalab-ia/OpenGateLLM/issues/708).
- Correction du streaming des réponses du chat [#692](https://github.com/etalab-ia/OpenGateLLM/issues/692).
- Correction de la gestion du seuil dans la recherche [#684](https://github.com/etalab-ia/OpenGateLLM/issues/684).
- Ajout de métriques orientées LLM au tableau de bord Grafana [#768](https://github.com/etalab-ia/OpenGateLLM/issues/768).
- Correction d'un bug lié aux métriques avec plusieurs workers [#681](https://github.com/etalab-ia/OpenGateLLM/issues/681).
- Ajout d'un CLI pour interagir avec l'API [#713](https://github.com/etalab-ia/OpenGateLLM/issues/713).
- Amélioration de la gestion des erreurs de configuration [#672](https://github.com/etalab-ia/OpenGateLLM/issues/672).
- Ajout de verbose_json et désactivation de giscus sur la page d'index de la documentation, et retour de l'email dans get collection [#774](https://github.com/etalab-ia/OpenGateLLM/issues/774).
- Adaptation du sérialiseur Mistral pour formater correctement la réponse [#773](https://github.com/etalab-ia/OpenGateLLM/issues/773).

### Évolutions techniques
- Refactorisation majeure de l'architecture vers une approche plus propre, incluant les routes et les endpoints [#718](https://github.com/etalab-ia/OpenGateLLM/issues/718), [#764](https://github.com/etalab-ia/OpenGateLLM/issues/764), [#767](https://github.com/etalab-ia/OpenGateLLM/issues/767), [#707](https://github.com/etalab-ia/OpenGateLLM/issues/707), [#691](https://github.com/etalab-ia/OpenGateLLM/issues/691), [#658](https://github.com/etalab-ia/OpenGateLLM/issues/658).
- Simplification de la méthode de recherche Elasticsearch [#763](https://github.com/etalab-ia/OpenGateLLM/issues/763).
- Suppression du helper de registre des routes [#697](https://github.com/etalab-ia/OpenGateLLM/issues/697).

### Autres changements
- Dépréciation des endpoints `/v1/files` et `/v1/ocr-beta` [#698](https://github.com/etalab-ia/OpenGateLLM/issues/698).
- Dépréciation de la fonctionnalité ProConnect [#693](https://github.com/etalab-ia/OpenGateLLM/issues/693).
- Dépréciation du paramètre `k` dans l'endpoint `/v1/search` [#694](https://github.com/etalab-ia/OpenGateLLM/issues/694).
- Dépréciation des arguments legacy du rerank [#705](https://github.com/etalab-ia/OpenGateLLM/issues/705).
- Mise à jour de la documentation et des liens [#772](https://github.com/etalab-ia/OpenGateLLM/issues/772).
- Mise à jour des modèles de templates d'issues [#711](https://github.com/etalab-ia/OpenGateLLM/issues/711).
- Suppression du fichier `import_circular_diagram.md` [#699](https://github.com/etalab-ia/OpenGateLLM/issues/699).
- Suppression du répertoire `docs/node_modules` [#769](https://github.com/etalab-ia/OpenGateLLM/issues/769).
- Déploiement de la documentation [#770](https://github.com/etalab-ia/OpenGateLLM/issues/770) et mise à jour des versions [#771](https://github.com/etalab-ia/OpenGateLLM/issues/771).
