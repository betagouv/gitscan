## Changelog : monstagedeseconde (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se sont concentrées sur la sécurité, la correction de bugs et l'amélioration de l'expérience utilisateur, notamment au niveau du formulaire de création d'offres et de la gestion des partenaires. Des refactorisations techniques ont également été effectuées pour améliorer la maintenabilité du code.

### Évolutions fonctionnelles
- Amélioration du formulaire de création d'offres : corrections de bugs et amélioration de la visualisation des erreurs [#937](https://github.com/betagouv/monstagedeseconde/pulls/937).
- Limitation de la longueur de la description des offres via l'API [#922](https://github.com/betagouv/monstagedeseconde/pulls/922).
- Modification de l'accès au formulaire de contact [#917](https://github.com/betagouv/monstagedeseconde/pulls/917).
- Suppression du bloc "Devenez partenaire" sur la page d'accueil [#921](https://github.com/betagouv/monstagedeseconde/pulls/921) et [#920](https://github.com/betagouv/monstagedeseconde/pulls/920).
- Optimisation de la gestion des offres publiques et privées [#912](https://github.com/betagouv/monstagedeseconde/pulls/912).

### Évolutions techniques
- Refactorisation du code pour mutualiser des éléments et améliorer la lisibilité et la maintenabilité [#938](https://github.com/betagouv/monstagedeseconde/pulls/938), [#933](https://github.com/betagouv/monstagedeseconde/pulls/933), [#932](https://github.com/betagouv/monstagedeseconde/pulls/932), [#929](https://github.com/betagouv/monstagedeseconde/pulls/929).
- Renforcement de la sécurité :
    - Correction d'une vulnérabilité XSS dans le rendu du contenu Prismic [#933](https://github.com/betagouv/monstagedeseconde/pulls/933).
    - Ajout de vérifications de sécurité pour prévenir le détournement de compte [#932](https://github.com/betagouv/monstagedeseconde/pulls/932).
    - Utilisation de `secure_compare` pour éviter les failles de timing attacks [#933](https://github.com/betagouv/monstagedeseconde/pulls/933).
- Mise à jour de plusieurs dépendances : Faraday, Nokogiri, webpack-dev-server, @babel/core, undici, http-proxy-middleware, concurrent-ruby, form-data, launch-editor.
- Amélioration de la gestion des tâches d'archivage annuelle [#931](https://github.com/betagouv/monstagedeseconde/pulls/931).
- Correction d'une erreur empêchant le seed de fonctionner correctement [#902](https://github.com/betagouv/monstagedeseconde/pulls/902).

### Autres changements
- Mise à jour des pages partenaires [#942](https://github.com/betagouv/monstagedeseconde/pulls/942).
- Amélioration des tests et correction de tests cassés.
- Suppression de code mort.
- Correction de problèmes liés aux routes et aux redirections.
- Amélioration de la gestion des états des candidatures dans les tableaux de bord [#936](https://github.com/betagouv/monstagedeseconde/pulls/936).
- Suppression du FAQ de la page d'accueil.
- Modification des libellés des états des candidatures dans les tableaux de bord [#936](https://github.com/betagouv/monstagedeseconde/pulls/936).
