## Changelog : ami-app-ios (30 derniers jours, au 15 septembre 2026)

### Résumé
Cette période a été marquée par l'amélioration de l'expérience utilisateur avec l'ajout du téléchargement de fichiers et la possibilité de lancer des démarches en ligne. L'infrastructure a également évolué avec la création d'un environnement de pré-production et le renforcement de la sécurité via l'activation des Passkeys sur l'environnement de staging.

### Évolutions fonctionnelles
- Possibilité de lancer une démarche en ligne ([#165](https://github.com/numerique-gouv/ami-app-ios/pull/165)).
- Support du téléchargement de fichiers directement depuis la WebView ([#173](https://github.com/numerique-gouv/ami-app-ios/pull/173)).
- Correction d'un bug provoquant une page blanche lors d'un second accès à une même application de revue ([#166](https://github.com/numerique-gouv/ami-app-ios/pull/166)).
- Amélioration de l'ouverture des vues de destination depuis la vue partenaire.
- Activation du support des Passkeys sur l'environnement de staging ([#171](https://github.com/numerique-gouv/ami-app-ios/pull/171)).

### Évolutions techniques
- Création d'un environnement de pré-production (Preprod) dédié ([#161](https://github.com/numerique-gouv/ami-app-ios/pull/161)).
- Refonte de la navigation dans la WebView via l'introduction d'un nouveau protocole de gestion des fenêtres.
- Amélioration du système de téléchargement pour permettre le stockage local des fichiers sur l'appareil.
- Optimisation de la gestion de la mémoire en supprimant le cache des ViewModels.
- Mise à jour des configurations de sécurité et d'infrastructure (Firebase, domaines associés, gestion des secrets et des entitlements).
- Migration de la gestion de la fermeture des vues (dismissal) vers SwiftUI.

### Autres changements
- Nettoyage des configurations de targets ([#162](https://github.com/numerique-gouv/ami-app-ios/pull/162)).
- Refactorisation sémantique du code (renommage de plusieurs classes et méthodes pour une meilleure clarté, ex: `Partner` vers `Service` ou `Destination`).
- Corrections de typos et amélioration de la documentation interne.
