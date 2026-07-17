## Changelog : proconnect-test-client (30 derniers jours, au 26 juillet 2026)

### Résumé
Les récentes mises à jour de proconnect-test-client se concentrent sur l'amélioration de la flexibilité du flux d'authentification, notamment avec l'ajout de la fonctionnalité "full acr" et la mise à jour des valeurs d'ACR par défaut pour l'authentification multi-facteurs (MFA). Des mises à jour de dépendances ont également été effectuées pour maintenir la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- Ajout de la fonctionnalité de connexion avec "full acr" permettant une configuration plus précise du flux d'authentification. [#207](https://github.com/proconnect-gouv/proconnect-test-client/pull/207)
- Mise à jour des valeurs d'ACR par défaut pour l'authentification multi-facteurs (MFA) afin de refléter les nouvelles configurations. [#202](https://github.com/proconnect-gouv/proconnect-test-client/pull/202)

### Évolutions techniques
- Mise à jour de TypeScript vers la version 7.0.2 dans le répertoire `/e2e`. [#216](https://github.com/proconnect-gouv/proconnect-test-client/pull/216)
- Mise à jour de l'action Docker metadata vers la version 6. [#170](https://github.com/proconnect-gouv/proconnect-test-client/pull/170)
- Mise à jour de plusieurs dépendances de développement (js-yaml, prettier, cypress, @badeball/cypress-cucumber-preprocessor) dans le répertoire `/e2e`. [#211](https://github.com/proconnect-gouv/proconnect-test-client/pull/211), [#214](https://github.com/proconnect-gouv/proconnect-test-client/pull/214), [#215](https://github.com/proconnect-gouv/proconnect-test-client/pull/215), [#213](https://github.com/proconnect-gouv/proconnect-test-client/pull/213)
- Mise à jour de Cypress vers la version 15.18.0 dans le répertoire `/e2e`. [#209](https://github.com/proconnect-gouv/proconnect-test-client/pull/209)
- Mise à jour de form-data vers la version 4.0.6 et body-parser vers la version 2.3.0. [#203](https://github.com/proconnect-gouv/proconnect-test-client/pull/203), [#205](https://github.com/proconnect-gouv/proconnect-test-client/pull/205)
- Mise à jour de l'action actions/checkout vers la version 7. [#204](https://github.com/proconnect-gouv/proconnect-test-client/pull/204)

### Autres changements
- Mise à jour du fichier `index.ejs`. [#207](https://github.com/proconnect-gouv/proconnect-test-client/pull/207)
- Amélioration de la configuration du linter et déplacement des fonctionnalités bêta dans une section dédiée. [#207](https://github.com/proconnect-gouv/proconnect-test-client/pull/207)
