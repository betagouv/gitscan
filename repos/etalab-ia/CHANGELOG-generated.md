# Synthèse d'activité : etalab-ia (du DD/MM au DD/MM)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une montée en maturité significative des outils de RAG (Retrieval-Augmented Generation) et des agents conversationnels. Les efforts se sont concentrés sur la structuration de la gestion des données via des systèmes de "collections" plus robustes et l'amélioration de l'expérience utilisateur grâce à des assistants de configuration interactifs. 

L'écosystème renforce également sa capacité d'évaluation et de production, avec le développement d'outils de benchmarking pour les transcriptions et l'optimisation des pipelines de données pour l'API Albert. Ces évolutions permettent de passer de prototypes à des solutions plus stables, prêtes pour des usages institutionnels et une intégration simplifiée dans des environnements variés.

## Sécurité
- Intégration des guides de sécurité de l'ANSSI et de la DINUM pour accompagner l'usage de l'IA dans le secteur public [skills](/repos/etalab-ia/skills).
- Renforcement de la protection des données sensibles via la sécurisation des logs OCR [document-ia](/repos/etalab-ia/document-ia) et la gestion rigoureuse des secrets de projet [just-code](/repos/etalab-ia/just-code).
- Durcissement de la sécurité des intégrations (iframe) et mise en place de limites d'utilisation pour prévenir les abus [chat-widget](/repos/etalab-ia/chat-widget).
- Ajout de mécanismes de consentement explicite pour la collecte de statistiques [just-code](/repos/etalab-ia/just-code) et de contrôles automatisés (gitleaks) dans les pipelines [eval-transcript](/repos/etalab-ia/eval-transcript).
- Amélioration de l'authentification pour l'accès aux environnements de développement [albert-code](/repos/etalab-ia/albert-code).

## Autres changements notables
- **Refonte architecturale et migration de données** : Passage à une gestion de collections via PostgreSQL pour remplacer Elasticsearch [OpenGateRAG-Next](/repos/etalab-ia/OpenGateRAG-Next) et refonte majeure de l'architecture interne pour plus de modularité [ragtime](/repos/etalab-ia/ragtime).
- **Évolution des standards de développement** : Adoption de la "Clean Architecture" et intégration de l'observabilité (Langfuse) pour le suivi de l'usage et de la latence [OpenGateLLM](/repos/etalab-ia/OpenGateLLM).
- **Optimisation de l'infrastructure** : Migration vers une architecture serverless pour l'API Albert [mediatech-to-albert-api](/repos/etalab-ia/mediatech-to-albert-api) et optimisation des images Docker pour les déploiements [marker-serve](/repos/etalab-ia/marker-serve).
- **Gestion des versions** : Introduction de la sauvegarde de version et du rollback pour les templates [letta](/repos/etalab-ia/letta).

## Dépôts les plus actifs
- [ragtime](/repos/etalab-ia/ragtime) : Refonte complète, renommage (ex-rag-facile) et ajout de l'authentification via Supabase.
- [lettabot](/repos/etalab-ia/lettabot) : Extension multi-plateforme (Slack, Discord, Telegram) et refonte du système de configuration.
- [letta](/repos/etalab-ia/letta) : Support de nouveaux modèles (Anthropic, Gemini) et enrichissement des fonctionnalités API.
- [chat-widget](/repos/etalab-ia/chat-widget) : Sortie de la version 0.2.0 avec de nouvelles méthodes d'intégration (Web Components).
- [just-code](/repos/etalab-ia/just-code) : Refonte de l'assistant de configuration (wizard) et renforcement de la sécurité.
- [OpenGateRAG-Next](/repos/etalab-ia/OpenGateRAG-Next) : Restructuration profonde autour de la gestion des collections de données.
