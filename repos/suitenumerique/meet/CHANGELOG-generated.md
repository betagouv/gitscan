## Changelog : meet (30 derniers jours, au 2026-07-03)

### Résumé
Les dernières mises à jour de Meet se concentrent sur l'amélioration de la stabilité, de la sécurité et de l'expérience utilisateur. Des corrections de bugs ont été apportées, notamment concernant la gestion des fichiers S3 et l'intégration avec des outils tiers comme Outlook. De nouvelles fonctionnalités ont été ajoutées, comme l'amélioration de la réduction du bruit et la possibilité de personnaliser l'interface avec des sondages de satisfaction. L'ajout d'un système d'analyse permet également de mieux comprendre l'utilisation de la plateforme.

### Évolutions fonctionnelles
- Ajout d'un système d'analyse configurable (PostHog) pour suivre les événements, notamment la génération de liens de réunion.
- Amélioration de la réduction du bruit grâce à un pipeline audio BBBA.
- Possibilité d'ajouter un formulaire de feedback dans le pied de page de l'application.
- Ajout d'un indicateur de satisfaction optionnel en bas de l'écran.
- Amélioration de l'intégration avec l'add-in Outlook : support de l'internationalisation, lien de feedback, et gestion plus intelligente des liens.
- Possibilité de masquer le bouton de connexion via un paramètre d'URL.
- Possibilité de désactiver le login silencieux via un paramètre d'URL.
- Amélioration de l'accessibilité des effets vidéo et du panneau des paramètres.
- Limitation du nombre de vignettes affichées en mode Picture-in-Picture pour améliorer les performances.
- Mise à jour de l'interface utilisateur pour remplacer "Premium" par "Avancé".

### Évolutions techniques
- Mise à jour de plusieurs dépendances, notamment `ffmpeg`, `posthog-js`, `jose`, `react-i18next`, et des librairies cryptographiques.
- Correction d'un problème de build frontend sur Scalingo.
- Amélioration de la gestion des variables d'environnement.
- Refactorisation de la gestion des clés d'objets S3 pour une meilleure compatibilité.
- Amélioration de la configuration de Content Security Policy (CSP) pour corriger des régressions.
- Mise à jour de l'image Alpine de base.
- Ajout d'un job Kubernetes pour exécuter la commande de fusion des utilisateurs en double.
- Amélioration de la gestion des erreurs et des exceptions dans le backend.
- Ajout d'un fallback pour l'enregistrement des réunions en cas de problème avec les webhooks S3/MinIO.
- Lazy loading de la librairie `@libreaudio/la-call` pour améliorer les performances.

### Autres changements
- Ajout de badges DPG au README.
- Mise à jour de la documentation pour refléter les changements et améliorer la clarté.
- Ajout de Clever Cloud à la liste des fournisseurs SaaS.
- Précision de la traduction française dans la documentation.
- Mise à jour des versions des charts Helm.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout de tests pour la gestion des clés S3 encodées.
- Documentation de la personnalisation du favicon via un volume mount.
- Suppression de l'utilisation de la police par défaut au profit de la police de l'application.
- Correction d'un problème d'affichage du bouton "Ajouter" dans l'add-in Outlook.
- Correction d'un bug empêchant la fermeture de l'agent de métadonnées.
