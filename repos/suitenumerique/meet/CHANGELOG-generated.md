## Changelog : meet (30 derniers jours)

### Résumé
Les dernières mises à jour de Meet se concentrent sur l'amélioration de la sécurité, de l'accessibilité et de la performance. De nouvelles fonctionnalités comme le chargement de fichiers ont été ajoutées, tandis que des corrections de bugs et des optimisations ont été apportées pour une meilleure expérience utilisateur. L'infrastructure a également été renforcée avec des mises à jour de sécurité et des améliorations de la configuration.

### Évolutions fonctionnelles
- Ajout de la possibilité de télécharger les enregistrements même avec un statut "échec d'arrêt" [#1129](https://github.com/suitenumerique/meet/issues/1129).
- Ajout d'une fonctionnalité de chargement de fichiers, désactivée par défaut avec une limite de nombre configurable [#1141](https://github.com/suitenumerique/meet/issues/1141).
- Ajout d'un lien vers l'application Windows web dans l'interface.
- Ajout d'un raccourci clavier pour ouvrir les paramètres (Ctrl+Shift+/).
- Possibilité d'afficher le statut actif/inactif d'une application dans l'interface d'administration.

### Évolutions techniques
- Renforcement de la validation des entrées API pour améliorer la sécurité.
- Mise à jour de plusieurs dépendances frontend (Rollup, @hono/node-server, minimatch, undici, prettier, tanstack, panda-related, i18next, vite, livekit).
- Passage de l'application principale Python à UV.
- Amélioration de la stabilité du stack Tilt.
- Configuration de Celery avec une file d'attente dédiée.
- Mise à jour de la configuration Helm pour inclure Celery et l'image de fond personnalisée.
- Utilisation d'une image de base Alpine pour améliorer la sécurité.
- Mise à jour de la version de Django (avec correctif de sécurité).
- Amélioration de la configuration CI/CD (permissions Docker Hub, actions de revue de sécurité Claude).
- Refactorisation de la gestion des fichiers téléchargés (regex, format des clés).
- Amélioration de la gestion du throttling dans le lobby (utilisation de l'ID participant).
- Suppression de pip des images de production et agents pour renforcer la sécurité.
- Mise à jour de protobuf pour corriger une vulnérabilité.

### Autres changements
- Améliorations de l'accessibilité :
    - Annonce de l'état du microphone/caméra aux lecteurs d'écran lors de l'utilisation des raccourcis.
    - Amélioration de la structure sémantique et des étiquettes ARIA pour les liens d'aide.
    - Amélioration de l'accessibilité du chat pour les lecteurs d'écran.
    - Amélioration de l'accessibilité du carrousel.
    - Ajout d'un lien de contournement pour la navigation au clavier.
    - Amélioration de l'accessibilité de la boîte de dialogue de connexion.
    - Ajout de la possibilité de modifier la taille du texte des sous-titres.
- Corrections de la documentation et des commentaires.
- Amélioration des traductions allemandes.
- Corrections de bugs mineurs dans l'interface utilisateur (overflow, raccourcis, focus).
- Corrections de l'organisation du changelog.
- Ajout de tests unitaires.
- Suppression de références à ProConnect dans l'interface utilisateur.
- Amélioration de la configuration de Tilt pour l'environnement de développement.
- Correction de problèmes liés aux caractères spéciaux dans le Makefile.
- Mise à jour de la configuration Renovate.
- Suppression de curl de l'image de production frontend.
