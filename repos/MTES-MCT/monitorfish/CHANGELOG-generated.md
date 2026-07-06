## Changelog : monitorfish (30 derniers jours, au 03 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'interface utilisateur, notamment pour les contrôles en mer et à la débarque dans le cadre du projet e-ISR. Des corrections de bugs et des optimisations techniques ont également été apportées, ainsi que des mises à jour de dépendances et de l'infrastructure de développement. L'ajout de groupes prioritaires pour les navires et l'amélioration de la gestion des informations sur les navires sont également des points forts de cette version.

### Évolutions fonctionnelles
- Ajout de champs pour l'armateur (#5245).
- Amélioration de la gestion des champs facultatifs et de leur affichage dans le cadre de l'e-ISR (#5257, #5168).
- Modification des contrôles en mer et à la débarque pour la version 1.3 de l'e-ISR (#5228, #5175).
- Ajout de groupes prioritaires pour les navires, avec affichage d'icônes et possibilité de réordonner la liste (#5215, #5231).
- Ajout d'un engin pour les navires auxiliaires dans la campagne BFT (#5202).
- Ajout du code NATINF 30013 (#5167).
- Amélioration de l'affichage des navires sous AIS v1.2 (#5177).
- Correction de bugs liés à la sauvegarde des infractions en attente et à l'affichage des zones FAO (#5226, #5217).
- Amélioration de l'affichage des messages manuels dans la marée du navire (#5222).
- Correction de l'affichage du champ infraction dans les CR de contrôle (#5225).
- Ajout de la possibilité d'afficher et de gérer les espèces non débarquées.
- Affichage des raisons de vérification avec un tiret dans les notifications préalables.

### Évolutions techniques
- Migration du linter frontend vers OxLint (hybride avec ESLint) pour une meilleure qualité du code (#5233, #5258, #5259).
- Mise à jour des dépendances frontend et backend (#5255, #5233).
- Amélioration des tests Cypress pour une meilleure couverture et fiabilité.
- Optimisation des performances du backend avec l'utilisation de ktlint pour le formatage du code.
- Mise en place de hooks Git pour l'application automatique des règles de linting.
- Utilisation de Zod pour la validation des schémas de données.
- Mise à jour des dépendances Python dans le pipeline CI/CD.
- Amélioration de la récupération des données des navires depuis navpro.

### Autres changements
- Correction de plusieurs erreurs de linting et amélioration de la cohérence du code.
- Documentation mise à jour.
- Corrections de l'UI des modals et des composants Dialogs.
- Suppression de code inutile et nettoyage du code.
- Amélioration de la gestion des erreurs et des messages d'information.
- Correction de bugs mineurs dans l'interface utilisateur.
- Mise à jour des tests unitaires et d'intégration.
