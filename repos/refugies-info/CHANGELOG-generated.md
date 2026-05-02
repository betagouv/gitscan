# Synthèse d'activité : refugies-info (du 15/05 au 22/05)

## Résumé de l'activité
Cette semaine, l'organisation refugies-info a concentré ses efforts sur l'amélioration de ses outils principaux, [playground](/repos/refugies-info/playground) et [karfur](/repos/refugies-info/karfur).  [playground](/repos/refugies-info/playground) a bénéficié d'une refonte majeure de son interface utilisateur avec le design système DSFR, ainsi que de fonctionnalités de filtrage et de tri des documents améliorées, facilitant ainsi l'accès à l'information pour les utilisateurs.  [karfur](/repos/refugies-info/karfur) a quant à lui reçu des corrections de bugs importants, notamment concernant l'affichage des données et la gestion des traductions, améliorant la fiabilité et l'expérience utilisateur.

## Sécurité
Plusieurs vulnérabilités de sécurité dans les dépendances de [karfur](/repos/refugies-info/karfur) ont été corrigées, notamment dans les librairies lodash, path-to-regexp et @smithy/config-resolver. De plus, l'ajout de hooks GitLeaks dans [playground](/repos/refugies-info/playground) et [karfur](/repos/refugies-info/karfur) permet une détection proactive des secrets potentiellement exposés dans le code.

## Autres changements notables
Une refactorisation de la gestion des rôles et des permissions (RBAC) a été réalisée dans [playground](/repos/refugies-info/playground) pour une meilleure sécurité et maintenabilité.  Des améliorations de performance ont été apportées à [karfur](/repos/refugies-info/karfur) grâce à l'ajout d'index MongoDB et à la refactorisation de la gestion des cartes Mongoose. L'accessibilité de [karfur](/repos/refugies-info/karfur) a également été améliorée pour une meilleure conformité RGAA.

## Dépôts les plus actifs
- [playground](/repos/refugies-info/playground) : Refonte de l'interface utilisateur et ajout de nouvelles fonctionnalités de filtrage et de gestion des documents.
- [karfur](/repos/refugies-info/karfur) : Corrections de bugs, améliorations de la performance et renforcement de la sécurité.
