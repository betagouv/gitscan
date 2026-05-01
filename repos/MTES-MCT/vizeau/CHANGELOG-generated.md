## Changelog : vizeau (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, Vizeau a bénéficié d'améliorations significatives en termes de fonctionnalités et d'expérience utilisateur, notamment dans la gestion des exploitations agricoles, la visualisation des données sur la carte et la gestion des contacts. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- **Exploitations agricoles :**
    - Ajout de la fonctionnalité d'export des parcelles d'une exploitation [#380](https://github.com/MTES-MCT/vizeau/pull/380).
    - Implémentation de l'export du journal de bord d'une exploitation [#371](https://github.com/MTES-MCT/vizeau/pull/371).
    - Possibilité d'exporter les données d'une exploitation [#372](https://github.com/MTES-MCT/vizeau/pull/372).
- **Visualisation des données :**
    - Ajout de nouvelles couches sur la carte de visualisation [#366](https://github.com/MTES-MCT/vizeau/pull/366).
    - Filtrage des AACs (Autorisations d'aménagement de captage) directement sur la carte [#368](https://github.com/MTES-MCT/vizeau/pull/368).
    - Traduction des codes NAF (Nomenclature d'Activités Française) en libellés pour une meilleure compréhension [#370](https://github.com/MTES-MCT/vizeau/pull/370).
- **Gestion des contacts :**
    - Amélioration de la gestion des contacts secondaires dans les formulaires [#363](https://github.com/MTES-MCT/vizeau/pull/363).
    - Ajout d'une indication de RPG (Responsable de Point de Prélèvement) [#357](https://github.com/MTES-MCT/vizeau/pull/357).
- **Territoires :**
    - Attribution de territoires aux comptes animateurs [#375](https://github.com/MTES-MCT/vizeau/pull/375).
    - Affectation de territoire aux CMD (Collectivités et Métropoles) [#359](https://github.com/MTES-MCT/vizeau/pull/359).
- **Page AAC :** Mise à jour de la page AAC [#383](https://github.com/MTES-MCT/vizeau/pull/383).
- **Composants UI :** Ajout des composants CheckboxCard et SearchWithFilters.

### Évolutions techniques
- Correction de la transparence des résultats dans le composant autocomplete [#378](https://github.com/MTES-MCT/vizeau/pull/378).
- Correction d'un crash lié à l'affichage du journal de bord [#372](https://github.com/MTES-MCT/vizeau/pull/372).
- Amélioration de la gestion des dépendances dans les `useEffect` pour le formulaire de contact.
- Correction de la navigation au clavier et amélioration de l'accessibilité.
- Déboucement de l'input autocomplete pour améliorer la performance.

### Autres changements
- Corrections diverses suite aux revues Copilot.
- Mise à jour de certaines dépendances npm et yarn.
- Ajout de composants pour le module Point de prélèvement [#381](https://github.com/MTES-MCT/vizeau/pull/381).
- Correction de bugs mineurs et améliorations de la qualité du code.
