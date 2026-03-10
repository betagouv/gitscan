## Changelog : dialog-integrations (30 derniers jours)

### Résumé
Ce projet a connu des améliorations significatives au cours des dernières semaines, notamment l'intégration de nouvelles sources de données (Brest, Sarthe) et l'ajout de fonctionnalités permettant la mise à jour des données. Des corrections ont également été apportées pour assurer la précision des informations, notamment concernant le tonnage. L'infrastructure a été améliorée avec des mises à jour de dépendances et des optimisations du code.

### Évolutions fonctionnelles
- Intégration de la source de données de Brest avec l'ajout de l'URL du lien associé. [#1](https://github.com/MTES-MCT/dialog-integrations/pull/1)
- Intégration des limitations de gabarits pour le département de la Sarthe. [#2](https://github.com/MTES-MCT/dialog-integrations/pull/2)
- Correction du statut de publication pour les données de la Sarthe, maintenant correctement défini comme "publié".
- Correction de l'unité de mesure du tonnage pour le département de la Sarthe, affiché en tonnes.
- Ajout de la possibilité de mettre à jour les données via la ligne de commande. [#2](https://github.com/MTES-MCT/dialog-integrations/pull/2)
- Ajout d'arrêtés pour la Sarthe lorsque le tonnage est nul.

### Évolutions techniques
- Refactorisation et harmonisation de certaines fonctions pour améliorer la lisibilité et la maintenabilité du code.
- Possibilité de gérer plusieurs sources de données.
- Ajout d'un fichier `.gitignore` à la racine du projet.
- Amélioration de la qualité du code avec l'utilisation de `ruff` pour le linting et le formatage.
- Tous les tests passent suite aux corrections et optimisations.

### Autres changements
- Mise à jour de la dépendance `nbconvert`.
