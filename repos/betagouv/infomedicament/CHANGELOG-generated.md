## Changelog : infomedicament (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, les améliorations se sont concentrées sur l'optimisation des performances du site, notamment en réduisant le temps de chargement des pages et en améliorant la réactivité. Des corrections de sécurité ont également été apportées, ainsi que des améliorations de l'interface utilisateur, notamment sur la page médicament avec l'ajout de surlignages dans le glossaire.

### Évolutions fonctionnelles
- Ajout de surlignages dans le glossaire sur la page médicament pour une meilleure compréhension des termes techniques. [#85313b1](https://github.com/betagouv/infomedicament/commit/85313b1)
- Affichage du nombre de médicaments commercialisés de manière dynamique. [#719c15d](https://github.com/betagouv/infomedicament/commit/719c15d)
- Ajout d'une indication de la fraîcheur des données dans le modal d'accueil. [#e49f32b](https://github.com/betagouv/infomedicament/commit/e49f32b)
- Correction de l'affichage des spécialités en tenant compte du flag `isBdm`. [#0a55d7e](https://github.com/betagouv/infomedicament/commit/0a55d7e)
- Amélioration de l'interface `ResumeMedicamentsTable` avec l'ajout d'une migration. [#b86edcd](https://github.com/betagouv/infomedicament/commit/b86edcd) et [#661780c](https://github.com/betagouv/infomedicament/commit/661780c)

### Évolutions techniques
- Optimisation des performances de la page médicament : chargement paresseux des composants détaillés, utilisation de `server-side` rendering pour `MedicamentGeneriqueContainer`. [#83506ea](https://github.com/betagouv/infomedicament/commit/83506ea), [#e5429ce](https://github.com/betagouv/infomedicament/commit/e5429ce)
- Amélioration du Largest Contentful Paint (LCP) en rendant les enfants de `ContentContainer` de manière synchrone. [#ca150ed](https://github.com/betagouv/infomedicament/commit/ca150ed)
- Optimisation de l'image SVG de la page d'accueil avec `svgo`. [#d702126](https://github.com/betagouv/infomedicament/commit/d702126)
- Suppression de la dépendance MUI et remplacement du composant `Autocomplete` par un combobox personnalisé. [#33ea8e3](https://github.com/betagouv/infomedicament/commit/33ea8e3), [#48a268b](https://github.com/betagouv/infomedicament/commit/48a268b), [#2963b3c](https://github.com/betagouv/infomedicament/commit/2963b3c)
- Déplacement de la fonction `sanitize-html` vers la couche de données côté serveur. [#4f11f1f](https://github.com/betagouv/infomedicament/commit/4f11f1f)
- Préchargement de la police `Marianne-Regular_Italic` pour éviter les retards d'affichage. [#39ace6c](https://github.com/betagouv/infomedicament/commit/39ace6c)
- Mise à jour de Next.js vers la version 16.1.6. [#26f337a](https://github.com/betagouv/infomedicament/commit/26f337a)
- Refonte du système de linting avec l'adoption d'ESLint. [#47b04bb](https://github.com/betagouv/infomedicament/commit/47b04bb)
- Amélioration de la gestion des requêtes et limitation du nombre de requêtes par IP pour l'endpoint `/rating`. [#2e49b78](https://github.com/betagouv/infomedicament/commit/2e49b78) et [#649c167](https://github.com/betagouv/infomedicament/commit/649c167)
- Correction d'une vulnérabilité potentielle d'IDOR sur la soumission de notes avancées. [#34219c6](https://github.com/betagouv/infomedicament/commit/34219c6)

### Autres changements
- Ajout de la vérification de la console de recherche Google via un fichier HTML. [#554e6ab](https://github.com/betagouv/infomedicament/commit/554e6ab)
- Configuration du seed-search-index pour les environnements de revue d'applications. [#ed5155c](https://github.com/betagouv/infomedicament/commit/ed5155c)
- Ajout de codes CIS généralement revus pour les revues d'applications. [#2eb7927](https://github.com/betagouv/infomedicament/commit/2eb7927)
- Correction de la configuration du proxy pour augmenter le nombre de requêtes par minute. [#6d9adef](https://github.com/betagouv/infomedicament/commit/6d9adef)
- Ajout d'une interface OpenSearch dans l'environnement de développement. [#0d8dde1](https://github.com/betagouv/infomedicament/commit/0d8dde1)
- Correction de l'accès à `onScrollEvent` avant sa déclaration. [#b7a8648](https://github.com/betagouv/infomedicament/commit/b7a8648)
- Suppression de `RatingToaster` de la page d'accueil. [#7b40805](https://github.com/betagouv/infomedicament/commit/7b40805)
- Correction d'un problème de préchargement. [#79420fb](https://github.com/betagouv/infomedicament/commit/79420fb)
- Suppression de la prélecture dans les liens du header et du footer. [#5de26ed](https://github.com/betagouv/infomedicament/commit/5de26ed)
- Correction de l'ajout de `pathosCodesNames` vide dans l'insertion de `resume_specialites`. [#afc4946](https://github.com/betagouv/infomedicament/commit/afc4946)
- Correction de compositions. [#d134941](https://github.com/betagouv/infomedicament/commit/d134941)
