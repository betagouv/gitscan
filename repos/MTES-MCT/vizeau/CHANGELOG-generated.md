## Changelog : vizeau (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, Vizeau a bénéficié d'améliorations significatives en termes de gestion de projet, d'export de données, d'expérience utilisateur sur la carte et dans les recherches, ainsi que de corrections de bugs et d'optimisations techniques. Les utilisateurs peuvent désormais exporter des données AAC et d'exploitation, et bénéficier d'une interface cartographique plus fluide et informative.

### Évolutions fonctionnelles
- **Gestion de projet :** Ajout d'un module de gestion de projet avec des fonctionnalités CRUD complètes. [#405](https://github.com/MTES-MCT/vizeau/pull/405)
- **Export de données :** Implémentation de l'export des données AAC au format CSV, avec des améliorations de robustesse et de formatage des données. [#386](https://github.com/MTES-MCT/vizeau/pull/386)
- **Export d'exploitation :** Ajout de la fonctionnalité d'export des parcelles d'une exploitation. [#372](https://github.com/MTES-MCT/vizeau/pull/372)
- **Carte :** Amélioration de l'affichage des parcelles sur la carte, avec une augmentation de la priorité d'affichage pour éviter les chevauchements. [#401](https://github.com/MTES-MCT/vizeau/pull/401)
- **Recherche d'exploitations :** Mise à jour du service de recherche d'exploitations. [#404](https://github.com/MTES-MCT/vizeau/pull/404)
- **Attribution de parcelles :** Ajout d'un toaster de confirmation lors de l'attribution des parcelles. [#403](https://github.com/MTES-MCT/vizeau/pull/403)
- **Analyses des installations de captage :** Ajout des analyses des installations de captage. [#393](https://github.com/MTES-MCT/vizeau/pull/393)
- **Page AAC :** Mise à jour de la page AAC. [#383](https://github.com/MTES-MCT/vizeau/pull/383)
- **Seeding des comptes :** Evolution du seeding des comptes animateurs avec attribution de territoire. [#371](https://github.com/MTES-MCT/vizeau/pull/371)

### Évolutions techniques
- **Composants Point de prélèvement :** Création de nouveaux composants pour le module Point de prélèvement. [#381](https://github.com/MTES-MCT/vizeau/pull/381)
- **Autocomplete :** Correction des champs autocomplete et amélioration de la transparence des résultats. [#378](https://github.com/MTES-MCT/vizeau/pull/378)
- **Déboucement Autocomplete :** Correction du déboucement de l'input autocomplete. [#390](https://github.com/MTES-MCT/vizeau/pull/390)
- **Composants UI :** Ajout des composants CheckboxCard et SearchWithFilters. [#391](https://github.com/MTES-MCT/vizeau/pull/391), [#392](https://github.com/MTES-MCT/vizeau/pull/392)
- **Accessibilité :** Amélioration de l'accessibilité de la navigation au clavier.
- **Corrections de bugs :** Correction d'un bug sur l'info-bulle du DSFR. [#395](https://github.com/MTES-MCT/vizeau/pull/395)
- **Correction de crash :** Correction d'un crash lors de l'export.

### Autres changements
- **Documentation :** Mise à jour du fichier .gitignore. [#399](https://github.com/MTES-MCT/vizeau/pull/399)
- **Nettoyage de code :** Plusieurs corrections et optimisations de code (copilot fixes).
- **Mises à jour de dépendances :** Mises à jour mineures de certaines dépendances.
