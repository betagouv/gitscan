## Changelog : territoires-en-transitions (30 derniers jours, au 09 octobre 2026)

### Résumé
Ce mois-ci, le projet a franchi des étapes clés avec l'amélioration du parcours de dépôt et de suivi du PCAET, le renforcement de l'importation intelligente de plans par IA, et l'ajout d'outils d'analyse plus fins pour les collectivités. L'accent a également été mis sur la fiabilité des données et la modernisation de l'infrastructure technique.

### Évolutions fonctionnelles
- **Parcours PCAET (Démarches) :**
  - Amélioration du suivi des instructions pour les agents (clarté des statuts, visibilité des étapes).
  - Optimisation de la gestion documentaire : possibilité de télécharger l'ensemble d'un dossier en ZIP, ajout de barres de progression pour les imports et gestion plus fine de la confidentialité des fichiers.
  - Clarification des étapes de dépôt et de validation pour les collectivités.
- **Importation par IA (Plans) :**
  - Amélioration majeure de l'importation automatique des plans d'actions (support des formats Word et PDF, meilleure segmentation des données extraites).
  - Mise en place d'une étape de vérification humaine obligatoire pour valider les données importées par l'IA.
  - Meilleure gestion des erreurs lors de l'importation pour faciliter le diagnostic par l'utilisateur.
- **Analyse et Pilotage :**
  - Introduction de nouvelles vues permettant aux collectivités de qualifier la pertinence de leurs "leviers" et "catégories" d'actions.
  - Ajout d'indicateurs de mobilisation pour mesurer l'engagement sur différents volets de la transition.
- **Actions de référence :**
  - Mise à disposition d'un nouveau module permettant de consulter, rechercher et filtrer une bibliothèque d'actions types.
- **Référentiels et Indicateurs :**
  - Amélioration du calcul des scores indicatifs et possibilité de déclarer certains indicateurs comme "non applicables".

### Évolutions techniques
- **Architecture et API :**
  - Migration progressive de la récupération de données de PostgREST vers tRPC pour renforcer la sécurité et le typage.
  - Optimisation de la gestion des sessions et de l'authentification via ProConnect.
- **Intelligence Artificielle :**
  - Optimisation de l'utilisation des modèles LLM (Gemini/Albert) : gestion des quotas, amélioration de la précision de l'extraction et support de l'entrée par image.
- **Observabilité et Monitoring :**
  - Remplacement de Sentry par PostHog et OpenTelemetry pour un suivi plus complet des erreurs (front et back) et des performances.
- **Infrastructure et CMS :**
  - Migration majeure vers Strapi 5, incluant la mise à jour des processus de déploiement et de gestion des contenus.
  - Optimisation des pipelines CI/CD pour accélérer les temps de build.
  - Amélioration de la configuration Redis et Supabase pour les environnements de développement et de production.

### Autres changements
- **Documentation :** Mise à jour importante des ADR (Architecture Decision Records) et des guides de configuration technique.
- **Nettoyage :** Suppression de fonctionnalités obsolètes (notamment le module "panier") et du code mort pour alléger l'application.
