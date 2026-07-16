## Changelog : docs (30 derniers jours, au 13 juillet 2026)

### Résumé
Les dernières mises à jour apportent des améliorations significatives à l'interface utilisateur, notamment une refonte de l'en-tête et l'ajout d'un menu utilisateur. Des corrections de bugs ont été implémentées pour améliorer la stabilité et l'expérience utilisateur, en particulier concernant l'arborescence des documents et le comportement du service worker. La documentation a également été enrichie avec des informations sur la configuration de la conversion de format et l'utilisation de S3.

### Évolutions fonctionnelles
- Ajout d'un menu utilisateur pour une meilleure gestion du profil et des paramètres [#2463](https://github.com/suitenumerique/docs/issues/2463).
- Refonte de l'en-tête avec une barre flottante pour une navigation plus intuitive [#2471](https://github.com/suitenumerique/docs/issues/2471).
- Possibilité de réinitialiser un document via une commande de gestion dédiée [#1882](https://github.com/suitenumerique/docs/issues/1882).
- Amélioration de la recherche de documents, notamment avec la prise en compte des documents parents [#1952](https://github.com/suitenumerique/docs/issues/1952).
- Les utilisateurs non authentifiés peuvent désormais effectuer des recherches [#2407](https://github.com/suitenumerique/docs/issues/2407).
- Ajout d'un bouton pour créer des sous-documents [#2423](https://github.com/suitenumerique/docs/issues/2423).
- Ajout de liens "mailto:" dans le menu d'aide pour faciliter le contact [#2416](https://github.com/suitenumerique/docs/issues/2416).

### Évolutions techniques
- Amélioration des performances de l'arborescence des documents [#2498](https://github.com/suitenumerique/docs/issues/2498).
- Correction d'une erreur de pointeur nul dans la configuration Helm pour les jobs backend [#2507](https://github.com/suitenumerique/docs/issues/2507).
- Mise à jour de la gestion de la suppression des utilisateurs pour une meilleure cohérence [#2480](https://github.com/suitenumerique/docs/issues/2480).
- Amélioration de la gestion des connexions de collaboration pour une meilleure cascade de suppression [#2501](https://github.com/suitenumerique/docs/issues/2501).
- Capture des erreurs de gestion des convertisseurs Yjs dans Sentry [#2516](https://github.com/suitenumerique/docs/issues/2516).
- Configuration de la journalisation avec la propagation activée [#2501](https://github.com/suitenumerique/docs/issues/2501).
- Utilisation de l'ID du document au lieu du chemin pour la recherche [#2501](https://github.com/suitenumerique/docs/issues/2501).

### Autres changements
- Mise à jour de la documentation pour expliquer la configuration du format de conversion et l'utilisation de S3 [#2481](https://github.com/suitenumerique/docs/issues/2481).
- Mise à jour des modèles de tickets (issue templates) [#2207](https://github.com/suitenumerique/docs/issues/2207).
- Ajout d'un badge DPG au README [#2459](https://github.com/suitenumerique/docs/issues/2459).
- Correction de fautes de frappe dans le guide de contribution [#2459](https://github.com/suitenumerique/docs/issues/2459).
- Mise à jour des chaînes de traduction [#2416](https://github.com/suitenumerique/docs/issues/2416).
- Ajout d'un badge Snyk au README [#2459](https://github.com/suitenumerique/docs/issues/2459).
- Correction de problèmes d'accessibilité (aria-label, focus, etc.) pour les utilisateurs de lecteurs d'écran [#2450](https://github.com/suitenumerique/docs/issues/2450), [#2449](https://github.com/suitenumerique/docs/issues/2449), [#2421](https://github.com/suitenumerique/docs/issues/2421), [#2384](https://github.com/suitenumerique/docs/issues/2384), [#2459](https://github.com/suitenumerique/docs/issues/2459).
