## Changelog : tchap-x-ios (30 derniers jours, au 24 avril 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à la gestion des espaces et des salons, notamment la possibilité de créer des salons accessibles par lien. Des corrections et des améliorations techniques ont également été apportées pour stabiliser l'application et faciliter le développement futur.

### Évolutions fonctionnelles
- **Accès par lien aux salons :** Implémentation de la fonctionnalité permettant de générer un lien d'accès pour un salon, facilitant ainsi l'invitation de participants. [#309](https://github.com/tchapgouv/tchap-x-ios/pull/309)
- **Gestion des espaces :** Amélioration de l'affichage et de la gestion des espaces, avec une action par défaut de filtrage des conversations. [#329](https://github.com/tchapgouv/tchap-x-ios/pull/329)
- **Création de salon :** Modification de l'écran de création de salon pour mieux s'intégrer avec la gestion des espaces, notamment en masquant la sélection d'espace. [#323](https://github.com/tchapgouv/tchap-x-ios/pull/323)
- **Désactivation de l'épinglage des données géographiques :** Désactivation temporaire de l'épinglage pour les données géographiques. [#331](https://github.com/tchapgouv/tchap-x-ios/pull/331)
- **Écran de récupération :** L'écran de récupération s'ouvre maintenant avant l'écran de confirmation d'identité. [#8959144c7](https://github.com/tchapgouv/tchap-x-ios/commit/8959144c7)

### Évolutions techniques
- **Mise à jour du SDK matrix-rust-components-swift :** Mise à jour vers la version `v0.9.10` du SDK. [#324](https://github.com/tchapgouv/tchap-x-ios/pull/324)
- **Correction temporaire de visibilité du SDK :** Correction temporaire de la visibilité du SDK. [#322](https://github.com/tchapgouv/tchap-x-ios/pull/322)
- **Formatage du code :** Formatage du code source avec `swiftformat v0.59.1` pour améliorer la lisibilité et la cohérence. [#ffddb50fc](https://github.com/tchapgouv/tchap-x-ios/commit/ffddb50fc)
- **Correction des tests unitaires :** Correction de problèmes de compilation et d'import dans les tests unitaires. [#b33d332f0](https://github.com/tchapgouv/tchap-x-ios/commit/b33d332f0)

### Autres changements
- **Terminologie Tchap :** Utilisation de la terminologie spécifique à Tchap dans l'application. [#3b59175ca](https://github.com/tchapgouv/tchap-x-ios/commit/3b59175ca)
- **Suppression de fichiers inutiles :** Suppression de fichiers hérités de ElementX. [#a278eff34](https://github.com/tchapgouv/tchap-x-ios/commit/a278eff34)
- **Génération de chaînes de caractères :** Ajout de chaînes de caractères générées. [#9f982bc8d](https://github.com/tchapgouv/tchap-x-ios/commit/9f982bc8d)
