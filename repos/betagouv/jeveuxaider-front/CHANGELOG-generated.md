## Changelog : jeveuxaider-front (30 derniers jours)

### Résumé
Ce mois-ci, l'application "Je veux aider" a bénéficié d'une série d'améliorations visant à faciliter la recherche de missions de bénévolat, à optimiser l'administration des organisations et des missions, et à améliorer l'expérience utilisateur globale. Des corrections de bugs et des mises à jour techniques ont également été apportées pour assurer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Ajout d'une section dédiée aux élections municipales avec un lien externe s'ouvrant dans un nouvel onglet (#272).
- Possibilité de sélectionner des référents régionaux avec une sélection multiple (#266).
- Ajout d'une fonctionnalité de revue des témoignages (#271).
- Amélioration de la gestion des notifications : clarification des libellés et descriptions pour les notifications bi-hebdomadaires (#274).
- Clarification du libellé pour l'accès mineur dans le formulaire de création de mission (#268).
- Ajout d'un champ "est ouvert aux mineurs" et de la logique correspondante dans les modèles de mission (#251).
- Ajout d'une section "Février pour protéger" et mise à jour des statistiques associées (#258).
- Refonte des espaces tableau de bord et profil (#259).
- Refonte des statistiques d'administration (#258).
- Amélioration de la recherche Algolia (#245).
- Ajout de badges "complet" et "clos" pour les inscriptions aux missions (#260).
- Ajout d'une alerte pour les utilisateurs inactifs (#247).
- Ajout de la possibilité de gérer les types d'organisations et de réseaux avec des statistiques optionnelles (#253).
- Amélioration de la validation des numéros RNA pour autoriser les caractères alphanumériques (#242).
- Ajout de la gestion des référents et responsables (#244).
- Amélioration de la récupération des miniatures de mission (#246, #257).

### Évolutions techniques
- Mise à jour de la gestion des tokens d'impersonation après la mise à niveau de Laravel Passport 13 (#276).
- Refactorisation de la gestion de `manualCrop` pour utiliser des tableaux au lieu de chaînes de caractères (#266).
- Mise à jour de Nuxt à la version 3.21.1 (#264, #247).
- Refactorisation de l'utilisation de Plausible dans un plugin client (#265).
- Mise à jour des imports pour utiliser `#app` au lieu de `#imports` dans plusieurs composants et pages (#252).
- Abandon des appels en attente lors du changement de route (#255).
- Refactorisation de `useAlgoliaQueryBuilder` pour supprimer les imports inutilisés et les événements de suivi commentés (#254).
- Mise en place d'un fichier `.nvmrc` pour spécifier la version de Node.js (24) (#253).
- Refactorisation de la logique de récupération de l'API pour les contenus d'administration (#261).
- Amélioration de la validation et de la désactivation de l'étape de mission dans la barre latérale (#250).
- Correction d'un problème d'importation de `auth-init` (#249).

### Autres changements
- Mise à jour de la version de minimatch (#275).
- Mises à jour de plusieurs dépendances : `devalue`, `swiper`, `fast-xml-parser`, `qs`, `@isaacs/brace-expansion`, `axios` (ces mises à jour sont gérées par Dependabot et ne sont pas détaillées individuellement).
- Suppression de sections API Engagement du menu dans la barre latérale et le menu secondaire des statistiques (#262).
- Correction d'un problème de marge inutile dans la section de localisation de la carte mission (#248).
- Correction de la récupération de l'URL de la miniature de mission (#257).
