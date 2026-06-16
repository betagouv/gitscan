## Changelog : infomedicament (30 derniers jours, au 15 juin 2026)

### Résumé
Ce mois-ci, l'équipe s'est concentrée sur l'amélioration de la performance et de la pertinence des résultats de recherche, ainsi que sur l'ajout de nouvelles fonctionnalités de recherche sémantique basées sur l'IA. Des améliorations ont également été apportées à l'interface utilisateur, notamment la refonte des cartes de résultats et l'ajout d'une date de dernière mise à jour des données. Enfin, des efforts ont été faits pour simplifier l'analyse et supprimer des outils de suivi obsolètes.

### Évolutions fonctionnelles
- **Recherche :** Amélioration de la recherche pour inclure les médicaments portant des noms de marque dans les résultats de recherche de substances [#4e943d5](https://github.com/betagouv/infomedicament/commit/4e943d5).
- **Recherche sémantique :** Ajout d'une nouvelle fonctionnalité de recherche sémantique utilisant un modèle de langage (LLM) pour répondre aux questions des utilisateurs et mettre en évidence les informations pertinentes dans les notices de médicaments.  Cette fonctionnalité inclut une recherche plein texte et une mise en évidence des phrases correspondantes [#7721df4](https://github.com/betagouv/infomedicament/commit/7721df4).
- **Nouvelle page médicament :** Refonte complète de la page de détail d'un médicament [#222](https://github.com/betagouv/infomedicament/pull/222).
- **Filtres de recherche :** Refonte des filtres de recherche avec une nouvelle version (v2) et des améliorations de l'interface utilisateur [#194](https://github.com/betagouv/infomedicament/pull/194).
- **Date de mise à jour :** Ajout d'une indication de la date de dernière mise à jour des données [#c800e29](https://github.com/betagouv/infomedicament/commit/c800e29).
- **Cartes de résultats :** Nouvelle conception des cartes de résultats de recherche [#fb9375d](https://github.com/betagouv/infomedicament/commit/fb9375d).

### Évolutions techniques
- **Performance :** Pré-rendu des 500 médicaments les plus consultés au moment de la construction (build time) pour améliorer la vitesse de chargement [#93ec820](https://github.com/betagouv/infomedicament/commit/93ec820).
- **Performance :** Déplacement de la récupération des données vers le serveur (Server Components) pour les génériques, les médicaments et les définitions, améliorant ainsi les performances globales [#b3a46cd](https://github.com/betagouv/infomedicament/commit/b3a46cd), [#64b63ee](https://github.com/betagouv/infomedicament/commit/64b63ee), [#f15834a](https://github.com/betagouv/infomedicament/commit/f15834a).
- **Infrastructure :** Vérification de la présence de données dans PostgreSQL avant de générer les pages de médicaments [#8b9611d](https://github.com/betagouv/infomedicament/commit/8b9611d).
- **Analyse :** Suppression de Hotjar et passage de Matomo en mode cookieless pour améliorer la confidentialité et les performances [#06058ff](https://github.com/betagouv/infomedicament/commit/06058ff), [#c6c52d0](https://github.com/betagouv/infomedicament/commit/c6c52d0).
- **Configuration :** Activation du mode `react-jsx` [#99cb6a8](https://github.com/betagouv/infomedicament/commit/99cb6a8).

### Autres changements
- **Documentation :** Ajout d'un commentaire "TODO" pour l'amélioration future de la fonction `getIndicationsBlock` [#4bb0690](https://github.com/betagouv/infomedicament/commit/4bb0690).
- **Tests :** Ajout et amélioration des tests unitaires et d'intégration, notamment pour la recherche sémantique et la nouvelle page médicament [#29ec51a](https://github.com/betagouv/infomedicament/commit/29ec51a), [#cf24ed0](https://github.com/betagouv/infomedicament/commit/cf24ed0), [#6aa8f02](https://github.com/betagouv/infomedicament/commit/6aa8f02).
- **Nettoyage de code :** Suppression de code obsolète lié à HyDE/OpenSearch [#1c066b4](https://github.com/betagouv/infomedicament/commit/1c066b4).
- **Correction :** Copie du fichier `resume_specialites` dans les environnements de revue (review apps) [#831d18e](https://github.com/betagouv/infomedicament/commit/831d18e).
- **Correction :** Correction d'un problème avec les icônes de grossesse, d'allaitement, de pédiatrie et de conduite [#f3f35de](https://github.com/betagouv/infomedicament/commit/f3f35de).
- **Correction :** Correction de la requête pour les alertes de grossesse [#fd277c0](https://github.com/betagouv/infomedicament/commit/fd277c0).
- **Correction :** Suppression d'une classe DSFR invalide [#8345b10](https://github.com/betagouv/infomedicament/commit/8345b10).
- **Correction :** Correction d'un bug dans le parsing de l'ID de bloc pour la recherche sémantique [#686df85](https://github.com/betagouv/infomedicament/commit/686df85).
- **Correction :** Correction d'un conflit de `scrollIntoView` avec la mise en évidence de la recherche sémantique [#01ba308](https://github.com/betagouv/infomedicament/commit/01ba308).
- **Correction :** Correction du type de l'helper `block()` pour accepter une chaîne de caractères ou un tableau de chaînes de caractères [#0a37d51](https://github.com/betagouv/infomedicament/commit/0a37d51).
