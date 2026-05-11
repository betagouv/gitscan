## Changelog : sill-deploy (30 derniers jours, au 7 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des sources de données et de leur provenance, notamment pour les données Wikidata. Des optimisations de performance ont été réalisées sur l'API, et des workflows de déploiement pour le SILL ont été ajoutés. L'interface utilisateur a également été améliorée avec l'ajout d'informations sur la provenance des données.

### Évolutions fonctionnelles
- Amélioration de l'affichage de la provenance des sources de données dans une table de comparaison dans l'interface web.
- Ajout d'options pour les systèmes d'exploitation mobiles manquants dans l'interface web.
- Possibilité de configurer le comportement de la passerelle via des fichiers de configuration. [#500](https://github.com/codegouvfr/sill-deploy/issues/500)
- Affichage de l'auteur de la déréférenciation et enregistrement de l'heure au format ISO dans l'API.

### Évolutions techniques
- Optimisation de la récupération des données Wikidata et des URLs des logos pour améliorer les performances de l'API.
- Refactorisation du type `SoftwareData` dans l'API et suppression des colonnes `content` de la table `softwares`.
- Unification des modifications utilisateur en tant que source et affichage de la provenance des données.
- Mise en place de workflows CI/CD pour le déploiement sur le SILL et la synchronisation avec le dépôt upstream.
- Amélioration de la robustesse de la passerelle Wikidata et mise en cache des autocomplétions pour éviter les erreurs 429.
- Utilisation de `Special:FilePath` pour les URLs des images Wikidata dans l'API.
- Correction d'un problème de type dans `gitbeaker` lié à des résolutions pnpm dupliquées.
- Utilisation de Vite CSP dans l'environnement Vite.
- Propagation de la nouvelle gestion de configuration via l'utilisation de fichiers.
- Refactorisation de la gestion des fonctionnalités de la passerelle.
- Réorganisation des migrations.

### Autres changements
- Nettoyage des artefacts de provenance et de revue.
- Amélioration de la configuration locale du CSP pour afficher les images.
- Correction de la préservation des remplacements d'entrée utilisateur.
- Encodage des valeurs de repli d'entrée utilisateur avec `null`.
- Correction d'un problème d'assertions dans les tests E2E pour éviter les collisions de provenance des sources.
- Plusieurs mises à jour de version (build bumps).
