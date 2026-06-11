## Changelog : conseillers-entreprises (30 derniers jours, au 8 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la génération et de la gestion des rapports d'activité, ainsi que sur des corrections de bugs et des optimisations techniques pour améliorer la stabilité et la performance de la plateforme. Des améliorations ont également été apportées à la recherche d'entreprises et à la gestion des logs.

### Évolutions fonctionnelles
- Ajout d'actions ActiveAdmin pour la génération de rapports. [#4495](https://github.com/betagouv/conseillers-entreprises/pull/4495)
- Amélioration de l'affichage des éléments de besoin de diagnostic avec une mise en page en grille. [#4483](https://github.com/betagouv/conseillers-entreprises/pull/4483)
- Correction d'un bug empêchant la recherche d'entreprises avec moins de 3 caractères. [#4481](https://github.com/betagouv/conseillers-entreprises/pull/4481)
- Correction d'un bug lié au traitement des statistiques de thème dans les rapports. [#4478](https://github.com/betagouv/conseillers-entreprises/pull/4478)
- Lien direct vers Sidekiq depuis le menu Jobs dans l'interface d'administration, remplaçant l'iframe. [#4487](https://github.com/betagouv/conseillers-entreprises/pull/4487)

### Évolutions techniques
- Mise à jour de Ruby en version 4.0.5 pour bénéficier des dernières corrections et améliorations. [#4493](https://github.com/betagouv/conseillers-entreprises/pull/4493)
- Refactorisation du code lié à la gestion de la durée des événements (TimeDurationService). [#4494](https://github.com/betagouv/conseillers-entreprises/pull/4494)
- Simplification de la classe `ActivityReports`. [#4495](https://github.com/betagouv/conseillers-entreprises/pull/4495)
- Suppression du code lié à l'ancienne API Adresse. [#4489](https://github.com/betagouv/conseillers-entreprises/pull/4489)
- Suppression des emails de notification concernant les jobs échoués. [#4488](https://github.com/betagouv/conseillers-entreprises/pull/4488)
- Mise à jour de la dépendance webpack-dev-server en version 5.2.4. [#4486](https://github.com/betagouv/conseillers-entreprises/pull/4486)
- Ajout de `SidekiqJob.status_for` pour faciliter le suivi des jobs.
- Amélioration de la gestion des logs pour éviter de journaliser des informations sensibles (adresses email) lors des échecs d'authentification. [#4479](https://github.com/betagouv/conseillers-entreprises/pull/4479)

### Autres changements
- Ajout d'un fichier de configuration pour la revue des dépendances GitHub. [#4492](https://github.com/betagouv/conseillers-entreprises/pull/4492)
- Nettoyage du fichier `.gitignore`. [#4497](https://github.com/betagouv/conseillers-entreprises/pull/4497)
- Corrections mineures de code et de style pour améliorer la lisibilité et la maintenabilité.
- Mise à jour de Bootsnap pour corriger un problème de compatibilité avec Ruby 4.0.4+.
