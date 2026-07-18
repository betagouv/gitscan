## Changelog : messages (30 derniers jours, au 9 juillet 2026)

### Résumé
Les dernières mises à jour de Messages se concentrent sur l'amélioration de la sécurité, la correction de bugs et l'amélioration de l'expérience utilisateur, notamment en matière de gestion des liens dans les emails, de configuration du frontend et de gestion des boîtes de réception. Une refonte importante de l'infrastructure MTA-in a été réalisée pour supprimer une dépendance à Postfix.

### Évolutions fonctionnelles
- Le frontend détecte désormais les liens dans le corps HTML des emails et avertit l'utilisateur avant de le rediriger. [#744](https://github.com/suitenumerique/messages/issues/744)
- Le nombre d'emails non lus est maintenant affiché dans le menu déroulant des boîtes de réception.
- Correction d'un problème d'espacement des lignes dans le compositeur d'emails sur Chrome Android. [#740](https://github.com/suitenumerique/messages/issues/740)
- Correction d'un problème de saut de ligne dans le compositeur. [#725](https://github.com/suitenumerique/messages/issues/725)
- Amélioration du re-traitement des messages entrants depuis l'administration.
- Ajout de webhooks, de postmarks de messages et de corrections anti-spam pour les messages entrants.
- Ajout d'une allowlist d'hôtes pour contourner les problèmes SSRF dans les réseaux internes.

### Évolutions techniques
- Suppression de la dépendance à Postfix pour le MTA-in, qui a été réécrit en Python pur. [#692](https://github.com/suitenumerique/messages/issues/692)
- La configuration du frontend est désormais récupérée depuis le backend. [#734](https://github.com/suitenumerique/messages/issues/734)
- Utilisation de la méthode intégrée pour générer l'ID des messages. [#730](https://github.com/suitenumerique/messages/issues/730)
- Ajout d'un header `X-Mailer` aux emails sortants.
- Suppression du composant `react-email`.
- Correction d'une indentation incorrecte dans le fichier `main.cf.j2` de MTA-out. [#733](https://github.com/suitenumerique/messages/issues/733)
- Mise à jour de la bibliothèque `django-lasuite` vers la version 0.0.27.
- Mise à jour de Keycloak vers les versions 26.6.3 et 26.6.4. [#718](https://github.com/suitenumerique/messages/issues/718), [#729](https://github.com/suitenumerique/messages/issues/729), [#732](https://github.com/suitenumerique/messages/issues/732)
- Correction d'un problème de langue codée en dur qui pouvait déclencher une traduction automatique.
- Linting des sous-projets.

### Autres changements
- Réinitialisation de la recherche lors du changement de boîte de réception. [#743](https://github.com/suitenumerique/messages/issues/743)
- Correction d'un problème de sélection non interactive des cases à cocher dans les éléments de thread. [#714](https://github.com/suitenumerique/messages/issues/714)
- Publication de la version 0.8.0. [#715](https://github.com/suitenumerique/messages/issues/715)
