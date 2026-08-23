## Changelog : meet (30 derniers jours, au 21 août 2026)

### Résumé
Ce mois-ci, Meet a bénéficié d'améliorations significatives axées sur la personnalisation et la fiabilité. Les utilisateurs disposent désormais de meilleurs outils pour tester leur matériel audio et gérer les rôles au sein des réunions. Parallèlement, une refonte technique majeure a été opérée pour optimiser la fluidité de l'interface, notamment pour le chat et l'affichage des participants.

### Évolutions fonctionnelles
- **Amélioration de l'expérience audio** : ajout d'une jauge de niveau pour le microphone, d'un testeur de haut-parleur et d'un système de surveillance du micro silencieux.
- **Gestion des rôles et participants** : possibilité de promouvoir des participants en cours de réunion, notification automatique lors d'un changement de rôle et introduction d'un badge pour les participants non authentifiés.
- **Personnalisation et configuration** : les utilisateurs peuvent désormais définir des configurations par défaut pour leurs liens de réunion et personnaliser la couleur d'arrière-plan de l'iframe du calendrier.
- **Outils de diagnostic** : ajout d'une fonctionnalité de test de connexion pour vérifier la qualité de la liaison réseau.
- **Interface utilisateur** : affichage de l'ID de la réunion sur l'écran de participation et amélioration de la visibilité des noms de participants.

### Évolutions techniques
- **Optimisations de performance** : 
    - Virtualisation des messages du chat pour réduire la charge du DOM.
    - Réduction massive des re-rendus inutiles via la mémoïsation de composants clés (Avatar, EffectsButton, ParticipantTile, etc.).
    - Optimisation de la gestion des métadonnées et des abonnements aux événements de présence.
- **Refactoring majeur** : 
    - Restructuration complète du module de chat.
    - Modularisation du code frontend par l'extraction de composants (Lobby, ParticipantTile, gestion des raccourcis clavier).
    - Encapsulation de la télémétrie et du suivi des erreurs dans un module dédié.
- **Fiabilité et corrections** :
    - Résolution de problèmes critiques liés à MediaPipe (mismatch de version WASM) et aux permissions de l'OS pour l'accès aux médias.
    - Correction de bugs d'affichage (alignement de la barre d'outils, centrage des avatars) et de synchronisation des périphériques.
    - Amélioration de la gestion des erreurs de partage d'écran et de la synchronisation des préférences utilisateur.
- **Backend** : intégration des préférences utilisateur dans le modèle de données et ajout d'API pour la gestion dynamique des rôles.

### Autres changements
- **Documentation et légal** : mise à jour des conditions générales d'utilisation et correction de la documentation technique.
- **Maintenance** : nettoyage du code (linting), suppression de composants obsolètes et ajout du fichier `publiccode.yml`.
