## Changelog : reva (30 derniers jours)

### Résumé
Les dernières semaines ont été marquées par une amélioration significative de l'intégration de FranceConnect, avec des optimisations pour la gestion des utilisateurs et des candidatures. Des améliorations ont également été apportées à l'interface d'administration, notamment pour la gestion des certifications et des organismes certificateurs, ainsi que des corrections de bugs et des refactorings pour améliorer la stabilité et la maintenabilité du code.

### Évolutions fonctionnelles

*   **FranceConnect :** Amélioration de l'intégration de FranceConnect pour la gestion des candidatures et de l'authentification, incluant la gestion des erreurs et des messages informatifs. [#153caf0](https://github.com/betagouv/reva/commit/153caf0)
*   **Admin - Gestion des certifications :** Ajout de la possibilité de filtrer les certifications par organisme certificateur local. [#5471379](https://github.com/betagouv/reva/commit/5471379)
*   **Admin - Organismes certificateurs :** Amélioration de la page de paramètres des organismes certificateurs avec l'ajout de la liste des parcours de certification et de l'ID de l'organisme certificateur dans l'URL. [#e227f9f](https://github.com/betagouv/reva/commit/e227f9f)
*   **Admin - Gestion des candidatures :** Ajout d'une vue paginée et filtrable pour l'assignation des certifications aux comptes locaux. [#77f93c8](https://github.com/betagouv/reva/commit/77f93c8)
*   **Admin - DF Demat :** Ajout d'un modèle de confirmation pour la déclaration de complétude du DF par l'organisme certificateur. [#77c1234](https://github.com/betagouv/reva/commit/77c1234)
*   **Candidat - Affichage des certifications :** Masquage des onglets de certification pour les exigences réduites. [#d0771e9](https://github.com/betagouv/reva/commit/d0771e9)
*   **Candidat - Informations personnelles :** Amélioration de l'affichage et de la gestion des informations personnelles, notamment en lien avec FranceConnect. [#3a43553](https://github.com/betagouv/reva/commit/3a43553)
*   **Candidat - Page d'enregistrement :** Amélioration de la page d'enregistrement avec l'intégration de FranceConnect et des améliorations de la mise en page. [#639ddd8](https://github.com/betagouv/reva/commit/639ddd8)

### Évolutions techniques

*   **Tests :** Migration de nombreux tests Cypress vers Playwright dans l'administration. [#9d19c95](https://github.com/betagouv/reva/commit/9d19c95)
*   **API :** Refactor de la gestion de l'état de connexion FranceConnect avec l'utilisation de JWT. [#76b0d2e](https://github.com/betagouv/reva/commit/76b0d2e)
*   **API :** Ajout de nouveaux champs et resolvers GraphQL pour la gestion des parcours de certification. [#2c53216](https://github.com/betagouv/reva/commit/2c53216)
*   **Frontend :** Mise à jour vers Next.js 16 et React 19. [#2c234e9](https://github.com/betagouv/reva/commit/2c234e9)
*   **Refactoring général :** Plusieurs refactorings ont été effectués pour simplifier le code, améliorer la lisibilité et la maintenabilité.

### Autres changements

*   **Documentation :** Ajout d'un schéma d'architecture applicative. [#c2573e9](https://github.com/betagouv/reva/commit/c2573e9)
*   **Corrections :** Correction de bugs mineurs dans l'interface d'administration et l'API.
*   **Dépendances :** Mises à jour de plusieurs dépendances (ajv, basic-ftp, bn.js, rollup, minimatch, jspdf, webpack, @isaacs/brace-expansion, fastify).
