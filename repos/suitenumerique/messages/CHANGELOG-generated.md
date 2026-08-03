## Changelog : messages (30 derniers jours, au 24 juillet 2026)

### Résumé
Les dernières mises à jour apportent des améliorations significatives à la sécurité, à l'expérience mobile et à la gestion des messages. L'ajout de notifications push, la prise en charge des applications mobiles et l'amélioration de la gestion des spams renforcent la collaboration et la productivité. Des corrections de bugs et des optimisations de performance complètent ces évolutions.

### Évolutions fonctionnelles
- Ajout d'un système de notifications push pour iOS, Android et le web.
- Prise en charge de la création d'applications mobiles (iOS/Android) avec des mises à jour OTA (Over-The-Air).
- Possibilité de détecter les liens texte dans le corps des emails HTML et d'avertir l'utilisateur avant redirection [#744].
- Affichage du nombre de messages non lus dans le menu déroulant des boîtes de réception [#738].
- Amélioration de la gestion des spams avec une documentation complète.
- Possibilité de créer une boîte de réception sans mot de passe lorsque la synchronisation d'identité est désactivée [#707].
- Amélioration du re-traitement des messages entrants depuis l'interface d'administration.
- Ajout de webhooks et de postmarks pour les messages entrants.

### Évolutions techniques
- Refonte de l'architecture MTA-in en Python pur pour supprimer la dépendance à Postfix [#692].
- Migration du frontend vers Vite et TanStack Router, abandonnant Next.js [#675].
- Utilisation d'une nouvelle bibliothèque `jmap-email` pour l'analyse et la composition des emails [#700].
- Amélioration de la sécurité avec l'ajout d'une liste blanche d'hôtes pour contourner les problèmes SSRF (Server-Side Request Forgery) dans les réseaux internes.
- Mise à jour de Keycloak pour corriger une vulnérabilité de sécurité (CERTFR-2026-AVI-0815) [#729].
- Livraison du token CSRF via la session au lieu d'un cookie.
- Amélioration du temps de configuration avec `make bootstrap` et de l'expérience développeur.

### Autres changements
- Correction de bugs liés à l'indentation des blocs relay, qui empêchait l'authentification SASL [#733].
- Correction d'un bug dans le gestionnaire Outlook Web concernant le décodage des caractères [#754].
- Correction d'un problème de saut de ligne prématuré dans le compositeur sur Safari [#740] et Chrome pour Android [#725].
- Suppression de la fonctionnalité `TESTDOMAIN`, remplacée par les domaines d'auto-adhésion.
- Suppression du composant `react-email` pour le rendu des messages sortants.
- Configuration du frontend à partir du backend [#734].
- Réinitialisation de la recherche lors du changement de boîte de réception [#743].
- Amélioration de l'expérience utilisateur avec un message plus clair en cas d'absence de boîte de réception.
- Ajout d'un en-tête `X-Mailer` aux messages sortants.
- Ajout d'un cache-busting de la version source dans le build.
- Linting des sous-projets.
- Correction de l'affichage des caractères spéciaux.
- Amélioration de l'accessibilité de la navigation des threads.
- Correction d'un problème de saut de ligne dans le compositeur sur Chrome pour Android.
