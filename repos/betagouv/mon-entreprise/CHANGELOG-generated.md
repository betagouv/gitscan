## Changelog : mon-entreprise (30 derniers jours, au 12 mars 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration du comparateur de statuts, notamment en matière de droits à la retraite. Des corrections ont été apportées pour une meilleure précision des calculs et une présentation plus claire des informations. Des refactorings techniques ont également été réalisés pour préparer l'avenir du projet, notamment en vue d'une migration vers Next.js.

### Évolutions fonctionnelles
- **Comparateur de statuts :** Ajout de la comparaison du revenu cotisé et des droits à la retraite (trimestres et points) dans le comparateur. [#4361](https://github.com/betagouv/mon-entreprise/issues/4361)
- **Comparateur de statuts :** Ajout de liens vers les simulateurs de l'Assurance retraite et de la Cnav pour faciliter l'estimation des droits.
- **Comparateur de statuts :** Correction de l'unité d'affichage du revenu cotisé retraite de base.
- **Comparateur de statuts :** Amélioration de l'affichage de la valeur du point dans la section retraite complémentaire (espace insécable, format "€ par an").
- **Salarié :** Ajout d'un message informant les utilisateurs des mises à jour pour 2026.
- **Droits Retraite :** Suppression de l'ACRE comme condition bloquant l'affichage des droits retraite.
- **Statistiques :** Correction du débordement de la pagination sur mobile et correction de la pagination qui revenait à la page 1.

### Évolutions techniques
- **Refactoring Navigation :** Préparation de la migration vers Next.js avec la création d'un adaptateur de navigation et la centralisation des hooks React Router.
- **Refactoring :** Suppression de code mort et simplification de certaines logiques pour améliorer la maintenabilité.
- **Design System :** Migration des composants Link et NavLink vers l'adaptateur de navigation.
- **Typage :** Amélioration du typage de certains composants.
- **Logic Fabric :** Ajout de nouveaux composants minimalist (ToggleGroup, YesOrNoToggleGroup, RadioGroup) et amélioration du typage.

### Autres changements
- **Documentation :** Précision dans la documentation concernant la dépendance des droits à la retraite au montant cotisé.
- **Mise à jour :** Mise à jour de l'Acre et de la CSG non déductible sur dividendes.
- **Normalisation :** Normalisation des caractères dans le fichier de traduction ui-fr.yaml.
- **Correction :** Correction de typos (Embeded -> Embedded).
- **Correction :** Suppression du lien vers le simulateur Cnav du comparateur.
- **Correction :** Suppression de la projection de montant de retraite des simulateurs indépendants.
- **Correction :** Suppression des objectifs de projection retraite base et complémentaire de la config PL.
- **Correction :** Correction de l'affichage mobile du montant des cotisations [#4290](https://github.com/betagouv/mon-entreprise/issues/4290)
