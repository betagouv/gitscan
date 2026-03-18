## Changelog : grist-core (30 derniers jours, au 03 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à l'importation depuis Airtable, notamment le support des pièces jointes et des champs de type "multiple lookup". Des corrections ont été apportées pour améliorer la stabilité et l'expérience utilisateur, notamment concernant l'affichage des couleurs en mode sombre, la comparaison de documents et la gestion des organisations. Des options de configuration supplémentaires ont été ajoutées, comme la limitation du nombre d'options dans les formulaires.

### Évolutions fonctionnelles
- **Importation Airtable :** Ajout du support des pièces jointes et des champs de type "multiple lookup" lors de l'importation de données depuis Airtable. [#2111](https://github.com/betagouv/grist-core/issues/2111), [#2119](https://github.com/betagouv/grist-core/issues/2119), [#2120](https://github.com/betagouv/grist-core/issues/2120)
- **Comparaison de documents :** Amélioration de la fonctionnalité de comparaison avec le document original. [#2068](https://github.com/betagouv/grist-core/issues/2068)
- **Gestion des organisations :** Possibilité de désactiver la création d'organisations. [#2124](https://github.com/betagouv/grist-core/issues/2124)
- **Options de formulaire :** Ajout d'une limite configurable au nombre d'options dans les formulaires. [#2100](https://github.com/betagouv/grist-core/issues/2100)
- **Accès aux pièces jointes :** Amélioration de la cohérence de l'accès aux pièces jointes via l'API. [#2116](https://github.com/betagouv/grist-core/issues/2116)
- **Importation depuis Desktop :** Extraction de la méthode d'importation `.grist` pour une utilisation dans l'application Desktop. [#2128](https://github.com/betagouv/grist-core/issues/2128)
- **Authentification OAuth2 :** Correction pour assurer le bon fonctionnement d'OAuth2 sur les sous-domaines autorisés. [#25ea37c8](https://github.com/betagouv/grist-core/commit/25ea37c8)
- **Affichage :** Correction d'un problème d'affichage des couleurs en mode sombre pour les bannières. [#2138](https://github.com/betagouv/grist-core/issues/2138)
- **Notifications :** Masquage de l'icône de cloche lorsque la connexion est normale. [#ef087643](https://github.com/betagouv/grist-core/commit/ef087643)

### Évolutions techniques
- **OAuth2 :** Déplacement des tokens OAuth2 vers l'objet utilisateur de session. [#f81a4262](https://github.com/betagouv/grist-core/commit/f81a4262)
- **GVisor :** Limitation du nombre de processus dans GVisor pour améliorer la stabilité. [#2106](https://github.com/betagouv/grist-core/issues/2106)
- **Tests :** Suppression d'un test GVisor qui échoue. [#90789095](https://github.com/betagouv/grist-core/commit/90789095)
- **Refactoring :** Refactorisation des tests DocApi.ts et DocApi2.ts. [#2092](https://github.com/betagouv/grist-core/issues/2092)
- **Corrections :** Correction d'un espace de 1px en bas de l'éditeur de cellule dans Firefox. [#b102b038](https://github.com/betagouv/grist-core/commit/b102b038)

### Autres changements
- **Traduction :** Mises à jour des traductions en français, suédois, tchèque, slovaque et arabe.
- **Accessibilité :** Ajout d'informations manquantes sur les commentaires pour l'accès granulaire. [#15dc0520](https://github.com/betagouv/grist-core/commit/15dc0520)
- **Version :** Publication de la version v1.7.11. [#2133](https://github.com/betagouv/grist-core/issues/2133)
- **Comportement :** Correction d'un bug concernant le nombre de suggestions sur un document copié et auto-forké. [#2117](https://github.com/betagouv/grist-core/issues/2117)
- **Organisation :** Masquage des organisations personnelles si elles sont désactivées sur le serveur. [#2129](https://github.com/betagouv/grist-core/issues/2129)
- **Normalisation :** Normalisation de l'adresse e-mail de l'utilisateur administrateur lors des comparaisons. [#2115](https://github.com/betagouv/grist-core/issues/2115)
