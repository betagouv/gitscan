## Changelog : standards-front (30 derniers jours, au 28 juillet 2026)

### Résumé
Les dernières évolutions se concentrent sur l'amélioration de la visibilité des données des incubateurs et la simplification de la navigation pour faciliter la consultation des indicateurs clés et des résumés de services.

### Évolutions fonctionnelles
- **Amélioration de la vue des incubateurs** : passage à un affichage sous forme de tableau, meilleur formatage des phases et ajout de compteurs pour les services et évaluations actifs [#185](https://github.com/betagouv/standards-front/pull/185).
- **Optimisation de la page de résumé** : introduction d'une liste de résumé et ajout d'informations de démarrage supplémentaires [#190](https://github.com/betagouv/standards-front/pull/190).
- **Navigation** : simplification du menu de l'en-tête pour une utilisation plus fluide.

### Évolutions techniques
- **Composants UI** : ajout de la possibilité de personnaliser la description des légendes de tableau.
- **Dépendances et performance** : mise à jour vers les versions récentes de `dsfr-view-components` et intégration de `rack-mini-profiler` pour le suivi des performances.
- **Maintenance et stabilité** : résolution de problèmes de tests instables via la mise à jour de `espace_membre-ruby` et ajustement de la configuration Zeitwerk ; refactorisation de la classe `EspaceMembre::Startup`.
