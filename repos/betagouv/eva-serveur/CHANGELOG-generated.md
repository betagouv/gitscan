## Changelog : eva-serveur (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface utilisateur avec une migration vers le Design System Fr (DSFR) pour une meilleure cohérence visuelle et accessibilité. Des corrections de bugs et des optimisations de performance ont également été apportées, notamment concernant la gestion des structures, des comptes utilisateurs et des actualités. Des fonctionnalités liées à la gestion des opérateurs de compétences ont été ajoutées.

### Évolutions fonctionnelles
- Les structures Opérateurs de compétences peuvent désormais être créées, modifiées et consultées. [#66d7cda](https://github.com/betagouv/eva-serveur/commit/66d7cda)
- Possibilité de filtrer les structures par numéro SIRET. [#7efed90](https://github.com/betagouv/eva-serveur/commit/7efed90)
- Amélioration de l'affichage et de la gestion des comptes en attente. [#2026-05-05T11:33:47+02:00](https://github.com/betagouv/eva-serveur/commit/de8e501)
- Correction de la redirection pour les comptes ProConnect sans structure. [#39c2887](https://github.com/betagouv/eva-serveur/commit/39c2887)
- Ajout d'une méthode pour calculer la complétude des évaluations EVAPRO. [#8e02961](https://github.com/betagouv/eva-serveur/commit/8e02961)
- Possibilité de fermer la modale de validation en attente en cliquant sur le fond. [#d28aa70](https://github.com/betagouv/eva-serveur/commit/d28aa70)
- Amélioration de l'affichage des actualités et des évaluations pour EvaPro. [#983496b](https://github.com/betagouv/eva-serveur/commit/983496b)
- Ajout de la possibilité de générer des PDF en environnement de développement. [#e1a4388](https://github.com/betagouv/eva-serveur/commit/e1a4388)

### Évolutions techniques
- Migration progressive de l'interface utilisateur vers le Design System Fr (DSFR). Cela inclut le remplacement des classes Bootstrap par les composants DSFR.
- Refactor de la logique de formatage du SIRET pour une meilleure maintenabilité. [#89bd691](https://github.com/betagouv/eva-serveur/commit/89bd691)
- Suppression des utilities Bootstrap obsolètes. [#241d9a8](https://github.com/betagouv/eva-serveur/commit/241d9a8)
- Mise à jour des dépendances : jwt, nokogiri, erb, postcss.
- Suppression de code mort et de fonctionnalités obsolètes (pages 'structures', 'nouvelle_structure', action 'rejoindre_structure', etc.).
- Amélioration de la performance en corrigeant un problème N+1 sur la page des actualités. [#08c97b1](https://github.com/betagouv/eva-serveur/commit/08c97b1)
- Refactor de la gestion des modales. [#8283a46](https://github.com/betagouv/eva-serveur/commit/8283a46)
- Ajout d'un composant Metabase iframe pour les structures. [#323a686](https://github.com/betagouv/eva-serveur/commit/323a686)

### Autres changements
- Documentation de la variable d'environnement du tableau Metabase des OPCO. [#038260f](https://github.com/betagouv/eva-serveur/commit/038260f)
- Suppression de fichiers inutilisés et nettoyage du code.
- Corrections de tests suite aux mises à jour de dépendances et aux modifications du code.
- Corrections de style et d'alignement pour améliorer l'apparence visuelle.
- Ajout de tests pour certaines corrections de bugs.
- Suppression des informations de géolocalisation inutilisées. [#fd343b5](https://github.com/betagouv/eva-serveur/commit/fd343b5)
- Ajout de migration pour créer les réponses "je ne sais pas" sur les questions des Impacts et risques. [#66d7cda](https://github.com/betagouv/eva-serveur/commit/66d7cda)
