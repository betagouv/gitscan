## Changelog : tchap-x-android (30 derniers jours, au 19 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à la stabilité et aux fonctionnalités de l'application.  La mise à jour vers Element X v26.06.2 inclut des corrections de bugs, des améliorations de l'interface utilisateur (notamment pour l'édition de médias et l'affichage des salons), et des optimisations des performances. Des fonctionnalités comme la gestion des autorisations de partage de position et la personnalisation de la carte ont également été améliorées.

### Évolutions fonctionnelles
- **Gestion des salons:** Correction de l'affichage du menu d'historique. [#6855](https://github.com/tchapgouv/tchap-x-android/issues/6855)
- **Interface utilisateur:**
    - Renommage de la section "Direct" en "Personnes".
    - Correction de l'icône d'envoi de message en mode sombre.
    - Amélioration de l'affichage des fichiers et de leur taille.
    - Amélioration de l'interface de la vue des médias (partage, téléchargement).
    - Amélioration de la conception et de l'ordre des éléments dans les détails du salon.
    - Ajout d'une option pour choisir des sons personnalisés pour les notifications de messages et d'appels.
- **Médias:**
    - Ajout de fonctions de recadrage et de rotation d'image avant envoi.
    - Amélioration de la génération et du nettoyage des snapshots des cartes.
    - Correction de l'affichage des images dans la vue des médias.
- **Localisation:**
    - Amélioration de la gestion des autorisations de partage de position.
    - Possibilité d'utiliser une URL de style de carte personnalisée.
- **Notifications:** Correction des badges de mentions.
- **Sécurité:** Autorisation des certificats Let's Encrypt sur l'environnement de développement.
- **Expiration de compte:** Ajout d'un écran d'expiration de compte.
- **Lecture des messages:** Correction de l'envoi incorrect des accusés de lecture dans les salons publics. [#6838](https://github.com/tchapgouv/tchap-x-android/issues/6838)
- **Indicateur de messages non lus:** Ajout du nombre de messages non lus à l'indicateur de messages non lus des salons. [#6887](https://github.com/tchapgouv/tchap-x-android/issues/6887)

### Évolutions techniques
- **Mise à jour des dépendances:**
    - Mise à jour du SDK Matrix Rust vers la version 26.06.3.
    - Mise à jour de Compound Design Tokens vers la version 10.2.1.
    - Mise à jour de Kotlin vers la version 2.3.9.
    - Mises à jour de diverses autres dépendances (Roborazzi, Maplibre, Posthog, etc.).
- **Architecture:**
    - Suppression du support d'Android Auto (mode voiture).
    - Utilisation d'un emplacement de clé brut pour les nouveaux sessions du SDK.
    - Refactorisation de la logique de rafraîchissement des tokens.
    - Amélioration de la gestion des erreurs de rafraîchissement des tokens.
    - Utilisation de `runBlocking` pour la logique de rafraîchissement des tokens.
    - Suppression du code généré par DI des rapports Kover.
- **Compilation:** Compilation du SDK en mode release par défaut.
- **Tests:** Ajout de tests unitaires et d'interface utilisateur.
- **CI/CD:** Amélioration du script de release.
- **Performances:** Amélioration des performances générales de l'application.
- **Sécurité:** Correction d'ID dupliqués dans le rust-sdk (BWI).

### Autres changements
- Mise à jour des captures d'écran.
- Correction de problèmes de linter.
- Ajout de sections RageShake et ClearCache dans les paramètres avancés.
- Suppression de la version 0.11.0.
- Ajout d'une étiquette Stefan au projet.
- Correction de la compilation du rust-sdk.
- Ajout de liens Figma.
- Suppression de la fonctionnalité `FloatingDateBadge`.
- Suppression de la fonctionnalité Vulkan.
- Amélioration de la gestion des erreurs et ajout de logs plus précis.
- Suppression de la possibilité de partager sa position via Maplibre, remplacée par une solution plus simple.
- Correction de problèmes de compilation et de tests.
- Synchronisation des chaînes de caractères depuis Localazy.
- Ajout de commentaires et nettoyage du code.
