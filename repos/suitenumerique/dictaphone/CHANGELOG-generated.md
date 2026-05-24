## Changelog : dictaphone (30 derniers jours, au 2026-05-22)

### Résumé
Cette version apporte des améliorations significatives à l'expérience d'enregistrement et de gestion des transcriptions, notamment sur l'application mobile. De nouvelles fonctionnalités comme l'enregistrement hors ligne, la reprise d'enregistrement en cas de perte de connexion, et la possibilité de regénérer les transcriptions ont été ajoutées. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été implémentées pour une meilleure stabilité et ergonomie.

### Évolutions fonctionnelles
- Ajout de la possibilité de regénérer une transcription depuis l'interface web et mobile. [#2345](https://github.com/suitenumerique/dictaphone/issues/2345)
- Implémentation de l'enregistrement hors ligne sur l'application mobile, avec sauvegarde locale des enregistrements.
- Amélioration de la gestion des erreurs et ajout d'une fonctionnalité de reprise automatique de l'enregistrement en cas de perte de connexion ou de problèmes de stockage.
- Ajout d'une indication visuelle du niveau sonore pendant l'enregistrement.
- Possibilité de sélectionner directement le texte transcrit.
- Ajout d'un lien vers la documentation dans l'application mobile.
- Ajout d'un bouton d'aide et de téléchargement de l'application mobile sur l'interface web.
- Amélioration de l'accessibilité de l'application web.
- Ajout d'un indicateur de progression lors du téléchargement des enregistrements sur l'application mobile.
- Ajout d'une option pour n'autoriser l'upload que via Wifi sur l'application mobile.
- Ajout d'un écran d'information avec un lien vers la documentation et la possibilité de supprimer son compte sur l'application mobile.
- Amélioration de l'expérience utilisateur lors de la réinitialisation du mot de passe sur l'application mobile.

### Évolutions techniques
- Mise à jour des dépendances backend pour renforcer la sécurité.
- Amélioration de la robustesse du système d'authentification avec JWT et PKCE sur l'application mobile.
- Refactorisation du code frontend pour améliorer les performances et la maintenabilité.
- Ajout d'un script pour automatiser la création des releases pour l'application mobile.
- Ajout d'une commande pour nettoyer les fichiers temporaires et supprimés.
- Amélioration de la gestion des erreurs et des logs.
- Optimisation de la détection des périphériques audio.
- Correction de problèmes liés à la gestion des états de l'enregistreur.
- Amélioration de la robustesse de la logique d'enregistrement.
- Mise en place de tests CI pour le linting du code mobile.
- Correction de bugs liés à l'affichage de la durée des enregistrements.
- Correction de problèmes de compatibilité avec certains navigateurs.

### Autres changements
- Mise à jour de la documentation.
- Correction de typos et amélioration de la lisibilité du code.
- Ajout de commentaires pour faciliter la compréhension du code.
- Mise à jour des fichiers de configuration pour l'environnement de développement.
- Amélioration des badges dans le fichier README.
- Mise à jour des documents légaux.
- Configuration de l'agent utilisateur pour les requêtes HTTP.
- Ajout d'un timeout plus élevé pour les requêtes backend.
- Correction d'un bug qui provoquait un crash de la page lors du chargement avec des informations utilisateur manquantes.
- Correction d'un bug lié à la gestion des jetons d'accès et de rafraîchissement en environnement de développement local.
- Ajout de la possibilité de configurer l'affichage de l'application mobile.
- Ajout de la possibilité de télécharger les applications mobiles.
