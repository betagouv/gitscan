## Changelog : benefriches (30 derniers jours, au 14 août 2026)

### Résumé
Ce mois a été marqué par une amélioration significative de l'analyse économique et de l'expérience utilisateur. L'outil propose désormais des vues plus détaillées pour le bilan économique et une navigation plus fluide lors de la modification de projets (notamment photovoltaïques). Parallèlement, une refonte technique majeure a été entreprise pour stabiliser et harmoniser les formulaires de saisie.

### Évolutions fonctionnelles
- **Analyse économique et impacts** :
    - Ajout de nouvelles fenêtres d'information (modals) pour détailler le bilan économique (revente de site, aides financières, installations photovoltaïques et projets urbains).
    - Amélioration de la visualisation des impacts : regroupement des données immobilières et passage à une classification par "bénéficiaires" pour plus de clarté.
    - Ajout de nouveaux graphiques (colonnes) pour le seuil de rentabilité et de modales descriptives sur les graphiques d'analyse.
- **Expérience utilisateur (UX)** :
    - Optimisation du parcours de modification des projets photovoltaïques : navigation simplifiée, ajout de liens d'édition par section et gestion des mises à jour en cascade.
    - Amélioration des formulaires guidés (wizards) : affichage d'étapes imbriquées et ajout d'infobulles pour guider la saisie.
- **Corrections** :
    - Résolution de plantages lors de la mise à jour de projets photovoltaïques.
    - Correction de l'affichage de certains labels, couleurs et contenus dans les modales d'impact.

### Évolutions techniques
- **Architecture et Refactoring** :
    - Renforcement de la structure logicielle via l'implémentation de règles de "Clean Architecture" (Oxlint).
    - Refactorisation majeure du moteur de formulaires (*wizard-form*) pour mutualiser la logique entre la création et la modification de projets.
    - Unification des passerelles de données (*gateways*) pour les sols et les données municipales afin d'éviter les duplications.
- **API** :
    - Ajout d'un endpoint de statistiques avec gestion de la périodicité.
    - Extension de l'export CSV des projets personnalisés vers le référentiel ADEME.
- **Tests** :
    - Augmentation significative de la couverture des tests de bout en bout (E2E) pour couvrir les scénarios réels de mise à jour de projets et de transformation de sols.

### Autres changements
- Mise à jour de la documentation technique (ADR) concernant le moteur de formulaires.
- Nettoyage de la structure des dossiers et de la configuration Git.
