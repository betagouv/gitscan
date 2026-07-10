## Changelog : OpenGateRAG (30 derniers jours, au 8 juillet 2026)

### Résumé
Ce mois-ci, OpenGateRAG a connu une phase d'initialisation et de stabilisation importante. Le projet a été mis en place avec une base solide, incluant des tests unitaires et de bout en bout, ainsi qu'une intégration continue/déploiement (CI/CD). Des corrections ont été apportées pour assurer le bon fonctionnement des tests, du déploiement et des endpoints. L'API a été unifiée avec OpenGateLLM pour une meilleure cohérence.

### Évolutions fonctionnelles
- Unification de la documentation OpenAPI avec OpenGateLLM [#3](https://github.com/etalab-ia/OpenGateRAG/issues/3).
- Ajout de tests de bout en bout (E2E) pour valider le fonctionnement de l'application [#1](https://github.com/etalab-ia/OpenGateRAG/issues/1).
- Ajout de tests unitaires pour améliorer la couverture et la fiabilité du code [#3](https://github.com/etalab-ia/OpenGateRAG/issues/3).
- Correction de l'accès au contrôleur (accesscontroler) pour garantir la sécurité et le bon fonctionnement des endpoints [#2](https://github.com/etalab-ia/OpenGateRAG/issues/2).
- Correction des endpoints pour assurer leur disponibilité et leur bon fonctionnement [#2](https://github.com/etalab-ia/OpenGateRAG/issues/2).

### Évolutions techniques
- Mise en place d'un pipeline CI/CD intégrant les tests E2E [#5](https://github.com/etalab-ia/OpenGateRAG/issues/5).
- Correction de la construction de l'image Docker pour assurer un déploiement correct [#5](https://github.com/etalab-ia/OpenGateRAG/issues/5).
- Ajout de `guvicorn` pour le lancement de l'application [#4](https://github.com/etalab-ia/OpenGateRAG/issues/4).
- Suppression du code obsolète (dépréciation) pour simplifier la base de code [#6](https://github.com/etalab-ia/OpenGateRAG/issues/6).
- Initialisation du dépôt avec une structure de base et des premiers composants [#7](https://github.com/etalab-ia/OpenGateRAG/issues/7).

### Autres changements
- Nettoyage de la documentation pour une meilleure clarté [#2](https://github.com/etalab-ia/OpenGateRAG/issues/2).
