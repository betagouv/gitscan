## Changelog : zacharie (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'interface utilisateur, notamment pour la création et la gestion des fiches de traçabilité. Des corrections de bugs et des améliorations de sécurité ont également été apportées, ainsi que des optimisations pour l'administration et le suivi des données. L'ajout de tableaux de bord et de filtres permet un meilleur suivi de l'activité.

### Évolutions fonctionnelles
- Amélioration de l'interface utilisateur pour la création de fiches, avec un meilleur flux d'utilisation. [#281](https://github.com/betagouv/zacharie/issues/281)
- Ajout de filtres par premier détenteur et CCG (Code Commun de Gestion) sur le tableau de bord. [#267](https://github.com/betagouv/zacharie/issues/267)
- Implémentation d'un nouveau tableau de bord pour l'administration, permettant la visualisation des saisies SVI (Suivi Vie Intégrée) avec taux et motifs. [#266](https://github.com/betagouv/zacharie/issues/266)
- Ajout d'un tableau de bord public présentant une matrice d'impact. [#272](https://github.com/betagouv/zacharie/issues/272)
- Possibilité de visualiser les carcasses même si elles appartiennent à un seul groupe. [#287](https://github.com/betagouv/zacharie/issues/287)
- Amélioration de l'accessibilité avec l'ajout d'attributs `alt` pour les iframes. [#274](https://github.com/betagouv/zacharie/issues/274)
- Ajout de la gestion de l'usage domestique. [#16f6ad2](https://github.com/betagouv/zacharie/commit/16f6ad2)

### Évolutions techniques
- Refonte du système de routage pour optimiser les performances et la gestion des requêtes. [#310](https://github.com/betagouv/zacharie/issues/310), [#308](https://github.com/betagouv/zacharie/issues/308), [#295](https://github.com/betagouv/zacharie/issues/295)
- Amélioration de la gestion des invitations. [#309](https://github.com/betagouv/zacharie/issues/309)
- Mise en place d'un script de build optimisé. [#300](https://github.com/betagouv/zacharie/issues/300)
- Ajout de tests Playwright et Vitest.
- Mise à jour des dépendances pour corriger des vulnérabilités de sécurité. [#280](https://github.com/betagouv/zacharie/issues/280)
- Amélioration de la sécurité avec l'ajout de Content Security Policy (CSP) et la correction de failles potentielles. [#275](https://github.com/betagouv/zacharie/issues/275), [#278](https://github.com/betagouv/zacharie/issues/278), [#235](https://github.com/betagouv/zacharie/issues/235), [#239](https://github.com/betagouv/zacharie/issues/239), [#240](https://github.com/betagouv/zacharie/issues/240), [#241](https://github.com/betagouv/zacharie/issues/241)
- Ajout de pre-commit hooks pour formater le code automatiquement. [#246](https://github.com/betagouv/zacharie/issues/246)
- Suppression de code inutilisé et nettoyage du code.

### Autres changements
- Désactivation de Claude. [#2868afb](https://github.com/betagouv/zacharie/commit/2868afb)
- Amélioration de la documentation et des messages d'erreur.
- Correction de problèmes d'affichage et de responsivité. [#289](https://github.com/betagouv/zacharie/issues/289)
- Correction de bugs divers sur l'interface utilisateur. [#311](https://github.com/betagouv/zacharie/issues/311), [#306](https://github.com/betagouv/zacharie/issues/306), [#305](https://github.com/betagouv/zacharie/issues/305), [#301](https://github.com/betagouv/zacharie/issues/301)
- Correction de problèmes liés aux entités fantômes. [#252](https://github.com/betagouv/zacharie/issues/252)
- Correction de problèmes de tri. [#5f2bec3](https://github.com/betagouv/zacharie/commit/5f2bec3)
