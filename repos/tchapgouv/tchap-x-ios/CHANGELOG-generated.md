## Changelog : tchap-x-ios (30 derniers jours, au 26 juin 2026)

### Résumé
Cette version apporte des améliorations à l'expérience utilisateur, notamment concernant la création de salles privées chiffrées, la gestion des mentions, et l'interface des appels. Des corrections de bugs et des mises à jour techniques ont également été implémentées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout d'un badge suggéré lors de la création d'une salle privée chiffrée.
- Correction de la couleur des mentions "autres" en mode sombre pour une meilleure lisibilité.
- Suppression du *feature flag* pour les salles privées non chiffrées, rendant cette fonctionnalité pleinement disponible.
- Amélioration de l'interface des boutons d'appel pour correspondre aux spécifications Figma et Element Web [#5696](https://github.com/tchapgouv/tchap-x-ios/issues/5696).
- Utilisation de la nouvelle icône de recadrage de Compound Design System [#5691](https://github.com/tchapgouv/tchap-x-ios/issues/5691).
- Intégration de la connexion Tchap Classic pour l'authentification automatique.
- Ajout d'un lien vers les paramètres depuis l'écran de déconnexion.
- Amélioration de l'espacement des icônes dans les étiquettes de liste (ListRowLabel) avec LiquidGlass.
- Correction d'un problème d'affichage des informations sur les fichiers.

### Évolutions techniques
- Mise à jour du SDK Rust Matrix.
- Mise à jour de la librairie Compound Design Tokens (version 10.2.1).
- Mise à jour de XcodeGen.
- Refactorisation de l'authentification OIDC vers OAuth.
- Correction de conflits de rebase lors de l'intégration de ElementX-ios v26.06.0 et v26.05.3.
- Correction d'un problème de clipping lié aux changements d'état du timestamp.
- Amélioration des tests unitaires.
- Mise à jour du submodule enterprise.
- Mise à jour des dépendances swift-argument-parser et yams.
- Amélioration de la gestion des mocks pour les tests.
- Correction de l'état de l'appel entrant pour éviter les problèmes lors de la fin d'un appel.

### Autres changements
- Traduction des titres des notes de publication en français.
- Incrémentation du numéro de version de l'application.
- Mise à jour de la documentation AGENTS.md pour améliorer la détection des avertissements SwiftLint/SwiftFormat.
- Mise à jour des traductions.
