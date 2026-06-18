## Changelog : dictaphone (30 derniers jours, au 15 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à l'application mobile et web, notamment en termes de gestion des enregistrements, de la sélection de la langue de transcription, de la robustesse et de l'accessibilité. Des corrections de bugs ont été implémentées pour améliorer l'expérience utilisateur globale. Des améliorations de sécurité et de configuration ont également été apportées au backend.

### Évolutions fonctionnelles
- **Mobile :**
    - Ajout de la possibilité de télécharger un fichier non encore uploadé.
    - Amélioration de la gestion des erreurs et des reprises d'upload.
    - Ajout de sons de démarrage et d'arrêt d'enregistrement.
    - Affichage et application de la politique de données.
    - Gestion des liens profonds (deeplinks) pour la déconnexion.
    - Suppression automatique des enregistrements locaux si le fichier correspondant n'existe plus sur le serveur.
- **Web & Mobile :**
    - Sélection de la langue de transcription dès la création du fichier.
    - Amélioration de l'interface utilisateur pour la reprise d'enregistrement et le changement de langue.
    - Affichage du badge d'état de la transcription.
- **Web :**
    - Ajout d'options d'export avancées pour les transcriptions, notamment au format SRT.
    - Ajout de la possibilité de copier le texte de la transcription et d'ouvrir les documents associés.
    - Amélioration de l'interface de la liste des enregistrements.
    - Ajout d'un indicateur visuel du niveau sonore pendant l'enregistrement.
    - Ajout d'un tooltip informatif sur le bouton d'upload.
    - Amélioration de l'accessibilité de l'application web.

### Évolutions techniques
- **Backend :**
    - Mise à jour de Python à la version 3.14.5 et de Django à la version 5.12.4.
    - Amélioration de la gestion des erreurs et des codes d'erreur.
    - Ajout de la configuration automatique de la politique de données.
    - Exposition des informations de la politique de données via une API.
    - Amélioration de la suppression des données temporaires (jobs AI et fichiers originaux).
    - Ajout de tâches cron pour la suppression automatique des fichiers.
    - Amélioration de la sécurité avec l'utilisation de `secrets.compare_digest`.
    - Prise en charge de davantage de formats audio/vidéo.
- **Frontend :**
    - Mise à jour de Node.js à la version 24.
    - Refonte de l'interface utilisateur de la page d'enregistrement avec un indicateur de niveau sonore.
    - Amélioration de la robustesse de la gestion de l'état de l'enregistrement.
    - Utilisation d'icônes UI-kit pour une meilleure cohérence visuelle.
    - Amélioration de la gestion des permissions et de l'affichage des messages d'erreur.
    - Optimisation des imports pour éviter les erreurs liées à Vite.
    - Ajout de tests d'accessibilité et corrections.
- **Mobile :**
    - Mise à jour de l'API React Native Audio.
    - Amélioration de la robustesse du composant d'enregistrement.
    - Mise en place d'un système de gestion des notifications.

### Autres changements
- Correction de vulnérabilités de sécurité via Snyk.
- Mise à jour des dépendances.
- Amélioration de la documentation.
- Ajout d'un lien vers la salle Matrix.
- Ajout de logs plus détaillés pour faciliter le débogage des problèmes de connexion mobile.
- Nettoyage du code et suppression de code inutile.
