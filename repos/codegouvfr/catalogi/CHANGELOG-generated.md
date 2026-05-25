## Changelog : catalogi (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'administration des attributs personnalisés, la gestion des sources de données et la robustesse de l'API, notamment en ce qui concerne l'intégration avec Wikidata. Des optimisations de performance ont également été apportées pour améliorer la réactivité de l'application.

### Évolutions fonctionnelles
- Ajout d'une page d'administration (`/admin`) pour gérer les attributs personnalisés, avec restriction de l'accès aux administrateurs. [#4377664](https://github.com/codegouvfr/catalogi/pull/4377664)
- Amélioration de l'affichage des attributs dans l'interface d'administration : troncature des étiquettes longues et limitation de la largeur de la page. [#b9f8d89](https://github.com/codegouvfr/catalogi/commit/b9f8d89)
- Affichage de la provenance des données (source) dans la modale DSFR sous forme de tableau comparatif. [#9058319](https://github.com/codegouvfr/catalogi/commit/9058319)
- Les modifications des utilisateurs sont maintenant unifiées en tant que source de données, permettant de mieux suivre la provenance des informations. [#2999e51](https://github.com/codegouvfr/catalogi/commit/2999e51)

### Évolutions techniques
- Optimisation de la récupération et du rafraîchissement des données Wikidata, incluant l'optimisation des URLs des logos. [#759cedb](https://github.com/codegouvfr/catalogi/commit/759cedb)
- Amélioration de la robustesse de l'API Wikidata pour éviter les erreurs 429 (limitation de débit) grâce à la mise en cache de l'autocomplétion. [#04a9455](https://github.com/codegouvfr/catalogi/commit/04a9455)
- Refactorisation du type `SoftwareData` dans l'API pour simplifier la structure des données et supprimer les colonnes de contenu obsolètes de la table `softwares`. [#4377664](https://github.com/codegouvfr/catalogi/pull/4377664)
- Suivi du déréférencement de l'auteur et enregistrement de l'heure au format ISO dans l'API. [#d99ffe4](https://github.com/codegouvfr/catalogi/commit/d99ffe4)
- Utilisation de `Special:FilePath` pour les URLs des images Wikidata afin d'améliorer la fiabilité. [#e06c5c5](https://github.com/codegouvfr/catalogi/commit/e06c5c5)
- Correction d'un problème de type dans `gitbeaker` lié à des résolutions pnpm en double. [#75c22f7](https://github.com/codegouvfr/catalogi/commit/75c22f7)

### Autres changements
- Mise à jour de la configuration CSP de Vite pour inclure l'environnement Vite. [#93dd20b](https://github.com/codegouvfr/catalogi/commit/93dd20b)
- Nettoyage des artefacts de provenance et de revue. [#5c7d400](https://github.com/codegouvfr/catalogi/commit/5c7d400)
- Correction d'une attente incorrecte dans le test de rafraîchissement de Wikidata. [#efde4eb](https://github.com/codegouvfr/catalogi/commit/efde4eb)
- Correction de la sélection de la dernière version dans Wikidata. [#f7fc708](https://github.com/codegouvfr/catalogi/commit/f7fc708)
- Correction de la préservation des remplacements par l'utilisateur. [#baf4f39](https://github.com/codegouvfr/catalogi/commit/baf4f39)
- Correction de l'encodage des valeurs de remplacement par l'utilisateur avec `null`. [#762e377](https://github.com/codegouvfr/catalogi/commit/762e377)
- Ajustement des assertions dans les tests E2E pour éviter les collisions de provenance des sources. [#3297648](https://github.com/codegouvfr/catalogi/commit/3297648)
