# Synthèse d'activité : etalab-ia (derniers 7 jours)

## Résumé de l'activité
La semaine écoulée a été marquée par une activité soutenue sur les différents dépôts d'etalab-ia, avec des améliorations significatives concernant l'expérience utilisateur, la stabilité et les fonctionnalités offertes.  Plusieurs projets ont bénéficié de refactorisations importantes pour une meilleure maintenabilité, comme OpenGateLLM avec une réorganisation de son API.  Des efforts importants ont également été consacrés à l'intégration de nouveaux modèles et à l'amélioration de l'interopérabilité avec d'autres services, notamment via l'API Albert et le support de nouveaux formats de données.  Enfin, des outils comme `rag-facile` ont été enrichis pour faciliter la création et l'évaluation de pipelines RAG, avec l'ajout de thèmes visuels conformes aux standards gouvernementaux.

## Sécurité
Aucun changement lié à la sécurité n'a été signalé durant cette période.

## Autres changements notables
Plusieurs dépôts ont connu des refactorisations importantes :
- **OpenGateLLM** [OpenGateLLM](/repos/etalab-ia/OpenGateLLM) a subi une refonte majeure de son API pour une architecture plus propre et maintenable.
- **BlockNote** [BlockNote](/repos/etalab-ia/BlockNote) a migré vers la version 6 du SDK IA et refactorisé la gestion des extensions.
- **rag-facile** [rag-facile](/repos/etalab-ia/rag-facile) a vu une refactorisation de son architecture pour une meilleure modularité et maintenabilité, et a migré vers `uv` pour la gestion des dépendances.
- **OpenGateLLM-helm** [opengatellm-helm](/repos/etalab-ia/opengatellm-helm) a séparé son chart en deux parties (core et stack) pour une plus grande flexibilité.

## Dépôts les plus actifs
- **BlockNote** [BlockNote](/repos/etalab-ia/BlockNote) : Corrections de bugs et améliorations de l'expérience utilisateur, notamment concernant les tableaux et l'IA.
- **OpenGateLLM** [OpenGateLLM](/repos/etalab-ia/OpenGateLLM) : Refactorisation de l'API, ajout de support pour de nouveaux modèles et amélioration de la recherche sémantique.
- **rag-facile** [rag-facile](/repos/etalab-ia/rag-facile) : Ajout d'un système de configuration, d'un thème DSFR et d'un système de traçabilité des pipelines RAG.
- **letta-code** [letta-code](/repos/etalab-ia/letta-code) : Intégration de nouveaux modèles (Kimi K2.5, Bedrock Opus 4.5) et amélioration de la gestion des agents.
- **evalap** [evalap](/repos/etalab-ia/evalap) : Ajout de l'export des résultats vers Hugging Face Hub et amélioration de la documentation.
