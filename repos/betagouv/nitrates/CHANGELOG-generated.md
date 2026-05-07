## Changelog : nitrates (30 derniers jours, au 05 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration significative de l'édition et de la gestion des arbres de décision, avec l'introduction d'un éditeur YAML en ligne, des fonctionnalités d'annulation/rétablissement, et une meilleure intégration des données. Des améliorations ont également été apportées à l'importation de données, à l'interface utilisateur et à la gestion des contacts.

### Évolutions fonctionnelles
- **Édition des arbres de décision :** Introduction d'un éditeur YAML en ligne pour la création et la modification des arbres de décision, avec des fonctionnalités d'annulation/rétablissement, de verrouillage pour l'édition concurrente et d'historique des révisions. [#27](https://github.com/betagouv/nitrates/pull/27)
- **Interface utilisateur :** Amélioration de l'interface utilisateur avec des boutons d'édition plus directs, une meilleure gestion des brouillons, et une intégration du cadastre IGN pour la zone d'activation.
- **Importation de données :** Importation des données ZV depuis Sandre WFS, remplacement des étiquettes codées en dur par des recherches côté serveur pour les données RPG. [#17](https://github.com/betagouv/nitrates/pull/17)
- **Gestion des contacts :** Amélioration de la gestion des informations de contact, avec un fallback sur la configuration la plus récente et des avertissements en cas de portail non activé.
- **Simulateur :** Ajout d'une vue simulateur avec un formulaire HTML brut et un template de résultat pour le débogage.
- **Cartographie :** Ajout de la possibilité de cliquer sur la carte pour pré-remplir les coordonnées de latitude/longitude.
- **Haies :** Ajout de la validation de la longueur maximale des haies, avec une limite configurable et des tests associés.

### Évolutions techniques
- **Refactoring :** Refactoring du code pour améliorer la structure et la maintenabilité, notamment avec la séparation des préoccupations et l'utilisation de nouveaux helpers.
- **Tests :** Ajout de tests E2E avec Playwright pour le simulateur et d'autres fonctionnalités.
- **Dépendances :** Ajout des dépendances `ruamel.yaml` et `Pygments` pour l'édition YAML.
- **Infrastructure :** Amélioration de la configuration Docker pour ARM64.
- **API :** Création d'endpoints API pour la cascade JavaScript et la récupération des référentiels.
- **Base de données :** Ajout d'un modèle `DecisionTreeRevision` pour le versionnement des arbres de décision.
- **Configuration :** Ajout d'un paramètre `NITRATES_SPECS_DIR` pour la configuration des spécifications YAML.

### Autres changements
- **Documentation :** Migration de la FAQ vers Gitbook.
- **Nettoyage de code :** Suppression de code obsolète et amélioration de la lisibilité du code.
- **Corrections de bugs :** Correction de plusieurs bugs, notamment liés à l'affichage des données, à la gestion des erreurs et à la validation des formulaires.
- **Améliorations de performance :** Optimisation des requêtes et du code pour améliorer les performances.
- **Mise à jour des dépendances :** Mise à jour de certaines dépendances. (Non listées individuellement)
