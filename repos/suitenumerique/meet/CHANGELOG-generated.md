## Changelog : meet (30 derniers jours, au 8 juillet 2026)

### Résumé
Cette version apporte des améliorations à la gestion des enregistrements, notamment en cas de problèmes avec les webhooks S3, et introduit un système d'analyse plus flexible basé sur des flags de fonctionnalités. Des corrections de bugs et des mises à jour de dépendances ont également été intégrées pour améliorer la stabilité et la sécurité de la plateforme. L'expérience utilisateur est améliorée avec des ajustements d'accessibilité et des corrections concernant le partage d'écran en mode image dans l'image.

### Évolutions fonctionnelles
- Ajout d'une gestion améliorée des enregistrements, avec une solution de repli pour les événements LiveKit `egress_ended` en cas de problèmes avec les webhooks S3.
- Implémentation d'un système d'analyse flexible basé sur des flags de fonctionnalités, permettant d'activer ou de désactiver le suivi d'événements spécifiques.
- Possibilité de masquer le bouton de connexion via un paramètre d'URL.
- Ajout d'un formulaire de feedback dans le pied de page de l'addon.
- Amélioration de la gestion des liens de réunion dans l'addon : insertion au curseur, suppression facile, et affichage d'un message de fallback si un lien existe déjà.
- Ajout d'un indicateur "Bêta" avec un style cohérent pour l'addon.
- Ajout d'un sondage de satisfaction optionnel à la fin des réunions.
- Amélioration de l'accessibilité des effets vidéo et des boutons de gestion du son.
- Amélioration du partage d'écran en mode image dans l'image (PiP) : activation du bouton de partage d'écran et interaction améliorée.
- Limitation du nombre de vignettes affichées en mode PiP et pagination pour une meilleure expérience utilisateur.

### Évolutions techniques
- Mise à jour de plusieurs dépendances : `livekit-client`, `posthog-js`, `@tanstack/react-query`, `ffmpeg`, `jose`, `i18next`, `@pandacss/preset-panda`.
- Refactorisation du backend d'analyse pour utiliser une classe abstraite au lieu du protocole.
- Mise à jour de l'image de base Alpine pour les builds.
- Amélioration de la sécurité avec la mise à jour de `jose` pour corriger une vulnérabilité (CVE-2026-49852).
- Utilisation de Node 22 pour les builds frontend.
- Mise à jour de l'image Docker nginx.
- Optimisation du chargement de `@libreaudio/la-call` via un import dynamique.
- Amélioration de la configuration CSP pour corriger une régression.
- Refactorisation de l'authentification Bearer.
- Ajout d'une configuration nginx paramétrable via un volume.
- Suppression du code lié à l'ancienne version de l'API de résumé (v1).
- Ajout d'instrumentation Sentry pour les agents.
- Mise à jour de Python à la version 3.14 slim pour les agents.

### Autres changements
- Correction de la déduplication des emails (insensible à la casse) dans la commande de fusion.
- Correction d'un bug empêchant l'exécution des tests avec des arguments.
- Correction d'un problème d'échec de build frontend sur Scalingo.
- Ajout de documentation pour la personnalisation du favicon via un volume mount.
- Ajout de Clever Cloud à la liste des fournisseurs SaaS.
- Clarification des directives de contribution.
- Précision de la traduction française dans la documentation.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Normalisation des clés d'objets S3 pour la compatibilité avec les notifications.
- Ajout de tests pour la couverture des clés S3 encodées.
- Ajout de docstrings aux parsers.
- Correction d'un bug lié à la récupération du `client_id` depuis la requête.
- Installation du SDK PostHog dans le backend.
- Ajout d'un suivi des événements de génération de liens de réunion.
- Mise à jour de la liste des instances connues dans la documentation.
- Correction d'un problème d'audio mono lors de la réduction du bruit.
- Correction de l'affichage du bouton "Ajouter" dans l'addon.
- Fixation des dépendances de l'addon à leurs versions actuelles.
- Ajout de la langue française à l'addon.
- Correction d'un bug dans le Makefile.
- Correction d'un bug lié à la vérification de l'activation du collecteur d'agents metadata.
- Correction d'un bug lié au chargement des styles en ligne.
- Correction d'un bug lié à l'absence de `default-src` dans la configuration CSP.
