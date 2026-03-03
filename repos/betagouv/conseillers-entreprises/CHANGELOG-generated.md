## Changelog : conseillers-entreprises (30 derniers jours)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la correction de bugs, l'amélioration de la gestion des données (notamment des codes SIRET et des URL), et l'optimisation de l'interface utilisateur pour les administrateurs. Des efforts ont également été faits pour améliorer la sécurité et la robustesse de l'application, notamment en corrigeant des erreurs liées aux dépendances et en renforçant l'authentification.

### Évolutions fonctionnelles
- Correction d'un bug qui transformait des erreurs 404 en erreurs 500. [#4294](https://github.com/betagouv/conseillers-entreprises/pull/4294)
- Amélioration de la gestion des périodes de monitoring. [#4299](https://github.com/betagouv/conseillers-entreprises/pull/4299)
- Correction d'un problème empêchant la création de sollicitations sans code INSEE. [#4269](https://github.com/betagouv/conseillers-entreprises/pull/4269)
- Ajout d'un avertissement de confidentialité dans le modal de personne. [#4263](https://github.com/betagouv/conseillers-entreprises/pull/4263)
- Ajout d'un nouvel onglet pour le suivi des antennes. [#4230](https://github.com/betagouv/conseillers-entreprises/pull/4230)
- Unification de l'onglet d'optimisation. [#4203](https://github.com/betagouv/conseillers-entreprises/pull/4203)
- Ajout de vidéos d'aide. [#4239](https://github.com/betagouv/conseillers-entreprises/pull/4239)
- Correction de l'export CSV des sollicitations. [#4229](https://github.com/betagouv/conseillers-entreprises/pull/4229)

### Évolutions techniques
- Refactorisation du code pour améliorer la gestion des filtres thématiques dans les besoins. [#4251](https://github.com/betagouv/conseillers-entreprises/pull/4251)
- Simplification du code pour réduire les chargements inutiles. [#4292](https://github.com/betagouv/conseillers-entreprises/pull/4292)
- Mise à jour de la gestion des URL des sollicitations pour utiliser des slugs. [#4288](https://github.com/betagouv/conseillers-entreprises/pull/4288)
- Intégration d'AppSignal pour le monitoring et le suivi des erreurs. [#4265](https://github.com/betagouv/conseillers-entreprises/pull/4265)
- Passage à gem.coop pour la gestion des dépendances Ruby. [#4232](https://github.com/betagouv/conseillers-entreprises/pull/4232)
- Mise à jour des dépendances : webpack (5.103.0 -> 5.104.1), rack (3.2.4 -> 3.2.5), nokogiri (1.18.10 -> 1.19.1).
- Correction d'une régression introduite par une mise à jour de dépendances. [#4236](https://github.com/betagouv/conseillers-entreprises/pull/4236)

### Autres changements
- Amélioration de la couverture des tests. [#4257](https://github.com/betagouv/conseillers-entreprises/pull/4257)
- Correction de fautes de frappe dans les workflows CI/CD. [#4233](https://github.com/betagouv/conseillers-entreprises/pull/4233)
- Suppression de fichiers `.vscode` du suivi Git. [#4277](https://github.com/betagouv/conseillers-entreprises/pull/4277)
- Ajout d'une mention de sponsoring AppSignal dans le README. [#4278](https://github.com/betagouv/conseillers-entreprises/pull/4278)
- Désactivation des robots d'indexation en environnement de staging. [#4237](https://github.com/betagouv/conseillers-entreprises/pull/4237)
- Suppression de code inutile et amélioration de la lisibilité du code.
- Correction de typos et amélioration de la documentation.
