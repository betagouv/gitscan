## Changelog : sante-mentale-etudiant (30 derniers jours, au 2026-07-17)

### Résumé
Ce mois-ci, le projet a connu des avancées significatives sur la fonctionnalité "Trouver du soutien", avec l'implémentation d'une page de résultats et de filtres, ainsi que le début de la construction de l'outil "Orienteur". Des améliorations ont également été apportées à l'infrastructure de build avec la migration vers pnpm et la configuration des jobs CI/CD. Enfin, une première bannière a été ajoutée à la page d'accueil.

### Évolutions fonctionnelles
- Implémentation de la page de résultats pour la fonctionnalité "Trouver du soutien" [#10](https://github.com/betagouv/sante-mentale-etudiant/pulls/10).
- Ajout de filtres conditionnels à la fonctionnalité "Trouver du soutien" [#2040](https://github.com/betagouv/sante-mentale-etudiant/issues/2040).
- Lancement de la structure principale et de l'arbre de décision pour l'outil "Orienteur" [#6](https://github.com/betagouv/sante-mentale-etudiant/pulls/6).
- Première bannière ajoutée à la page d'accueil [#1](https://github.com/betagouv/sante-mentale-etudiant/pulls/1).
- Lien entre l'Orienteur et la page de résultats de "Trouver du soutien" [#11](https://github.com/betagouv/sante-mentale-etudiant/pulls/11).
- Amélioration de l'interface utilisateur avec un nouveau composant de carte personnalisé [#3040](https://github.com/betagouv/sante-mentale-etudiant/issues/3040).

### Évolutions techniques
- Migration vers pnpm 11 pour la gestion des dépendances et amélioration de la performance des builds.
- Configuration des jobs CI/CD initiaux sur GitHub Actions [#5](https://github.com/betagouv/sante-mentale-etudiant/pulls/5).
- Approbation des scripts de build pnpm pour le déploiement.
- Correction d'une vulnérabilité dans la dépendance `postcss` via pnpm audit.

### Autres changements
- Corrections de style et de noms de variables CSS pour améliorer la cohérence du code.
- Correction de bugs mineurs dans l'interface utilisateur (padding mobile, hauteur d'image, thème par défaut).
- Refactorisation des filtres de la fonctionnalité "Trouver du soutien".
- Amélioration de la présentation des titres et sous-titres dans "Trouver du soutien".
- Initialisation du dépôt avec un premier commit.
