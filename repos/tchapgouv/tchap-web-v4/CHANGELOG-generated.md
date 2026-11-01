## Changelog : tchap-web-v4 (30 derniers jours, au 30 octobre 2026)

### Résumé
Ce mois-ci, Tchap a bénéficié d'améliorations significatives de son interface utilisateur, notamment avec l'ajout d'un lecteur Markdown pour les documents et une meilleure gestion de la visibilité des détails de chiffrement. Une importante phase de nettoyage technique a également été menée pour simplifier le code et améliorer la stabilité de l'application, tout en renforçant la sécurité par défaut lors de la vérification des appareils.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités** :
    - Ajout d'un lecteur Markdown intégré pour visualiser les pièces jointes `.md` dans le panneau latéral ([#35203](https://github.com/tchapgouv/tchap-web-v4/pull/35203)).
    - Affichage des échos locaux des messages dans la nouvelle timeline pour une meilleure visibilité ([#35269](https://github.com/tchapgouv/tchap-web-v4/pull/35269)).
    - Possibilité de masquer ou d'afficher les détails de chiffrement dans les paramètres.
    - Ajout d'une information Tchap dans la nouvelle liste de salons.
    - Le filtre "non lus" est désormais réglé par défaut sur "tous les messages non lus".
- **Expérience utilisateur et interface** :
    - Amélioration de l'authentification avec l'ajout d'une alerte en cas d'utilisation d'un email externe pour éviter les erreurs de serveur.
    - Ajustements visuels sur la taille du bouton de rejoint d'appel et la disposition des boutons d'export et d'invitation.
- **Corrections de bugs** :
    - Résolution d'un crash lors de la prévisualisation d'un salon ([#35500](https://github.com/tchapgouv/tchap-web-v4/pull/35500)).
    - Correction de la perte des brouillons de messages à la fin d'un appel ([#35261](https://github.com/tchapgouv/tchap-web-v4/pull/35261)).
    - Correction des problèmes d'affichage des cartes (MapLibre) ([#35423](https://github.com/tchapgouv/tchap-web-v4/pull/35423)).
    - Correction de la réinitialisation des valeurs d'analytics au redémarrage.
- **Sécurité** :
    - Renforcement de la sécurité : la possibilité de sauter la vérification des appareils est désormais désactivée par défaut ([#35259](https://github.com/tchapgouv/tchap-web-v4/pull/35259)).
    - Suppression du support des liens de démarrage NEB et des jetons d'accès invités.

### Évolutions techniques
- **Refactorisation et maintenance** :
    - Simplification massive du système de personnalisation : suppression de nombreux "overrides" obsolètes (UserMenu, RoomTypeSelector, CreateRoomDialog, etc.) au profit d'imports directs pour améliorer la maintenabilité du code.
    - Migration de la logique de scan des réponses vers le `ReplyTileViewModel`.
- **Infrastructure et CI/CD** :
    - Amélioration et correction des processus de build Docker (ajout de `jq`, mise à jour des workflows).
    - Optimisation des workflows de tests unitaires.
- **Qualité logicielle** :
    - Amélioration de la stabilité des tests en résolvant plusieurs problèmes de tests "instables" (flaky tests) avec Vitest ([#35327](https://github.com/tchapgouv/tchap-web-v4/pull/35327), [#35317](https://github.com/tchapgouv/tchap-web-v4/pull/35317)).

### Autres changements
- **Documentation** : Mise à jour de la documentation concernant les avertissements de recherche et les prérequis pour les invités restreints ([#34729](https://github.com/tchapgouv/tchap-web-v4/pull/34729)).
- **Internationalisation** : Diverses corrections et nettoyages des fichiers de traduction.
