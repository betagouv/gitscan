# Synthèse d'activité : etalab-ia (du 01/05 au 24/07)

## Résumé de l'activité
L'activité de cette période est marquée par une montée en puissance majeure des capacités d'agents et des systèmes de génération augmentée par récupération (RAG). Les projets [ragtime](/repos/etalab-ia/ragtime) et [letta](/repos/etalab-ia/letta) ont franchi des étapes clés en intégrant de nouveaux modèles de langage, des systèmes de mémoire avancés et des fonctionnalités de persistance des conversations, rendant les agents plus autonomes et performants.

Parallèlement, l'organisation renforce ses infrastructures de données et d'évaluation. L'automatisation des pipelines d'ingestion (notamment via [mediatech](/repos/etalab-ia/mediatech) et [mediatech-to-albert-api](/repos/etalab-ia/mediatech-to-albert-api)) et l'amélioration des outils de mesure de qualité ([evalap](/repos/etalab-ia/evalap) et [eval-transcript](/repos/etalab-ia/eval-transcript)) permettent de garantir des résultats plus fiables et une meilleure exploitation des données publiques pour l'IA.

## Sécurité
- Renforcement de la sécurité pour empêcher l'énumération d'utilisateurs dans [OpenGateLLM](/repos/etalab-ia/OpenGateLLM).
- Sécurisation de la saisie des clés API lors de la configuration dans [ragtime](/repos/etalab-ia/ragtime).
- Mise en place de vérifications automatiques des vulnérabilités des dépendances dans [parcours-rag](/repos/etalab-ia/parcours-rag).
- Amélioration de la gestion de la sécurité et des validations dans [skills](/repos/etalab-ia/skills).

## Autres changements notables
- **Évolutions architecturales et renommage** : Le projet [rag-facile](/repos/etalab-ia/rag-facile) a été intégralement refondu et renommé en [ragtime](/repos/etalab-ia/ragtime). [OpenGateRAG](/repos/etalab-ia/OpenGateRAG) a également été stabilisé avec l'unification de son API avec [OpenGateLLM](/repos/etalab-ia/OpenGateLLM).
- **Migrations et infrastructures** : Migration de la base de données vers une architecture serverless pour [mediatech-to-albert-api](/repos/etalab-ia/mediatech-to-albert-api) et optimisation des images Docker pour [marker-serve](/repos/etalab-ia/marker-serve).
- **Optimisations techniques** : Améliorations significatives de la gestion de la mémoire et de la concurrence pour [letta](/repos/etalab-ia/letta) et refactorisation de la connexion PostgreSQL pour [mediatech](/repos/etalab-ia/mediatech).
- **Automatisation** : Mise en place de la mise à jour quotidienne automatisée des dictionnaires de données pour [albert-data-collections](/repos/etalab-ia/albert-data-collections).

## Dépôts les plus actifs
- [ragtime](/repos/etalab-ia/ragtime) : Évolutions majeures incluant l'authentification, la gestion de collections et une nouvelle interface CLI.
- [letta](/repos/etalab-ia/letta) : Extension massive des capacités des agents (nouveaux modèles, gestion de la mémoire et des templates).
- [lettabot](/repos/etalab-ia/lettabot) : Amélioration de l'expérience utilisateur et de l'intégration sur Slack, Discord et Telegram.
- [mediatech](/repos/etalab-ia/mediatech) : Optimisation du traitement et de l'intégration de nouveaux jeux de données publics.
- [evalap](/repos/etalab-ia/evalap) : Amélioration de l'exportation des résultats d'évaluation vers Hugging Face Hub.
