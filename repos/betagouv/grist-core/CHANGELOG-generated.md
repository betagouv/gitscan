## Changelog : grist-core (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe de Grist s'est concentrée sur l'amélioration de l'importation de données depuis Airtable, l'amélioration de l'expérience utilisateur avec des corrections de couleurs et de l'interface, ainsi que des améliorations de la sécurité et de la configuration. Plusieurs traductions ont également été mises à jour grâce à la communauté Weblate.

### Évolutions fonctionnelles
- **Importation Airtable :** Ajout de la fonctionnalité d'importation de données depuis Airtable, incluant le support des champs de type "multipleLookupValue" et des pièces jointes. [#2137](https://github.com/betagouv/grist-core/issues/2137), [#2119](https://github.com/betagouv/grist-core/issues/2119), [#2120](https://github.com/betagouv/grist-core/issues/2120), [#2111](https://github.com/betagouv/grist-core/issues/2111)
- **Comparaison avec l'original :** Amélioration de la fonctionnalité de comparaison avec la version originale d'un document. [#2068](https://github.com/betagouv/grist-core/issues/2068)
- **Limitation des options de formulaire :** Possibilité de configurer une limite au nombre d'options dans les formulaires. [#2100](https://github.com/betagouv/grist-core/issues/2100)
- **Accès conditionnel :** Ajout d'informations sur les commentaires dans l'accès granulaire. [#15dc0520](https://github.com/betagouv/grist-core/commit/15dc0520)
- **Déclencheurs :** Ajout de la condition de formule aux déclencheurs. [#e48c84f5](https://github.com/betagouv/grist-core/commit/e48c84f5)

### Évolutions techniques
- **OAuth2 :** Correction pour assurer le bon fonctionnement d'OAuth2 sur les sous-domaines autorisés. [#25ea37c8](https://github.com/betagouv/grist-core/commit/25ea37c8)
- **Sécurité :** Amélioration de la cohérence du contrôle d'accès sur les endpoints d'attachements. [#0fbc3bc8](https://github.com/betagouv/grist-core/commit/0fbc3bc8)
- **GVisor :** Limitation du nombre de processus dans GVisor pour améliorer la stabilité. [#392fba9d](https://github.com/betagouv/grist-core/commit/392fba9d)
- **Mise à jour de dépendances :** Mise à jour de `webpack` vers la version 5.104.1 et `lazy-object-proxy` vers la version 1.12.0. [#2099](https://github.com/betagouv/grist-core/issues/2099), [#2105](https://github.com/betagouv/grist-core/issues/2105)
- **Refactoring :** Refactorisation des tests `DocApi.ts` et `DocApi2.ts`. [#bfda58fc](https://github.com/betagouv/grist-core/commit/bfda58fc)
- **Amélioration de l'interface :** Correction des couleurs illisibles en mode sombre pour les bannières. [#42bf3fe8](https://github.com/betagouv/grist-core/commit/42bf3fe8)
- **Correction d'un bug Firefox :** Correction d'un espace de 1px en bas de l'éditeur de cellule dans Firefox. [#b102b038](https://github.com/betagouv/grist-core/commit/b102b038)

### Autres changements
- **Traductions :** Mises à jour des traductions en français, suédois, tchèque, hongrois, arabe et slovaque grâce à la communauté Weblate.
- **Gestion des organisations :** Masquage des organisations personnelles si elles sont désactivées sur le serveur. [#2129](https://github.com/betagouv/grist-core/issues/2129)
- **Création d'organisations :** Ajout de flags pour désactiver la création d'organisations. [#2124](https://github.com/betagouv/grist-core/issues/2124)
- **Version EE :** Mise à jour de la version Enterprise Edition. [#f70c5035](https://github.com/betagouv/grist-core/commit/f70c5035)
