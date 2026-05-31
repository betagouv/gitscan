## Changelog : dictaphone (30 derniers jours, au 22 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment concernant l'enregistrement audio sur mobile et la gestion des transcriptions. Des corrections de bugs et des optimisations de performance ont également été implémentées, tant sur le frontend que sur le backend. L'application mobile a bénéficié d'une refonte de l'interface et de l'ajout de nouvelles fonctionnalités comme la possibilité de contourner l'authentification et la gestion du stockage.

### Évolutions fonctionnelles
- Ajout de la possibilité de regénérer une transcription depuis l'interface web et l'application mobile. [#issue à retrouver]
- Amélioration de l'interface utilisateur pour la gestion des enregistrements, avec des icônes plus claires et une meilleure accessibilité.
- Ajout d'un indicateur de niveau sonore pendant l'enregistrement audio sur mobile.
- Possibilité de télécharger les enregistrements uniquement en Wi-Fi sur l'application mobile.
- Amélioration de l'expérience utilisateur lors de l'authentification sur mobile.
- Ajout d'un indicateur de progression lors du téléchargement des enregistrements sur mobile.
- Possibilité de sélectionner directement le texte de la transcription sur le frontend et l'application mobile.
- Ajout d'un bouton pour naviguer vers la liste des enregistrements après la suppression d'un enregistrement.
- Amélioration de la gestion des erreurs et ajout de messages d'erreur plus précis.
- Ajout d'un tooltip sur le bouton d'upload.
- Mise à jour du menu d'aide.
- Ajout d'un son de démarrage/arrêt lors de l'enregistrement.
- Amélioration de l'affichage des durées courtes.
- Possibilité de contourner l'écran de connexion sur mobile.

### Évolutions techniques
- Refonte de la gestion de l'état de l'enregistreur sur le frontend pour corriger des problèmes de concurrence.
- Amélioration de la robustesse de la logique de nouveau enregistrement.
- Optimisation des performances du frontend en évitant les importations indirectes.
- Ajout d'un mécanisme pour arrêter automatiquement l'enregistrement en cas de manque d'espace de stockage.
- Mise à jour de la configuration de l'agent utilisateur pour les requêtes HTTP.
- Augmentation du délai d'attente pour les requêtes au backend.
- Amélioration de la gestion des jetons JWT et PKCE pour une sécurité accrue.
- Ajout d'une tâche cron pour nettoyer les fichiers temporaires.
- Activation du support vidéo par défaut.
- Amélioration de la gestion des erreurs dans le backend.
- Mise à jour des dépendances et correction de bugs liés à la configuration de l'environnement de développement local.

### Autres changements
- Mise à jour de la documentation pour l'intégration continue et le déploiement mobile.
- Correction de fautes de frappe dans le code et la documentation.
- Mise à jour des badges dans le fichier README.
- Mise à jour des documents légaux.
- Nettoyage du code et refactoring de certains composants.
- Amélioration de la structure du code sur l'application mobile.
- Ajout de commentaires et documentation pour faciliter la maintenance du code.
