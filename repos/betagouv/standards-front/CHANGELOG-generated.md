## Changelog : standards-front (30 derniers jours, au 28 juillet 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de la lisibilité des données et la simplification de l'interface. L'accent a été mis sur l'optimisation de la vue des incubateurs et la refonte de la page de résumé pour offrir une présentation plus claire et plus dense des informations clés.

### Évolutions fonctionnelles
- **Amélioration de la vue des incubateurs** : présentation des listes sous forme de tableaux, affichage du nombre de services et d'évaluations actifs, et amélioration du formatage des phases de progression. [#185](https://github.com/betagouv/standards-front/pull/185)
- **Optimisation de l'interface utilisateur** : simplification du menu de navigation dans l'en-tête et refonte de la page de résumé pour un affichage plus compact incluant de nouvelles informations de démarrage. [#190](https://github.com/betagouv/standards-front/pull/190)
- **Évolution des composants** : introduction d'une nouvelle liste de résumé et suppression de certaines formulations redondantes dans les évaluations.

### Évolutions techniques
- **Mise à jour des composants UI** : migration vers les versions récentes de `dsfr-view-components` et ajout de la possibilité de personnaliser les descriptions de légende des tableaux.
- **Maintenance et stabilité** : mise à jour de la gem `espace_membre-ruby` pour corriger des tests instables et ajustements de configuration liés à Zeitwerk.
- **Performance et outils** : intégration de `rack-mini-profiler` pour faciliter le profilage des performances et refactorisation de la classe `EspaceMembre::Startup`.
