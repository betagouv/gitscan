## Changelog : monstagedeseconde (30 derniers jours, au 06 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la sécurité, notamment en corrigeant des failles potentielles liées à l'injection de code et au détournement de compte. Des corrections de bugs et des optimisations ont également été apportées, notamment au niveau du formulaire de création d'offres, de la gestion des candidatures et de la duplication d'offres. Enfin, des refactorings techniques ont été réalisés pour améliorer la maintenabilité du code.

### Évolutions fonctionnelles

- Amélioration du formulaire de création d'offres : visualisation améliorée des erreurs et limitation de la longueur de la description. [#937](https://github.com/betagouv/monstagedeseconde/pull/937)
- Suppression du bloc "Devenez Partenaire" de l'interface. [#921](https://github.com/betagouv/monstagedeseconde/pull/921), [#920](https://github.com/betagouv/monstagedeseconde/pull/920), [#906](https://github.com/betagouv/monstagedeseconde/pull/906)
- Possibilité d'associer un personnel pédagogique à plusieurs établissements. [#881](https://github.com/betagouv/monstagedeseconde/pull/881)
- Modification de l'accès au formulaire de contact. [#917](https://github.com/betagouv/monstagedeseconde/pull/917)
- Correction d'un bug empêchant la suppression d'offres.
- Correction d'un problème de double publication d'offres due à des clics intempestifs. [#907](https://github.com/betagouv/monstagedeseconde/pull/907)
- Possibilité de modifier l'adresse email des représentants légaux. [#910](https://github.com/betagouv/monstagedeseconde/pull/910)

### Évolutions techniques

- Renforcement de la sécurité : correction de failles XSS potentielles dans le rendu du contenu Prismic. [#933](https://github.com/betagouv/monstagedeseconde/pull/933)
- Renforcement de la sécurité : protection contre le détournement de compte par un élève. [#932](https://github.com/betagouv/monstagedeseconde/pull/932)
- Refactoring de l'architecture des états des candidatures dans les tableaux de bord pour une meilleure lisibilité. [#936](https://github.com/betagouv/monstagedeseconde/pull/936)
- Refactoring de l'implémentation de l'autorisation (Ability) pour une meilleure maintenabilité. [#889](https://github.com/betagouv/monstagedeseconde/pull/889)
- Amélioration de la gestion des erreurs et des validations dans le formulaire d'offre.
- Optimisation de la gestion des offres publiques et privées. [#912](https://github.com/betagouv/monstagedeseconde/pull/912)
- Correction de problèmes liés à la reconstruction de l'environnement de revue.
- Amélioration de la gestion des dates pour la duplication d'offres.
- Correction de bugs liés à la gestion des utilisateurs et des établissements.
- Mise à jour de plusieurs dépendances (Faraday, Nokogiri, webpack-dev-server, Babel, Undici, http-proxy-middleware, concurrent-ruby, form-data, launch-editor, puma, net-imap).

### Autres changements

- Amélioration de la documentation et des tests.
- Nettoyage du code et suppression de code mort.
- Correction de problèmes de configuration et de seed.
- Ajout d'un lien vers "letter thief".
- Correction de problèmes de configuration Redis.
- Amélioration de la gestion des erreurs dans le code.
- Correction de problèmes de typographie et de wording.
- Ajout de tests unitaires et système.
- Mise à jour de la configuration de Sidekiq sur Heroku.
