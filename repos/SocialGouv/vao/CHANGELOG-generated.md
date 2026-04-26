## Changelog : vao (30 derniers jours, au 24 avril 2026)

### Résumé
Ce changelog couvre une période d'intenses améliorations et corrections, principalement axées sur le module d'agrément et les parcours de renouvellement. Les efforts se sont concentrés sur la conformité RGAA, l'amélioration de l'expérience utilisateur, notamment dans la gestion des documents et des messages, et la correction de bugs impactant les étapes clés des processus. Des améliorations techniques ont également été apportées pour la qualité du code et l'automatisation des tests.

### Évolutions fonctionnelles
- **Agrément :**
    - Ajout de la gestion des messages non lus pour les agréments côté DREETS. [#1272](https://github.com/SocialGouv/vao/issues/1272)
    - Amélioration de l'interface pour la gestion des documents d'agrément dans le back-office. [#1270](https://github.com/SocialGouv/vao/issues/1270) et [#1269](https://github.com/SocialGouv/vao/issues/1269)
    - Ajout de la possibilité de donner un avis sur les agréments dans le fusager. [#1268](https://github.com/SocialGouv/vao/issues/1268)
    - Ajout d'une action pour refuser un agrément dans le back-office. [#1245](https://github.com/SocialGouv/vao/issues/1245)
    - Amélioration de l'affichage des boutons et labels pour une meilleure accessibilité (RGAA). [#1281](https://github.com/SocialGouv/vao/issues/1281)
- **Renouvellement d'agrément :**
    - Corrections et améliorations des étapes 1, 2, 3 et 4 du processus de renouvellement d'agrément. [#1282](https://github.com/SocialGouv/vao/issues/1282), [#1279](https://github.com/SocialGouv/vao/issues/1279), [#1259](https://github.com/SocialGouv/vao/issues/1259), [#1258](https://github.com/SocialGouv/vao/issues/1258), [#1265](https://github.com/SocialGouv/vao/issues/1265)
    - Correction de problèmes de validation en brouillon lors de l'étape 2 du renouvellement. [#1279](https://github.com/SocialGouv/vao/issues/1279)
- **Autres :**
    - Amélioration de l'affichage du nom et prénom des personnes dans l'OVA. [#1273](https://github.com/SocialGouv/vao/issues/1273)

### Évolutions techniques
- Refactoring et migration de code JavaScript vers TypeScript dans certaines parties du module d'agrément.
- Amélioration de la gestion des requêtes avec suppression des paramètres vides. [#1285](https://github.com/SocialGouv/vao/issues/1285)
- Mise à jour des pré-commits pour vérifier l'absence de `console.log` dans le code. [#1246](https://github.com/SocialGouv/vao/issues/1246)
- Amélioration des tests E2E pour la suppression d'utilisateurs et la gestion des personnes physiques. [#1235](https://github.com/SocialGouv/vao/issues/1235) et [#1244](https://github.com/SocialGouv/vao/issues/1244)
- Nettoyage du code et suppression de code obsolète dans `shared-ui`. [#1234](https://github.com/SocialGouv/vao/issues/1234)

### Autres changements
- Documentation mise à jour pour refléter les changements apportés.
- Corrections mineures et ajustements de l'interface utilisateur.
- Amélioration de la gestion des erreurs et des logs.
