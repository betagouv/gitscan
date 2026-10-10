# Synthèse d'activité : IA-Generative (du 20/05 au 23/09)

## Résumé de l'activité
Cette période est marquée par une montée en puissance des capacités d'intelligence artificielle et une amélioration significative de l'expérience utilisateur à travers l'écosystème. L'organisation a franchi des étapes clés dans la gestion documentaire intelligente avec de nouvelles fonctionnalités de génération et d'analyse ([dig-dig-doc](/repos/IA-Generative/dig-dig-doc), [mcr](/repos/IA-Generative/mcr)) et a renforcé ses capacités d'automatisation via des extensions n8n ([n8n-nodes-async-api](/repos/IA-Generative/n8n-nodes-async-api)).

Parallèlement, un effort majeur a été porté sur l'accompagnement des utilisateurs (onboarding) et la stabilisation des interfaces ([drive](/repos/IA-Generative/drive), [IAssistant-Direct](/repos/IA-Generative/IAssistant-Direct)), tout en intégrant des technologies de pointe comme le protocole MCP ou le RAG pour rendre les outils plus contextuels et performants.

## Sécurité
- **Protection contre les attaques IA** : Renforcement de la sécurité contre les injections de prompt et mise en place de détecteurs d'anomalies ([owuiapps-agents](/repos/IA-Generative/owuiapps-agents)).
- **Gestion des accès et authentification** : Généralisation de l'authentification à deux facteurs (2FA/TOTP) et gestion fine des niveaux de sécurité eIDAS ([myvault](/repos/IA-Generative/myvault), [keycloak-jar-test](/repos/IA-Generative/keycloak-jar-test)).
- **Protection des données sensibles** : Utilisation des coffres-forts natifs de l'OS pour le stockage des secrets, nettoyage des logs pour éviter les fuites de jetons et chiffrement des notes personnelles ([iassistant-libreoffice](/repos/IA-Generative/iassistant-libreoffice), [dictaphone](/repos/IA-Generative/dictaphone), [myvault](/repos/IA-Generative/myvault)).
- **Durcissement des infrastructures** : Sécurisation des API (clés M2M, protection CSRF), passage à l'exécution en mode "non-root" pour les conteneurs et vérification systématique des checksums des binaires ([ocr-api](/repos/IA-Generative/ocr-api), [abrege](/repos/IA-Generative/abrege), [device-management](/repos/IA-Generative/device-management)).

## Autres changements notables
- **Évolutions architecturales majeures** : Migration vers une architecture en microservices ([mcr](/repos/IA-Generative/mcr)), remplacement de Kafka par Redis pour la gestion des files d'attente ([kevent-ai](/repos/IA-Generative/kevent-ai)) et passage de Qdrant à Meilisearch pour optimiser la recherche hybride ([Muffin](/repos/IA-Generative/Muffin)).
- **Nouvelles capacités d'IA et protocoles** : Support du protocole MCP ([dig-dig-doc](/repos/IA-Generative/dig-dig-doc)), intégration de systèmes RAG ([Stirling-PDF](/repos/IA-Generative/Stirling-PDF)) et intégration opérationnelle des modèles GLM-5.2 de Scaleway ([claude-code-scaleway](/repos/IA-Generative/claude-code-scaleway)).
- **Modernisation de la CI/CD et de l'infrastructure** : Migration du build vers BuildKit rootless ([mirai-mesreunions](/repos/IA-Generative/mirai-mesreunions)), automatisation des environnements de preview ([mirai-api](/repos/IA-Generative/mirai-api)) et amélioration de la gestion des ressources Kubernetes ([claim-controller](/repos/IA-Generative/claim-controller)).

## Dépôts les plus actifs
- [myvault](/repos/IA-Generative/myvault) : Travaux intensifs sur la sécurité, le chiffrement et la robustesse du système.
- [iassistant-libreoffice](/repos/IA-Generative/iassistant-libreoffice) : Sortie de la version 0.3.0 avec internationalisation et refonte du système de mise à jour.
- [mcr](/repos/IA-Generative/mcr) : Refactorisation majeure de l'architecture vers les microservices et optimisation du pipeline de transcription.
- [abrege](/repos/IA-Generative/abrege) : Ajout de capacités d'analyse sémantique avancées et modernisation de l'interface.
- [claude-code-scaleway](/repos/IA-Generative/claude-code-scaleway) : Intégration des modèles Scaleway et optimisation de la gestion des tokens.
