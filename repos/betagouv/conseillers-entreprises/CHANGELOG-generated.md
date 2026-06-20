## Changelog : conseillers-entreprises (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la génération et de la présentation des rapports statistiques, la correction de bugs liés à la gestion des SIRET et des appels API, ainsi que des améliorations de la documentation et de la maintenance technique du projet. Des témoignages d'experts ont également été ajoutés au site.

### Évolutions fonctionnelles
- Ajout d'une colonne "Évolution" au rapport des coopérations pour suivre les changements dans le temps. [#4500](https://github.com/betagouv/conseillers-entreprises/pull/4500)
- Intégration de témoignages d'experts sur le site web, avec une mise à jour du sitemap. [#4506](https://github.com/betagouv/conseillers-entreprises/pull/4506)
- Amélioration de l'interface pour les besoins de diagnostic, avec une mise en page en grille. [#4483](https://github.com/betagouv/conseillers-entreprises/pull/4483)
- Correction d'un bug empêchant la réutilisation d'un SIRET lors d'une sollicitation. [#4524](https://github.com/betagouv/conseillers-entreprises/pull/4524)
- Correction d'un problème empêchant l'affichage correct des statistiques thématiques. [#4516](https://github.com/betagouv/conseillers-entreprises/pull/4516)

### Évolutions techniques
- Mise à jour de Ruby vers la version 4.0.5. [#4493](https://github.com/betagouv/conseillers-entreprises/pull/4493)
- Refactorisation du code lié à la génération de rapports pour simplifier la logique et améliorer la maintenabilité. [#4478](https://github.com/betagouv/conseillers-entreprises/pull/4478)
- Simplification des tests liés à la gestion de la durée. [#4494](https://github.com/betagouv/conseillers-entreprises/pull/4494)
- Suppression du code lié à l'API adresse, qui n'est plus utilisé. [#4489](https://github.com/betagouv/conseillers-entreprises/pull/4489)
- Correction d'un problème lié à la gestion des jobs échoués dans Sidekiq. [#4488](https://github.com/betagouv/conseillers-entreprises/pull/4488)
- Mise à jour des dépendances du projet. [#4496](https://github.com/betagouv/conseillers-entreprises/pull/4496)
- Amélioration de la configuration CircleCI pour l'utilisation des caches et la publication de la couverture de code. [#4463](https://github.com/betagouv/conseillers-entreprises/pull/4463)

### Autres changements
- Mise à jour de la documentation de l'architecture du projet, notamment pour refléter le changement de nom de "Pôle-Emploi" à "France Travail" et préciser les statistiques liées aux besoins des entreprises. [#4463](https://github.com/betagouv/conseillers-entreprises/pull/4463)
- Ajout d'un lien direct vers Sidekiq dans le menu d'administration des jobs. [#4487](https://github.com/betagouv/conseillers-entreprises/pull/4487)
- Suppression d'un mail de notification concernant les jobs échoués. [#4514](https://github.com/betagouv/conseillers-entreprises/pull/4514)
- Ajout d'un fichier `.dependency-review.yml` pour la revue des dépendances par GitHub. [#4492](https://github.com/betagouv/conseillers-entreprises/pull/4492)
- Correction d'une vulnérabilité potentielle liée à l'injection de code. [#4513](https://github.com/betagouv/conseillers-entreprises/pull/4513)
