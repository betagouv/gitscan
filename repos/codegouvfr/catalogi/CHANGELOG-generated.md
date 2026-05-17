## Changelog : catalogi (30 derniers jours, au 2026-05-13)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la fiabilité et la performance de l'intégration avec Wikidata, ainsi que sur l'amélioration de la traçabilité des données. L'interface utilisateur a également été enrichie pour afficher plus clairement la provenance des informations sur les logiciels.

### Évolutions fonctionnelles
- Amélioration de l'affichage de la provenance des données dans l'interface utilisateur, avec une comparaison tabulaire des sources [#2999e51](https://github.com/codegouvfr/catalogi/commit/2999e51).
- Correction de la sélection de la dernière version disponible sur Wikidata [#f7fc708](https://github.com/codegouvfr/catalogi/commit/f7fc708).
- Amélioration de la gestion des valeurs par défaut et des saisies utilisateur [#baf4f39](https://github.com/codegouvfr/catalogi/commit/baf4f39), [#762e377](https://github.com/codegouvfr/catalogi/commit/762e377).

### Évolutions techniques
- Optimisation de la récupération des logos et du rafraîchissement des données Wikidata pour améliorer la performance de l'API [#759cedb](https://github.com/codegouvfr/catalogi/commit/759cedb).
- Utilisation de `Special:FilePath` pour les URL des images Wikidata afin d'améliorer la robustesse [#e06c5c5](https://github.com/codegouvfr/catalogi/commit/e06c5c5).
- Renforcement de la gestion des erreurs 429 (limitation de débit) lors de l'appel à l'API Wikidata [#04a9455](https://github.com/codegouvfr/catalogi/commit/04a9455).
- Unification du type `SoftwareData` et suppression des colonnes de contenu redondantes dans la table `softwares` [#4377664](https://github.com/codegouvfr/catalogi/commit/4377664).
- Suivi du déréférencement de l'auteur et enregistrement de l'heure au format ISO dans l'API [#d99ffe4](https://github.com/codegouvfr/catalogi/commit/d99ffe4).
- Correction d'un problème de type dans `gitbeaker` lié à des résolutions pnpm en double [#75c22f7](https://github.com/codegouvfr/catalogi/commit/75c22f7).

### Autres changements
- Mise à jour des tests d'actualisation de Wikidata [#efde4eb](https://github.com/codegouvfr/catalogi/commit/efde4eb).
- Nettoyage des artefacts de provenance et de revue [#5c7d400](https://github.com/codegouvfr/catalogi/commit/5c7d400).
- Utilisation de la CSP de Vite dans l'environnement Vite [#93dd20b](https://github.com/codegouvfr/catalogi/commit/93dd20b).
- Corrections des tests E2E pour éviter les collisions de provenance des sources [#3297648](https://github.com/codegouvfr/catalogi/commit/3297648).
- Mises à jour de version (build bumps) [#39a4ada](https://github.com/codegouvfr/catalogi/commit/39a4ada), [#61055bb](https://github.com/codegouvfr/catalogi/commit/61055bb), [#94d3cf5](https://github.com/codegouvfr/catalogi/commit/94d3cf5), [#2d13d03](https://github.com/codegouvfr/catalogi/commit/2d13d03).
