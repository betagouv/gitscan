## Changelog : messages (30 derniers jours, au 20 juillet 2026)

### Résumé
Les dernières mises à jour de Messages se concentrent sur l'amélioration de la sécurité, la correction de bugs et l'optimisation de l'expérience utilisateur, notamment dans la gestion des emails et l'interface utilisateur. Une refonte majeure du MTA-in a été effectuée pour éliminer une dépendance à Postfix.

### Évolutions fonctionnelles
- Détection des liens hypertextes dans le corps des emails HTML : un avertissement est affiché à l'utilisateur avant la redirection. [#744](https://github.com/suitenumerique/messages/issues/744)
- Affichage du nombre de messages non lus dans le menu déroulant des boîtes de réception.
- Correction de problèmes d'affichage des sauts de ligne dans le compositeur d'emails sur Chrome Android. [#725](https://github.com/suitenumerique/messages/issues/725)
- Correction du problème de pré-rupture de ligne dans le compositeur. [#740](https://github.com/suitenumerique/messages/issues/740)
- Amélioration du re-traitement des messages entrants depuis l'administration.
- Sauvegarde de l'adresse IP d'origine lors des redémarrages STARTTLS.
- Ajout de webhooks, de balises de message et de corrections anti-spam.
- Correction du nom de fichier des pièces jointes.
- Correction de l'indentation du bloc relay dans main.cf. [#733](https://github.com/suitenumerique/messages/issues/733)
- Réinitialisation de la recherche lors du changement de boîte de réception. [#743](https://github.com/suitenumerique/messages/issues/743)

### Évolutions techniques
- Refonte complète du MTA-in en Python pur pour supprimer la dépendance à Postfix. [#692](https://github.com/suitenumerique/messages/issues/692)
- Configuration du frontend à partir du backend. [#734](https://github.com/suitenumerique/messages/issues/734)
- Utilisation de la méthode intégrée pour générer l'ID des messages. [#730](https://github.com/suitenumerique/messages/issues/730)
- Ajout d'une liste blanche d'hôtes pour contourner les problèmes SSRF dans les réseaux internes.
- Ajout de l'en-tête X-Mailer aux emails sortants.
- Mise à jour de la bibliothèque django-lasuite vers la version 0.0.27.
- Mise à jour de la bibliothèque Keycloak vers les versions 26.6.3 et 26.6.4. [#718](https://github.com/suitenumerique/messages/issues/718), [#729](https://github.com/suitenumerique/messages/issues/729), [#732](https://github.com/suitenumerique/messages/issues/732)
- Suppression du composant react-email.
- Linting des sous-projets.

### Autres changements
- Configuration du navigateur pour supporter Chrome >= 109. [#750](https://github.com/suitenumerique/messages/issues/750)
- Correction d'un problème de gestion du handler Outlook Web dans la logique d'extraction des URL. [#754](https://github.com/suitenumerique/messages/issues/754)
