## Changelog : synapse (30 derniers jours, au 28 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives en termes de performance et de stabilité, notamment grâce à l'intégration de code Rust pour certaines opérations critiques. Des corrections de sécurité importantes ont également été implémentées pour protéger contre diverses vulnérabilités. Enfin, des améliorations ont été apportées à la gestion des comptes utilisateurs et à l'expérience de synchronisation.

### Évolutions fonctionnelles
- Amélioration de la gestion des règles de push avec le support du flag `de.sorunome.msc2409.push_ephemeral` pour les appservices. [#19928](https://github.com/tchapgouv/synapse/issues/19928)
- Possibilité de recréer le profil utilisateur lors de la réactivation d'un compte. [#19902](https://github.com/tchapgouv/synapse/issues/19902)
- Ajout de filtres "avant" et "après" à la méthode de suppression d'un utilisateur pour une plus grande flexibilité. [#19802](https://github.com/tchapgouv/synapse/issues/19802)
- Support MSC4446 : possibilité de déplacer les marqueurs de lecture en arrière. [#19663](https://github.com/tchapgouv/synapse/issues/19663)
- Amélioration de l'endpoint MSC3814 pour les appareils déshydratés, passant de POST à GET pour une meilleure conformité aux spécifications. [#19896](https://github.com/tchapgouv/synapse/issues/19896)
- Amélioration de l'idempotence des requêtes PUT pour l'authentification avec QR code (MSC4388). [#19808](https://github.com/tchapgouv/synapse/issues/19808)

### Évolutions techniques
- Intégration de code Rust pour la sérialisation d'événements et l'accès à la base de données, améliorant significativement les performances. [#19878](https://github.com/tchapgouv/synapse/issues/19878), [#19837](https://github.com/tchapgouv/synapse/issues/19837), [#19871](https://github.com/tchapgouv/synapse/issues/19871)
- Ajout d'index sur la table `sliding_sync_connections` pour optimiser les requêtes de synchronisation. [#19912](https://github.com/tchapgouv/synapse/issues/19912), [#19923](https://github.com/tchapgouv/synapse/issues/19923)
- Amélioration de la gestion des connexions Sliding Sync pour éviter les blocages. [#19826](https://github.com/tchapgouv/synapse/issues/19826)
- Optimisation de la gestion de la présence et ajout de timers configurables. [#19939](https://github.com/tchapgouv/synapse/issues/19939), [#19941](https://github.com/tchapgouv/synapse/issues/19941)
- Correction de bugs liés à la gestion des états obsolètes de présence. [#19948](https://github.com/tchapgouv/synapse/issues/19948)
- Utilisation d'un budget de temps CPU pour les tests afin de réduire les faux positifs liés à PostgreSQL. [#19929](https://github.com/tchapgouv/synapse/issues/19929)
- Ajout de `golangci-lint` au CI pour améliorer la qualité du code Go. [#19888](https://github.com/tchapgouv/synapse/issues/19888)

### Autres changements
- Corrections de sécurité pour prévenir les vulnérabilités de traversée de chemin et les attaques par usurpation d'identité.
- Suppression du support legacy de l'auth delegation MSC3861. [#19895](https://github.com/tchapgouv/synapse/issues/19895)
- Mise à jour de la documentation et des notes de version.
- Correction de bugs et améliorations générales de la stabilité.
- Reconfiguration du build Docker avec un Dockerfile personnalisé. [#4f92402](https://github.com/tchapgouv/synapse/commit/4f92402)
- Ajout d'une configuration pour définir le nombre maximal de résultats de recherche. [#11](https://github.com/tchapgouv/synapse/issues/11)
- Activation de l'expiration des comptes avec MAS. [#5](https://github.com/tchapgouv/synapse/issues/5)
- Copie des règles d'accès aux salles lors de la mise à niveau. [#10](https://github.com/tchapgouv/synapse/issues/10)
- Amélioration du cache MAS introspection.
- Publication d'un artefact pour le développement. [#1](https://github.com/tchapgouv/synapse/issues/1)
- Correction d'un bug lié à la sensibilité à la casse de la mitigation `multipart/form-data`.
- Correction de problèmes d'accès à des chemins non autorisés.
- Limitation de la taille des règles de push.
- Correction d'un problème lié à la vérification de la salle pour l'endpoint `/get_missing_events`.
- Validation des champs de nom d'utilisateur, d'avatar et de héros avant de les envoyer en synchronisation.
- Correction de régressions de configuration liées aux fonctionnalités expérimentales. [#19987](https://github.com/tchapgouv/synapse/issues/19987)
- Diverses mises à jour de dépendances.
