## Changelog : meet (30 derniers jours, au 6 juillet 2026)

### Résumé
Les dernières mises à jour de Meet se concentrent sur l'amélioration de la stabilité, l'ajout de fonctionnalités pour le résumé vocal (summary), l'amélioration de l'accessibilité, et l'intégration d'un système d'analyse pour mieux comprendre l'utilisation de la plateforme. Des corrections de bugs et des mises à jour de dépendances ont également été effectuées.

### Évolutions fonctionnelles
- Ajout d'un système de sondage de satisfaction optionnel en bas de page des résumés vocaux.
- Amélioration de la gestion des fichiers multimédias avec des flux audio/vidéo corrompus dans les résumés.
- Possibilité de masquer le bouton de connexion via un paramètre d'URL.
- Amélioration de la gestion des liens de réunion dans l'extension Outlook (ajout, suppression, positionnement).
- Ajout d'un lien vers un formulaire de feedback dans l'extension Outlook.
- Amélioration de la réduction du bruit avec un pipeline audio BBBA.
- Amélioration de l'accessibilité des effets vidéo (labels ARIA, structure).
- Limitation et pagination des vignettes dans la vue PiP (Picture-in-Picture).
- Prise en charge de la génération de liens de réunion avec un domaine dédié pour l'API des flags de fonctionnalités.
- Support des fichiers avec des clés S3 encodées.

### Évolutions techniques
- Refactorisation de l'authentification Bearer Auth.
- Mise à jour de l'image de base Alpine et de FFmpeg.
- Mise à jour de plusieurs dépendances (Posthog, joserfc, react-i18next, etc.) pour corriger des vulnérabilités et améliorer la stabilité.
- Amélioration de la gestion des variables d'environnement.
- Ajout d'un système d'analyse configurable basé sur PostHog (suivi de la génération de liens de réunion).
- Amélioration de la gestion des erreurs et des logs.
- Optimisation de la gestion des ressources pour les grandes réunions (mute par défaut, désactivation du son de notification).
- Lazy loading de `@libreaudio/la-call` pour améliorer les performances.
- Correction d'une régression CSP (Content Security Policy) qui bloquait les styles en ligne et ProConnect.
- Mise à jour des packages React Aria et React Stately.

### Autres changements
- Documentation : Ajout d'informations sur le rebranding du favicon via un volume mount.
- Documentation : Ajout de Clever Cloud comme fournisseur SaaS de La Suite Meet.
- Documentation : Clarification des directives de contribution.
- Documentation : Ajout d'email.eu à la liste des instances connues.
- Nettoyage du code : Suppression du code lié à l'ancienne version 1 de l'API de résumé.
- Correction de tests et de la configuration du Makefile.
- Amélioration de la configuration Helm pour les jobs cron.
- Ajout de badges DPG au README.
- Correction de l'affichage des labels ARIA pour les backgrounds personnalisés.
- Correction de bugs mineurs et améliorations de la qualité du code.
