## Changelog : zacharie (30 derniers jours, au 07 mai 2026)

### Résumé
Ce mois-ci, l'application Zacharie a bénéficié d'améliorations significatives de l'interface utilisateur, notamment au niveau des fiches, des tableaux de bord et de la gestion des carcasses. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la fiabilité de l'application, ainsi que des optimisations pour l'utilisation hors ligne et la gestion des erreurs.

### Évolutions fonctionnelles
- Ajout de la possibilité d'afficher les commentaires des intermédiaires dans la modale d'une fiche. [#358](https://github.com/betagouv/zacharie/issues/358)
- Amélioration des filtres pour les collecteurs. [#357](https://github.com/betagouv/zacharie/issues/357)
- Nouvelle sidebar pour l'ETG. [#351](https://github.com/betagouv/zacharie/issues/351)
- Ajout d'un tableau de bord FND/FDC. [#330](https://github.com/betagouv/zacharie/issues/330)
- Ajout de la liste des lésions. [#331](https://github.com/betagouv/zacharie/issues/331)
- Amélioration de l'affichage des cartes carcasses. [#312](https://github.com/betagouv/zacharie/issues/312)
- Ajout des headers SVI/FEI et FEI/ETG. [#323](https://github.com/betagouv/zacharie/issues/323), [#319](https://github.com/betagouv/zacharie/issues/319)
- Amélioration du flux d'ajout de carcasses. [#284](https://github.com/betagouv/zacharie/issues/284)
- Ajout d'un bouton de connexion pour les utilisateurs administrateurs.
- Ajout de routes pour les circuits courts. [#310](https://github.com/betagouv/zacharie/issues/310)
- Ajout de routes pour les collecteurs. [#308](https://github.com/betagouv/zacharie/issues/308)
- Ajout d'une route pour le SVI. [#296](https://github.com/betagouv/zacharie/issues/296)

### Évolutions techniques
- Correction de tests aléatoires (flaky tests). [#352](https://github.com/betagouv/zacharie/issues/352)
- Mise à jour de la gestion des cookies pour les environnements de staging et de production.
- Passage de l'application sur le domaine `zacharie.incubateur.net`. [#350](https://github.com/betagouv/zacharie/issues/350)
- Implémentation d'un système de bearer token pour les appels API. [#336](https://github.com/betagouv/zacharie/issues/336)
- Amélioration de la gestion des erreurs et des messages d'erreur.
- Optimisation de la pagination des carcasses pour éviter les limitations de 100 lignes. [#329](https://github.com/betagouv/zacharie/issues/329)
- Amélioration de la gestion des images stockées localement. [#328](https://github.com/betagouv/zacharie/issues/328)
- Ajout de support pour l'utilisation hors ligne avec Expo. [#327](https://github.com/betagouv/zacharie/issues/327)
- Refonte de la gestion des routes et des redirections.
- Ajout de tests E2E. [#340](https://github.com/betagouv/zacharie/issues/340), [#315](https://github.com/betagouv/zacharie/issues/315)
- Utilisation de Prettier pour formater le code. [#320](https://github.com/betagouv/zacharie/issues/320)

### Autres changements
- Correction de divers problèmes d'UI (sidebar, header, scroll-to-top, etc.). [#345](https://github.com/betagouv/zacharie/issues/345), [#348](https://github.com/betagouv/zacharie/issues/348), [#325](https://github.com/betagouv/zacharie/issues/325), [#322](https://github.com/betagouv/zacharie/issues/322), [#318](https://github.com/betagouv/zacharie/issues/318), [#313](https://github.com/betagouv/zacharie/issues/313), [#311](https://github.com/betagouv/zacharie/issues/311), [#306](https://github.com/betagouv/zacharie/issues/306), [#305](https://github.com/betagouv/zacharie/issues/305), [#301](https://github.com/betagouv/zacharie/issues/301)
- Correction de bugs liés au décompte des carcasses totales. [#344](https://github.com/betagouv/zacharie/issues/344)
- Correction de problèmes de déconnexion. [#341](https://github.com/betagouv/zacharie/issues/341)
- Correction de la clôture automatique des circuits courts. [#343](https://github.com/betagouv/zacharie/issues/343)
- Correction de problèmes de wording pour les motifs. [#342](https://github.com/betagouv/zacharie/issues/342)
- Correction de l'affichage du score BPH.
- Suppression d'un bouton inutile sur les fiches. [#347](https://github.com/betagouv/zacharie/issues/347)
- Mise à jour de la documentation E2E. [#340](https://github.com/betagouv/zacharie/issues/340)
- Nettoyage des logs.
- Suppression d'images volumineuses.
- Désactivation de Claude.
