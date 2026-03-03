## Changelog : jeveuxaider-front (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la plateforme "Je veux aider" en se concentrant sur de nouvelles fonctionnalités pour les missions (notamment l'ouverture aux mineurs et les statistiques), l'amélioration de l'expérience utilisateur (gestion des erreurs, validation des formulaires) et des refactorings techniques pour une meilleure maintenance et performance. Une nouvelle section dédiée aux élections municipales a également été ajoutée.

### Évolutions fonctionnelles
- Ajout d'une section dédiée aux élections municipales avec des statistiques et des liens vers des informations pertinentes. [#272](https://github.com/betagouv/jeveuxaider-front/issues/272)
- Possibilité de spécifier si une mission est ouverte aux mineurs lors de sa création. [#251](https://github.com/betagouv/jeveuxaider-front/issues/251)
- Amélioration de la validation du numéro RNA des organisations, acceptant désormais les caractères alphanumériques. [#472e9aa](https://github.com/betagouv/jeveuxaider-front/commit/472e9aa)
- Ajout de badges indiquant le nombre d'inscriptions complètes et clôturées sur les missions. [#260](https://github.com/betagouv/jeveuxaider-front/issues/260)
- Ajout d'une fonctionnalité de revue des témoignages. [#271](https://github.com/betagouv/jeveuxaider-front/issues/271)
- Ajout de la possibilité de sélectionner un référent régional lors de la recherche de missions. [#6e08e99](https://github.com/betagouv/jeveuxaider-front/commit/6e08e99)
- Amélioration des messages d'erreur pour une meilleure clarté et une meilleure expérience utilisateur. [#1192886](https://github.com/betagouv/jeveuxaider-front/commit/1192886)
- Amélioration des descriptions des notifications dans le formulaire de gestion des notifications utilisateur. [#d025269](https://github.com/betagouv/jeveuxaider-front/commit/d025269)
- Clarification du libellé pour l'accès mineur dans le formulaire de création de mission. [#943b5bf](https://github.com/betagouv/jeveuxaider-front/commit/943b5bf)

### Évolutions techniques
- Refactorisation de la gestion des images de crop pour utiliser des tableaux au lieu de chaînes de caractères. [#c137647](https://github.com/betagouv/jeveuxaider-front/commit/c137647)
- Mise à jour de Nuxt à la version 3.21.1. [#264](https://github.com/betagouv/jeveuxaider-front/issues/264)
- Refactorisation de l'import des modules `useRoute` et `useRouter` pour utiliser `#app` au lieu de `#imports`. [#d373390](https://github.com/betagouv/jeveuxaider-front/commit/d373390)
- Implémentation d'un plugin pour gérer l'intégration de Plausible Analytics. [#265](https://github.com/betagouv/jeveuxaider-front/issues/265)
- Refactorisation de la logique de fetch dans un plugin API dédié. [#253](https://github.com/betagouv/jeveuxaider-front/issues/253)
- Mise en place d'une gestion des appels en attente lors du changement de route pour améliorer la performance. [#af24eea](https://github.com/betagouv/jeveuxaider-front/commit/af24eea)
- Mise à jour de la version de Vue (temporairement annulée puis rétablie). [#257](https://github.com/betagouv/jeveuxaider-front/issues/257)
- Mise à jour de la version de Axios. [#263](https://github.com/betagouv/jeveuxaider-front/issues/263)
- Mise à jour de la version de Algolia. [#245](https://github.com/betagouv/jeveuxaider-front/issues/245)
- Ajout d'un fichier `.nvmrc` pour spécifier la version de Node utilisée (24). [#555b016](https://github.com/betagouv/jeveuxaider-front/commit/555b016)

### Autres changements
- Mise à jour de plusieurs dépendances (devalue, swiper, tar, fast-xml-parser, qs, minimatch, ajv, @isaacs/brace-expansion) pour corriger des vulnérabilités et améliorer la stabilité. [#273](https://github.com/betagouv/jeveuxaider-front/issues/273), [#275](https://github.com/betagouv/jeveuxaider-front/issues/275), [#269](https://github.com/betagouv/jeveuxaider-front/issues/269), [#268](https://github.com/betagouv/jeveuxaider-front/issues/268), [#267](https://github.com/betagouv/jeveuxaider-front/issues/267), [#270](https://github.com/betagouv/jeveuxaider-front/issues/270), [#249](https://github.com/betagouv/jeveuxaider-front/issues/249)
- Suppression d'éléments de menu obsolètes liés à l'API Engagement. [#0c2e943](https://github.com/betagouv/jeveuxaider-front/commit/0c2e943), [#db4f1b2](https://github.com/betagouv/jeveuxaider-front/commit/db4f1b2)
- Amélioration de l'interface utilisateur pour l'alerte des utilisateurs absents. [#042138c](https://github.com/betagouv/jeveuxaider-front/commit/042138c)
- Refactorisation du dashboard et des espaces profil. [#259](https://github.com/betagouv/jeveuxaider-front/issues/259)
- Refactorisation des statistiques d'administration. [#258](https://github.com/betagouv/jeveuxaider-front/issues/258)
- Correction de l'initialisation de `auth-init` pour garantir que le plugin API est chargé en premier. [#147af45](https://github.com/betagouv/jeveuxaider-front/commit/147af45)
- Suppression d'une marge inutile dans la section de localisation des missions. [#e455daa](https://github.com/betagouv/jeveuxaider-front/commit/e455daa)
- Suppression d'imports inutilisés et de code commenté dans `useAlgoliaQueryBuilder`. [#038eb4a](https://github.com/betagouv/jeveuxaider-front/commit/038eb4a)
- Mise à jour de la gestion des types d'organisation et de réseau pour inclure des statistiques optionnelles. [#a1efb5d](https://github.com/betagouv/jeveuxaider-front/commit/a1efb5d)
- Ajout d'une transformation `emptyToNull` pour la validation des chaînes de caractères et amélioration de la gestion du champ téléphone. [#a36c084](https://github.com/betagouv/jeveuxaider-front/commit/a36c084)
- Mise à jour de la validation des missions et désactivation de l'étape dans la barre latérale si elle est incomplète. [#91ae44d](https://github.com/betagouv/jeveuxaider-front/commit/91ae44d)
