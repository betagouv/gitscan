## Changelog : monstagedeseconde (30 derniers jours)

### Résumé
Les dernières mises à jour de MonStage se concentrent sur la correction de bugs et l'amélioration de la gestion des données, notamment concernant les offres de stages, les établissements scolaires et les conventions. Des améliorations ont également été apportées à l'importation de données et à la gestion des signatures électroniques. Enfin, des ajustements ont été faits pour optimiser la performance et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Correction d'un bug empêchant l'affichage correct des candidatures ([#777](https://github.com/betagouv/monstagedeseconde/issues/777)).
- Amélioration de la gestion des codes CEDEX pour la région de la Réunion, assurant une redirection correcte vers le code départemental approprié ([#782](https://github.com/betagouv/monstagedeseconde/issues/782)).
- Correction de l'affichage des descriptions d'entreprises tronquées dans l'API.
- Correction d'un bug dans le script de duplication d'offres, qui manquait de la description de l'employeur.
- Amélioration de la gestion des erreurs lors de l'analyse JSON dans le contrôleur `ApiEntrepriseProxyController`.
- Correction d'une erreur liée à un attribut manquant dans le modèle `User` lors de la gestion des établissements scolaires ([#778](https://github.com/betagouv/monstagedeseconde/issues/778)).
- Correction d'un bug lié à l'affichage des signatures pour les gestionnaires d'établissements scolaires ([#752](https://github.com/betagouv/monstagedeseconde/issues/752)).
- Amélioration de l'envoi d'emails pour les signatures de conventions ([#771](https://github.com/betagouv/monstagedeseconde/issues/771)).
- Correction de l'affichage des accords multiples.
- Amélioration de la gestion des places disponibles pour les offres de stages collège et lycée.
- Ajout de la gem `letter_thief` pour la gestion des emails ([#750](https://github.com/betagouv/monstagedeseconde/issues/750)).
- Correction de l'affichage des accents dans l'interface.
- Correction d'un bug lié à la recherche mobile.
- Correction de l'importation des classes des élèves depuis Sygne.
- Amélioration de la gestion des offres inappropriées.
- Correction d'un bug dans le script de duplication d'offres, permettant de gérer les offres qui ne peuvent pas être sauvegardées.
- Correction de l'affichage des offres de stages sur mobile.
- Amélioration du wording de l'application.
- Correction de l'importation des écoles.

### Évolutions techniques
- Mise à jour de la gem `nokogiri` vers la version 1.19.1.
- Mise à jour de la gem `immutable` vers la version 5.1.5.
- Mise à jour de la gem `qs` vers la version 6.14.2.
- Mise à jour de la gem `faraday` vers la version 2.14.1.
- Mise à jour de la gem `rack` vers la version 3.2.5.
- Configuration de Ruby LSP.
- Amélioration de la gestion des paramètres de production dans le fichier `structure.sql`.
- Refactoring du code pour supprimer les assignations vides.

### Autres changements
- Synchronisation des fichiers de configuration traditionnels et masquage des fichiers de versionnement.
- Correction de tests unitaires et système.
- Mise à jour de la documentation.
- Intégration continue et déploiement (CI/CD) avec CircleCI.
- Amélioration de la gestion des tests KPI.
- Ajout de la configuration pour Ruby LSP.
- Suppression de dépendances inutiles dans le Gemfile.
- Correction de tests.
- Merge de branches staging et review.
- Correction de wording.
- Fix Prismic.
