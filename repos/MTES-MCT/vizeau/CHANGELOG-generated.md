## Changelog : vizeau (30 derniers jours, au 25 mai 2026)

### Résumé
Ce mois-ci, Vizeau a bénéficié d'améliorations significatives en termes de gestion des données, d'expérience utilisateur et de fonctionnalités pour les agents de l'administration. Les principales évolutions concernent l'ajout de nouvelles fonctionnalités pour la gestion des territoires et des projets, l'amélioration de la visualisation des données (notamment des parcelles et des substances), ainsi que des corrections de bugs et des optimisations de l'interface utilisateur.

### Évolutions fonctionnelles
- **Gestion des territoires :** Possibilité de créer de nouveaux territoires depuis la ligne de commande. [#410](https://github.com/MTES-MCT/vizeau/pull/410)
- **Gestion des projets :** Ajout d'un module CRUD (Créer, Lire, Mettre à jour, Supprimer) pour la gestion des projets. [#405](https://github.com/MTES-MCT/vizeau/pull/405)
- **Recherche d'exploitations :** Amélioration du service de recherche d'exploitations. [#404](https://github.com/MTES-MCT/vizeau/pull/404)
- **Affichage des parcelles :** Améliorations de l'affichage des parcelles sur la carte, notamment en augmentant le z-index pour assurer leur visibilité au-dessus des contrôles de la carte. [#401](https://github.com/MTES-MCT/vizeau/pull/401)
- **Suivi des substances :** Amélioration de la visualisation du suivi des substances. [#409](https://github.com/MTES-MCT/vizeau/pull/409)
- **AAC :** Mise à jour de la page AAC et ajout de la fonctionnalité d'export des données AAC en CSV (avec des améliorations de robustesse et de format). [#386](https://github.com/MTES-MCT/vizeau/pull/386)
- **Import de graphiques :** Correction d'un bug lors de l'import d'un graphique. [#400](https://github.com/MTES-MCT/vizeau/pull/400)
- **Attribution de parcelles :** Ajout d'un toaster de confirmation lors de l'attribution des parcelles. [#403](https://github.com/MTES-MCT/vizeau/pull/403)
- **Analyses des installations de captage :** Ajout des analyses des installations de captage. [#393](https://github.com/MTES-MCT/vizeau/pull/393)
- **Tri des substances :** Les substances affichées dans la liste déroulante sont maintenant triées. [#407](https://github.com/MTES-MCT/vizeau/pull/407)

### Évolutions techniques
- **Composant SingleSelectMenu :** Ajout d'un nouveau composant `SingleSelectMenu` pour remplacer le composant `Select` du DSFR, avec gestion de la longueur des labels et ajout de la propriété `caption`. [#409](https://github.com/MTES-MCT/vizeau/pull/409)
- **Refactoring :** Remplacement de `<Select/>` par `<SingleSelectMenu/>` dans plusieurs composants.
- **Amélioration de l'accessibilité :** Corrections pour améliorer l'accessibilité de l'application, notamment la navigation au clavier et les aspects liés au DSFR. [#391](https://github.com/MTES-MCT/vizeau/pull/391)
- **Déboucement de l'autocomplétion :** Correction d'un problème de déboucement de l'autocomplétion. [#390](https://github.com/MTES-MCT/vizeau/pull/390)

### Autres changements
- **Documentation :** Mise à jour du fichier `.gitignore`. [#399](https://github.com/MTES-MCT/vizeau/pull/399)
- **Corrections diverses :** Plusieurs corrections de bugs et améliorations de l'interface utilisateur, notamment liées au DSFR et à Copilot.
- **Priorité des alertes :** Mise à jour de la priorité des alertes.
