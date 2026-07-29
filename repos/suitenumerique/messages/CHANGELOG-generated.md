## Changelog : messages (30 derniers jours, au 24 juillet 2026)

### Résumé
Les dernières mises à jour apportent des améliorations significatives à la sécurité, à l'expérience mobile et à la gestion des messages. L'ajout de notifications push, la prise en charge des applications mobiles et la refonte du MTA-in sont des évolutions majeures. Des corrections de bugs et des améliorations de l'interface utilisateur complètent cette version.

### Évolutions fonctionnelles
- Ajout d'un système de notifications push pour iOS, Android et le web.
- Prise en charge de la création d'applications mobiles (iOS/Android) via Capacitor, partageant la même base de code que l'application web.
- Mise en place d'un mécanisme de mise à jour OTA (Over-The-Air) pour les applications mobiles auto-hébergées.
- Possibilité d'afficher le nombre de messages non lus dans le menu déroulant des boîtes de réception.
- Détection des liens texte dans le corps des emails HTML, avec un avertissement avant redirection [#744](https://github.com/suitenumerique/messages/issues/744).
- Ajout d'un paramètre `next` à la connexion pour restaurer la route demandée après authentification.
- Amélioration de la vue "pas de boîte de réception".
- Amélioration du re-traitement des messages entrants depuis l'administration.
- Correction du problème de saut de ligne prématuré dans le compositeur sur Safari [#740](https://github.com/suitenumerique/messages/issues/740).
- Correction du problème de saut de ligne dans le compositeur sur Chrome pour Android [#725](https://github.com/suitenumerique/messages/issues/725).

### Évolutions techniques
- Refonte complète du MTA-in en Python pur pour supprimer la dépendance à Postfix [#692](https://github.com/suitenumerique/messages/issues/692).
- Refactorisation des imports pour les retries, le mode continu, l'UI de liste et le stockage direct [#742](https://github.com/suitenumerique/messages/issues/742).
- Utilisation de la session pour la transmission du token CSRF au lieu d'un cookie.
- Configuration du frontend désormais gérée depuis le backend [#734](https://github.com/suitenumerique/messages/issues/734).
- Mise à jour de Keycloak vers la version 26.6.4 (correction de sécurité CERTFR-2026-AVI-0815) [#729](https://github.com/suitenumerique/messages/issues/729).
- Mise à jour du thème Keycloak vers la version 2.3.4 [#732](https://github.com/suitenumerique/messages/issues/732).
- Mise en place d'une liste blanche d'hôtes pour contourner les problèmes de SSRF dans les réseaux internes.
- Amélioration du temps de configuration de "make bootstrap" et de l'expérience de développement globale.
- Ajout d'un en-tête `X-Mailer` aux messages sortants.
- Mise en place d'un mécanisme de cache-busting pour la version source dans le build.
- Configuration de `browserlist` et ajout d'un plugin legacy pour supporter Chrome >= 109 [#750](https://github.com/suitenumerique/messages/issues/750).

### Autres changements
- Documentation complète sur le traitement du spam.
- Suppression de la fonctionnalité `TESTDOMAIN`, remplacée par les domaines d'auto-adhésion.
- Suppression du composant `react-email` pour le rendu des messages sortants.
- Correction de l'indentation du bloc relay qui cassait l'authentification SASL dans MTA out [#733](https://github.com/suitenumerique/messages/issues/733).
- Correction du gestionnaire Outlook Web dans la logique d'unquote [#754](https://github.com/suitenumerique/messages/issues/754).
- Correction de la génération de l'ID de message avec la méthode intégrée `email.utils.make_msgid` [#730](https://github.com/suitenumerique/messages/issues/730).
- Linting des sous-projets.
- Mapping de la valeur ACR eidas1 dans le realm de développement.
- Ajout de la gestion de session OIDC pour mobile.
