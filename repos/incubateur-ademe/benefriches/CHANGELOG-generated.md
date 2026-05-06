## Changelog : benefriches (30 derniers jours, au 5 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur dans la création et la visualisation de projets, notamment pour les projets urbains et photovoltaïques. Des corrections de bugs et des optimisations techniques ont également été apportées, ainsi que des améliorations de la documentation et de l'infrastructure CI/CD. L'ajout de nouvelles fonctionnalités permet un calcul plus précis des impacts économiques et environnementaux des reconversions de friches.

### Évolutions fonctionnelles
- Ajout de visualisations de l'allocation des surfaces dans les projets urbains ([65e17b8](https://github.com/incubateur-ademe/benefriches/commit/65e17b8)).
- Affichage des dépenses de construction et de réhabilitation dans les projets urbains, tant dans la vue des caractéristiques que dans les documents exportés ([0afc523](https://github.com/incubateur-ademe/benefriches/commit/0afc523)).
- Ajout de graphiques pour chaque bénéficiaire d'impact dans l'onglet "niveau de seuil de rentabilité" ([245d401](https://github.com/incubateur-ademe/benefriches/commit/245d401)).
- Implémentation du calcul du niveau de seuil de rentabilité et ajout d'onglets correspondants dans la vue des impacts ([cb3b6ea](https://github.com/incubateur-ademe/benefriches/commit/cb3b6ea)).
- Ajout d'un onglet "Résumé" dans la page des impacts, présentant une vue d'ensemble des données ([63b4698](https://github.com/incubateur-ademe/benefriches/commit/63b4698)).
- Ajout de toutes les templates de projets existants dans l'étape de sélection de template de projet de démonstration ([3e6f100](https://github.com/incubateur-ademe/benefriches/commit/3e6f100)).
- Amélioration des instructions contextuelles dans les formulaires de création de projets (site, urbain, photovoltaïque) ([b69f356](https://github.com/incubateur-ademe/benefriches/commit/b69f356), [595b1aa](https://github.com/incubateur-ademe/benefriches/commit/595b1aa), [be56201](https://github.com/incubateur-ademe/benefriches/commit/be56201), [fc9e358](https://github.com/incubateur-ademe/benefriches/commit/fc9e358)).
- Ajout d'un endpoint pour calculer le coût de l'inaction sur une friche ([fae2976](https://github.com/incubateur-ademe/benefriches/commit/fae2976)).
- Inclusion des coûts de construction et de réhabilitation des bâtiments dans le bilan économique des impacts ([b9c3fd4](https://github.com/incubateur-ademe/benefriches/commit/b9c3fd4)).

### Évolutions techniques
- Refactorisation de la gestion des dépenses de construction des bâtiments pour une meilleure réutilisation du code ([c521574](https://github.com/incubateur-ademe/benefriches/commit/c521574)).
- Création d'un DTO partagé pour les caractéristiques des projets de reconversion ([63d8480](https://github.com/incubateur-ademe/benefriches/commit/63d8480)).
- Amélioration des tests d'intégration pour l'API, notamment pour la gestion des caractéristiques des projets ([277485a](https://github.com/incubateur-ademe/benefriches/commit/277485a)).
- Mise à jour des dépendances (Vitest, Axios, Testcontainers, etc.) ([7f4ecd4](https://github.com/incubateur-ademe/benefriches/commit/7f4ecd4), [047c413](https://github.com/incubateur-ademe/benefriches/commit/047c413), [890c5df](https://github.com/incubateur-ademe/benefriches/commit/890c5df), [397c36b](https://github.com/incubateur-ademe/benefriches/commit/397c36b)).
- Amélioration de l'infrastructure CI/CD : ajout de vérifications de santé après le déploiement, gestion des secrets, contrôle de la concurrence des workflows ([ff0410b](https://github.com/incubateur-ademe/benefriches/commit/ff0410b), [0fc32a3](https://github.com/incubateur-ademe/benefriches/commit/0fc32a3), [a0a4ea8](https://github.com/incubateur-ademe/benefriches/commit/a0a4ea8), [e481d03](https://github.com/incubateur-ademe/benefriches/commit/e481d03), [df6d7fc](https://github.com/incubateur-ademe/benefriches/commit/df6d7fc), [1b7a7ab](https://github.com/incubateur-ademe/benefriches/commit/1b7a7ab)).
- Utilisation de variables d'environnement pour la configuration de la base de données en développement ([2ecf6cd](https://github.com/incubateur-ademe/benefriches/commit/2ecf6cd)).

### Autres changements
- Documentation : ajout de commentaires aux fichiers `.env.example` ([081d380](https://github.com/incubateur-ademe/benefriches/commit/081d380)).
- Documentation : ajout d'une note sur l'utilisation du français et de l'anglais dans la documentation ([1ed4c1a](https://github.com/incubateur-ademe/benefriches/commit/1ed4c1a)).
- Documentation : amélioration du fichier README ([3038b47](https://github.com/incubateur-ademe/benefriches/commit/3038b47)).
- Suppression de fichiers obsolètes du `.gitignore` ([593d43c](https://github.com/incubateur-ademe/benefriches/commit/593d43c)).
- Correction de la documentation de l'API concernant les tâches cron ([db42605](https://github.com/incubateur-ademe/benefriches/commit/db42605)).
- Ajout de la synchronisation quotidienne des abonnements à la newsletter depuis le CRM via un cron Scalingo ([91b0481](https://github.com/incubateur-ademe/benefriches/commit/91b0481)).
- Correction de bugs mineurs et améliorations de la qualité du code.
