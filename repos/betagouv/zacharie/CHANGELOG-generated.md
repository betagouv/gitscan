## Changelog : zacharie (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, l'application Zacharie a bénéficié d'améliorations significatives en termes de sécurité, de gestion des utilisateurs et de l'interface utilisateur, notamment au niveau de l'administration et du suivi des données. Plusieurs corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout d'un nouveau tableau de bord public présentant une matrice d'impact. [#272](https://github.com/betagouv/zacharie/issues/272)
- Implémentation de filtres par premier détenteur et CCG (Collecteur de Carcasses Groupées) sur le tableau de bord. [#267](https://github.com/betagouv/zacharie/issues/267)
- Création d'une nouvelle interface pour la création de Fiches d'Enregistrement d'Intervention (FEI). [#219](https://github.com/betagouv/zacharie/issues/219)
- Ajout d'une vue administrateur pour la gestion des carcasses. [#256](https://github.com/betagouv/zacharie/issues/256)
- Ajout d'une liste d'entités pour l'administration. [#255](https://github.com/betagouv/zacharie/issues/255)
- Amélioration du flux de création de fiche pour une meilleure expérience utilisateur. [#281](https://github.com/betagouv/zacharie/issues/281)
- Amélioration de l'UX de la page des statistiques. [#273](https://github.com/betagouv/zacharie/issues/273)
- Ajout d'un tableau de bord administrateur pour les saisies SVI (Suivi Vie Intégrée) avec taux et motifs. [#266](https://github.com/betagouv/zacharie/issues/266)

### Évolutions techniques
- Refonte du système de routage pour optimiser les performances et la gestion des requêtes. [#310](https://github.com/betagouv/zacharie/issues/310), [#308](https://github.com/betagouv/zacharie/issues/308), [#293](https://github.com/betagouv/zacharie/issues/293), [#283](https://github.com/betagouv/zacharie/issues/283)
- Amélioration de la gestion des erreurs et des validations côté client.
- Mise en place de bonnes pratiques de sécurité (CSP, headers, etc.). [#278](https://github.com/betagouv/zacharie/issues/278), [#275](https://github.com/betagouv/zacharie/issues/275), [#260](https://github.com/betagouv/zacharie/issues/260), [#259](https://github.com/betagouv/zacharie/issues/259), [#235](https://github.com/betagouv/zacharie/issues/235)
- Correction de vulnérabilités de dépendances avec `npm audit fix`. [#280](https://github.com/betagouv/zacharie/issues/280)
- Suppression de code inutilisé et nettoyage général du code. [#297](https://github.com/betagouv/zacharie/issues/297)
- Amélioration du script de build. [#300](https://github.com/betagouv/zacharie/issues/300)

### Autres changements
- Corrections de bugs d'interface utilisateur (UI) concernant la création de fiches, l'affichage des fiches envoyées et les erreurs d'examinateur. [#313](https://github.com/betagouv/zacharie/issues/313), [#311](https://github.com/betagouv/zacharie/issues/311), [#306](https://github.com/betagouv/zacharie/issues/306), [#305](https://github.com/betagouv/zacharie/issues/305), [#301](https://github.com/betagouv/zacharie/issues/301), [#292](https://github.com/betagouv/zacharie/issues/292), [#291](https://github.com/betagouv/zacharie/issues/291), [#289](https://github.com/betagouv/zacharie/issues/289), [#286](https://github.com/betagouv/zacharie/issues/286), [#274](https://github.com/betagouv/zacharie/issues/274)
- Correction de bugs liés à la gestion des invitations et des carcasses. [#309](https://github.com/betagouv/zacharie/issues/309), [#287](https://github.com/betagouv/zacharie/issues/287), [#284](https://github.com/betagouv/zacharie/issues/284), [#262](https://github.com/betagouv/zacharie/issues/262), [#254](https://github.com/betagouv/zacharie/issues/254), [#252](https://github.com/betagouv/zacharie/issues/252), [#253](https://github.com/betagouv/zacharie/issues/253)
- Suppression de la configuration de Claude. [#2868afb](https://github.com/betagouv/zacharie/commit/2868afb)
- Correction de problèmes liés à l'affichage des entités fantômes. [#252](https://github.com/betagouv/zacharie/issues/252)
- Amélioration de l'accessibilité (balises alt pour les iframes). [#274](https://github.com/betagouv/zacharie/issues/274)
- Suppression du rôle administrateur dans les rôles utilisateurs. [#248](https://github.com/betagouv/zacharie/issues/248)
- Correction de problèmes liés au rafraîchissement des FEI. [#250](https://github.com/betagouv/zacharie/issues/250)
- Mise en place de logs uniquement pour les utilisateurs connectés. [#261](https://github.com/betagouv/zacharie/issues/261)
- Correction de problèmes de confidentialité. [#81c9453](https://github.com/betagouv/zacharie/commit/81c9453)
