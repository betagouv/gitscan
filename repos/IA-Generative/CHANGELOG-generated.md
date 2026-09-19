# Synthèse d'activité : IA-Generative (du DD/MM au DD/MM)

## Résumé de l'activité
L'activité de l'organisation a été intensément portée par deux axes majeurs : la sécurisation accrue des services d'IA et l'enrichissement des capacités fonctionnelles des produits. Les efforts de développement ont permis de renforcer la protection contre les attaques (injections de prompts, fuites de données) et d'améliorer la fiabilité des échanges via des protocoles d'authentification et de validation plus robustes.

En parallèle, l'expérience utilisateur a franchi un nouveau cap avec l'intégration de fonctionnalités avancées comme le RAG (Retrieval-Augmented Generation) dans [Stirling-PDF](/repos/IA-Generative/Stirling-PDF), la génération de questions/réponses dans [abrege](/repos/IA-Generative/abrege), et la modernisation des interfaces et des SDK pour [ocr-api](/repos/IA-Generative/ocr-api). Ces évolutions visent à offrir des outils plus intelligents, plus simples à intégrer et plus sûrs pour les utilisateurs finaux.

## Sécurité
- Protection contre les injections de prompts (OWASP LLM01) ([owuiapps-agents](/repos/IA-Generative/owuiapps-agents)).
- Renforcement de l'authentification (implémentation de la 2FA/TOTP, gestion des jetons OIDC, clés API et protocoles JWT/PKCE) ([myvault](/repos/IA-Generative/myvault), [keycloak-jar-test](/repos/IA-Generative/keycloak-jar-test), [ocr-api](/repos/IA-Generative/ocr-api), [dictaphone](/repos/IA-Generative/dictaphone)).
- Sécurisation des données et des flux (garde-fous anti-leak, chiffrement des notes, validation d'URL, signatures WOPI et vérification d'intégrité des fichiers par checksum) ([myvault](/repos/IA-Generative/myvault), [mycollections](/repos/IA-Generative/mycollections), [drive](/repos/IA-Generative/drive), [device-management](/repos/IA-Generative/device-management)).

## Autres changements notables
- Évolutions architecturales majeures (passage vers une architecture microservices et migration de la gestion des files d'attente de Kafka vers Redis) ([mcr](/repos/IA-Generative/mcr), [kevent-ai](/repos/IA-Generative/kevent-ai)).
- Modernisation de l'infrastructure et de la CI/CD (utilisation de BuildKit rootless, durcissement des images Docker, intégration de Helm et optimisation des builds) ([mirai-mesreunions](/repos/IA-Generative/mirai-mesreunions), [ocr-api](/repos/IA-Generative/ocr-api), [claim-controller](/repos/IA-Generative/claim-controller)).
- Nouvelles capacités produit (support des modèles Scaleway, intégration RAG, scraping web et génération de questions/réponses) ([claude-code-scaleway](/repos/IA-Generative/claude-code-scaleway), [Stirling-PDF](/repos/IA-Generative/Stirling-PDF), [abrege](/repos/IA-Generative/abrege)).

## Dépôts les plus actifs
- [ocr-api](/repos/IA-Generative/ocr-api) : Passage à la version 0.20.0 avec un nouveau SDK TypeScript et une interface modernisée.
- [myvault](/repos/IA-Generative/myvault) : Travaux intensifs sur la sécurité, la protection des données et l'authentification multi-facteurs.
- [mcr](/repos/IA-Generative/mcr) : Refonte vers une architecture microservices et optimisation du pipeline de transcription.
- [abrege](/repos/IA-Generative/abrege) : Ajout de capacités de scraping web et de génération de questions/réponses.
- [drive](/repos/IA-Generative/drive) : Amélioration du partage collaboratif et sécurisation de l'intégration WOPI.
