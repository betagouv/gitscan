## Changelog : tchap-x-ios (30 derniers jours, au 30 avril 2026)

### Résumé
Cette version apporte des améliorations à la gestion des espaces, notamment dans l'affichage et la création de salons. Des corrections ont été apportées pour améliorer la stabilité et l'expérience utilisateur, notamment en cas de perte de connexion au serveur et lors de l'utilisation de liens d'invitation. Des mises à jour de dépendances ont également été intégrées.

### Évolutions fonctionnelles
- **Espaces :** Modification de l'action par défaut dans les espaces pour filtrer les conversations. [#329](https://github.com/tchapgouv/tchap-x-ios/issues/329)
- **Création de salon :** Modifications de l'écran de création de salon pour les espaces, avec suppression temporaire de la sélection d'espace. [#309](https://github.com/tchapgouv/tchap-x-ios/issues/309)
- **Liens d'invitation :** Correction d'un problème lié à l'accès par lien à un salon. [#309](https://github.com/tchapgouv/tchap-x-ios/issues/309)
- **Affichage de la timeline :** Correction du gradient de la timeline.
- **Bannière de déconnexion :** Affichage d'une bannière lorsque le serveur est inaccessible. [#338](https://github.com/tchapgouv/tchap-x-ios/issues/338)
- **Taxonomie :** Amélioration de la taxonomie. [#323](https://github.com/tchapgouv/tchap-x-ios/issues/323)

### Évolutions techniques
- **Mise à jour des dépendances :**
    - `matrix-rust-components-swift` mis à jour vers la version 26.03.10.
    - `compound-design-token` mis à jour vers la version 6.10-angelo 65b1517530e9772bc656ac20b09b7ad733455008.
- **Rebase :** Rebase de la branche ElementX-ios v26.03.3 dans la branche Tchap.
- **Désactivation du pinning géolocalisation :** Désactivation du pinning des données géolocalisées. [#331](https://github.com/tchapgouv/tchap-x-ios/issues/331) et [#336](https://github.com/tchapgouv/tchap-x-ios/issues/336)
- **Correction CA Staging :** Correction d'un problème avec le CA en environnement de staging. [#335](https://github.com/tchapgouv/tchap-x-ios/issues/335)

### Autres changements
- Utilisation de la terminologie spécifique à Tchap.
- Correction de conflits de rebase.
- Tentative de correction du CI. [#325](https://github.com/tchapgouv/tchap-x-ios/issues/325)
