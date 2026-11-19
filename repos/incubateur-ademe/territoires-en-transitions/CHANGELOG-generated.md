## Changelog : territoires-en-transitions (30 derniers jours, au 18 novembre 2026)

### Résumé
Ce mois a été marqué par une évolution majeure de la plateforme avec l'intégration de la trajectoire SNBC 3 et le renforcement des outils de pilotage des plans d'actions (PCAET). Les utilisateurs bénéficient désormais de nouvelles jauges d'avancement, d'un suivi plus fin des statuts et d'un système d'importation assisté par intelligence artificielle. La gestion des relations entre les territoires (Supras et EPCI) a également été fluidifiée pour mieux accompagner les démarches de transition.

### Évolutions fonctionnelles

**Suivi et pilotage des plans (PCAET)**
- Introduction de jauges d'avancement visuelles pour les fiches, les axes et les plans, permettant un suivi en temps réel de la progression.
- Création de nouveaux blocs de pilotage : évolution des statuts sur une période donnée et avancement par axe.
- Possibilité d'ajouter des modules personnalisés au suivi du plan, partageables avec le tableau de bord.
- Amélioration de l'importation de plans via l'IA : le processus est désormais guidé étape par étape et propose des suggestions d'effets attendus pour chaque action.
- Ajout de fonctionnalités d'exportation (Excel et PNG) pour les blocs de pilotage et les graphiques de suivi.

**Indicateurs et trajectoire SNBC 3**
- Intégration complète de la méthodologie et des données de la trajectoire SNBC 3.
- Mise à disposition de nouveaux outils pour consulter et exporter les données SNBC 3 (classeurs dédiés, outils Excel).
- Amélioration de la personnalisation des indicateurs : possibilité de créer des sous-indicateurs avec une profondeur illimitée et de choisir leur mode de calcul (addition des valeurs).
- Optimisation de l'interface des indicateurs : édition des pilotes directement en ligne et export Excel simplifié depuis les vignettes.

**Gestion des démarches et des territoires**
- Optimisation de la gestion des "Supras" : un Supra peut désormais piloter un dépôt PCAET pour un groupe d'EPCI, avec une visibilité adaptée pour chaque membre.
- Mise en place d'un mode "démo" pour les administrateurs, permettant de simuler un parcours complet de dépôt PCAET (du diagnostic à l'adoption).
- Amélioration du suivi d'instruction : ajout des dates de saisine et d'adoption, et nouveaux filtres par département.
- Déploiement de nouveaux outils de gestion pour les programmes d'audit et de labellisation (programme TETE).

**Priorisation et recherche**
- Refonte de l'outil de priorisation des leviers : interface de la matrice améliorée, ajout d'une aide visuelle pour identifier le levier prioritaire et accès direct à la documentation méthodologique.
- Nouveau composant de recherche performant avec suggestions groupées et tolérance aux fautes de frappe.

### Évolutions techniques

**Infrastructure et Déploiement**
- Migration de l'infrastructure vers une gestion "as code" via Coolify et Terraform sur Scaleway (réseaux, bases de données, serveurs, stockage).
- Amélioration de l'observabilité du système avec l'intégration de Grafana Alloy et la mise en place de tableaux de bord de monitoring.
- Mise en place d'une infrastructure de préproduction (preprod) isolée et automatisée.

**Intelligence Artificielle et Assistance**
- Développement d'un serveur MCP (Model Context Protocol) permettant d'offrir une assistance intelligente basée sur les données métier de la plateforme.
- Renforcement du tracking analytique via PostHog pour suivre précisément les parcours utilisateurs, les succès/échecs des imports IA et les événements métier.

**Architecture et Performance**
- Refactoring massif de la gestion des indicateurs pour améliorer la maintenabilité (utilisation de contextes React et découpage en vues spécialisées).
- Migration de la gestion d'état côté client de SWR vers React Query sur le site vitrine.
- Optimisation des performances de recherche et de chargement des référentiels.
- Amélioration de la robustesse du système de génération de rapports PDF (utilisation de worker threads interruptibles).

### Autres changements
- Mise à jour de la vidéo de démonstration sur la page d'accueil.
- Enrichissement de la documentation technique (ADR, plans de migration, runbooks d'infrastructure).
- Nettoyage général du code et suppression de composants et tests obsolètes.
