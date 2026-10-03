# Synthèse d'activité : IA-Generative (du 16/09 au 23/09)

## Résumé de l'activité
L'activité de la semaine est marquée par une accélération majeure des capacités d'intelligence documentaire et d'automatisation. Les produits phares évoluent vers des fonctionnalités de pointe, notamment avec l'intégration de systèmes RAG (Retrieval-Augmented Generation) dans [Stirling-PDF](/repos/IA-Generative/Stirling-PDF), la génération de documents par IA dans [dig-dig-doc](/repos/IA-Generative/dig-dig-doc), et l'ajout de capacités de recherche web et de questions-réponses dans [abrege](/repos/IA-Generative/abrege).

Parallèlement, l'organisation renforce l'expérience utilisateur et l'accompagnement (onboarding) sur des outils comme [drive](/repos/IA-Generative/drive) et [IAssistant-Direct](/repos/IA-Generative/IAssistant-Direct), tout en consolidant la robustesse technique de l'infrastructure pour soutenir ces nouveaux usages.

## Sécurité
- **Protection contre les attaques IA** : Renforcement de la sécurité contre les injections de prompt (OWASP LLM01) dans [owuiapps-agents](/repos/IA-Generative/owuiapps-agents).
- **Authentification forte** : Implémentation de l'authentification à deux facteurs (2FA/TOTP) pour [myvault](/repos/IA-Generative/myvault) et gestion fine des niveaux de sécurité eIDAS pour ProConnect dans [keycloak-jar-test](/repos/IA-Generative/keycloak-jar-test).
- **Durcissement des accès et des données** : Mise en place de protections contre les abus (rate limiting), chiffrement des notes sensibles dans [myvault](/repos/IA-Generative/myvault), et sécurisation des jetons JWT/PKCE dans [dictaphone](/repos/IA-Generative/dictaphone).
- **Sécurité infrastructurelle** : Durcissement des images Docker et des contextes de sécurité dans [ocr-api](/repos/IA-Generative/ocr-api) et vérification des checksums des binaires dans [device-management](/repos/IA-Generative/device-management).

## Autres changements notables
- **Évolutions architecturales majeures** : Migration vers une architecture en microservices pour [mcr](/repos/IA-Generative/mcr) et passage d'une gestion de files d'attente Kafka à Redis pour [kevent-ai](/repos/IA-Generative/kevent-ai).
- **Intégration de nouveaux modèles** : Support opérationnel des modèles GLM-5.2 de Scaleway via [claude-code-scaleway](/repos/IA-Generative/claude-code-scaleway).
- **Optimisation de la recherche** : Migration du moteur de recherche de Qdrant vers Meilisearch pour améliorer la recherche hybride dans [Muffin](/repos/IA-Generative/Muffin).
- **Modernisation DevOps** : Amélioration des processus de build et de déploiement (CI/CD) pour [mirai-mesreunions](/repos/IA-Generative/mirai-mesreunions) et [n8n-nodes-async-api](/repos/IA-Generative/n8n-nodes-async-api).

## Dépôts les plus actifs
- [ocr-api](/repos/IA-Generative/ocr-api) : Passage à la version 0.20.0 avec un nouveau SDK TypeScript et une interface modernisée.
- [myvault](/repos/IA-Generative/myvault) : Travaux intensifs sur la sécurité, le chiffrement et l'authentification multi-facteurs.
- [dig-dig-doc](/repos/IA-Generative/dig-dig-doc) : Lancement de fonctionnalités avancées de génération et d'analyse de documents.
- [abrege](/repos/IA-Generative/abrege) : Extension significative des capacités (QA, scraping web, gestion des tâches).
- [claude-code-scaleway](/repos/IA-Generative/claude-code-scaleway) : Intégration de nouveaux modèles et stabilisation de la passerelle API.
