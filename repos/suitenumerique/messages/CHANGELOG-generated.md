## Changelog : messages (30 derniers jours, au 9 juillet 2026)

### Résumé
Les dernières mises à jour apportent des améliorations significatives à la sécurité, à la gestion des emails entrants et sortants, ainsi qu'à l'expérience utilisateur du frontend. Des corrections de bugs ont été implémentées pour améliorer la stabilité et la fiabilité de la plateforme.

### Évolutions fonctionnelles
- Ajout d'une alerte à l'utilisateur lorsqu'un lien est détecté dans le corps HTML d'un email, avant la redirection. [#744](https://github.com/suitenumerique/messages/issues/744)
- Affichage du nombre d'emails non lus dans le menu déroulant des boîtes de réception.
- Correction de problèmes d'affichage des retours à la ligne dans le compositeur d'emails sur les appareils Android. [#725](https://github.com/suitenumerique/messages/issues/725)
- Correction d'un problème de sur-développement de ligne dans le compositeur sur Chrome Android. [#740](https://github.com/suitenumerique/messages/issues/740)
- Correction du comportement de réinitialisation de la recherche lors du changement de boîte de réception. [#743](https://github.com/suitenumerique/messages/issues/743)

### Évolutions techniques
- Refonte complète du MTA-in en Python pur, supprimant la dépendance à Postfix. [#692](https://github.com/suitenumerique/messages/issues/692)
- Ajout d'une liste blanche d'hôtes pour contourner les problèmes de SSRF dans les réseaux internes.
- Utilisation de la méthode intégrée pour générer l'ID des messages. [#730](https://github.com/suitenumerique/messages/issues/730)
- Ajout de l'en-tête X-Mailer aux emails sortants.
- Configuration du frontend à partir du backend. [#734](https://github.com/suitenumerique/messages/issues/734)
- Mise à jour de la bibliothèque `django-lasuite` vers la version 0.0.27.
- Mise à jour de la bibliothèque `dompurify` vers la dernière version.
- Correction de l'ajout du header `To` aux emails sortants qui en étaient dépourvus. [#712](https://github.com/suitenumerique/messages/issues/712)
- Correction d'un problème de langue codée en dur qui pouvait déclencher une traduction automatique.
- Suppression du composant `react-email`.

### Autres changements
- Amélioration du re-traitement des messages entrants depuis l'administration.
- Sauvegarde de l'adresse IP d'origine lors des redémarrages STARTTLS dans Pymta.
- Ajout de webhooks, de balises de message et de corrections anti-spam.
- Linting des sous-projets.
- Mise à jour de Keycloak vers les versions 26.6.3 et 26.6.4. [#718](https://github.com/suitenumerique/messages/issues/718), [#729](https://github.com/suitenumerique/messages/issues/729), [#732](https://github.com/suitenumerique/messages/issues/732)
- Correction de l'indentation du bloc relay dans main.cf.j2. [#733](https://github.com/suitenumerique/messages/issues/733)
