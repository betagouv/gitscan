# Synthèse d'activité : IA-Generative (du 20/07 au 27/07)

## Résumé de l'activité
L'activité de cette période a été marquée par un renforcement massif de la sécurité des données et une extension significative des capacités d'intelligence artificielle. L'organisation a introduit des fonctionnalités avancées telles que la génération de questions-réponses et le scraping web dans [abrege](/repos/IA-Generative/abrege), ainsi que l'intégration de systèmes RAG (Retrieval-Augmented Generation) pour [Stirling-PDF](/repos/IA-Generative/Stirling-PDF).

Parallèlement, l'expérience utilisateur et la fiabilité des services ont été améliorées grâce à de nouveaux outils de transcription multimédia pour [ocr-api](/repos/IA-Generative/ocr-api) et [mcr](/repos/IA-Generative/mcr), ainsi qu'à une modernisation profonde des infrastructures pour supporter une montée en charge plus importante.

## Sécurité
- Protection contre les injections de prompt (OWASP LLM01) et détection d'anomalies dans [owuiapps-agents](/repos/IA-Generative/owuiapps-agents).
- Renforcement de l'authentification avec l'ajout du 2FA (TOTP) et protection accrue des accès machine-to-machine dans [myvault](/repos/IA-Generative/myvault).
- Sécurisation des données par le cloisonnement des collections via Keycloak et prévention des attaques SSRF/CORS dans [mycollections](/repos/IA-Generative/mycollections).
- Amélioration de la gestion des jetons JWT et du protocole PKCE pour [dictaphone](/repos/IA-Generative/dictaphone).
- Corrections de vulnérabilités et durcissement des configurations dans [ocr-api](/repos/IA-Generative/ocr-api), [myvault](/repos/IA-Generative/myvault) et [abrege](/repos/IA-Generative/abrege).

## Autres changements notables
- **Migrations architecturales** : Passage à un modèle de microservices pour [mcr](/repos/IA-Generative/mcr) et remplacement de Kafka par Redis pour la gestion des files d'attente dans [kevent-ai](/repos/IA-Generative/kevent-ai).
- **Optimisation DevOps** : Migration vers un modèle de build "in-cluster" avec BuildKit pour [mirai-mesreunions](/repos/IA-Generative/mirai-mesreunions) et préparation au déploiement cloud-native via Helm pour [device-management](/repos/IA-Generative/device-management).
- **Évolutions fonctionnelles majeures** : Ajout de la transcription de vidéos YouTube pour [ocr-api](/repos/IA-Generative/ocr-api) et mise en place de la gestion des priorités de requêtes dans [kevent-ai](/repos/IA-Generative/kevent-ai).

## Dépôts les plus actifs
- [myvault](/repos/IA-Generative/myvault) : Travaux intensifs sur la sécurité (2FA, chiffrement, anti-leak) et la robustesse.
- [mycollections](/repos/IA-Generative/mycollections) : Amélioration de l'administration, de la sécurité des données et de l'interface utilisateur.
- [ocr-api](/repos/IA-Generative/ocr-api) : Extension des capacités de transcription et de support de formats de fichiers.
- [abrege](/repos/IA-Generative/abrege) : Développement de nouvelles fonctionnalités d'analyse IA (QA, scraping).
- [mcr](/repos/IA-Generative/mcr) : Refonte majeure de l'architecture vers les microservices.
