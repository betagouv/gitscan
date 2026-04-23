## Changelog : dictaphone (30 derniers jours, au 22 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur, notamment sur la page d'accueil, les listes d'enregistrements et la gestion des fichiers. L'application mobile iOS a également fait des progrès importants avec l'implémentation des fonctionnalités d'enregistrement, de listage et de suppression, ainsi que l'intégration de l'authentification. De plus, l'intégration avec un service d'IA pour la transcription et la création de résumés a été initiée.

### Évolutions fonctionnelles
- **Interface utilisateur (Frontend):**
    - Nouvelle page d'accueil avec une mise en page responsive.
    - Amélioration de l'interface de la page d'enregistrement et de la liste des enregistrements.
    - Ajout d'un indicateur visuel pour les enregistrements supprimés.
    - Possibilité de copier la transcription dans le presse-papier.
    - Affichage de la durée des enregistrements.
    - Ajout d'une icône audio à la liste des enregistrements.
    - Intégration de l'affichage du résumé et de la transcription.
    - Amélioration de l'expérience utilisateur pour le téléchargement et la lecture des fichiers.
    - Ajout d'un menu d'actions pour les fichiers (ouvrir dans Docs, partager).
- **Application Mobile (iOS):**
    - Implémentation de l'enregistrement audio.
    - Liste des enregistrements avec suppression par glissement.
    - Intégration du système d'authentification (connexion/déconnexion).
    - Amélioration de l'interface utilisateur et de la navigation.
- **Intégration IA:**
    - Intégration avec un service d'IA pour la transcription et la création de résumés.
    - Possibilité d'ouvrir la transcription dans un outil de documentation.
- **Gestion des fichiers:**
    - Ajout d'une page "Corbeille" pour les fichiers supprimés avec possibilité de restauration.

### Évolutions techniques
- **Backend:**
    - Mise en place d'une vue pour la gestion des jobs IA.
    - Amélioration de la gestion des permissions pour les jobs IA et les médias.
    - Support amélioré des formats audio `m4a` et `webm`.
    - Implémentation d'un système de redirection mobile pour faciliter l'intégration avec l'application iOS.
    - Correction de bugs liés au tri des enregistrements.
    - Support de la transcription via l'API Docs.
- **Infrastructure:**
    - Mise à jour du Dockerfile pour inclure la bibliothèque `libmagic` nécessaire à `collectstatic`.
- **Frontend:**
    - Refonte de l'architecture de l'interface utilisateur pour une meilleure maintenabilité.
    - Amélioration de la gestion des langues (i18n).
    - Utilisation de composants UI réutilisables.
    - Optimisation des performances et correction de bugs.
- **Mobile:**
    - Initialisation du projet React Native pour l'application mobile iOS.
    - Configuration de l'environnement de développement et de build.
    - Intégration de bibliothèques essentielles pour l'enregistrement audio et la gestion de l'interface utilisateur.

### Autres changements
- Ajout de documentation concernant la redirection mobile.
- Mise à jour des dépendances et des configurations.
- Amélioration du code et refactoring pour une meilleure lisibilité et maintenabilité.
- Ajout de tests unitaires et d'intégration.
- Mise en place d'un système d'analyse pour suivre l'utilisation de l'application.
- Suppression de l'écriture inclusive dans les textes en français.
- Publication de la version 0.4.0.
- Publication des versions 0.1 et 0.2 de l'application mobile iOS.
