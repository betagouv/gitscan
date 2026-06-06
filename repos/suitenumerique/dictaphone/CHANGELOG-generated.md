## Changelog : dictaphone (30 derniers jours, au 5 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à l'application mobile, notamment en termes de gestion des enregistrements hors ligne, de robustesse et d'expérience utilisateur. Des corrections de bugs et des optimisations ont également été apportées au backend et à l'interface web, avec un focus particulier sur l'accessibilité et la gestion des transcriptions.

### Évolutions fonctionnelles
- L'application mobile permet désormais de supprimer les enregistrements locaux si le fichier correspondant n'existe plus sur le serveur.
- L'application mobile gère les liens profonds pour la déconnexion.
- L'application mobile affiche une raison plus explicite en cas de blocage de l'upload (ex: pas de wifi).
- L'application mobile propose une gestion améliorée des erreurs et des retours en arrière.
- L'application mobile permet de télécharger un fichier non uploadé.
- L'application mobile permet de contourner l'écran de connexion.
- L'interface web permet d'exporter les transcriptions au format SRT.
- L'interface web permet de copier le texte de la transcription et d'ouvrir le document dans Indoc.
- L'interface web affiche la source et la durée des fichiers dans l'administration.
- L'interface web affiche correctement la durée des enregistrements.
- L'interface web propose une nouvelle interface pour la liste des enregistrements.
- Le backend permet de relancer la génération d'une transcription en cas d'échec.
- Le backend supporte désormais plus de formats audio/vidéo.
- Le backend stocke la source de l'enregistrement audio pour l'analyse.

### Évolutions techniques
- Mise à jour des dépendances pour corriger des vulnérabilités de sécurité (React, i18next, formatjs, tanstack/react-query).
- Mise à jour de Python à la version 3.14.5 et Django à la version 5.12.4.
- Amélioration de la robustesse de l'authentification avec JWT et PKCE.
- Refactoring du code mobile pour une meilleure organisation.
- Ajout d'un script pour automatiser les releases mobiles.
- Amélioration des logs pour faciliter le débogage des problèmes de connexion mobile.
- Ajout d'une commande pour nettoyer les fichiers temporaires et supprimés.
- Configuration du nettoyage des fichiers en tant que tâche cron.
- Amélioration de la configuration du logging.
- Backport de la configuration du logging depuis la documentation.

### Autres changements
- Amélioration de l'accessibilité de l'interface web (titres, labels, contraste).
- Mise à jour de la documentation et des fichiers README.
- Ajout d'un lien vers la salle Matrix du projet.
- Corrections de typos et améliorations de la lisibilité du code.
- Ajout de tests Posthog pour le suivi des erreurs sur mobile.
- Amélioration des messages d'alerte et des indications visuelles sur mobile.
- Ajout de sons pour le démarrage et l'arrêt de l'enregistrement sur mobile.
- Amélioration du rendu du niveau sonore sur l'interface web.
- Ajout de commentaires et de documentation pour faciliter la maintenance du code.
