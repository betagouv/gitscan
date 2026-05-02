## Changelog : tchap-web-v4 (30 derniers jours, au 30 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à la sécurité, notamment en corrigeant une vulnérabilité liée à l'ouverture de fichiers. Des options de configuration supplémentaires ont été ajoutées pour répondre aux besoins spécifiques de l'administration, comme la gestion de la visibilité des accès et l'ouverture de différents types d'appels groupés. L'interface utilisateur a également été améliorée avec l'ajout d'un thème haute contraste et des modifications visuelles mineures.

### Évolutions fonctionnelles
- Correction d'une faille de sécurité concernant l'ouverture de fichiers depuis le bureau [#1574](https://github.com/tchapgouv/tchap-web-v4/pull/1574).
- Ajout d'un thème haute contraste pour une meilleure accessibilité [#1524](https://github.com/tchapgouv/tchap-web-v4/pull/1524).
- Configuration de la visibilité des accès dans les règles d'accès Tchap [#1585](https://github.com/tchapgouv/tchap-web-v4/pull/1585).
- Refonte du flux de connexion et d'enregistrement pour utiliser un pré-contrôle par email [#1583](https://github.com/tchapgouv/tchap-web-v4/pull/1583).
- Ouverture des appels groupés "Intradef" [#1579](https://github.com/tchapgouv/tchap-web-v4/pull/1579).
- Suppression de la fonctionnalité MAS (Messaging API Service) et activation par défaut [#1575](https://github.com/tchapgouv/tchap-web-v4/pull/1575).
- Ajout d'un schéma de lien profond personnalisé pour le bureau [#1571](https://github.com/tchapgouv/tchap-web-v4/pull/1571).
- Ouverture des appels groupés "Intérieur" [#1570](https://github.com/tchapgouv/tchap-web-v4/pull/1570).
- Ouverture des appels groupés "Collectivité" [#1569](https://github.com/tchapgouv/tchap-web-v4/pull/1569).
- Amélioration du design des labels [#1567](https://github.com/tchapgouv/tchap-web-v4/pull/1567).
- Possibilité d'utiliser le chiffrement de bout en bout (EC) dans les discussions directes via un flag de fonctionnalité [#1563](https://github.com/tchapgouv/tchap-web-v4/pull/1563).
- Ajout de badges pour les discussions directes [#1536](https://github.com/tchapgouv/tchap-web-v4/pull/1536).
- Ajout de la possibilité de créer des salons privés non chiffrés [#1536](https://github.com/tchapgouv/tchap-web-v4/pull/1536).
- Modification du libellé de la vérification des emojis [#1556](https://github.com/tchapgouv/tchap-web-v4/pull/1556).

### Évolutions techniques
- Mise à jour de la librairie `compound-web` vers la version 5.0.6 [#1524](https://github.com/tchapgouv/tchap-web-v4/pull/1524).
- Mise à jour de `compound-design-token` pour le thème haute contraste.
- Suppression du toast de fin de téléchargement sur le bureau et déplacement de l'action vers le backend Tauri [#149b6d844](https://github.com/tchapgouv/tchap-web-v4/commit/149b6d844).
- Refactorisation du flux de confirmation de réinitialisation d'identité [#1558](https://github.com/tchapgouv/tchap-web-v4/pull/1558).
- Mise à jour de la librairie `gaufre` [#1553](https://github.com/tchapgouv/tchap-web-v4/pull/1553).
- Mise à jour vers la version 4.19.6 [#1580](https://github.com/tchapgouv/tchap-web-v4/pull/1580).
- Mise à jour vers la version 4.19.5 [#1568](https://github.com/tchapgouv/tchap-web-v4/pull/1568).
- Mise à jour vers la version 4.19.4 [#1561](https://github.com/tchapgouv/tchap-web-v4/pull/1561).

### Autres changements
- Ajout de tests pour le hook `tchaproomtype`.
- Amélioration de la configuration des règles d'accès Tchap.
- Nettoyage du code lié à la fonctionnalité MAS.
- Modification du routage pour différencier la connexion et l'enregistrement.
- Ajout de badges pour les salons privés non chiffrés.
- Ajout de la configuration pour l'ouverture des appels groupés.
- Correction de problèmes de linting et de tests.
