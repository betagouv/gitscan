## Changelog : monstagedeseconde (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la sécurité, la correction de bugs et l'amélioration de l'expérience utilisateur, notamment au niveau de la gestion des offres et des candidatures. Des améliorations ont également été apportées à la gestion des conventions et à la gestion des utilisateurs. Plusieurs mises à jour de dépendances ont été intégrées pour maintenir la sécurité et la stabilité de la plateforme.

### Évolutions fonctionnelles
- **Gestion des candidatures :** Correction d'un bug permettant d'éviter les candidatures en double. [#898](https://github.com/betagouv/monstagedeseconde/issues/898)
- **Gestion des offres :** Correction d'un bug empêchant l'affichage correct des offres d'un employeur.
- **Gestion des conventions :** Amélioration de la gestion des conventions, notamment pour la duplication et l'affichage des URL des ressources. [#893](https://github.com/betagouv/monstagedeseconde/issues/893), [#872](https://github.com/betagouv/monstagedeseconde/issues/872)
- **Sécurité :** Correction d'une vulnérabilité XSS potentielle dans le CMS Prismic en échappant le contenu HTML.
- **Sécurité :** Renforcement de la sécurité pour prévenir le détournement de compte par un élève. [#932](https://github.com/betagouv/monstagedeseconde/issues/932)
- **Gestion des utilisateurs :** Possibilité d'associer un personnel pédagogique à plusieurs établissements. [#881](https://github.com/betagouv/monstagedeseconde/issues/881)
- **Gestion des utilisateurs :** Importation d'étudiants depuis le tableau de bord administrateur. [#880](https://github.com/betagouv/monstagedeseconde/issues/880)
- **Interface utilisateur :** Suppression du bloc "Devenez partenaire" de la page d'accueil. [#921](https://github.com/betagouv/monstagedeseconde/issues/921), [#920](https://github.com/betagouv/monstagedeseconde/issues/920)
- **Interface utilisateur :** Amélioration de la gestion des semaines vides dans la recherche. [#851](https://github.com/betagouv/monstagedeseconde/issues/851)

### Évolutions techniques
- **Refactoring :** Refactorisation du code pour améliorer la lisibilité et la maintenabilité, notamment au niveau de l'ability. [#889](https://github.com/betagouv/monstagedeseconde/issues/889)
- **Tests :** Ajout de tests unitaires et système pour améliorer la couverture et la qualité du code.
- **CI/CD :** Amélioration du processus de rebuild en revue, notamment en ajoutant des étapes de nettoyage et de vérification.
- **Infrastructure :** Configuration de Redis sur Heroku.
- **Mises à jour :** Mises à jour de plusieurs dépendances (Faraday, Nokogiri, Webpack, Babel, Undici, http-proxy-middleware, concurrent-ruby, form-data, launch-editor, puma, net-imap, shell-quote).
- **Base de données :** Ajout d'une migration pour gérer les relations entre les utilisateurs et les établissements scolaires.
- **Sécurité :** Utilisation de `secure_compare` pour éviter les vulnérabilités de comparaison de chaînes de caractères.

### Autres changements
- **Documentation :** Mise à jour de la documentation.
- **Configuration :** Mise à jour de la configuration de l'environnement de revue.
- **Nettoyage de code :** Suppression de code mort et de commentaires inutiles.
- **Seed :** Correction de problèmes dans le seed pour éviter les erreurs lors de l'initialisation de la base de données.
- **Amélioration des logs :** Ajout de traces pour faciliter le débogage.
- **Correction de bugs mineurs :** Correction de divers bugs mineurs affectant l'interface utilisateur et le comportement de l'application.
