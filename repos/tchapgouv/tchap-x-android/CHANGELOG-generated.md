## Changelog : tchap-x-android (30 derniers jours, au 28 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la sécurité et à la compatibilité de l'application, notamment la gestion des certificats et la prise en charge des appareils 32 bits. Des corrections ont également été apportées pour améliorer la connexion avec Tchap Classique et l'authentification OAuth. Enfin, de nouvelles fonctionnalités comme les commandes dans les messages et l'activation de la visioconférence ont été ajoutées.

### Évolutions fonctionnelles
- Activation des commandes dans les messages, permettant d'interagir directement depuis l'application. [#2157fcc8b4](https://github.com/tchapgouv/tchap-x-android/commit/2157fcc8b4)
- Ajout de la commande `/visio` pour lancer une visioconférence. [#132aeafe86](https://github.com/tchapgouv/tchap-x-android/commit/132aeafe86)
- Amélioration de la connexion via Tchap Classique avec ProConnect. [#7bd7a33f01](https://github.com/tchapgouv/tchap-x-android/commit/7bd7a33f01)
- Amélioration de la connexion OAuth avec détection du package de l'application. [#29e54cf664](https://github.com/tchapgouv/tchap-x-android/commit/29e54cf664)
- Instructions ajoutées pour activer la sauvegarde automatique dans Tchap Classique. [#4712546b22](https://github.com/tchapgouv/tchap-x-android/commit/4712546b22)
- Masquage du bandeau de réinitialisation d'identité d'un membre. [#72f5f3555f](https://github.com/tchapgouv/tchap-x-android/commit/72f5f3555f)
- Mise à jour des certificats de juillet 2026 pour une sécurité accrue. [#7518e72b7f](https://github.com/tchapgouv/tchap-x-android/commit/7518e72b7f)
- Renommage de l'application Tchap beta en Tchap. [#a3fea70d86](https://github.com/tchapgouv/tchap-x-android/commit/a3fea70d86)

### Évolutions techniques
- Gestion améliorée des certificats CRL-only, autorisant le trafic en clair dans certains cas. [#9539864188](https://github.com/tchapgouv/tchap-x-android/commit/9539864188), [#e2c3915cb9](https://github.com/tchapgouv/tchap-x-android/commit/e2c3915cb9), [#b3873999b3](https://github.com/tchapgouv/tchap-x-android/commit/b3873999b3)
- Correction pour la compatibilité avec les appareils 32 bits. [#916280a72c](https://github.com/tchapgouv/tchap-x-android/commit/916280a72c), [#13e9519074](https://github.com/tchapgouv/tchap-x-android/commit/13e9519074)
- Configuration des URL de Push en fonction de l'environnement. [#0b8d1a6dbe](https://github.com/tchapgouv/tchap-x-android/commit/0b8d1a6dbe)
- Mise à jour de Compound et amélioration des badges. [#624e73bb76](https://github.com/tchapgouv/tchap-x-android/commit/624e73bb76)
- Suppression des noms de domaine Element non utilisés. [#a5bcfa26b4](https://github.com/tchapgouv/tchap-x-android/commit/a5bcfa26b4)

### Autres changements
- Ajout de logs d'erreur lors de l'appel à `get_instance`. [#d7798b3456](https://github.com/tchapgouv/tchap-x-android/commit/d7798b3456)
- Suppression de la bordure pour les badges neutres. [#31839dba2d](https://github.com/tchapgouv/tchap-x-android/commit/31839dba2d)
- Changement du format de numéro de version. [#72f5f3555f](https://github.com/tchapgouv/tchap-x-android/commit/72f5f3555f)
- Désactivation de Unified Push, car non fonctionnel actuellement. [#35e1699a51](https://github.com/tchapgouv/tchap-x-android/commit/35e1699a51)
- Ajout des certificats pour autoriser les anciennes versions Android à se connecter. [#860a17b810](https://github.com/tchapgouv/tchap-x-android/commit/860a17b810)
- Remplacement du certificat Harica root par l'intermédiaire. [#23d3806546](https://github.com/tchapgouv/tchap-x-android/commit/23d3806546)
- Lister les hash des APKs lors de la génération de la release. [#d860e38504](https://github.com/tchapgouv/tchap-x-android/commit/d860e38504)
- Ajout du lien du Play Store dans le script de release. [#f17037e507](https://github.com/tchapgouv/tchap-x-android/commit/f17037e507)
- Corrections mineures du script de release. [#f129707eb7](https://github.com/tchapgouv/tchap-x-android/commit/f129707eb7)
- Le rapport contient les statuts de vérification et de sauvegarde. [#f19a4d4446](https://github.com/tchapgouv/tchap-x-android/commit/f19a4d4446)
