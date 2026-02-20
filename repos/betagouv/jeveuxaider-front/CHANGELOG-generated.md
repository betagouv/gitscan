## Changelog : jeveuxaider-front (30 derniers jours)

### Résumé
Les dernières mises à jour de "Je veux aider" se concentrent sur l'amélioration de l'interface utilisateur, la correction de bugs et l'optimisation des performances. Des refactorings importants ont été effectués pour moderniser le code et préparer le terrain pour de nouvelles fonctionnalités, notamment l'intégration d'Algolia pour la recherche et l'amélioration de la gestion des missions. L'accent a également été mis sur la correction de problèmes de mémoire et l'amélioration de l'accessibilité.

### Évolutions fonctionnelles
- Ajout d'un champ `is_open_to_minors` et de la logique correspondante dans les templates de mission (#251).
- Amélioration de la validation du numéro RNA pour autoriser les caractères alphanumériques (#257).
- Ajout de badges "complet" et "clos" pour les inscriptions aux missions (#260).
- Refonte des espaces tableau de bord et profil (#259, #258).
- Intégration d'une page de quiz pour la campagne "Février pour protéger" (#240).
- Amélioration de l'affichage des organisations et réseaux avec des statistiques optionnelles (#241).
- Ajout d'une alerte pour les utilisateurs inactifs (#242).
- Intégration de la recherche Algolia (#245).
- Ajout de la possibilité de créer des missions et de vider le formulaire après la création (#241).
- Amélioration de la gestion des miniatures de missions (#246).
- Ajout de la gestion des référents et responsables (#244).

### Évolutions techniques
- Refactorisation de l'utilisation de Plausible Analytics dans un plugin client (#265).
- Refactorisation de l'API pour la gestion des contenus (#261).
- Mise à jour de Nuxt à la version 3.21.1 (#264, #236).
- Refactorisation de l'utilisation des stores Pinia pour éviter d'utiliser `$stores` directement (#235).
- Utilisation de `#app` au lieu de `#imports` pour les imports de `useRoute` et `useRouter` (#256, #252, #255).
- Suppression de code inutile et commentaires dans `useAlgoliaQueryBuilder` (#231).
- Correction d'un problème de chargement de `auth-init` avant le plugin API (#255).
- Suppression d'un hook de build manifest pour simplifier le processus de build (#233).
- Ajout de nettoyages pour les timeouts et watchers afin de prévenir les fuites de mémoire (#230, #232).
- Suppression de la restriction `maximum-scale` pour améliorer l'accessibilité (#236).
- Amélioration de la gestion des erreurs et des options de requête dans `useFetcher` (#243).
- Ajout d'un fichier `.nvmrc` pour spécifier la version de Node.js (24) (#250).

### Autres changements
- Résolution de vulnérabilités dans la dépendance `ajv` (#270).
- Mises à jour mineures de dépendances : `tar`, `fast-xml-parser`, `qs`, `axios`, `lodash-es`, `lodash` (#269, #268, #267, #263, #239, #238, #237).
- Correction de l'espacement du bouton d'ajout d'email (#253).
- Suppression de sections d'API Engagement dans le menu de navigation (#254).
- Correction d'un problème de conflit avec une propriété calculée dans `CardMissionPreview` (#255).
- Amélioration du texte d'infobulle pour la fonctionnalité d'amélioration de texte par IA dans CKEditor (#234).
