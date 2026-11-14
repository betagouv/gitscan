# Synthèse d'activité : etalab-ia (du 01/11 au 07/11)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une montée en puissance des capacités de RAG (Retrieval-Augmented Generation) et une maturation des frameworks d'agents IA. Les projets [ragtime](/repos/etalab-ia/ragtime) et [OpenGateRAG-Next](/repos/etalab-ia/OpenGateRAG-Next) ont franchi des étapes clés avec des refontes architecturales visant une meilleure gestion des collections de données et une plus grande modularité. En parallèle, l'écosystème d'agents s'enrichit avec [letta](/repos/etalab-ia/letta) et [codebox](/repos/etalab-ia/codebox), offrant un support élargi pour les nouveaux modèles (Anthropic, Gemini, Kimi) et des outils de gestion de la mémoire et des secrets plus robustes.

Enfin, l'organisation renforce ses capacités d'évaluation et de conformité, notamment via le lancement de [eval-ocr-htr](/repos/etalab-ia/eval-ocr-htr) et l'intégration des guides de sécurité de l'ANSSI dans [skills](/repos/etalab-ia/skills) et [chat-widget](/repos/etalab-ia/chat-widget), garantissant ainsi un usage plus sécurisé de l'IA pour les agents publics.

## Sécurité
- Renforcement de la gestion et de l'injection sécurisée des secrets dans [codebox](/repos/etalab-ia/codebox).
- Sécurisation des logs OCR pour prévenir les fuites de données sensibles dans [document-ia](/repos/etalab-ia/document-ia).
- Durcissement de la sécurité des iframes et de l'isolation du widget dans [chat-widget](/repos/etalab-ia/chat-widget).
- Amélioration de la gestion des clés API (révocation, filtrage) et du rate limiting dans [OpenGateLLM](/repos/etalab-ia/OpenGateLLM).
- Ajout d'un hook de détection de secrets (gitleaks) dans [eval-transcript](/repos/etalab-ia/eval-transcript).

## Autres changements notables
- Rebranding majeur de plusieurs projets, notamment `just-code` vers [codebox](/repos/etalab-ia/codebox) et `rag-facile` vers [ragtime](/repos/etalab-ia/ragtime).
- Migrations architecturales stratégiques : passage de l'architecture Elasticsearch vers PostgreSQL pour [OpenGateRAG-Next](/repos/etalab-ia/OpenGateRAG-Next) et adoption de la "Clean Architecture" pour [OpenGateLLM](/repos/etalab-ia/OpenGateLLM).
- Migration de la base de données vers une architecture serverless pour [mediatech-to-albert-api](/repos/etalab-ia/mediatech-to-albert-api).
- Refonte du système de configuration pour passer de fichiers `.env` à des fichiers YAML dans [lettabot](/repos/etalab-ia/lettabot) et [letta](/repos/etalab-ia/letta).

## Dépôts les plus actifs
- [codebox](/repos/etalab-ia/codebox) : Rebranding complet et introduction d'un assistant de configuration interactif (wizard).
- [letta](/repos/etalab-ia/letta) : Expansion massive du support de modèles et nouvelles capacités d'agents (mode listener, gestion memfs).
- [ragtime](/repos/etalab-ia/ragtime) : Refonte de l'architecture et intégration de l'authentification via Supabase.
- [chat-widget](/repos/etalab-ia/chat-widget) : Sortie de la version 0.2.0 avec support des Web Components et synchronisation des guides ANSSI.
- [OpenGateRAG-Next](/repos/etalab-ia/OpenGateRAG-Next) : Restructuration profonde centrée sur la gestion des collections via une nouvelle API.
