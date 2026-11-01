## Changelog : territoires-en-transitions (30 derniers jours, au 30 octobre 2026)

### Résumé
Ce mois a été marqué par une montée en puissance de l'intelligence artificielle et de l'aide à la décision. La plateforme intègre désormais des capacités d'importation automatique de plans via IA, une refonte complète de l'outil d'aide à la priorisation des actions, et un suivi plus fin du cycle de vie des démarches PCAET (adoption, archivage, suivi des dates).

### Évolutions fonctionnelles

**Intelligence Artificielle & Importation**
- **Importation intelligente de plans :** Support étendu des formats Word et PDF avec extraction automatique des partenaires, financements, moyens humains et objectifs.
- **Robustesse de l'import :** Mise en place de la reprise d'importation en cas d'interruption ou d'échec, et meilleure gestion des erreurs de segmentation.
- **Suivi de l'import :** Ajout d'une barre de progression détaillée et d'une liste d'étapes pour suivre l'avancement de l'extraction IA.

**Aide à la priorisation**
- **Nouvelle interface :** Refonte visuelle incluant une matrice "Impact × Mobilisation", un treemap interactif et un classement des leviers.
- **Parcours utilisateur :** Ajout d'une visite guidée pour découvrir l'outil et d'un système de sauvegarde d'actions pour construire une stratégie.
- **Analyse :** Amélioration de la précision des analyses et ajout d'un bouton d'accès direct à la méthodologie.

**Gestion des démarches (PCAET)**
- **Cycle de vie :** Automatisation de l'archivage des anciens PCAET lors de l'adoption d'un nouveau plan et gestion des statuts (Adopté, En instruction).
- **Suivi administratif :** Ajout des dates de saisine et d'adoption dans le tableau de suivi, avec possibilité de tri par date.
- **Gestion documentaire :** Possibilité pour les instructeurs de télécharger l'ensemble des documents d'un dossier sous forme de fichier ZIP.
- **Saisie des données :** Amélioration de la saisie des secteurs réglementaires, de la vulnérabilité et de la séquestration carbone.

**Indicateurs & Référentiels**
- **Périodicité :** Extension du support des cadences de saisie (mensuelle, trimestrielle, semestrielle).
- **Saisie unifiée :** Regroupement de la saisie des résultats et des objectifs pour simplifier l'expérience utilisateur.
- **Export :** Amélioration des exports Excel pour les indicateurs et les scores des référentiels (ajout des thématiques, de l'adaptation et de la labellisation).

### Évolutions techniques

**IA & Protocoles**
- **Serveur MCP (Model Context Protocol) :** Implémentation d'un serveur MCP permettant à des agents IA d'accéder à des outils métier et à une base analytique en lecture seule.
- **Multi-modèles :** Intégration et tests de différents modèles (Albert, Gemini, Mistral AI) pour l'analyse et l'extraction de données.

**Observabilité & Monitoring**
- **Migration de l'error tracking :** Remplacement de Sentry par PostHog pour le suivi des erreurs front-end et back-end.
- **Traces & Logs :** Introduction d'OpenTelemetry pour la gestion des traces et des logs serveur.

**Infrastructure & Backend**
- **Optimisation PDF :** Déplacement du rendu des PDF dans des *worker threads* pour éviter de bloquer le serveur et permettre l'interruption des tâches.
- **Sécurité :** Renforcement de la vérification TLS pour les connexions PostgreSQL.
- **Mises à jour majeures :** Migration vers Strapi 5, mise à jour de Node.js et de Playwright pour la CI.
- **Performance :** Optimisation des requêtes SQL (pagination) et séparation des définitions et des états des actions pour accélérer le chargement des référentiels.

### Autres changements
- **Documentation :** Mise à jour des documents d'architecture (ADR) concernant le cycle de vie des données.
- **UI/UX :** Nettoyage général des composants (badges, tooltips, espacements) pour une meilleure conformité au design system.
