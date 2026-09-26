# Synthèse d'activité : IA-Generative (du DD/MM au DD/MM)

## Résumé de l'activité
L'organisation IA-Generative a franchi des étapes majeures dans la maturité de ses produits, transformant plusieurs outils en plateformes complètes d'intelligence artificielle. L'accent a été mis sur l'analyse documentaire avancée (génération de questions/réponses, recherche hybride, minutes structurées) et sur l'amélioration de l'expérience utilisateur grâce à des interfaces modernes basées sur le design système DSFR et des parcours d'onboarding guidés.

Parallèlement, un effort massif de sécurisation et de robustesse a été déployé à travers l'ensemble de l'écosystème. Les développements ont permis de renforcer la protection des données sensibles, d'optimiser les infrastructures de déploiement et d'intégrer de nouveaux modèles de langage (LLM) performants, garantissant ainsi des services plus fiables et prêts pour des usages critiques.

## Sécurité
- **Protection contre les attaques IA** : Renforcement de la sécurité contre les injections de prompt (OWASP LLM01) dans [owuiapps-agents](/repos/IA-Generative/owuiapps-agents).
- **Authentification forte** : Introduction de l'authentification à deux facteurs (2FA/TOTP) et gestion fine des niveaux de sécurité eIDAS dans [myvault](/repos/IA-Generative/myvault) et [keycloak-jar-test](/repos/IA-Generative/keycloak-jar-test).
- **Protection des données et des accès** : Mise en place de mécanismes anti-leak, de chiffrement des notes, de limitation de débit (rate limiting) et de hachage des secrets dans [myvault](/repos/IA-Generative/myvault).
- **Intégrité et conformité** : Amélioration de la vérification des sommes de contrôle (checksums) pour garantir l'intégrité des fichiers dans [device-management](/repos/IA-Generative/device-management) et sécurisation des sessions via JWT/PKCE dans [dictaphone](/repos/IA-Generative/dictaphone).
- **Durcissement des infrastructures** : Renforcement de la sécurité des images Docker et des composants Helm dans [ocr-api](/repos/IA-Generative/ocr-api).

## Autres changements notables
- **Migrations d'infrastructure majeures** : Passage de la gestion des files d'attente de Kafka vers Redis dans [kevent-ai](/repos/IA-Generative/kevent-ai) et transition vers une architecture de microservices pour [mcr](/repos/IA-Generative/mcr).
- **Évolutions de l'IA et des modèles** : Intégration des modèles GLM-5.2 de Scaleway dans [claude-code-scaleway](/repos/IA-Generative/claude-code-scaleway) et intégration de systèmes RAG (Retrieval-Augmented Generation) dans [Stirling-PDF](/repos/IA-Generative/Stirling-PDF).
- **Modernisation DevOps** : Migration vers BuildKit rootless pour les processus de construction dans [mirai-mesreunions](/repos/IA-Generative/mirai-mesreunions) et automatisation des environnements de preview pour [mirai-api](/repos/IA-Generative/mirai-api).
- **Optimisation de la recherche** : Migration du moteur de recherche de Qdrant vers Meilisearch pour optimiser la recherche hybride dans [Muffin](/repos/IA-Generative/Muffin).

## Dépôts les plus actifs
- [dig-dig-doc](/repos/IA-Generative/dig-dig-doc) : Évolution massive vers une plateforme complète incluant chat IA, analyse de documents et interface DSFR.
- [ocr-api](/repos/IA-Generative/ocr-api) : Passage à la version 0.20.0 avec un nouveau SDK TypeScript, une interface modernisée et le support GPU.
- [myvault](/repos/IA-Generative/myvault) : Travaux intensifs sur la sécurité, le chiffrement et l'authentification multi-facteurs.
- [abrege](/repos/IA-Generative/abrege) : Ajout de fonctionnalités de génération de QA, de scraping web et d'amélioration de l'OCR.
- [kevent-ai](/repos/IA-Generative/kevent-ai) : Refonte technique majeure de l'infrastructure de gestion des tâches.
