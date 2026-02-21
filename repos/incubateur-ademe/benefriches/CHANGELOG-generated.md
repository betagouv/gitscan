## Changelog : benefriches (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration du processus de création de projets urbains, notamment en introduisant un nouveau flux pour les usages et les espaces, et en ajoutant des tests automatisés pour garantir la qualité et la stabilité de l'application. Des améliorations ont également été apportées à l'infrastructure et aux outils de développement.

### Évolutions fonctionnelles
- Amélioration du flux de création de projets urbains avec une nouvelle approche pour les usages et les espaces (#419a1cc, #608bbdf, #7555898, #a4618b1, #d3087b9, #e1b0312, #7cc190f, #9f15613, #7cfdcbc, #bf3083a, #076fc86, #20aa39c).
- Ajout de la possibilité de créer des sites agricoles personnalisés et des friches personnalisées avec des tests automatisés associés (#419a1cc, #7cc2d58, #9f15613).
- Ajout de menus d'actions pour la gestion des projets sur les pages "Mes évaluations" et de détails de site (#08f10e2, #bef2355).
- Ajout de la possibilité d'archiver un projet de reconversion (#d8b3adb).
- Amélioration de l'affichage des types de sols de manière cohérente dans les vues avec des diagrammes circulaires (#86dbd6d).
- Ajout de dialogues de blocage de navigation sur les formulaires de création de site et de projet (#7f91806).
- Ajout de séparateurs de milliers pour les montants monétaires (#032146a).
- Mise à jour du libellé du bouton de création de projet pour "Évaluer un projet sur ce site" (#bf3083a).
- Ajout de pictogrammes pour tous les nouveaux usages urbains (#9c399c9).
- Correction de l'acteur incorrect dans la description modale de la régulation de l'eau (#1ab513a).
- Correction du chargement des données du site et du projet pour la mise à jour du projet (#5dcf753).
- Mise à jour du pictogramme de téléchargement sur la page des impacts (#8112d6d).
- Correction du retour de la liste des sites avec des projets même si la récupération de la mutabilité de l'évaluation à partir de mutafriches échoue (#717a345).

### Évolutions techniques
- Refactorisation du code lié aux usages et aux espaces des projets urbains pour une meilleure maintenabilité (#a7e25fa, #429e148, #876f17e).
- Mise à jour des dépendances de l'API et des tests E2E (#5fe1745, #e4254ff, #52bae42).
- Amélioration de la gestion des adresses avec la mise en cache des résultats et la suppression du "race condition" (#d2bc5e3, #d7bd12a, #2fb660f).
- Refactorisation de l'utilisation des DTO (Data Transfer Object) pour une meilleure cohérence entre le frontend et le backend (#fc015f1, #a6a2f98).
- Simplification du processus de build Scalingo en laissant le buildpack gérer la compilation (#1d47c9d).
- Ajout de tests E2E (End-to-End) pour la création de projets urbains et la page "Mes évaluations" (#2716d6d, #44a3f28, #80fa5eb).
- Amélioration de l'architecture de la gestion des features du site (#58eec35, #689391b).
- Ajout de nouveaux outils et compétences basés sur l'IA pour la revue de code, la migration de bases de données et la création de tests E2E (#4e0e25a, #b058552, #9dae962, #29cabd7, #6dd6d1e, #5b142ab).

### Autres changements
- Mise à jour de la documentation pour les générateurs de projets urbains avec des informations sur la distribution des sols (#69e588d).
- Correction de fautes de frappe et amélioration de la formulation dans l'interface utilisateur (#04af246, #4c72e0f, #20aa39c).
- Mise à jour des scripts et configurations pour l'utilisation de worktrees et l'installation des dépendances (#a2367a9, #b639a32).
- Amélioration de la configuration de Docker pour une meilleure gestion des services et des ports (#e4c4a99).
- Ajout d'une option pour spécifier un fichier d'environnement pour la commande docker compose dans le script de suppression des worktrees (#4ea0246).
