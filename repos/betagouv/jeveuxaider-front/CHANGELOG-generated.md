## Changelog : jeveuxaider-front (30 derniers jours)

### Résumé
Les dernières semaines ont été marquées par une refonte importante de plusieurs parties de l'application, notamment le tableau de bord, les statistiques d'administration et la gestion des missions. Des améliorations ont été apportées à la recherche de missions avec l'intégration d'Algolia, et des corrections de bugs ont été implémentées pour améliorer la stabilité et l'expérience utilisateur. Une campagne spéciale "Février pour protéger" a été intégrée avec l'ajout d'un quiz dédié.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité permettant de consulter et d'évaluer les témoignages (#271).
- Amélioration de la gestion des missions avec l'ajout d'un champ "ouvert aux mineurs" et de la logique associée (#251).
- Intégration d'Algolia pour améliorer la recherche de missions (#245).
- Ajout d'un quiz pour la campagne "Février pour protéger" (#240).
- Amélioration de l'affichage des badges "complet" et "clos" sur les cartes missions (#260).
- Ajout d'alertes pour les utilisateurs inactifs (#242).
- Amélioration de la validation du numéro RNA, acceptant désormais les caractères alphanumériques (#472e9aa).
- Ajout de la possibilité de gérer les organisations et réseaux avec des statistiques et des décomptes (#a1efb5d).
- Ajout d'une fonctionnalité pour améliorer le texte avec l'IA dans l'éditeur CKEditor, avec un texte d'aide amélioré (#0f20f2e).
- Ajout de la possibilité de créer une mission et de vider le formulaire après la création (#241).
- Ajout de la gestion des référents et responsables (#244).

### Évolutions techniques
- Refactorisation de l'utilisation de Plausible dans un plugin client (#265).
- Refactorisation de l'utilisation des stores, en accédant directement aux stores au lieu de `$stores` (#235).
- Mise à jour de Nuxt à la version 3.21.1 (#264, #236).
- Refactorisation de la récupération des vignettes de missions pour gérer les modèles manquants (#fe8837f).
- Amélioration de la gestion des erreurs et des options de requête dans `useFetcher` (#243).
- Mise à jour des imports pour utiliser `#app` au lieu de `#imports` dans plusieurs composants et pages (#d373390, #080c08d).
- Correction d'un problème empêchant le chargement correct du plugin d'authentification (#147af45).
- Abandon temporaire d'un downgrade de Vue (#262).
- Suppression des appels potentiellement bloquants lors du changement de route (#255).
- Suppression de code commenté et d'imports inutilisés dans `useAlgoliaQueryBuilder` (#038eb4a).
- Ajout d'un fichier `.nvmrc` pour spécifier la version de Node.js (24) (#555b016).

### Autres changements
- Correction de l'étiquette et de la description du résumé pour les notifications bi-hebdomadaires (#d025269).
- Clarification de l'étiquette pour l'accès mineur dans le formulaire de modèle de mission (#943b5bf).
- Suppression de sections d'API Engagement dans le menu latéral et le menu secondaire des statistiques (#0c2e943, #db4f1b2).
- Correction de l'URL du tableau de bord dans la configuration Nuxt (#7d6ab3d).
- Suppression d'une marge inutile dans la section de localisation de la carte mission (#e455daa).
- Correction de la récupération de l'URL de la vignette de mission (#06f78e6).
- Mise à jour de plusieurs dépendances (ajv, tar, fast-xml-parser, qs, axios, lodash, lodash-es, @isaacs/brace-expansion) (#270, #269, #268, #267, #263, #239, #238, #237, #249).
