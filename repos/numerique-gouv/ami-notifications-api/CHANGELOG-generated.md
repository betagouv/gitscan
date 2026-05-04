## Changelog : ami-notifications-api (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur de l'application mobile, notamment avec l'ajout de la gestion des zones géographiques pour l'agenda et des corrections concernant l'affichage et le comportement de l'interface. Des améliorations techniques ont également été apportées, notamment pour la réplication de la base de données et la gestion des logs.

### Évolutions fonctionnelles
- **Agenda et zones géographiques :** Ajout de la gestion des zones géographiques (A, B, C) pour l'affichage des vacances scolaires dans l'agenda. L'utilisateur peut désormais définir ses préférences de zones et d'adresses. [#508](https://github.com/numerique-gouv/ami-notifications-api/issues/508)
- **Notifications planifiées :** Amélioration de l'envoi des notifications planifiées avec l'ajout de l'URL interne. [#779](https://github.com/numerique-gouv/ami-notifications-api/issues/779)
- **Confirmation de déconnexion :** Ajout d'une modal de confirmation lors de la déconnexion de l'utilisateur. [#753](https://github.com/numerique-gouv/ami-notifications-api/issues/753)
- **Améliorations de l'interface utilisateur :**
    - Correction du centrage vertical du bouton FranceConnect. [#515](https://github.com/numerique-gouv/ami-notifications-api/issues/515)
    - Amélioration du défilement et de l'affichage des champs d'adresse. [#568](https://github.com/numerique-gouv/ami-notifications-api/issues/568)
    - Correction des paddings sur la page d'accueil. [#764](https://github.com/numerique-gouv/ami-notifications-api/issues/764)
- **Gestion des partenaires :**  Correction pour empêcher les identifiants de partenaires nuls ou vides. [#798](https://github.com/numerique-gouv/ami-notifications-api/issues/798)

### Évolutions techniques
- **Réplication de la base de données :** Amélioration des tests de réplication de la base de données et ajout d'une commande Django pour répliquer les utilisateurs. [#791](https://github.com/numerique-gouv/ami-notifications-api/issues/791)
- **Logging :** Ajout des headers dans les logs des erreurs d'API Part.
- **Refactoring :** Refactorisation de la méthode de réplication et ajout de tests d'interaction avec la base de données.
- **Cache :** Ajout de cache pour les requêtes des vacances scolaires.
- **API :** Déplacement des endpoints agenda et follow-p derrière `/api/v1`. [#762](https://github.com/numerique-gouv/ami-notifications-api/issues/762)
- **Commandes planifiées :** Simplification des commandes et des tests pour les notifications planifiées. [#786](https://github.com/numerique-gouv/ami-notifications-api/issues/786)
- **Suppression de django-admin :** Suppression de l'utilisation de `django-admin` et ajout d'une commande pour donner le rôle d'administrateur à un agent. [#795](https://github.com/numerique-gouv/ami-notifications-api/issues/795)

### Autres changements
- **Documentation :** Mise à jour de la documentation CONTRIBUTING.
- **Linting :** Corrections de linting pour l'application front-end (warnings noNonNullAssertion, noExplicitAny, noDescendingSpecificity, useTemplate, noImportantStyles). [#792](https://github.com/numerique-gouv/ami-notifications-api/issues/792)
- **Correction de l'URL SECTOR_IDENTIFIER_URL :** Correction des usages de l'URL SECTOR_IDENTIFIER_URL. [#767](https://github.com/numerique-gouv/ami-notifications-api/issues/767)
- **Correction de bugs mineurs :** Diverses corrections de bugs et améliorations de la qualité du code.
