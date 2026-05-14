## Changelog : plusfraichemaville-site (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, le site plusfraichemaville-site a bénéficié d'améliorations significatives, notamment sur l'onglet "Financement" avec l'ajout d'incitations pour les espaces projets et une meilleure gestion des redirections. Des corrections ont été apportées pour l'affichage des données Climadiag, notamment pour les collectivités d'outre-mer, et la page d'accueil a été refactorisée. Des améliorations de l'expérience utilisateur ont également été apportées, comme la redirection vers la page de connexion lorsque l'accès à certaines fonctionnalités est restreint.

### Évolutions fonctionnelles
- **Financement :** Ajout d'une incitation pour les espaces projets dans l'onglet "Financement" [#492](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/492).
- **Financement :** Correction d'une redirection lors de la création d'un projet depuis l'onglet "Financement" [#491](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/491).
- **Statut personnel :** Redirection vers la page de connexion pour les utilisateurs non authentifiés accédant à la page "Statut personnel" [#491](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/491).
- **Informations utilisateur :** Correction d'une redirection vers les informations utilisateur pour les utilisateurs non connectés [#488](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/488).
- **Page d'accueil :** Refonte de la page d'accueil avec une nouvelle structure [#487](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/487).
- **Climadiag :** Amélioration de l'affichage des données Climadiag pour les collectivités d'outre-mer, en utilisant des métriques différentes [#815d2194](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/815d2194).
- **Climadiag :** Correction du libellé affiché pour Climadiag [#494](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/494).
- **Climadiag :** Filtrage des aides territoires qui ne sont pas "live" [#07694e82](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/07694e82).
- **Création de projet :** Ajout d'un bouton d'annulation au formulaire de création de projet [#2d54ec06](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/2d54ec06).

### Évolutions techniques
- **Dépendances :** Mise à jour de la version de `pnpm` [#dc786a11](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/dc786a11).
- **CI/CD :** Mise à jour de la version de l'action `actions/setup-node` à 6.4.0 [#594b062a](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/594b062a).
- **Scripts :** Amélioration du script d'importation des données Climadiag [#69132b24](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/69132b24).
- **Prettier :** Mise à jour de la version de Prettier pour le CI [#ca346ebf](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/ca346ebf).
- **Refactoring :** Refactorisation de la page d'accueil [#af3e0a82](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/af3e0a82).

### Autres changements
- Suppression de l'attribut `lien_aides_territoires` [#ebc67a07](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/ebc67a07).
- Correction de l'utilisation du seuil Climadiag dans tout le code [#81b90e03](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/81b90e03).
- Suppression de la mention "Climadiag non disponible en outre-mer" [#c495f44c](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/c495f44c).
- Correction du linting et du formattage du code avec Prettier [#20dc064d](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/20dc064d).
