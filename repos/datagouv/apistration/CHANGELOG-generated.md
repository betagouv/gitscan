## Changelog : apistration (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité et de la gestion des utilisateurs, notamment avec l'ajout d'un délai d'inactivité pour les sessions et une gestion plus fine des rôles des administrateurs. Des améliorations de la documentation et de la robustesse de l'API ont également été apportées, ainsi que l'ajout d'un SDK JavaScript pour faciliter l'intégration.

### Évolutions fonctionnelles

*   **Gestion des utilisateurs :**
    *   Les sessions utilisateurs expirent désormais après 12 heures d'inactivité pour renforcer la sécurité. [#182](https://github.com/datagouv/apistration/issues/182)
    *   Un délai maximal de 24 heures est imposé pour la durée de vie des sessions. [#182](https://github.com/datagouv/apistration/issues/182)
    *   Amélioration de la gestion des administrateurs avec une interface revue pour la gestion des éditeurs (ajout, recherche, filtrage, affichage des informations). [#139](https://github.com/datagouv/apistration/issues/139)
    *   Possibilité de gérer les membres (ajout/suppression) des éditeurs. [#139](https://github.com/datagouv/apistration/issues/139)
    *   Journalisation des activités des administrateurs pour un audit plus fiable. [#171](https://github.com/datagouv/apistration/issues/171)
*   **API :**
    *   Ajout d'un SDK JavaScript (Node.js/TypeScript) pour faciliter l'intégration avec l'API Entreprise et l'API Particulier. [#142](https://github.com/datagouv/apistration/issues/142)
    *   Documentation améliorée pour l'utilisation de FranceConnect en staging. [#167](https://github.com/datagouv/apistration/issues/167)
    *   Ajout d'une API pour récupérer les délégations des éditeurs. [#144](https://github.com/datagouv/apistration/issues/144)
*   **Documentation :**
    *   Clarification du périmètre du quotient familial dans la documentation. [#136](https://github.com/datagouv/apistration/issues/136)
    *   Ajout d'informations sur les scopes et périmètres de l'API Particulier dans la documentation. [#168](https://github.com/datagouv/apistration/issues/168)

### Évolutions techniques

*   **Sécurité :**
    *   Renforcement de la protection contre les attaques CSRF et configuration explicite de SameSite=Lax. [#183](https://github.com/datagouv/apistration/issues/183)
    *   Restriction de l'accès à l'endpoint ANTS identite_particulier via son scope dédié. [#169](https://github.com/datagouv/apistration/issues/169)
*   **Infrastructure :**
    *   Mise à jour des dépendances (Ruby, Rails, Docker, etc.).
    *   Mise à jour des actions GitHub et des versions de Ruby et Node.js.
*   **Code :**
    *   Refactoring du code pour améliorer la lisibilité et la maintenabilité.
    *   Amélioration des tests et des spécifications.
    *   Suppression de code obsolète (serializer DGFIP situation_ir v2). [#166](https://github.com/datagouv/apistration/issues/166)

### Autres changements

*   Correction de typos dans les spécifications et la documentation. [#181](https://github.com/datagouv/apistration/issues/181), [#185](https://github.com/datagouv/apistration/issues/185), [#179](https://github.com/datagouv/apistration/issues/179)
*   Correction d'erreurs dans les URLs de ping de l'API Particulier. [#177](https://github.com/datagouv/apistration/issues/177)
*   Correction d'un problème de fuite de mémoire avec Timecop dans les tests. [#181](https://github.com/datagouv/apistration/issues/181)
*   Amélioration du changelog pour les liasses fiscales. [#179](https://github.com/datagouv/apistration/issues/179)
*   Correction d'un bug lié à la validation des dates de naissance. [#153](https://github.com/datagouv/apistration/issues/153)
*   Correction d'un problème avec les URLs de ping dans l'API Particulier. [#177](https://github.com/datagouv/apistration/issues/177)
*   Mise à jour du lien vers le Bureau Ouvert. [#157](https://github.com/datagouv/apistration/issues/157)
*   Ajout de données pour la v5 de scolarité pour la région PACA. [#156](https://github.com/datagouv/apistration/issues/156)
