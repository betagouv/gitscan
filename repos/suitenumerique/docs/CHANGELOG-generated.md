## Changelog : docs (30 derniers jours, au 28 juillet 2026)

### Résumé
Les dernières mises à jour apportent des améliorations significatives à l'éditeur de présentation, avec la possibilité d'ouvrir et de partager une présentation à une diapositive spécifique. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été implémentées, notamment pour la gestion des documents, la barre latérale et le mode présentation. La documentation a été enrichie avec des informations sur la configuration de la conversion de format et l'utilisation de S3.

### Évolutions fonctionnelles
- Possibilité d'ouvrir et de partager une présentation à une diapositive spécifique. [#2508](https://github.com/suitenumerique/docs/issues/2508)
- Amélioration de l'interface utilisateur de la barre latérale. [#2516](https://github.com/suitenumerique/docs/issues/2516)
- Ajout d'une animation Lottie à la barre flottante dans l'en-tête.
- Restauration du lien "Passer au contenu" après la refonte de l'en-tête. [#2510](https://github.com/suitenumerique/docs/issues/2510)
- Ajout de la gestion des locales `zh_CN`, `eo_PL` et `zh_TW`. [#2486](https://github.com/suitenumerique/docs/issues/2486)
- Correction d'un problème de redirection vers la page de connexion lorsque la fonctionnalité de page d'accueil est désactivée. [#2521](https://github.com/suitenumerique/docs/issues/2521)

### Évolutions techniques
- Adaptation de la commande de build `y-provider` suite à une mise à jour de `tsc-alias`.
- Mise à jour de la configuration de l'IA pour exclure les fichiers du suivi Git.
- Amélioration de l'architecture du mode présentateur pour une meilleure réutilisation des composants.
- Refonte de l'en-tête avec une barre flottante plus générique et réutilisable.
- Correction d'un problème de focus sur les diapositives du présentateur.
- Utilisation d'éléments `<p>` sémantiques dans la carte d'informations du document pour l'accessibilité. [#2379](https://github.com/suitenumerique/docs/issues/2379)
- Modification de la recherche de documents pour utiliser l'ID au lieu du chemin. [#2501](https://github.com/suitenumerique/docs/issues/2501)

### Autres changements
- Mise à jour de la documentation pour expliquer la configuration du format de conversion et l'utilisation de S3.
- Mise à jour des modèles de formulaires pour les issues. [#2207](https://github.com/suitenumerique/docs/issues/2207)
- Correction de bugs et améliorations de l'expérience utilisateur mineures.
- Mise à jour des chaînes de traduction.
- Publication des versions 5.4.0 et 5.4.1.
