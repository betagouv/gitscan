## Changelog : monstagedeseconde (30 derniers jours, au 22 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations de la sécurité, des corrections de bugs et des optimisations de l'interface utilisateur. Des mises à jour ont été apportées aux formulaires d'offres, aux pages partenaires et à la gestion des candidatures. Des refactorings techniques ont également été réalisés pour améliorer la maintenabilité du code.

### Évolutions fonctionnelles
- **Offres d'emploi :** Limitation de la longueur de la description des offres via l'API [#922](https://github.com/betagouv/monstagedeseconde/pulls/922).
- **Formulaire d'offre :** Amélioration de la visualisation des erreurs lors de la création d'une offre [#937](https://github.com/betagouv/monstagedeseconde/pulls/937).
- **Pages partenaires :** Mise à jour des pages partenaires avec un carrousel de logos [#941](https://github.com/betagouv/monstagedeseconde/pulls/941), [#944](https://github.com/betagouv/monstagedeseconde/pulls/944), [#942](https://github.com/betagouv/monstagedeseconde/pulls/942).
- **Page étudiant :** Mise à jour de la page étudiant [#941](https://github.com/betagouv/monstagedeseconde/pulls/941).
- **Suppression FAQ :** Suppression du bloc FAQ de la page d'accueil [#921](https://github.com/betagouv/monstagedeseconde/pulls/921).
- **Statut des candidatures :** Simplification des libellés des états des candidatures dans les tableaux de bord [#936](https://github.com/betagouv/monstagedeseconde/pulls/936).

### Évolutions techniques
- **Sécurité :** Correction de potentielles failles XSS dans le rendu du contenu Prismic [#933](https://github.com/betagouv/monstagedeseconde/pulls/933) et renforcement de la sécurité contre le détournement de compte [#932](https://github.com/betagouv/monstagedeseconde/pulls/932). Utilisation de `secure_compare` pour les comparaisons sensibles [#920](https://github.com/betagouv/monstagedeseconde/pulls/920).
- **Refactoring :** Mutualisation de code et suppression de code mort dans divers composants [#938](https://github.com/betagouv/monstagedeseconde/pulls/938), [#920](https://github.com/betagouv/monstagedeseconde/pulls/920).
- **Archivage :** Mise à jour des tâches d'archivage des offres et des employeurs [#943](https://github.com/betagouv/monstagedeseconde/pulls/943), [#947](https://github.com/betagouv/monstagedeseconde/pulls/947).
- **Maintenance :** Préparation pour la maintenance d'été 2026 [#943](https://github.com/betagouv/monstagedeseconde/pulls/943).

### Autres changements
- Mise à jour des dépendances : plusieurs dépendances ont été mises à jour (webpack-dev-server, babel/core, undici, http-proxy-middleware, concurrent-ruby, js-yaml, form-data, launch-editor, nokogiri, faraday, view_component, websocket-driver).
- Amélioration de la gestion des erreurs et des tests.
- Corrections mineures et améliorations de la qualité du code.
