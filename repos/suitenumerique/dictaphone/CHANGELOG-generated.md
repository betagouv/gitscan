## Changelog : dictaphone (30 derniers jours, au 01 Juillet 2026)

### Résumé
Cette période a été marquée par une série d'améliorations significatives sur l'ensemble des plateformes (web, mobile et backend). Les efforts se sont concentrés sur l'amélioration de la robustesse de l'application mobile, notamment en matière de gestion des fichiers audio et de la reprise après interruption. Des améliorations ont également été apportées à l'expérience utilisateur, avec une interface plus claire et des fonctionnalités de gestion des enregistrements plus intuitives. Enfin, des corrections de sécurité et des mises à jour de dépendances ont été effectuées pour assurer la stabilité et la sécurité du système.

### Évolutions fonctionnelles
- **Mobile :** Amélioration des performances d'upload audio sur Android [#1234](https://github.com/suitenumerique/dictaphone/issues/1234).
- **Mobile :** Ajout d'une fonctionnalité de récupération des fichiers audio en cas d'interruption de l'enregistrement.
- **Mobile :** Affichage de la durée du traitement en cours.
- **Mobile :** Amélioration de la gestion des liens profonds (deeplinks) pour la déconnexion.
- **Mobile :** Affichage d'une alerte lors du premier lancement concernant l'optimisation de la batterie.
- **Web :** Ajout d'un bouton de réglage de la vitesse de lecture.
- **Web :** Amélioration de l'interface de la liste des enregistrements.
- **Web :** Ajout d'informations sur la politique de confidentialité des données.
- **Backend :** Amélioration de l'estimation de la durée de traitement des fichiers audio.
- **Backend :** Ajout d'une configuration pour la politique de confidentialité des données.
- **Backend :** Suppression sécurisée des données S3 après la suppression des fichiers.
- **Backend :** Amélioration de la gestion des accès à l'API pour renforcer la sécurité.

### Évolutions techniques
- **Backend :** Mise à jour de Django en version 5.2.15.
- **Frontend :** Utilisation de Node 24.
- **Mobile :** Mise à jour des dépendances, notamment React Native.
- **Mobile :** Correction de problèmes de concurrence dans l'API React Native Audio.
- **Mobile :** Amélioration de la gestion des fichiers audio locaux.
- **Mobile :** Correction de bugs liés à l'affichage des numéros de participants.
- **Frontend :** Amélioration de la robustesse de la sauvegarde des données audio.
- **Frontend :** Ajout de tests pour la construction de l'application.
- **Frontend :** Amélioration de l'accessibilité du site web (titres, labels, etc.).
- **Helm :** Ajout de tâches cron pour la suppression des fichiers originaux et la suppression définitive des données.
- **Sécurité :** Correction de vulnérabilités identifiées par Snyk.

### Autres changements
- Documentation mise à jour.
- Nettoyage du code et suppression de logs de développement inutiles.
- Correction de typos et amélioration de la lisibilité du code.
- Mise à jour des dépendances (hors mises à jour de sécurité).
- Suppression de code inutile.
