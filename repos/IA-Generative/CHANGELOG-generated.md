# Synthèse d'activité : IA-Generative (du 22/08 au 29/08)

## Résumé de l'activité
L'activité de cette période est marquée par une double priorité : l'extension des capacités d'intelligence artificielle et un durcissement massif de la sécurité de l'écosystème. Les utilisateurs bénéficient de nouvelles fonctionnalités de transcription et de gestion documentaire ([mcr](/repos/IA-Generative/mcr), [dictaphone](/repos/IA-Generative/dictaphone)), ainsi que de l'intégration de systèmes RAG (Retrieval-Augmented Generation) permettant une interaction plus intelligente avec les contenus ([Stirling-PDF](/repos/IA-Generative/Stirling-PDF), [abrege](/repos/IA-Generative/abrege)).

Parallèlement, l'organisation a consolidé la fiabilité de ses services par l'implémentation de l'authentification à deux facteurs et de protections avancées contre les injections de prompts ([myvault](/repos/IA-Generative/myvault), [owuiapps-agents](/repos/IA-Generative/owuiapps-agents)). Ces évolutions visent à offrir une plateforme plus robuste, sécurisée et prête pour des usages professionnels critiques.

## Sécurité
- **Authentification et accès** : Déploiement de l'authentification à deux facteurs (2FA/TOTP) ([myvault](/repos/IA-Generative/myvault), [keycloak-jar-test](/repos/IA-Generative/keycloak-jar-test)) et renforcement de la gestion des jetons OIDC ([owuiapps-agents](/repos/IA-Generative/owuiapps-agents), [mirai-mesreunions](/repos/IA-Generative/mirai-mesreunions)).
- **Protection contre les attaques IA** : Mise en place de protections contre les injections de prompts (OWASP LLM01) et de détecteurs d'anomalies ([owuiapps-agents](/repos/IA-Generative/owuiapps-agents)).
- **Sécurisation des données et des échanges** : Renforcement de la sécurité des requêtes WOPI ([drive](/repos/IA-Generative/drive)), protection contre les attaques SSRF et XSS ([mycollections](/repos/IA-Generative/mycollections), [drive](/repos/IA-Generative/drive)), et chiffrement des données sensibles ([myvault](/repos/IA-Generative/myvault)).
- **Contrôle des flux** : Implémentation de limitations de débit (rate limiting) pour prévenir les abus ([owuiapps-agents](/repos/IA-Generative/owuiapps-agents), [myvault](/repos/IA-Generative/myvault)).
- **Infrastructure sécurisée** : Durcissement des conteneurs (systèmes de fichiers en lecture seule, images non-root) et correction de vulnérabilités critiques ([ocr-api](/repos/IA-Generative/ocr-api), [device-management](/repos/IA-Generative/device-management), [owuiapps-agents](/repos/IA-Generative/owuiapps-agents)).

## Autres changements notables
- **Évolutions architecturales** : Migration majeure vers un modèle de microservices ([mcr](/repos/IA-Generative/mcr)) et transition de la gestion des files d'attente de Kafka vers Redis ([kevent-ai](/repos/IA-Generative/kevent-ai)).
- **Intégration de nouveaux modèles** : Support opérationnel des modèles GLM-5.2 de Scaleway ([claude-code-scaleway](/repos/IA-Generative/claude-code-scaleway)).
- **Modernisation CI/CD et Cloud** : Optimisation des pipelines de déploiement, migration vers BuildKit rootless et préparation au déploiement cloud-native ([ocr-api](/repos/IA-Generative/ocr-api), [claim-controller](/repos/IA-Generative/claim-controller), [device-management](/repos/IA-Generative/device-management), [mirai-mesreunions](/repos/IA-Generative/mirai-mesreunions)).
- **Développement de nouveaux connecteurs** : Lancement des premiers nœuds n8n pour les services IA BRIO ([n8n-nodes-async-api](/repos/IA-Generative/n8n-nodes-async-api)).

## Dépôts les plus actifs
- [myvault](/repos/IA-Generative/myvault) : Travaux intensifs sur la sécurité (2FA, chiffrement) et la protection contre les abus.
- [mcr](/repos/IA-Generative/mcr) : Refactorisation vers les microservices et amélioration des fonctions de transcription.
- [abrege](/repos/IA-Generative/abrege) : Ajout de capacités de génération QA, de scraping web et de gestion de tâches.
- [drive](/repos/IA-Generative/drive) : Amélioration du partage collaboratif et sécurisation de l'intégration WOPI.
- [mycollections](/repos/IA-Generative/mycollections) : Évolutions de l'interface utilisateur et renforcement de l'isolation des données.
- [owuiapps-agents](/repos/IA-Generative/owuiapps-agents) : Sécurisation des interactions LLM et harmonisation de l'interface.
