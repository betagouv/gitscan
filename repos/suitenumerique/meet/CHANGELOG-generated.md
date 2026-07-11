## Changelog : meet (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité, l'expérience utilisateur et l'ajout de fonctionnalités d'analyse. Des corrections de bugs ont été apportées pour améliorer la fiabilité, notamment concernant les enregistrements et l'affichage des informations. L'expérience utilisateur a été améliorée avec des ajustements de l'interface, notamment dans la disposition des vignettes en mode image dans l'image et l'ajout d'indicateurs visuels. Enfin, un système d'analyse a été introduit pour mieux comprendre l'utilisation de la plateforme et optimiser les performances.

### Évolutions fonctionnelles
- Ajout d'un gradient de couleur pour les participants lorsque leur caméra est désactivée [#1490](https://github.com/suitenumerique/meet/issues/1490).
- Possibilité de forcer l'affichage du nom d'utilisateur SSO pour les utilisateurs authentifiés.
- Amélioration de la disposition des vignettes en mode image dans l'image, avec priorisation du partage d'écran et pagination.
- Ajout d'un indicateur visuel pour le partage d'écran en mode image dans l'image.
- Possibilité de rechercher les enregistrements par adresse email du propriétaire.
- Ajout d'un formulaire de feedback dans le footer de l'addon.
- Amélioration de l'accessibilité des effets vidéo.
- Possibilité de générer un lien de réunion directement depuis l'addon.

### Évolutions techniques
- Mise à jour de plusieurs dépendances (LiveKit, PostHog, React Query, etc.) pour bénéficier des dernières corrections et améliorations.
- Refactor de la gestion du nom d'utilisateur pour une meilleure cohérence.
- Implémentation d'un système d'analyse configurable basé sur PostHog.
- Refactor de l'authentification Bearer.
- Suppression du support de la version 1 du service de résumé.
- Amélioration de la gestion des variables d'environnement.
- Mise à jour de l'image de construction du frontend (Node 22).
- Mise à jour de l'image Docker pour Nginx.
- Correction d'un bug empêchant l'affichage correct des styles en ligne (CSP).
- Correction d'un bug lié à la récupération de l'ID client depuis la requête.
- Amélioration de la gestion des erreurs et ajout d'instrumentation Sentry pour les agents.
- Mise à jour de l'image de base Alpine pour le service de résumé.
- Mise à jour de ffmpeg.

### Autres changements
- Ajout de documentation pour le rebrand du favicon via un volume mount.
- Ajout de Clever Cloud à la liste des fournisseurs SaaS.
- Clarification des directives de contribution.
- Précision de la traduction française dans la documentation.
- Mise à jour du changelog.
- Suppression de la configuration obsolète `SUMMARY_SERVICE_VERSION=1`.
- Ajout d'une note concernant la suppression de la version v1 du service de résumé.
- Bump de la version du chart Helm.
- Correction d'un bug empêchant le bon fonctionnement du build frontend sur Scalingo.
- Correction d'un bug lié à la déduplication des emails.
- Correction d'un bug lié au crash du panneau d'informations pour les salles non enregistrées.
- Correction d'un bug lié à la normalisation des clés S3.
- Ajout de tests pour la normalisation des clés S3.
- Correction d'un bug lié à la gestion des utilisateurs provisionnés en externe.
- Correction d'un bug lié à l'affichage du bouton "Mute Everyone".
- Mise à jour de la configuration Tilt pour la gestion des noms complets et courts.
- Correction d'un bug lié à l'affichage du bouton d'arrêt en mode plein écran.
- Correction d'un bug lié à l'audio mono lors de la réduction du bruit.
- Correction d'un bug lié à l'affichage du bouton d'ajout de lien dans l'addon.
- Ajout de commentaires et de documentation pour améliorer la lisibilité du code.
