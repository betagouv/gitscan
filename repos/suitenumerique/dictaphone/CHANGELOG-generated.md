## Changelog : dictaphone (30 derniers jours, au 22 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur, tant sur le web que sur mobile (iOS). L'application mobile est en cours de développement et voit l'implémentation de fonctionnalités essentielles comme l'enregistrement, la liste des enregistrements, la suppression et l'authentification.  Des améliorations ont également été apportées à l'intégration avec un service d'IA pour la transcription et la création de résumés, ainsi qu'à la gestion des fichiers et des permissions.

### Évolutions fonctionnelles
- **Interface utilisateur (Web) :**
    - Nouvelle page d'accueil avec un design amélioré.
    - Amélioration de la réactivité de l'interface.
    - Ajout d'un indicateur de progression lors du chargement des transcriptions.
    - Ajout d'un badge "supprimé" pour les enregistrements supprimés.
    - Création d'une page "corbeille" avec des actions de suppression et de restauration.
    - Possibilité de copier la transcription dans le presse-papier.
    - Affichage de la durée de l'enregistrement.
    - Amélioration de l'affichage des informations de la transcription.
- **Application mobile (iOS) :**
    - Implémentation de l'authentification (connexion/déconnexion).
    - Enregistrement audio fonctionnel.
    - Liste des enregistrements avec suppression par glissement.
    - Navigation améliorée.
    - Gestion des permissions (microphone).
- **Intégration Docs :**
    - Intégration avec un service de documentation pour ouvrir les transcriptions.
- **Gestion des fichiers :**
    - Support amélioré des formats audio `m4a` et `webm`.
    - Ajout de la durée des enregistrements.

### Évolutions techniques
- **Backend :**
    - Mise en place d'une API pour la gestion des "jobs" d'IA (transcription, résumé).
    - Intégration avec un service d'IA externe pour la transcription.
    - Amélioration de la gestion des permissions et de l'authentification.
    - Ajout d'un endpoint de redirection pour l'application mobile.
    - Support amélioré des formats audio.
- **Frontend :**
    - Refonte de l'architecture de l'interface utilisateur.
    - Utilisation de composants UI plus modernes.
    - Amélioration de la gestion des états et des requêtes API.
    - Mise en place d'un système de rafraîchissement automatique des jobs en attente.
- **Mobile :**
    - Initialisation du projet React Native.
    - Configuration de l'environnement de développement.
    - Implémentation de la navigation de base.
    - Utilisation de bibliothèques pour l'enregistrement audio et la lecture.
- **Divers :**
    - Ajout de tests pour l'intégration avec le service de documentation.
    - Mise à jour de la documentation.
    - Amélioration de la configuration du Dockerfile.

### Autres changements
- Ajout d'un favicon.
- Correction de problèmes de typographie en français.
- Suppression d'écritures inclusives du code.
- Amélioration de la configuration de l'outil de linting.
- Mise à jour des dépendances.
- Publication de la version 0.4.0.
- Publication des versions 0.1 et 0.1-5 de l'application mobile iOS.
- Ajout de l'analyse (analytics) pour suivre l'utilisation de l'application.
