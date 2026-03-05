## Changelog : projects (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration des performances de l'application, en particulier lors de la manipulation de listes de tâches importantes. Plusieurs corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, notamment concernant l'édition de contenu, les filtres et l'affichage des commentaires. Enfin, des améliorations ont été apportées à l'interface utilisateur et aux notifications.

### Évolutions fonctionnelles
- Ajout d'un modèle d'email personnalisé pour les notifications, avec la marque de l'application. [#62](https://github.com/suitenumerique/projects/issues/62) et [#64](https://github.com/suitenumerique/projects/issues/64)
- Ajout d'un badge indiquant le nombre de tâches dans chaque liste. [#58](https://github.com/suitenumerique/projects/issues/58)
- Les membres et les étiquettes filtrés sont maintenant automatiquement assignés aux nouvelles tâches créées. [#57](https://github.com/suitenumerique/projects/issues/57)
- Affichage par défaut de toutes les activités dans le modal d'une tâche, avec possibilité de les masquer. [#56](https://github.com/suitenumerique/projects/issues/56)
- Ajout d'un bouton avec un lien de partage pour les tâches, incluant une info-bulle explicative.
- Correction d'un bug empêchant la sélection multiple de filtres. [#60](https://github.com/suitenumerique/projects/issues/60)
- Correction d'un bug empêchant l'affichage correct des commentaires en Markdown.
- Correction d'un bug aléatoire lors de la création de tâches.
- Correction de l'affichage des tableaux partagés dans le menu latéral. [#59](https://github.com/suitenumerique/projects/issues/59)

### Évolutions techniques
- Optimisations significatives des performances lors du déplacement de tâches dans les listes, notamment en utilisant la mémoïsation et des composants intermédiaires.
- Suppression des hooks lint bloquant les opérations Git et npm, la CI/CD assurant désormais la qualité du code.
- Possibilité de désactiver l'indexation par les moteurs de recherche pour les environnements non-production.
- Mise à jour de la librairie de drag-and-drop vers la dernière version pour tenter de résoudre les problèmes de performance.
- Correction de l'utilisation incorrecte de certains sélecteurs dans les composants, améliorant les performances.

### Autres changements
- Correction de l'affichage d'une bannière masquée par le contenu de la page.
- Correction de problèmes liés à l'éditeur Markdown, notamment la séparation des paragraphes et le déclenchement des actions.
- Mise à jour de la version de l'application à 1.2.0.
- Corrections et améliorations du kit UI.
- Mise à jour de la documentation.
