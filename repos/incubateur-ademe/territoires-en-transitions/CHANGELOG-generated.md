## Changelog : territoires-en-transitions (30 derniers jours, au 20 octobre 2026)

### Résumé
Ce mois a été marqué par une transformation majeure de l'expérience utilisateur avec le lancement de l'outil « Aide à la priorisation » et l'amélioration significative de l'importation de données par intelligence artificielle. La plateforme renforce également son accompagnement des collectivités pour le dépôt des PCAET, en proposant un parcours dédié, plus fluide et mieux documenté.

### Évolutions fonctionnelles

**Aide à la priorisation**
- Renommage de l'outil en « Aide à la priorisation » pour plus de clarté.
- Refonte complète de l'interface : nouvelle barre d'en-tête (analyse, leviers, actions sauvegardées), nouvelle matrice impact × mobilisation et vue Mondrian.
- Amélioration de la visualisation : ajout d'un treemap cliquable, d'un histogramme par levier/catégorie et de tooltips harmonisés.
- Introduction d'une visite guidée interactive pour accompagner les utilisateurs dans la découverte des outils.
- Possibilité de sauvegarder des actions et de les retirer via une nouvelle page dédiée.

**Importation par Intelligence Artificielle (IA)**
- Support étendu des formats : l'importation accepte désormais les documents Word (.docx).
- Amélioration de la fiabilité : gestion de la reprise automatique des imports interrompus ou en échec et meilleure détection des doublons.
- Suivi de l'utilisateur : la barre de progression est remplacée par une liste détaillée des étapes de l'import avec leur état d'avancement.
- Traitement des documents longs : les documents volumineux sont désormais découpés en segments pour un traitement plus efficace.

**Gestion des démarches PCAET**
- Lancement d'un service dédié au dépôt et au pilotage des PCAET, incluant une page de démonstration et une FAQ spécifique.
- Automatisation de l'archivage : le PCAET précédent est automatiquement archivé lors de l'adoption du nouveau.
- Amélioration du suivi : nouveaux badges de statut, gestion des délais d'avis et possibilité de télécharger l'ensemble des documents d'un dossier en format ZIP.
- Consultation : ouverture de la lecture des démarches adoptées et archivées pour les utilisateurs autorisés.

**Indicateurs et Référentiels**
- Flexibilité des données : introduction de nouvelles périodicités pour le suivi (mensuelle, trimestrielle, semestrielle).
- Simplification de la saisie : unification de la saisie des résultats et des objectifs dans une interface commune.
- Évolution des scores : amélioration du calcul des scores indicatifs intégrant de nouveaux critères (progression SNBC, réduction).
- Actions de référence : nouvelle vue détaillée présentant les descriptions, secteurs, leviers et les collectivités liées.

### Évolutions techniques

**Intelligence Artificielle & LLM**
- Migration vers Gemini via Vertex AI pour une meilleure stabilité et performance.
- Optimisation des performances : parallélisation des tâches d'importation (Albert et Gemini) pour réduire les temps d'attente.
- Observabilité : mise en place d'un traçage détaillé des appels LLM (durée, jetons consommés, tentatives).

**Architecture & Backend**
- Migration progressive : remplacement des appels PostgREST par tRPC pour les plans, le site et les collectivités, améliorant la sécurité et le typage.
- Observabilité et monitoring : remplacement de Sentry par PostHog pour le suivi des erreurs (front et back) et OpenTelemetry pour les traces et logs.
- Sécurité : configuration des cookies de session Supabase par environnement et renforcement de l'authentification via ProConnect.

**Infrastructure & CI/CD**
- Optimisation des bases de données : amélioration des processus de restauration de backups et gestion des transactions pour les imports de données.
- Performance CI : accélération des builds d'images de déploiement et optimisation du cache.

### Autres changements
- **Documentation** : mise à jour de la documentation technique pour Strapi 5 et des guides de processus pour les cycles PCAET.
- **Nettoyage** : suppression définitive du module « Panier » et de ses dépendances obsolètes.
- **Maintenance** : mise à jour majeure vers Strapi 5.
