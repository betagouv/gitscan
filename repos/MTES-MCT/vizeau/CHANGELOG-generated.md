## Changelog : vizeau (30 derniers jours, au 7 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à l'export de données, notamment pour les données AAC et les exploitations agricoles. Des corrections ont été apportées à l'affichage des parcelles sur la carte, à l'import de graphiques et à l'accessibilité de certains composants. De nouvelles fonctionnalités sont disponibles pour l'analyse des installations de captage et le seeding des territoires aux utilisateurs.

### Évolutions fonctionnelles
- **Export de données AAC :** Implémentation de l'export des données AAC, avec des améliorations de robustesse et de formatage des données exportées ([#386](https://github.com/MTES-MCT/vizeau/pull/386)).
- **Export des exploitations :** Ajout de la fonctionnalité d'export des parcelles d'une exploitation ([#380](https://github.com/MTES-MCT/vizeau/pull/380), [#372](https://github.com/MTES-MCT/vizeau/pull/372)).
- **Analyses des installations de captage :** Ajout des analyses pour les installations de captage ([#393](https://github.com/MTES-MCT/vizeau/pull/393)).
- **Amélioration de l'affichage des parcelles :** Améliorations sur l'affichage des parcelles sur la carte ([#401](https://github.com/MTES-MCT/vizeau/issues/401)).
- **Seeding des territoires aux utilisateurs :** Evolution du seeding des comptes animateurs avec attribution de territoire ([#375](https://github.com/MTES-MCT/vizeau/pull/375)).
- **Correction de l'import de graphique :** Correction d'un bug lors de l'import d'un graphique ([#400](https://github.com/MTES-MCT/vizeau/issues/400)).
- **Augmentation du z-index de la carte :** Augmentation du z-index pour assurer que la carte s'affiche au-dessus des contrôles ([#402](https://github.com/MTES-MCT/vizeau/issues/402)).

### Évolutions techniques
- **Composants Point de prélèvement :** Création de nouveaux composants pour le module Point de prélèvement ([#381](https://github.com/MTES-MCT/vizeau/pull/381)).
- **Refactoring Autocomplete :** Correction de la transparence des résultats et des champs autocomplete ([#378](https://github.com/MTES-MCT/vizeau/pull/378), [#387](https://github.com/MTES-MCT/vizeau/pull/387)).
- **Amélioration de l'accessibilité :** Corrections d'accessibilité sur certains composants, notamment la navigation au clavier et l'utilisation de labels ([#390](https://github.com/MTES-MCT/vizeau/pull/390), [#391](https://github.com/MTES-MCT/vizeau/pull/391), [#392](https://github.com/MTES-MCT/vizeau/pull/392)).
- **Nouveaux composants UI :** Ajout des composants `CheckboxCard` et `SearchWithFilters` ([#391](https://github.com/MTES-MCT/vizeau/pull/391), [#392](https://github.com/MTES-MCT/vizeau/pull/392)).
- **Mise à jour du .gitignore :** Mise à jour du fichier `.gitignore` ([#399](https://github.com/MTES-MCT/vizeau/issues/399)).

### Autres changements
- **Correction d'un bug sur l'info-bulle du DSFR :** Correction d'un bug d'affichage sur l'info-bulle du Design System Français (DSFR) ([#395](https://github.com/MTES-MCT/vizeau/issues/395)).
- **Mise à jour de la page AAC :** Mise à jour de la page AAC ([#383](https://github.com/MTES-MCT/vizeau/pull/383)).
- **Corrections diverses :** Plusieurs corrections mineures et améliorations du code.
- **Mise à jour des dépendances :** Mises à jour de certaines dépendances (AdonisJS, npm/yarn).
