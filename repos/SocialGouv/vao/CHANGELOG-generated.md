## Changelog : vao (30 derniers jours, au 29 avril 2026)

### Résumé
Ce changelog couvre une période d'un mois riche en améliorations et corrections, principalement axées sur la gestion des agréments (renouvellement, messagerie, et statut), ainsi que sur des corrections d'interface et des optimisations techniques. Plusieurs améliorations ont été apportées pour répondre aux retours d'utilisateurs et améliorer la conformité RGAA.

### Évolutions fonctionnelles
- **Agrément :**
    - Implémentation de l'envoi de mails de confirmation pour les demandes d'agrément. [#1286](https://github.com/SocialGouv/vao/issues/1286)
    - Ajout de la gestion des messages non lus dans la messagerie d'agrément côté Dreets.
    - Amélioration de la gestion des activités et des fichiers lors du renouvellement d'agrément.
    - Correction de bugs et améliorations de l'interface pour les étapes 1, 2, 3 et 4 du processus de renouvellement d'agrément. [#1256](https://github.com/SocialGouv/vao/issues/1256), [#1259](https://github.com/SocialGouv/vao/issues/1259), [#1265](https://github.com/SocialGouv/vao/issues/1265), [#1272](https://github.com/SocialGouv/vao/issues/1272)
    - Ajout d'une fonctionnalité pour gérer les agréments refusés dans le back-office. [#1245](https://github.com/SocialGouv/vao/issues/1245)
- **Fusager :**
    - Ajout de fonctionnalités pour la gestion des listes JDMA et l'expression d'avis. [#1248](https://github.com/SocialGouv/vao/issues/1248), [#1268](https://github.com/SocialGouv/vao/issues/1268)
    - Amélioration de l'affichage des informations et de la gestion des agréments dans l'interface Fusager. [#1266](https://github.com/SocialGouv/vao/issues/1266)
- **RGAA :**
    - Corrections pour améliorer l'accessibilité de l'application, notamment au niveau des labels et des boutons. [#1281](https://github.com/SocialGouv/vao/issues/1281)
- **Autres :**
    - Correction du formatage des adresses lors de la saisie. [#1284](https://github.com/SocialGouv/vao/issues/1284)
    - Correction de l'affichage des dates et du statut dans l'interface OVA. [#1294](https://github.com/SocialGouv/vao/issues/1294)
    - Correction de l'accès à la liste des usages. [#1293](https://github.com/SocialGouv/vao/issues/1293)

### Évolutions techniques
- Mise en place de tests E2E pour la gestion des personnes physiques et la suppression des utilisateurs. [#1235](https://github.com/SocialGouv/vao/issues/1235), [#1244](https://github.com/SocialGouv/vao/issues/1244)
- Refactoring et nettoyage du code, notamment dans la gestion des requêtes et des composants d'interface utilisateur.
- Passage de certains composants en TypeScript.
- Amélioration de la gestion des fichiers et des doublons lors de l'upload de documents. [#1295](https://github.com/SocialGouv/vao/issues/1295)
- Optimisation de la construction des requêtes pour supprimer les paramètres vides. [#1285](https://github.com/SocialGouv/vao/issues/1285)

### Autres changements
- Mise à jour de la documentation.
- Corrections mineures et améliorations de la qualité du code.
- Ajout de tests unitaires.
- Suppression de code inutile.
