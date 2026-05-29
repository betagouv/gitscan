## Changelog : catalogi (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'administration du catalogue, la robustesse de l'intégration avec Wikidata, et l'amélioration de la provenance des données. Des optimisations de performance ont également été apportées à l'API, notamment concernant la récupération des logos et l'actualisation des données Wikidata.

### Évolutions fonctionnelles
- Ajout d'une page d'administration accessible via `/admin` permettant de gérer les attributs personnalisés, restreints aux administrateurs. [#52bdc24](https://github.com/codegouvfr/catalogi/pull/52bdc24)
- Amélioration de l'affichage de l'interface d'administration : largeur de page contrainte et troncature des labels d'attributs trop longs. [#b9f8d89](https://github.com/codegouvfr/catalogi/pull/b9f8d89)
- Affichage de la provenance des données (source) dans une table comparative dans la modale DSFR. [#9058319](https://github.com/codegouvfr/catalogi/pull/9058319)
- Unification des modifications utilisateur comme une source de données et affichage de la provenance des données. [#2999e51](https://github.com/codegouvfr/catalogi/pull/2999e51)

### Évolutions techniques
- Optimisation de la récupération des URLs des logos Wikidata et de l'actualisation des données Wikidata pour améliorer les performances de l'API. [#759cedb](https://github.com/codegouvfr/catalogi/pull/759cedb)
- Amélioration de la robustesse de l'intégration avec Wikidata : utilisation de `Special:FilePath` pour les URLs d'images et mise en cache de l'autocomplétion pour éviter les erreurs 429. [#e06c5c5](https://github.com/codegouvfr/catalogi/pull/e06c5c5), [#04a9455](https://github.com/codegouvfr/catalogi/pull/04a9455)
- Correction de la sélection de la dernière version disponible sur Wikidata. [#f7fc708](https://github.com/codegouvfr/catalogi/pull/f7fc708)
- Refactorisation du type `SoftwareData` et suppression des colonnes `content` de la table `softwares`. [#4377664](https://github.com/codegouvfr/catalogi/pull/4377664)
- Suivi du déréférencement de l'auteur et enregistrement de l'heure au format ISO dans l'API. [#d99ffe4](https://github.com/codegouvfr/catalogi/pull/d99ffe4)
- Correction d'un problème de type dans `gitbeaker` lié à des résolutions pnpm en double. [#75c22f7](https://github.com/codegouvfr/catalogi/pull/75c22f7)

### Autres changements
- Mise à jour de la configuration CSP de Vite. [#93dd20b](https://github.com/codegouvfr/catalogi/pull/93dd20b)
- Nettoyage des artefacts de provenance et de revue. [#5c7d400](https://github.com/codegouvfr/catalogi/pull/5c7d400)
- Mise à jour des tests d'actualisation Wikidata. [#efde4eb](https://github.com/codegouvfr/catalogi/pull/efde4eb)
- Correction de bugs mineurs et améliorations de la stabilité. [#baf4f39](https://github.com/codegouvfr/catalogi/pull/baf4f39), [#762e377](https://github.com/codegouvfr/catalogi/pull/762e377)
- Ajustement des assertions dans les tests E2E pour éviter des collisions avec la provenance des sources. [#3297648](https://github.com/codegouvfr/catalogi/pull/3297648)
