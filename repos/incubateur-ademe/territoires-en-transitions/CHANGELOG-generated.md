## Changelog : territoires-en-transitions (30 derniers jours, au 26 octobre 2026)

### Résumé
Ce mois a été marqué par une transformation majeure de l'expérience utilisateur, notamment avec le lancement de l'outil "Aide à la priorisation" doté d'une interface visuelle enrichie (matrice et treemap). L'intelligence artificielle est désormais au cœur du processus grâce à une refonte complète de l'import de plans, permettant d'automatiser la lecture de documents (PDF, Word) avec un suivi de progression détaillé. Enfin, la gestion des indicateurs et des démarches PCAET a été stabilisée pour offrir un suivi plus précis et flexible dans le temps.

### Évolutions fonctionnelles

**Aide à la priorisation**
- Renommage de l'outil en "Aide à la priorisation" pour plus de clarté.
- Nouvelle interface visuelle incluant une matrice impact/mobilisation et une vue en treemap pour identifier les leviers prioritaires.
- Ajout d'une visite guidée interactive pour accompagner les utilisateurs dans la découverte de l'outil.
- Amélioration de l'interaction : les leviers et catégories sont désormais plus facilement filtrables et sélectionnables via la matrice.

**Import par Intelligence Artificielle (IA)**
- Extension des formats supportés : l'import IA accepte désormais les documents Word et les fichiers PDF.
- Amélioration du suivi : ajout d'une barre de progression et d'une liste détaillée des étapes de l'import (extraction, structuration, revue).
- Fiabilisation du processus : gestion des reprises après échec, détection des doublons et meilleure segmentation des documents complexes.
- Notification automatique par email dès que le plan importé est prêt pour vérification.

**Indicateurs et Scores**
- Introduction de nouvelles périodicités pour la saisie des données (mensuelle, trimestrielle, semestrielle).
- Amélioration du calcul des scores en intégrant de nouveaux critères (progression SNBC, réduction).
- Interface de saisie optimisée permettant de gérer simultanément les objectifs et les résultats.

**Gestion des Plans et Démarches (PCAET)**
- Gestion des secteurs réglementaires : les fiches d'un plan peuvent désormais être liées à des secteurs spécifiques.
- Automatisation de l'archivage : le système archive désormais automatiquement le PCAET précédent lors de l'adoption d'un nouveau.
- Amélioration de la consultation : les visiteurs peuvent désormais consulter les démarches PCAET adoptées et archivées en lecture seule.
- Fonctionnalité de téléchargement groupé des documents d'un dossier d'instruction au format ZIP.

**Référentiels et Actions de référence**
- Refonte de la vue détaillée des actions de référence pour une meilleure lisibilité des secteurs et leviers.
- Mise en place de la transition vers le mode "Climat Ressources" (CR) avec gestion des référentiels archivés.
- Amélioration de la recherche et du filtrage des actions de référence via l'URL.

### Évolutions techniques

**Observabilité et Monitoring**
- Migration du système de tracking des erreurs : PostHog remplace Sentry pour le suivi des erreurs front-end et back-end.
- Introduction d'OpenTelemetry pour la gestion des traces et des logs serveur.

**Intelligence Artificielle (LLM)**
- Diversification des modèles : intégration de Gemini (via Vertex AI), Mistral AI et Albert API.
- Optimisation des appels : gestion fine des quotas, des délais d'attente (timeouts) et de la consommation de jetons (tokens).
- Amélioration de la robustesse : implémentation de stratégies de "retry" et de gestion des erreurs de parsing.

**Performance et Architecture**
- Optimisation des performances : réduction des temps de chargement via le découplage des définitions et des états, et mise en cache des statistiques de la page d'accueil.
- Refactoring API : migration progressive des appels de PostgREST vers tRPC pour une meilleure cohérence des données.
- Mise à jour majeure de l'infrastructure : passage à Strapi 5 et optimisation des builds d'images Docker.

### Autres changements

**Design et UI**
- Harmonisation visuelle : application de la police Marianne et mise à jour des design tokens (notamment les couleurs d'erreur et de succès).
- Amélioration de l'accessibilité : corrections sur la navigation au clavier (Accordion, boutons).

**Documentation**
- Mise à jour des ADR (Architecture Decision Records) concernant le cycle de vie des données.
- Documentation technique enrichie pour la configuration de Strapi 5 et les processus d'import IA.
