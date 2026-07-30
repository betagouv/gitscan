## Changelog : benefriches (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'expérience utilisateur pour la création et la modification de projets photovoltaïques, ainsi que sur une refactorisation importante du code pour une meilleure maintenabilité et évolutivité. Des améliorations ont également été apportées au calcul et à l'affichage des impacts économiques et environnementaux des projets.

### Évolutions fonctionnelles
- Ajout de liens d'édition par section dans le résumé des projets photovoltaïques.
- Amélioration de la navigation et de la convivialité lors de la modification des projets photovoltaïques.
- Intégration de l'affichage de la surface contaminée et de la surface totale du site dans les exports CSV des projets de reconversion.
- Ajout de modals pour l'analyse économique des projets de réhabilitation de sites, d'installation de panneaux photovoltaïques et d'assistance financière.
- Affichage de la répartition des sols dans les modals d'analyse économique.
- Regroupement des acquisitions immobilières (revente de sites, bâtiments et achat de sites) dans la catégorie "acquisition immobilière" dans la vue des impacts.
- Ajout d'info-bulles pour expliquer les champs de la réhabilitation de site.
- Amélioration de l'affichage des impacts dans l'onglet d'analyse du retour sur investissement.

### Évolutions techniques
- Refactorisation majeure du code de la création et de la mise à jour des projets, notamment pour les projets photovoltaïques, en utilisant le moteur "wizard-form".
- Amélioration de l'architecture du code avec une séparation plus claire des responsabilités et une meilleure organisation des dossiers.
- Mise à jour des outils de linting (oxlint) et des tests pour garantir la qualité du code.
- Amélioration de la couverture des tests unitaires et end-to-end.
- Refactorisation de la gestion des données de l'adresse nationale.
- Simplification et unification du code pour le calcul des impacts environnementaux.
- Amélioration de la gestion des états et des données dans l'interface utilisateur.
- Suppression de code obsolète et simplification de la configuration.

### Autres changements
- Documentation mise à jour pour refléter les changements apportés au code et aux fonctionnalités.
- Amélioration des outils internes pour faciliter le développement et la maintenance du projet.
- Ajout de nouveaux outils pour automatiser certaines tâches, comme la création de worktrees et la correction des erreurs de CI.
- Clarification des règles de test et des bonnes pratiques de codage.
- Suppression de références mortes dans la documentation.
- Correction de bugs mineurs et amélioration de la performance.
- Mise à jour des dépendances.
