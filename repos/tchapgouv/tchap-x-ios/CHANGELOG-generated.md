## Changelog : tchap-x-ios (30 derniers jours, au 17 juillet 2026)

### Résumé
Cette version apporte des améliorations à l'expérience utilisateur, notamment concernant la gestion des clés de chiffrement, l'identification des utilisateurs et la création de salles privées. Des corrections de texte et de terminologie ont également été effectuées. Des mises à jour de certificats de sécurité ont été appliquées pour assurer la continuité du service.

### Évolutions fonctionnelles
- Amélioration de l'écran d'instruction concernant la clé de sauvegarde et la restauration.
- Réactivation du flux d'enregistrement MAS (Matrix Account Service).
- Ajout d'un badge suggéré lors de la création d'une salle privée chiffrée. [#51c4a3a1e](https://github.com/tchapgouv/tchap-x-ios/commit/51c4a3a1e)
- Correction de la couleur d'affichage des mentions d'autres utilisateurs en mode sombre. [#d4314613c](https://github.com/tchapgouv/tchap-x-ios/commit/d4314613c)
- Conversion de l'identifiant utilisateur du format classique de l'application au format email. [#a166cc61b](https://github.com/tchapgouv/tchap-x-ios/commit/a166cc61b)

### Évolutions techniques
- Mise à jour des certificats SSL/TLS en production et pré-production pour garantir la sécurité des communications. [#098c1382c](https://github.com/tchapgouv/tchap-x-ios/commit/098c1382c), [#4c16563c6](https://github.com/tchapgouv/tchap-x-ios/commit/4c16563c6)
- Restriction des domaines suffixés autorisés pour une meilleure sécurité. [#963b75f6e](https://github.com/tchapgouv/tchap-x-ios/commit/963b75f6e)
- Suppression de l'effet de verre sur l'en-tête des salles. [#c3226c3de](https://github.com/tchapgouv/tchap-x-ios/commit/c3226c3de)
- Renommage de l'environnement "staging" en "preprod". [#074e5d22a](https://github.com/tchapgouv/tchap-x-ios/commit/074e5d22a)
- Suppression du "X" dans les noms d'environnement de production et de développement. [#def7c30bd](https://github.com/tchapgouv/tchap-x-ios/commit/def7c30bd)

### Autres changements
- Corrections de typographie et de terminologie dans l'application. [#15e236a6d](https://github.com/tchapgouv/tchap-x-ios/commit/15e236a6d), [#0bd048328](https://github.com/tchapgouv/tchap-x-ios/commit/0bd048328), [#9b4a7b064](https://github.com/tchapgouv/tchap-x-ios/commit/9b4a7b064)
- Restrictions sur l'écran des espaces pour améliorer l'expérience utilisateur. [#3319f0966](https://github.com/tchapgouv/tchap-x-ios/commit/3319f0966), [#0ce67b8fc](https://github.com/tchapgouv/tchap-x-ios/commit/0ce67b8fc)
- Montée de version de l'application. [#53d0e74b2](https://github.com/tchapgouv/tchap-x-ios/commit/53d0e74b2), [#7fe26d9b7](https://github.com/tchapgouv/tchap-x-ios/commit/7fe26d9b7)
