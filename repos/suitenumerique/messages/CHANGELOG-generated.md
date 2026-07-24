## Changelog : messages (30 derniers jours, au 24 juillet 2026)

### Résumé
Les dernières semaines ont été marquées par d'importantes améliorations de la plateforme, notamment l'ajout de notifications push pour iOS, Android et le web, ainsi que la préparation du support mobile avec des applications Capacitor. Des améliorations significatives ont également été apportées à la gestion des emails entrants et sortants, et à la sécurité globale de la plateforme.

### Évolutions fonctionnelles
- Ajout de notifications push pour iOS, Android et le web.
- Possibilité de se connecter en spécifiant un paramètre `next` pour être redirigé vers une page spécifique après l'authentification.
- Affichage du nombre de messages non lus dans le menu déroulant des boîtes de réception.
- Détection des liens texte dans le corps des emails HTML avec un avertissement avant redirection [#744](https://github.com/suitenumerique/messages/issues/744).
- Amélioration de l'interface utilisateur pour l'absence de boîte de réception.
- Amélioration du re-traitement des messages entrants depuis l'interface d'administration.

### Évolutions techniques
- Refonte de l'implémentation MTA-in en Python pur, supprimant la dépendance à Postfix [#692](https://github.com/suitenumerique/messages/issues/692).
- Mise en place d'un système de cache-busting pour les fichiers sources lors de la construction.
- Utilisation de la session pour la transmission du token CSRF au lieu des cookies.
- Configuration du frontend à partir du backend [#734](https://github.com/suitenumerique/messages/issues/734).
- Intégration de la gestion des sessions OIDC pour les applications mobiles.
- Mise en place d'une liste blanche d'hôtes pour contourner les problèmes de SSRF dans les réseaux internes.
- Bootstrap des applications mobiles Capacitor (iOS/Android) partageant la même SPA.
- Mise en place d'une chaîne de mise à jour OTA auto-hébergée pour les applications mobiles.
- Refactorisation des imports pour les retries, le mode continu et l'interface utilisateur de liste [#742](https://github.com/suitenumerique/messages/issues/742).
- Mise à jour de la bibliothèque Keycloak vers la version 26.6.4 (correction de sécurité CERTFR-2026-AVI-0815) [#729](https://github.com/suitenumerique/messages/issues/729).
- Mise à jour du thème Keycloak vers la version 2.3.4 [#732](https://github.com/suitenumerique/messages/issues/732).

### Autres changements
- Amélioration du temps de démarrage de l'environnement de développement avec `make bootstrap`.
- Documentation complète du processus de traitement du spam.
- Suppression de la fonctionnalité `TESTDOMAIN`.
- Correction de l'indentation du bloc relay dans `main.cf` pour résoudre un problème d'authentification SASL.
- Correction d'un problème de saut de ligne dans le compositeur sur Chrome pour Android [#725](https://github.com/suitenumerique/messages/issues/725).
- Correction d'un problème de saut de ligne dans le compositeur sur Safari [#740](https://github.com/suitenumerique/messages/issues/740).
- Correction d'un problème de gestion du nom de fichier des pièces jointes.
- Correction d'un problème de traduction automatique potentielle due à `lang=en` en dur.
- Amélioration de la gestion des erreurs lors du traitement des messages entrants.
- Sauvegarde de l'adresse IP d'origine lors des redémarrages STARTTLS (pymta).
- Ajout d'un en-tête `X-Mailer` aux messages sortants.
- Mise à jour de la configuration du navigateur pour supporter Chrome >= 109 [#750](https://github.com/suitenumerique/messages/issues/750).
- Correction du gestionnaire Outlook Web dans la logique d'extraction de caractères [#754](https://github.com/suitenumerique/messages/issues/754).
- Linting des sous-projets.
- Suppression du composant `react-email`.
