## Changelog : territoires-en-transitions (30 derniers jours, au 15 octobre 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape majeure avec l'intégration de l'intelligence artificielle pour automatiser l'analyse des fiches et l'importation des plans de transition (PCAET). L'outil d'aide à la priorisation a été entièrement repensé avec une interface plus intuitive et une visite guidée pour accompagner les utilisateurs. Enfin, la gestion des indicateurs et le suivi des démarches ont été renforcés pour offrir une plus grande précision dans le pilotage des actions écologiques.

### Évolutions fonctionnelles

**Intelligence Artificielle & Automatisation**
- Intégration de l'IA (Mistral AI, Gemini via Vertex AI) pour l'analyse automatique des fiches et la classification des leviers.
- Nouveau système d'importation assistée par IA pour les plans PCAET (support des formats PDF et Word), incluant la détection des partenaires, financements et moyens humains.
- Amélioration de la fiabilité de l'IA avec un suivi précis de la progression, de la consommation de jetons et une gestion robuste des erreurs d'importation.

**Aide à la priorisation**
- Refonte complète de l'interface de priorisation : nouvelle matrice impact/mobilisation, treemap interactif et graphiques à barres.
- Ajout d'une visite guidée pour faciliter la prise en main de l'outil.
- Meilleure visibilité des leviers et sous-leviers à prioriser grâce à un nouveau système de mise en avant visuelle.

**Gestion des démarches (PCAET) et des plans**
- Amélioration du cycle de vie des démarches : gestion optimisée du dépôt, de l'instruction, de l'adoption et de l'archivage.
- Possibilité pour les instructeurs de télécharger l'intégralité des documents d'un dossier sous forme de fichier ZIP.
- Meilleure gestion des secteurs réglementaires et des vulnérabilités au sein des plans.

**Indicateurs et Référentiels**
- Flexibilité accrue des indicateurs avec la prise en charge de nouvelles périodicités (mensuelle, trimestrielle, semestrielle).
- Calcul des scores plus précis intégrant de nouveaux critères (SNBC, réduction des émissions).
- Amélioration de la gestion des référentiels et de leur archivage.

### Évolutions techniques

**Architecture & API**
- Migration progressive des appels API de PostgREST vers tRPC pour améliorer la robustesse et le typage (notamment pour les collectivités, les plans et le site public).
- Refonte de la gestion des documents et des preuves pour une meilleure traçabilité.

**Observabilité & Monitoring**
- Remplacement de Sentry par PostHog pour le suivi des erreurs (front et back) et l'analyse du comportement utilisateur.
- Introduction d'OpenTelemetry pour la gestion des traces et des logs.

**Infrastructure & CI/CD**
- Mise à jour majeure de Strapi vers la version 5.
- Optimisation des processus de déploiement et de restauration des bases de données (AWS CLI, gestion des backups).
- Amélioration des performances de build des images de déploiement.

### Autres changements
- Mise à jour de la documentation technique (ADR, guides de configuration Strapi 5).
- Nettoyage du code source (suppression de code mort via Knip).
- Refonte de la présentation du site web (FAQ, mise en avant des services PCAET).
