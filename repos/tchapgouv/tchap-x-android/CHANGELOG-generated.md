## Changelog : tchap-x-android (30 derniers jours, au 10 juin 2026)

### Résumé
Cette période a été marquée par une série de corrections de bugs, d'améliorations de l'interface utilisateur et de mises à jour de dépendances. L'application a bénéficié d'améliorations de la stabilité, notamment au niveau de la gestion des appels et de la connexion, ainsi que de nouvelles fonctionnalités comme l'ajout du logo Tchap dans la liste des sessions. Plusieurs efforts ont été faits pour optimiser les performances et la gestion des ressources, notamment en améliorant la qualité des images et en optimisant le chargement des médias.

### Évolutions fonctionnelles
- Renommage de la section "Direct" en "Personnes" pour une meilleure clarté.
- Ajout du nouveau logo Tchap dans la liste des sessions.
- Amélioration de la création de salons publics.
- Possibilité de se connecter à partir de Tchap Legacy.
- Ajout d'un écran d'expiration de compte.
- Suppression du support pour Android Auto (mode voiture).
- Amélioration de la gestion des invitations dans les conversations privées : création automatique d'une salle si nécessaire [#6756](https://github.com/tchapgouv/tchap-x-android/issues/6756).
- Correction de l'icône d'envoi de message en mode sombre.
- Correction des badges de mentions.
- Amélioration de la qualité des images par défaut.
- Ajout de la lecture MIDI [#6770](https://github.com/tchapgouv/tchap-x-android/pull/6770).
- Amélioration de l'affichage des appels en mode plein écran [#6634](https://github.com/tchapgouv/tchap-x-android/pull/6634).
- Suppression de la fonctionnalité Live Location Sharing (via un feature flag).
- Amélioration de la détection des doublons dans la liste des salles [#6791](https://github.com/tchapgouv/tchap-x-android/issues/6791).

### Évolutions techniques
- Mise à jour du SDK Matrix Rust vers la version 26.05.18 [#6805](https://github.com/tchapgouv/tchap-x-android/pull/6805).
- Compilation du SDK Rust en mode release par défaut.
- Amélioration du script de release.
- Correction des ID dupliqués dans le SDK Rust (BWI).
- Mise à jour des thèmes (compound-design-tokens).
- Amélioration de la génération des snapshots et nettoyage automatique des anciennes cartes.
- Optimisation du chargement des médias : chargement complet uniquement de l'élément visible [#6794](https://github.com/tchapgouv/tchap-x-android/pull/6794).
- Amélioration de la fiabilité du `FetchPushForegroundService` [#6757](https://github.com/tchapgouv/tchap-x-android/pull/6757).
- Correction de la compilation du SDK Rust.
- Ajout de sections RageShake et ClearCache dans les paramètres avancés.
- Correction pour la création de salons publiques.
- Amélioration de la gestion des erreurs et des logs.
- Suppression de la version 0.11.0.
- Correction de l'utilisation des spans analytics.

### Autres changements
- Ajout de fichiers Fastlane pour les versions 26.05.1 et 26.05.2.
- Synchronisation des chaînes de caractères depuis Localazy.
- Suppression de la fonctionnalité SignInWithClassic via un feature flag.
- Ajout de tests unitaires et d'UI.
- Mise à jour de diverses dépendances (Firebase, Sentry, Compose, etc.).
- Corrections de code et améliorations de la lisibilité.
- Ajout de la possibilité de revenir en arrière avec la touche "Esc" dans les webviews [#6725](https://github.com/tchapgouv/tchap-x-android/pull/6725).
- Désactivation des captures d'écran dans l'application.
- Nettoyage des access rules lors de la création de salons.
- Correction de l'utilisation du MediaPlayer lors de la navigation.
- Suppression de l'autorisation des certificats Let's Encrypt sur l'environnement de développement.
- Ajout d'un suffixe au nom de l'application pour indiquer le buildType (debug/nightly).
- Suppression de la fonctionnalité de déverrouillage biométrique lors de la désactivation du code PIN [#6781](https://github.com/tchapgouv/tchap-x-android/pull/6781).
- Correction de l'état de Maestro après les modifications du flux d'invitation [#6796](https://github.com/tchapgouv/tchap-x-android/pull/6796).
- Correction d'un bug empêchant la détection des doublons dans la liste des salles [#6793](https://github.com/tchapgouv/tchap-x-android/issues/6793).
