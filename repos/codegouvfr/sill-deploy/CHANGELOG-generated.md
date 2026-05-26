## Changelog : sill-deploy (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'administration des attributs personnalisés, la robustesse de l'API (notamment concernant Wikidata) et l'amélioration de l'expérience utilisateur en affichant la provenance des données. Des optimisations de performance ont également été apportées, ainsi que l'ajout de workflows de déploiement SILL et de synchronisation avec le dépôt upstream.

### Évolutions fonctionnelles
- Ajout d'une page d'administration accessible via `/admin` pour gérer les attributs personnalisés, avec restriction de l'accès à un rôle administrateur. [#52bdc24](https://github.com/codegouvfr/sill-deploy/pull/52bdc24)
- Amélioration de l'affichage de la provenance des données dans la modale DSFR, avec une présentation sous forme de tableau comparatif. [#9058319](https://github.com/codegouvfr/sill-deploy/pull/9058319)
- Affichage de la source des modifications utilisateur. [#2999e51](https://github.com/codegouvfr/sill-deploy/pull/2999e51)
- Contrainte de la largeur de la page d'administration et troncature des étiquettes d'attributs trop longues pour une meilleure lisibilité. [#b9f8d89](https://github.com/codegouvfr/sill-deploy/pull/b9f8d89)

### Évolutions techniques
- Ajout de workflows CI/CD pour le déploiement SILL et la synchronisation avec le dépôt upstream. [#f99c7d9](https://github.com/codegouvfr/sill-deploy/pull/f99c7d9), [#98a4217](https://github.com/codegouvfr/sill-deploy/pull/98a4217), [#10ac978](https://github.com/codegouvfr/sill-deploy/pull/10ac978)
- Optimisation de la récupération des logos et des données Wikidata pour améliorer les performances de l'API. [#759cedb](https://github.com/codegouvfr/sill-deploy/pull/759cedb)
- Refactorisation du type `SoftwareData` et suppression des colonnes `content` de la table `softwares` pour simplifier la structure des données. [#4377664](https://github.com/codegouvfr/sill-deploy/pull/4377664)
- Amélioration de la gestion des erreurs et des limites de débit (429) lors de l'accès à l'API Wikidata. [#04a9455](https://github.com/codegouvfr/sill-deploy/pull/04a9455)
- Correction d'un problème de sélection de la dernière version Wikidata. [#f7fc708](https://github.com/codegouvfr/sill-deploy/pull/f7fc708)
- Utilisation de `Special:FilePath` pour les URLs des images Wikidata. [#e06c5c5](https://github.com/codegouvfr/sill-deploy/pull/e06c5c5)
- Suivi de l'auteur de la déréférenciation et stockage de l'heure au format ISO. [#d99ffe4](https://github.com/codegouvfr/sill-deploy/pull/d99ffe4)
- Correction d'un problème de type dans `gitbeaker`. [#75c22f7](https://github.com/codegouvfr/sill-deploy/pull/75c22f7)

### Autres changements
- Mise à jour de la documentation pour utiliser la CSP de Vite dans l'environnement Vite. [#93dd20b](https://github.com/codegouvfr/sill-deploy/pull/93dd20b)
- Nettoyage du code et suppression d'artefacts de provenance et de revue. [#5c7d400](https://github.com/codegouvfr/sill-deploy/pull/5c7d400)
- Mise à jour de l'attente du test de rafraîchissement Wikidata. [#efde4eb](https://github.com/codegouvfr/sill-deploy/pull/efde4eb)
- Correction de la préservation des remplacements d'entrée utilisateur. [#baf4f39](https://github.com/codegouvfr/sill-deploy/pull/baf4f39)
- Encodage des valeurs de secours d'entrée utilisateur avec null. [#762e377](https://github.com/codegouvfr/sill-deploy/pull/762e377)
- Exclusion de `UserInput` de la source principale et remplissage des valeurs héritées complètes. [#f8c5051](https://github.com/codegouvfr/sill-deploy/pull/f8c5051)
- Ajustement des assertions dans les tests E2E pour éviter les collisions de provenance des sources. [#3297648](https://github.com/codegouvfr/sill-deploy/pull/3297648)
