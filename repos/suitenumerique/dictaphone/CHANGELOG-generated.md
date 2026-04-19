## Changelog : dictaphone (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur le développement de l'application mobile (iOS), l'intégration de la transcription via un service externe (Docs), et l'amélioration de l'interface utilisateur web. Des fonctionnalités de suppression et de restauration de fichiers ont également été implémentées, ainsi que des améliorations de la gestion des tâches d'intelligence artificielle.

### Évolutions fonctionnelles
- **Application Mobile (iOS):** Développement significatif de l'application mobile iOS, incluant l'authentification, l'enregistrement, la liste des enregistrements, la gestion des permissions, et la possibilité de partager et d'ouvrir les transcriptions dans l'application Docs. Une version 0.2 a été publiée.
- **Intégration Docs:** Possibilité de créer et d'ouvrir les transcriptions directement dans l'application Docs. L'ID de l'application Docs est maintenant exposé pour une meilleure intégration.
- **Suppression et Restauration:** Ajout de la fonctionnalité de suppression et de restauration des enregistrements. Un badge visuel indique les fichiers supprimés.
- **Interface Utilisateur Web:** Amélioration de l'interface utilisateur web, notamment la page de liste des enregistrements, la page de détails des enregistrements, et l'ajout d'une barre latérale de navigation.
- **Copier la transcription:** Possibilité de copier la transcription dans le presse-papier depuis l'interface web.
- **Affichage de la durée:** Affichage de la durée des enregistrements.
- **Gestion des tâches IA:** Amélioration de la gestion des tâches d'intelligence artificielle, avec la création automatique des tâches et la gestion des erreurs.

### Évolutions techniques
- **Backend:**
    - Support amélioré du format audio m4a.
    - Correction de permissions pour les jobs IA et l'accès aux médias.
    - Mise en place d'un système de redirection sécurisé pour l'application mobile.
    - Intégration avec un service AI partagé.
- **Frontend:**
    - Refonte de l'architecture du frontend avec l'utilisation de composants réutilisables.
    - Amélioration de la gestion des langues (i18n).
    - Mise à jour des dépendances et correction de problèmes de build.
    - Utilisation de la librairie `react-native-nitro-player` pour l'application mobile.
- **Mobile:**
    - Initialisation du projet React Native.
    - Configuration de l'environnement de build pour iOS.
    - Mise en place d'une gestion robuste des permissions.
- **Docker:** Correction d'un problème lié à la librairie `libmagic` dans le Dockerfile.

### Autres changements
- Ajout de tests pour l'intégration Docs.
- Amélioration de la documentation concernant la redirection mobile.
- Suppression de l'écriture inclusive dans la documentation française.
- Mise à jour des assets et du logo.
- Amélioration du style et de la cohérence du code avec l'utilisation de Prettier et ESLint.
- Correction de divers bugs et améliorations de la performance.
