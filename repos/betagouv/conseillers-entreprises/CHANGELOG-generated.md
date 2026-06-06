## Changelog : conseillers-entreprises (30 derniers jours, au 02 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la stabilité et de la sécurité de la plateforme, ainsi que sur des corrections de bugs et des ajustements de l'interface utilisateur. Des améliorations ont été apportées aux logs d'authentification, à la gestion des erreurs de recherche d'entreprises et à l'export CSV des satisfactions entreprises. Une mise à jour de Ruby a également été effectuée.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la recherche d'entreprises avec des termes de recherche de moins de 3 caractères [#4481](https://github.com/betagouv/conseillers-entreprises/pull/4481).
- Amélioration de l'export CSV des satisfactions entreprises dans l'espace administrateur [#4459](https://github.com/betagouv/conseillers-entreprises/pull/4459).
- Suppression du code lié à l'API Adresse, qui n'est plus utilisée [#4489](https://github.com/betagouv/conseillers-entreprises/pull/4489).
- Suppression du mail de notification concernant les jobs ayant échoué [#4488](https://github.com/betagouv/conseillers-entreprises/pull/4488).
- Amélioration de la présentation des éléments de besoin de diagnostic [#4483](https://github.com/betagouv/conseillers-entreprises/pull/4483).
- Le lien vers les jobs dans l'espace administrateur pointe désormais directement vers Sidekiq au lieu d'un iframe [#4487](https://github.com/betagouv/conseillers-entreprises/pull/4487).

### Évolutions techniques
- Mise à jour de Ruby vers la version 4.0.5 [#4493](https://github.com/betagouv/conseillers-entreprises/pull/4493).
- Amélioration des logs d'authentification pour inclure l'adresse IP, le port et les en-têtes X-Forwarded-For [#4464](https://github.com/betagouv/conseillers-entreprises/pull/4464).
- Correction d'un problème de traitement des statistiques de thème [#4478](https://github.com/betagouv/conseillers-entreprises/pull/4478).
- Synchronisation du schéma de la base de données [#4468](https://github.com/betagouv/conseillers-entreprises/pull/4468).
- Suppression de code inutile et nettoyage du fichier `.gitignore` [#4497](https://github.com/betagouv/conseillers-entreprises/pull/4497).

### Autres changements
- Mise à jour des dépendances npm et yarn (webpack-dev-server, fast-uri) [#4486](https://github.com/betagouv/conseillers-entreprises/pull/4486), [#4471](https://github.com/betagouv/conseillers-entreprises/pull/4471).
- Mise à jour de la gem Devise vers la version 5.0.4 [#4470](https://github.com/betagouv/conseillers-entreprises/pull/4470).
- Mise à jour de la documentation et des noms d'institutions (Baleen remplacé par Ubika, CE renommé en SPCE) [#4457](https://github.com/betagouv/conseillers-entreprises/pull/4454).
- Ajout d'articles et d'améliorations diverses [#4457](https://github.com/betagouv/conseillers-entreprises/pull/4457).
- Ajout d'un fichier `.dependency-review.yml` pour la revue des dépendances GitHub [#4492](https://github.com/betagouv/conseillers-entreprises/pull/4492).
