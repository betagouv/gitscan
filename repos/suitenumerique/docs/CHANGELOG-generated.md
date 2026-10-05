## Changelog : docs (30 derniers jours, au octobre 2026)

### Résumé
Ce mois a été marqué par une transition majeure de l'infrastructure de collaboration vers YHub, apportant une plus grande robustesse et le support du mode hors ligne. Nous avons également introduit un nouveau système de mentions avec notifications par email, enrichi les options d'exportation et affiné l'interface utilisateur pour une expérience plus fluide.

### Évolutions fonctionnelles
- **Système de mentions** : ajout de notifications par email (traitées de manière asynchrone), gestion fine des accès (exclusion des lecteurs des mentions) et amélioration du contenu des emails.
- **Collaboration et Édition** : support du mode hors ligne, accès à l'historique des versions, duplication de documents avec sous-documents et amélioration de l'interliage automatique lors du collage de liens.
- **Interface et UX** : refonte des pages d'erreur (401, 403, 404) et de la page de confirmation d'email ; nouveaux raccourcis clavier (mode présentation) ; sélection de langue simplifiée et gestion améliorée des images (conservation des légendes et alignements lors du remplacement).
- **Export et Navigation** : nouvelles options d'export (Markdown, PDF avec gestion des ratios d'image) ; ouverture des résultats de recherche dans un nouvel onglet et défilement automatique vers les blocs liés.

### Évolutions techniques
- **Moteur de collaboration** : migration complète du serveur de collaboration de HocusPocus vers YHub (v0.9.0), incluant la migration des documents et de l'historique depuis le stockage S3 legacy.
- **Infrastructure et Déploiement** : déploiement de la version 6.0.0-alpha.1 du chart Helm, intégration de métriques Prometheus et amélioration des outils de tests de charge (scénarios k6, canaries de navigation et tableaux de bord Grafana).
- **Sécurité et Backend** : renforcement de l'authentification via JWT, ajout de limitations de débit (throttling) sur les endpoints de mentions et validation stricte des identifiants (UUID).
- **Développement et CI/CD** : migration du serveur YHub en TypeScript, amélioration des tests E2E et ajout de la validation (lint, typecheck, build) pour le serveur de collaboration.
- **Optimisations** : remplacement de Minio par Silo et optimisation des requêtes SQL et du cache Redis.

### Autres changements
- **Documentation** : mise à jour des guides d'installation (YHub, Kubernetes/Helm) et de la documentation d'architecture.
- **Internationalisation** : mise à jour des chaînes traduites et optimisation du processus d'export pour Crowdin.
