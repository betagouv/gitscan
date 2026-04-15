## Changelog : maestro (30 derniers jours, au 15 avril 2026)

### Résumé
Ce mois-ci, les évolutions de Maestro se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau des prélèvements, des plans et des analyses. Des corrections de bugs ont été apportées pour améliorer la fiabilité et la fluidité de l'application. Des refactorings techniques ont également été réalisés pour préparer l'application à de futures évolutions et optimiser les performances.

### Évolutions fonctionnelles
- Possibilité d'éditer les descripteurs des prélèvements [#652](https://github.com/betagouv/maestro/issues/652).
- Amélioration de la gestion des filtres pour les prélèvements, permettant de sélectionner plusieurs valeurs [#705](https://github.com/betagouv/maestro/issues/705).
- Correction de l'affichage des décalages horaires dans les prélèvements [#710](https://github.com/betagouv/maestro/issues/710).
- Notification des coordinateurs régionaux lors de l'ajout d'un nouveau document [#709](https://github.com/betagouv/maestro/issues/709).
- Possibilité de consulter le tableau de bord des plans fermés [#696](https://github.com/betagouv/maestro/issues/696).
- Affichage de l'historique de la programmation [#668](https://github.com/betagouv/maestro/issues/668).
- Amélioration du filtre des prélèvements par plan [#667](https://github.com/betagouv/maestro/issues/667).
- Possibilité de saisir le résultat des résidus complexes dans l'analyse [#739](https://github.com/betagouv/maestro/issues/739).
- Correction permettant de valider une programmation si la région l'a approuvée [#738](https://github.com/betagouv/maestro/issues/738).
- Correction du nom du fichier et de l'extension pour les DAI [#744](https://github.com/betagouv/maestro/issues/744).
- Déblocage des DAI pour les LNR [#714](https://github.com/betagouv/maestro/issues/714).
- Gestion des erreurs pour les RAI [#749](https://github.com/betagouv/maestro/issues/749).

### Évolutions techniques
- Migration vers `biomejs` pour le linting, remplaçant ESLint et Prettier [#672](https://github.com/betagouv/maestro/issues/672).
- Refactoring de la gestion des données spécifiques aux prélèvements, migration vers une table dédiée [#649](https://github.com/betagouv/maestro/issues/649).
- Refactoring des pages pour extraire un composant commun [#666](https://github.com/betagouv/maestro/issues/666).
- Typage des requêtes via les définitions des routes dans `shared` [#693](https://github.com/betagouv/maestro/issues/693).
- Préparation à la migration vers PostgreSQL 17 [#708](https://github.com/betagouv/maestro/issues/708).
- Ajout de schémas pour les échanges hors EDI Sacha [#711](https://github.com/betagouv/maestro/issues/711).
- Amélioration de la performance des tests d'intégration [#724](https://github.com/betagouv/maestro/issues/724).

### Autres changements
- Correction de divers bugs et améliorations de la stabilité.
- Documentation mise à jour.
- Correction de sigles pour la compatibilité avec Sigal [#664](https://github.com/betagouv/maestro/issues/664).
- Ajout de focus sur les champs de recherche [#643](https://github.com/betagouv/maestro/issues/643).
- Correction de l'affichage de l'unité des prélèvements [#651](https://github.com/betagouv/maestro/issues/651).
- Correction du wording des instructions pour les coordinateurs régionaux [#645](https://github.com/betagouv/maestro/issues/645).
- Correction de l'affichage de la date d'envoi des prélèvements [#641](https://github.com/betagouv/maestro/issues/641).
- Correction du filtre des laboratoires pour afficher "Tous" par défaut [#640](https://github.com/betagouv/maestro/issues/640).
- Correction de la récupération de l'utilisateur dans le local storage [#7a9b32d](https://github.com/betagouv/maestro/commit/7a9b32d4989770798f4c6566f665309b84815187).
- Correction de l'injection des échantillons dans le seed [#662](https://github.com/betagouv/maestro/issues/662).
- Correction du filtre par entreprise [#7551fd](https://github.com/betagouv/maestro/commit/f7551fd931458559924d6a913027a863147693d2).
