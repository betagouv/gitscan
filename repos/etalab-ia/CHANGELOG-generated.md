# Synthèse d'activité : etalab-ia (derniers 7 jours)

## Résumé de l'activité
La semaine écoulée a été marquée par des avancées significatives sur plusieurs fronts. L'organisation a continué à renforcer ses outils d'IA conversationnelle avec des améliorations notables sur [rag-facile/ragtime](/repos/etalab-ia/rag-facile) et [lettabot](/repos/etalab-ia/lettabot), notamment en matière d'authentification, de gestion des conversations et d'intégration de nouvelles fonctionnalités comme l'évaluation de la qualité des réponses.  L'accent a également été mis sur l'amélioration de l'accès aux données publiques avec des mises à jour sur [mediatech](/repos/etalab-ia/mediatech) et [mediatech-to-albert-api](/repos/etalab-ia/mediatech-to-albert-api) pour faciliter leur intégration dans les applications d'IA. Enfin, des efforts ont été déployés pour améliorer la sécurité et la maintenabilité des infrastructures avec [OpenGateLLM](/repos/etalab-ia/OpenGateLLM).

## Sécurité
- Renforcement de la sécurité d'OpenGateLLM en dissociant la clé de chiffrement des clés API du mot de passe maître ([OpenGateLLM](/repos/etalab-ia/OpenGateLLM)).
- Ajout d'outils d'analyse de vulnérabilités (Trivy et Semgrep) pour améliorer la sécurité de la chaîne d'approvisionnement et du code ([OpenGateLLM](/repos/etalab-ia/OpenGateLLM)).
- Ajout de `gitleaks` pour la détection de secrets dans le code de [skills](/repos/etalab-ia/skills).

## Autres changements notables
- Migration de la base de données de [mediatech-to-albert-api](/repos/etalab-ia/mediatech-to-albert-api) vers une architecture serverless pour une meilleure scalabilité.
- Refonte de l'architecture interne de [rag-facile/ragtime](/repos/etalab-ia/rag-facile) pour une meilleure modularité et maintenabilité.
- Changement de nom de [rag-facile](/repos/etalab-ia/rag-facile) en [ragtime](/repos/etalab-ia/ragtime).
- Migration vers la version 6 du SDK IA dans [BlockNote](/repos/etalab-ia/BlockNote).

## Dépôts les plus actifs
- [rag-facile/ragtime](/repos/etalab-ia/rag-facile) : Amélioration majeure de la plateforme avec ajout d'authentification, persistance des conversations et refonte de l'architecture.
- [lettabot](/repos/etalab-ia/lettabot) : Ajout d'un assistant de configuration interactif pour Slack et amélioration de la gestion des modèles d'IA.
- [OpenGateLLM](/repos/etalab-ia/OpenGateLLM) : Renforcement de la sécurité et ajout d'outils d'analyse de vulnérabilités.
- [mediatech](/repos/etalab-ia/mediatech) : Amélioration de l'intégration des données et ajout d'un tutoriel RAG.
- [skills](/repos/etalab-ia/skills) : Ajout de nouvelles skills pour les assistants de code et intégration de skills pour data.gouv.fr et LaSuite React.
