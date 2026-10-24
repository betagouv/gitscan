# Synthèse d'activité : etalab-ia (du DD/MM au DD/MM)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une montée en puissance des capacités de RAG (Retrieval-Augmented Generation) et de l'orchestration d'agents. Les efforts se sont concentrés sur l'amélioration de l'évaluation des modèles (transcription, OCR), l'automatisation des pipelines de données pour alimenter les services d'IA, et la maturation des frameworks d'agents. Les outils comme [lettabot](/repos/etalab-ia/lettabot) et [letta](/repos/etalab-ia/letta) gagnent en polyvalence grâce à un support étendu de nouveaux modèles et une meilleure gestion de la mémoire et de la configuration.

Parallèlement, l'organisation renforce son alignement avec les standards de l'État français. Cela se traduit par une intégration accrue des guides de sécurité de l'ANSSI dans [skills](/repos/etalab-ia/skills) et une mise en conformité avec les dernières versions du Design Système de l'État (DSFR) pour [chartsgouv](/repos/etalab-ia/chartsgouv).

## Sécurité
- Renforcement de l'isolation des environnements et de la gestion sécurisée des identifiants dans [just-code](/repos/etalab-ia/just-code).
- Intégration des recommandations de sécurité de l'ANSSI et de la DINUM pour accompagner les agents publics dans l'usage de l'IA via [skills](/repos/etalab-ia/skills).
- Mise en place de vérifications de vulnérabilités des dépendances et de hooks de sécurité (gitleaks) dans [parcours-rag](/repos/etalab-ia/parcours-rag) et [eval-transcript](/repos/etalab-ia/eval-transcript).

## Autres changements notables
- **Évolutions architecturales** : Migration vers une "Clean Architecture" pour [OpenGateLLM](/repos/etalab-ia/OpenGateLLM) et refonte modulaire de [ragtime](/repos/etalab-ia/ragtime) (anciennement [rag-facile](/repos/etalab-ia/rag-facile)).
- **Infrastructure et déploiement** : Migration vers une architecture serverless pour [mediatech-to-albert-api](/repos/etalab-ia/mediatech-to-albert-api) et optimisation des images Docker pour [marker-serve](/repos/etalab-ia/marker-serve).
- **Mises à jour majeures** : Passage à la version 2.0.0 de [chartsgouv](/repos/etalab-ia/chartsgouv) avec alignement sur le DSFR 6.1.

## Dépôts les plus actifs
- [lettabot](/repos/etalab-ia/lettabot) : Extension massive des plateformes supportées (Slack, Discord, Telegram, WhatsApp) et refonte du système de configuration.
- [ragtime](/repos/etalab-ia/ragtime) : Ajout de l'authentification, de la gestion de collections et d'une interface CLI.
- [letta](/repos/etalab-ia/letta) : Support de nouveaux modèles (Anthropic, Gemini) et optimisation de la gestion de la mémoire.
- [just-code](/repos/etalab-ia/just-code) : Diversification des runtimes (Windows, macOS) et renforcement de l'isolation par défaut.
- [evalap](/repos/etalab-ia/evalap) : Amélioration de l'export des résultats vers Hugging Face Hub et de l'interface d'exploration locale.
