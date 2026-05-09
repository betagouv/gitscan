# Synthèse d'activité : etalab-ia (du 1er mai 2026 au 29 avril 2026)

## Résumé de l'activité
L'organisation etalab-ia a connu une semaine riche en activités, avec des avancées significatives sur plusieurs fronts. L'accent a été mis sur l'amélioration des capacités de recherche et de génération de langage, notamment avec l'intégration de nouvelles "skills" RAG et l'optimisation de l'API WhisperX. Plusieurs projets ont également bénéficié d'améliorations de l'infrastructure et de la sécurité, comme la migration vers des architectures serverless et l'intégration de Gitleaks pour la détection de secrets. Enfin, des efforts importants ont été consacrés à l'amélioration de l'expérience utilisateur, avec l'ajout d'assistants de configuration et de nouvelles fonctionnalités dans des projets comme lettabot et BlockNote. Les dépôts les plus actifs sont [skills](/repos/etalab-ia/skills), [ragtime](/repos/etalab-ia/ragtime), [mediatech](/repos/etalab-ia/mediatech) et [lettabot](/repos/etalab-ia/lettabot).

## Sécurité
- Intégration de `gitleaks` au pre-commit dans [skills](/repos/etalab-ia/skills) pour détecter et prévenir la présence de secrets sensibles dans le code.
- Amélioration de la sécurité du playground d'OpenGateLLM via une image Docker privée dans [OpenGateLLM](/repos/etalab-ia/OpenGateLLM).

## Autres changements notables
- Migration de la base de données de [mediatech-to-albert-api](/repos/etalab-ia/mediatech-to-albert-api) vers une architecture serverless pour une meilleure scalabilité.
- Refonte de l'architecture interne de [rag-facile](/repos/etalab-ia/rag-facile) pour une meilleure modularité et maintenabilité.
- Renommage complet du projet [ragtime](/repos/etalab-ia/ragtime) de "rag-facile" à "ragtime".
- Mise en place d'un pipeline automatisé pour importer les données Mediatech de HuggingFace vers l'API Albert dans [mediatech-to-albert-api](/repos/etalab-ia/mediatech-to-albert-api).

## Dépôts les plus actifs
- [skills](/repos/etalab-ia/skills) : Ajout de nouvelles "skills" RAG et amélioration de la gestion des secrets.
- [ragtime](/repos/etalab-ia/ragtime) : Amélioration de la gestion des collections via la CLI et refonte de l'architecture.
- [mediatech](/repos/etalab-ia/mediatech) : Ajout de la gestion de nouveaux jeux de données et amélioration du traitement des données.
- [lettabot](/repos/etalab-ia/lettabot) : Ajout d'un assistant de configuration interactif pour Slack et amélioration de l'expérience utilisateur.
- [OpenGateLLM](/repos/etalab-ia/OpenGateLLM) : Ajout du support de nouveaux formats de transcription et intégration avec Langfuse.
