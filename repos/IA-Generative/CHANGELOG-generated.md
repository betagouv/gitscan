# Synthèse d'activité : IA-Generative (du DD/MM au DD/MM)

## Résumé de l'activité
L'organisation a franchi des étapes majeures dans le développement de ses solutions d'intelligence documentaire et d'assistance, en mettant l'accent sur l'analyse sémantique avancée, la génération de documents et l'intégration de protocoles de communication modernes (MCP). Les évolutions récentes visent à transformer l'expérience utilisateur grâce à des interfaces plus intuitives (vues en grille, ergonomie mobile, onboarding guidé) et des capacités d'IA plus transparentes et performantes.

Ces avancées renforcent la maturité des produits pour les utilisateurs finaux, tout en offrant des outils de gestion et de suivi de la qualité de l'IA de plus en plus précis. L'impact se traduit par des outils plus fiables, capables de gérer des flux de travail complexes (transcription, analyse de dossiers, génération de rapports) de manière automatisée et sécurisée.

## Sécurité
- **Protection contre les attaques IA** : Renforcement de la sécurité contre les injections de prompt (OWASP LLM01) et mise en place de détecteurs d'anomalies et de garde-fous anti-leak dans [owuiapps-agents](/repos/IA-Generative/owuiapps-agents).
- **Authentification et gestion des accès** : Généralisation de l'authentification à deux facteurs (2FA/TOTP) et gestion fine des niveaux de sécurité eIDAS dans [myvault](/repos/IA-Generative/myvault) et [keycloak-jar-test](/repos/IA-Generative/keycloak-jar-test).
- **Sécurisation des API et des échanges** : Implémentation de clés API pour les communications machine-to-machine (M2M), de jetons de rafraîchissement et de protections CSRF dans [ocr](/repos/IA-Generative/ocr) et [ocr-api](/repos/IA-Generative/ocr-api).
- **Confidentialité et protection des données** : Migration des secrets vers les coffres-forts natifs de l'OS, chiffrement des données sensibles et nettoyage des journaux (logs) pour éviter les fuites d'informations dans [iassistant-libreoffice](/repos/IA-Generative/iassistant-libreoffice) et [myvault](/repos/IA-Generative/myvault).
- **Durcissement des infrastructures** : Amélioration de la sécurité des conteneurs (exécution non-root, vérification de checksums) dans [toolmesh](/repos/IA-Generative/toolmesh), [ocr](/repos/IA-Generative/ocr), [ocr-api](/repos/IA-Generative/ocr-api), [abrege](/repos/IA-Generative/abrege) et [device-management](/repos/IA-Generative/device-management).

## Autres changements notables
- **Évolutions architecturales majeures** : Migration vers des modèles de microservices, changement de moteurs de gestion de données (passage de Kafka à Redis, de Minio à RustFS, ou de Qdrant à Meilisearch) et optimisation des pipelines de transcription dans [mcr](/repos/IA-Generative/mcr), [kevent-ai](/repos/IA-Generative/kevent-ai), [ocr-api](/repos/IA-Generative/ocr-api) et [Muffin](/repos/IA-Generative/Muffin).
- **Intégration du protocole MCP (Model Context Protocol)** : Support de ce nouveau standard pour enrichir les capacités des agents dans [toolmesh](/repos/IA-Generative/toolmesh), [mille-feuille](/repos/IA-Generative/mille-feuille) et [dig-dig-doc](/repos/IA-Generative/dig-dig-doc).
- **Modernisation de la CI/CD et du déploiement** : Optimisation des processus de construction (BuildKit rootless, Helm, automatisation des environnements de preview) dans [mirai-mesreunions](/repos/IA-Generative/mirai-mesreunions), [claim-controller](/repos/IA-Generative/claim-controller) et [mirai-api](/repos/IA-Generative/mirai-api).

## Dépôts les plus actifs
- [mycollections](/repos/IA-Generative/mycollections) : Amélioration significative de l'UX mobile, de la recherche et de la gestion de la qualité des générations IA.
- [myvault](/repos/IA-Generative/myvault) : Travaux intensifs sur la sécurité, la 2FA et la protection des données sensibles.
- [ocr](/repos/IA-Generative/ocr) et [ocr-api](/repos/IA-Generative/ocr-api) : Évolutions majeures de l'interface, des SDK et du durcissement de la sécurité.
- [iassistant-libreoffice](/repos/IA-Generative/iassistant-libreoffice) : Sortie de la version 0.3.0 avec internationalisation et refonte de la gestion des secrets.
- [abrege](/repos/IA-Generative/abrege) : Ajout de capacités d'analyse sémantique (Q&A, entités) et modernisation de l'interface.
