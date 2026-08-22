# Synthèse d'activité : etalab-ia (du 20/05 au 27/05)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une montée en maturité significative de ses solutions de RAG (Retrieval-Augmented Generation) et d'agents IA. Les projets phares comme [ragtime](/repos/etalab-ia/ragtime) (anciennement [rag-facile](/repos/etalab-ia/rag-facile)) et la suite [OpenGate](/repos/etalab-ia/OpenGateLLM) franchissent un cap de production grâce à des refontes architecturales majeures et l'intégration de fonctionnalités essentielles telles que l'authentification (SSO, Supabase) et la persistance des données.

Parallèlement, l'écosystème de données et d'évaluation se renforce. L'automatisation des pipelines d'ingestion vers [Albert](/repos/etalab-ia/mediatech-to-albert-api) et l'amélioration des capacités d'exportation des résultats de benchmarks vers Hugging Face via [evalap](/repos/etalab-ia/evalap) et [eval-transcript](/repos/etalab-ia/eval-transcript) permettent une exploitation plus fluide et professionnelle des modèles et des données.

## Sécurité
- Amélioration de la sécurisation de la saisie des clés API dans [ragtime](/repos/etalab-ia/ragtime).
- Mise en place du support SSO pour l'authentification dans [OpenGateLLM](/repos/etalab-ia/OpenGateLLM).
- Intégration de vérifications de vulnérabilités des dépendances et de détection de secrets (gitleaks) dans [parcours-rag](/repos/etalab-ia/parcours-rag) et [eval-transcript](/repos/etalab-ia/eval-transcript).
- Sécurisation de l'accès aux machines virtuelles via l'authentification GitHub dans [albert-code](/repos/etalab-ia/albert-code).
- Renforcement des validations pour la fonctionnalité de sécurité du développement dans [skills](/repos/etalab-ia/skills).

## Autres changements notables
- **Refonte architecturale** : Migration massive vers une "Clean Architecture" pour [OpenGateLLM](/repos/etalab-ia/OpenGateLLM) et unification de l'API avec [OpenGateRAG](/repos/etalab-ia/OpenGateRAG).
- **Évolution de l'offre RAG** : Renommage officiel du projet de [rag-facile](/repos/etalab-ia/rag-facile) vers [ragtime](/repos/etalab-ia/ragtime).
- **Infrastructure et données** : Migration de la base de données vers une architecture serverless pour [mediatech-to-albert-api](/repos/etalab-ia/mediatech-to-albert-api) et optimisation du support GPU H200 pour [whisperx-openai-api](/repos/etalab-ia/whisperx-openai-api).
- **Mises à jour technologiques** : Migration vers la version 6 du SDK IA pour [BlockNote](/repos/etalab-ia/BlockNote).

## Dépôts les plus actifs
- [lettabot](/repos/etalab-ia/lettabot) : Extension massive des capacités d'intégration (Slack, Discord, Telegram) et refonte complète du système de configuration.
- [ragtime](/repos/etalab-ia/ragtime) : Transformation profonde de la plateforme incluant l'authentification, la gestion de collections et une architecture modulaire.
- [OpenGateLLM](/repos/etalab-ia/OpenGateLLM) : Évolutions structurelles majeures (Clean Architecture) et amélioration de l'expérience utilisateur (SSO, Playground).
- [letta](/repos/etalab-ia/letta) et [letta-code](/repos/etalab-ia/letta-code) : Support de nouveaux modèles de pointe et ajout d'outils spécialisés pour les agents (planification, mémoire, sous-agents).
- [evalap](/repos/etalab-ia/evalap) et [eval-transcript](/repos/etalab-ia/eval-transcript) : Amélioration des capacités d'évaluation et d'exportation automatique des résultats vers Hugging Face.
