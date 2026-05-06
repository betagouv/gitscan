## Changelog : api-engagement (30 derniers jours, au 5 mai 2026)

### Résumé
Ce mois-ci, les évolutions de l'API Engagement se sont concentrées sur l'amélioration de la performance et de la robustesse de l'API, notamment en optimisant les recherches et en gérant mieux les charges. Des corrections ont également été apportées à l'interface utilisateur du back office pour améliorer l'accessibilité et l'ergonomie. De nouvelles fonctionnalités ont été ajoutées pour supporter les missions de service civique et des scripts pour les missions SDIS.

### Évolutions fonctionnelles
- Ajout de la prise en charge des missions de service civique dans le job Grimpio. [#977](https://github.com/betagouv/api-engagement/issues/977)
- Correction de l'affichage des filtres de modération et du débordement des onglets dans le back office. [#975](https://github.com/betagouv/api-engagement/issues/975)
- Correction de l'alignement horizontal du sélecteur de date dans le back office. [#976](https://github.com/betagouv/api-engagement/issues/976)
- Amélioration de l'accessibilité du sélecteur de date et de la liste des utilisateurs dans le back office. [#928](https://github.com/betagouv/api-engagement/issues/928) et [#922](https://github.com/betagouv/api-engagement/issues/922)
- Correction du problème de déconnexion lors d'erreurs réseau dans le back office. [#930](https://github.com/betagouv/api-engagement/issues/930)
- Ajout de scripts pour les missions SDIS. [#942](https://github.com/betagouv/api-engagement/issues/942)
- Correction d'un problème de redirection lorsque la mission n'est pas trouvée. [#926](https://github.com/betagouv/api-engagement/issues/926)

### Évolutions techniques
- Refactorisation de la recherche d'organisations dans l'API en utilisant `tsvector` pour améliorer la performance. [#950](https://github.com/betagouv/api-engagement/issues/950)
- Refactorisation de la gestion des missions avec exclusion de l'organisation publiant. [#965](https://github.com/betagouv/api-engagement/issues/965)
- Exécution séquentielle de l'agrégation des widgets pour éviter les problèmes de concurrence. [#966](https://github.com/betagouv/api-engagement/issues/966)
- Suppression du store partagé pour la limitation de débit (rate limit). [#959](https://github.com/betagouv/api-engagement/issues/959)
- Suppression de la colonne `mission_id` dans la table `stat_events` pour simplifier la base de données. [#933](https://github.com/betagouv/api-engagement/issues/933) et [#921](https://github.com/betagouv/api-engagement/issues/921)
- Ajout de jobs de sauvegarde de la base de données RDB. [#955](https://github.com/betagouv/api-engagement/issues/955)
- Ajout de limiteurs de débit (rate limit) pour les requêtes API (par publisher et par IP). [#932](https://github.com/betagouv/api-engagement/issues/932)
- Mise à l'échelle de l'API (scaling) pour gérer une charge plus importante. [#949](https://github.com/betagouv/api-engagement/issues/949)
- Amélioration des règles CLAUDE pour la modération. [#957](https://github.com/betagouv/api-engagement/issues/957)

### Autres changements
- Ajout d'une configuration Mockoon pour les tests. [#978](https://github.com/betagouv/api-engagement/issues/978)
- Amélioration du script de vérification des champs orphelins de mission dans `stat_event`.
- Correction de la page d'organisation désactivée dans le back office.
- Mise à jour des dépendances (voir les commits dependabot).
