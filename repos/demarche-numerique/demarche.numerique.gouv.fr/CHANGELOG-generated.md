## Changelog : demarche.numerique.gouv.fr (30 derniers jours)

### Résumé
Cette période a été marquée par des améliorations significatives de l'accessibilité, de la performance et de la stabilité de la plateforme. Des corrections de bugs ont été apportées, notamment concernant l'affichage des PDF, la gestion des erreurs et les champs de formulaire. Des optimisations ont été réalisées pour l'analyse d'images et le traitement des jobs asynchrones. De nouvelles fonctionnalités ont été implémentées, comme la gestion des groupes d'instructeurs et l'intégration de l'API Part pour le quotient familial.

### Évolutions fonctionnelles
- Possibilité de créer un nouveau groupe d'instructeurs depuis une modale [#12724](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/12724).
- Amélioration de l'affectation d'instructeurs à des groupes, avec des actions pour ajouter ou retirer des instructeurs à plusieurs groupes simultanément [#12625](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/12625).
- Intégration de l'API Part pour le quotient familial, incluant l'affichage des données, la gestion des erreurs et la transmission sécurisée des informations [#12524](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/12524).
- Ajout d'un bouton pour réactiver les utilisateurs bloqués dans l'interface de gestion [#12703](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/12703).
- Amélioration de l'affichage des PDF dans la galerie, avec l'utilisation de variantes pour les aperçus [#12678](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/12678).
- Amélioration de l'interface pour l'ajout de fichiers, notamment en affichant un bouton "Déposer" même lorsque le dossier est en construction [#12655](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/12655).
- Amélioration de l'affichage des filtres pour les instructeurs, avec troncature des labels trop longs [#12608](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/12608).

### Évolutions techniques
- Remplacement de MiniMagick par ruby-vips pour le traitement des images, améliorant ainsi les performances et la sécurité [#12662](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/12662).
- Optimisation des jobs de traitement d'images pour éviter les analyses antivirus inutiles [#12671](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/12671).
- Amélioration de la gestion des erreurs et des retries pour les jobs asynchrones, avec l'utilisation de `ActiveJob::RetryOnStandardError` [#12642](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/12642).
- Refactoring du code pour améliorer la lisibilité et la maintenabilité, notamment dans les concerns et les composants React [#12739](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/12739).
- Mise à jour des dépendances, notamment Rack et Nokogiri.
- Ajout d'un linter pour vérifier le format des apostrophes dans les fichiers YAML [#12656](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/12656).
- Amélioration de la gestion des clés de chiffrement GPG [#12752](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/12752).

### Autres changements
- Amélioration de l'accessibilité de divers éléments de l'interface, tels que les boutons de copie, les champs de formulaire et les notifications [#12710](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/12710), [#12634](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/12634).
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout de tests pour améliorer la couverture et la fiabilité du code.
- Mise à jour de la documentation.
- Suppression de code obsolète et de fonctionnalités non utilisées.
- Amélioration de la gestion des logs et du monitoring.
- Intégration de Crisp pour le support client.
- Amélioration de la sécurité en restreignant les autorisations de Crisp.
- Ajout d'un cache warming action pour améliorer les performances [#12705](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/12705).
