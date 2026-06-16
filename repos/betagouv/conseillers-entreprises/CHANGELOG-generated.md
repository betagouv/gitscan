## Changelog : conseillers-entreprises (30 derniers jours, au 15 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des rapports statistiques disponibles dans l'interface d'administration, avec l'ajout d'une colonne d'évolution et de nouvelles actions pour la génération de rapports. Des corrections et simplifications de code ont également été apportées, notamment concernant la gestion des jobs Sidekiq et l'affichage des besoins de diagnostic. Une vulnérabilité potentielle d'injection de code a été corrigée.

### Évolutions fonctionnelles
- Ajout d'une colonne "Évolution" dans le rapport des coopérations, permettant de suivre les changements dans le temps. [#4500](https://github.com/betagouv/conseillers-entreprises/pull/4500)
- Ajout d'actions dans l'interface d'administration pour générer les rapports. [#4495](https://github.com/betagouv/conseillers-entreprises/pull/4495)
- Correction de l'affichage des besoins de diagnostic, avec une mise en page améliorée et la suppression de code inutile. [#4483](https://github.com/betagouv/conseillers-entreprises/pull/4483)
- Correction du lien vers les jobs Sidekiq dans l'interface d'administration, qui pointe désormais directement vers Sidekiq. [#4487](https://github.com/betagouv/conseillers-entreprises/pull/4487)

### Évolutions techniques
- Refactoring et simplification du code lié à la gestion des rapports, notamment concernant l'enqueuing et la génération des jobs. [#4498](https://github.com/betagouv/conseillers-entreprises/pull/4498) et [#4493](https://github.com/betagouv/conseillers-entreprises/pull/4493)
- Mise à jour de Ruby vers la version 4.0.5. [#4493](https://github.com/betagouv/conseillers-entreprises/pull/4493)
- Correction d'une vulnérabilité potentielle d'injection de code détectée par l'analyse de code. [#4514](https://github.com/betagouv/conseillers-entreprises/pull/4514)
- Suppression du code lié à l'API Adresse, qui n'est plus utilisée. [#4489](https://github.com/betagouv/conseillers-entreprises/pull/4489)
- Suppression du mail de notification concernant les jobs ayant échoué. [#4488](https://github.com/betagouv/conseillers-entreprises/pull/4488)
- Mise à jour de dépendances : webpack-dev-server. [#4486](https://github.com/betagouv/conseillers-entreprises/pull/4486) et net-imap. [#4512](https://github.com/betagouv/conseillers-entreprises/pull/4512)

### Autres changements
- Ajout d'un fichier de configuration pour la revue des dépendances GitHub. [#4492](https://github.com/betagouv/conseillers-entreprises/pull/4492)
- Amélioration de la configuration Rubocop. [#4496](https://github.com/betagouv/conseillers-entreprises/pull/4496)
- Nettoyage du fichier `.gitignore`. [#4497](https://github.com/betagouv/conseillers-entreprises/pull/4497)
- Correction d'une erreur de traitement des statistiques de thème. [#4478](https://github.com/betagouv/conseillers-entreprises/pull/4478)
