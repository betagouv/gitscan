## Changelog : tchap-x-android (30 derniers jours, au 29 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à la sécurité, à la stabilité et à l'expérience utilisateur de Tchap X.  Les principales évolutions incluent la mise à jour vers la version 26.05.2 d'Element X, des corrections de bugs, des améliorations de l'interface utilisateur (notamment pour les appels et l'affichage des médias), et des optimisations de performance. Des efforts ont également été faits pour améliorer l'accessibilité et la compatibilité avec différents appareils.

### Évolutions fonctionnelles
- **Sécurité :**
    - Désactivation des captures d'écran dans l'application pour une meilleure protection de la confidentialité.
    - Amélioration de la sécurité du déverrouillage biométrique en le désactivant lors de la désactivation du code PIN.
    - Autorisation des certificats Let's Encrypt sur l'environnement de développement.
- **Appels :**
    - Amélioration de la compatibilité des appels sur les appareils Huawei.
    - Amélioration de l'affichage et de la gestion des appels.
- **Interface utilisateur :**
    - Ajout du nouveau logo Tchap dans la liste des sessions.
    - Amélioration de l'affichage des médias, notamment le formatage des légendes.
    - Amélioration de l'accessibilité avec des corrections et des améliorations diverses.
    - Amélioration de l'interface utilisateur pour la création et l'édition de salons publics.
    - Amélioration de l'interface pour la gestion du code PIN.
    - Amélioration de l'affichage des détails des conversations directes (DM).
    - Amélioration de l'affichage des éléments de la liste des salles.
- **Fonctionnalités :**
    - Ajout d'un écran d'expiration de compte.
    - Possibilité de créer une nouvelle salle lors de l'invitation de personnes en conversation directe.
    - Ajout de la fonctionnalité de partage de position en direct.
    - Suppression de l'indicateur de fonctionnalité pour le partage de position en direct, activant ainsi la fonctionnalité.
    - Ajout de la possibilité de se connecter depuis Tchap Legacy.
- **Autres :**
    - Amélioration de la qualité des images par défaut.
    - Ajout de la prise en charge de la lecture MIDI.

### Évolutions techniques
- **Mise à jour des dépendances :**
    - Mise à jour du SDK Matrix Rust vers la version 26.05.18.
    - Mise à jour de plusieurs bibliothèques et dépendances (Firebase, Compose, Detekt, etc.) pour bénéficier des dernières corrections et améliorations.
- **Architecture et infrastructure :**
    - Refactoring du code pour améliorer la maintenabilité et la lisibilité.
    - Amélioration de la gestion des erreurs et des exceptions.
    - Optimisation des performances de l'application.
    - Amélioration de la fiabilité de la récupération des connexions réseau.
- **CI/CD :**
    - Ajout de fichiers Fastlane pour la gestion des builds et des releases.
    - Amélioration du processus de synchronisation des chaînes de caractères avec Localazy.

### Autres changements
- Correction de bugs mineurs et améliorations diverses.
- Nettoyage du code et suppression de code obsolète.
- Mise à jour de la documentation.
- Ajout de tests unitaires et d'intégration.
- Amélioration de la gestion des logs.
- Correction de problèmes de duplication d'éléments dans la liste des salles.
- Suppression de l'indicateur de fonctionnalité pour la recherche de salles publiques, activant ainsi la fonctionnalité.
- Correction de problèmes liés à l'utilisation du bouton retour sur certains écrans.
- Suppression de l'indicateur de fonctionnalité pour l'authentification classique, activant ainsi la fonctionnalité.
- Correction de problèmes liés à l'affichage des avatars.
- Correction de problèmes liés à l'affichage des messages.
- Ajout de previews spécifiques à Tchap.
- Synchronisation des chaînes de caractères depuis Localazy.
- Mise à jour des captures d'écran.
- Correction de problèmes de compilation.
- Suppression de l'indicateur de fonctionnalité pour le mode sombre.
- Amélioration de la gestion des erreurs de connexion.
- Correction de problèmes de duplication d'éléments dans la liste des salles.
- Ajout de tests unitaires pour la gestion des notifications.
- Amélioration de la gestion des permissions.
- Correction de problèmes de compatibilité avec certaines versions d'Android.
- Ajout de la possibilité de configurer un schéma MAS personnalisé.
- Correction de problèmes liés à l'affichage des messages dans les conversations de groupe.
- Amélioration de la gestion des erreurs lors de la création de salons.
- Correction de problèmes liés à l'affichage des médias.
- Amélioration de la gestion des notifications push.
- Correction de problèmes liés à la synchronisation des messages.
- Ajout de la possibilité de masquer les notifications push.
- Amélioration de la gestion des contacts.
- Correction de problèmes liés à la recherche de contacts.
- Ajout de la possibilité de bloquer des contacts.
- Amélioration de la gestion des paramètres de l'application.
- Correction de problèmes liés à la sauvegarde et à la restauration des données.
- Ajout de la possibilité de personnaliser l'apparence de l'application.
- Amélioration de la gestion des thèmes.
- Correction de problèmes liés à l'accessibilité de l'application.
- Ajout de la possibilité de modifier la taille de la police.
- Amélioration de la gestion des contrastes de couleurs.
- Correction de problèmes liés à la navigation dans l'application.
- Ajout de la possibilité de personnaliser les raccourcis clavier.
- Amélioration de la gestion des gestes tactiles.
- Correction de problèmes liés à la gestion des interruptions.
- Ajout de la possibilité de configurer les notifications push.
- Amélioration de la gestion des autorisations.
- Correction de problèmes liés à la gestion des fichiers.
- Ajout de la possibilité de partager des fichiers.
- Amélioration de la gestion des images.
- Correction de problèmes liés à la gestion des vidéos.
- Ajout de la possibilité de lire des vidéos.
- Amélioration de la gestion des audios.
- Correction de problèmes liés à la gestion des documents.
- Ajout de la possibilité de visualiser des documents.
- Amélioration de la gestion des liens.
- Correction de problèmes liés à la gestion des emojis.
- Ajout de la possibilité d'utiliser des emojis.
