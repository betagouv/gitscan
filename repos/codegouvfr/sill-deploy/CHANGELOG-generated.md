## Changelog : sill-deploy (30 derniers jours, au 14 mai 2026)

### Résumé
Ce changelog couvre les améliorations apportées à sill-deploy au cours du dernier mois. Les changements se concentrent sur l'amélioration de la provenance des données, l'optimisation des performances de l'API, la gestion de la configuration et l'ajout de workflows de déploiement pour le SILL. Des corrections de bugs ont également été implémentées pour améliorer la stabilité et la fiabilité de l'application.

### Évolutions fonctionnelles
- Amélioration de l'affichage de la provenance des données dans l'interface utilisateur, avec une comparaison tabulaire des sources [#2999e51](https://github.com/codegouvfr/sill-deploy/issues/2999e51).
- Ajout d'options pour les systèmes d'exploitation mobiles dans l'interface web [#caffbcf](https://github.com/codegouvfr/sill-deploy/commit/caffbcf).
- Possibilité de configurer l'application via des fichiers [#c081289](https://github.com/codegouvfr/sill-deploy/commit/c081289).

### Évolutions techniques
- Ajout de workflows CI/CD pour le déploiement sur le SILL et synchronisation avec le dépôt upstream [#98a4217](https://github.com/codegouvfr/sill-deploy/commit/98a4217), [#10ac978](https://github.com/codegouvfr/sill-deploy/commit/10ac978), [#583fa27](https://github.com/codegouvfr/sill-deploy/commit/583fa27), [#c986f23](https://github.com/codegouvfr/sill-deploy/commit/c986f23).
- Optimisation de la récupération et de l'affichage des logos Wikidata [#759cedb](https://github.com/codegouvfr/sill-deploy/commit/759cedb), [#e06c5c5](https://github.com/codegouvfr/sill-deploy/commit/e06c5c5).
- Refactoring du type `SoftwareData` et suppression des colonnes de contenu de la table `softwares` [#4377664](https://github.com/codegouvfr/sill-deploy/commit/4377664).
- Amélioration de la gestion des erreurs 429 lors de l'accès à l'API Wikidata [#04a9455](https://github.com/codegouvfr/sill-deploy/commit/04a9455).
- Unification des modifications utilisateur en tant que source de données et affichage de la provenance des données [#2999e51](https://github.com/codegouvfr/sill-deploy/commit/2999e51).
- Mise à jour de la gestion des fonctionnalités du gateway [#9af0faa](https://github.com/codegouvfr/sill-deploy/commit/9af0faa).
- Correction d'un problème de type dans `gitbeaker` [#75c22f7](https://github.com/codegouvfr/sill-deploy/commit/75c22f7).
- Amélioration du suivi de la déréférenciation des auteurs et stockage de l'heure au format ISO [#d99ffe4](https://github.com/codegouvfr/sill-deploy/commit/d99ffe4).
- Correction de la sélection de la dernière version de Wikidata [#f7fc708](https://github.com/codegouvfr/sill-deploy/commit/f7fc708).
- Correction de la préservation des remplacements de saisie utilisateur [#baf4f39](https://github.com/codegouvfr/sill-deploy/commit/baf4f39).
- Correction de l'encodage des valeurs de remplacement de saisie utilisateur avec null [#762e377](https://github.com/codegouvfr/sill-deploy/commit/762e377).

### Autres changements
- Mise à jour de l'attente du test de rafraîchissement Wikidata [#efde4eb](https://github.com/codegouvfr/sill-deploy/commit/efde4eb).
- Nettoyage des artefacts de provenance et de revue [#5c7d400](https://github.com/codegouvfr/sill-deploy/commit/5c7d400).
- Utilisation de Vite CSP dans l'environnement Vite [#93dd20b](https://github.com/codegouvfr/sill-deploy/commit/93dd20b).
- Correction des dépendances pour les tests [#7273912](https://github.com/codegouvfr/sill-deploy/commit/7273912).
- Amélioration de la configuration locale de CSP pour afficher les images [#0e83b75](https://github.com/codegouvfr/sill-deploy/commit/0e83b75).
- Plusieurs mises à jour de version (build bumps) [#39a4ada](https://github.com/codegouvfr/sill-deploy/commit/39a4ada), [#61055bb](https://github.com/codegouvfr/sill-deploy/commit/61055bb), [#94d3cf5](https://github.com/codegouvfr/sill-deploy/commit/94d3cf5), [#2d13d03](https://github.com/codegouvfr/sill-deploy/commit/2d13d03), [#b3a645b](https://github.com/codegouvfr/sill-deploy/commit/b3a645b), [#6e88656](https://github.com/codegouvfr/sill-deploy/commit/6e88656).
- Réorganisation de la migration [#7c0385d](https://github.com/codegouvfr/sill-deploy/commit/7c0385d).
