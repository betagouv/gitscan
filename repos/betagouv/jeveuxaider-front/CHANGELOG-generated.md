## Changelog : jeveuxaider-front (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la plateforme "Je veux aider" en ajoutant de nouvelles fonctionnalités pour faciliter l'engagement citoyen, notamment concernant les missions ouvertes aux mineurs et les élections municipales. Des corrections de bugs et des améliorations de l'interface ont également été apportées pour une meilleure expérience utilisateur. Des efforts ont été faits pour améliorer la robustesse et la performance de l'application.

### Évolutions fonctionnelles
- Ajout de la possibilité de sélectionner une région référente avec des options multisélection dans les filtres de recherche. [#266](https://github.com/betagouv/jeveuxaider-front/pull/266)
- Ajout d'une section dédiée aux élections municipales avec des statistiques et des liens utiles. [#274](https://github.com/betagouv/jeveuxaider-front/pull/274)
- Possibilité de consulter et de valider les témoignages des utilisateurs. [#271](https://github.com/betagouv/jeveuxaider-front/pull/271)
- Amélioration de la gestion des inscriptions avec l'ajout de badges indiquant si une mission est complète ou clôturée. [#260](https://github.com/betagouv/jeveuxaider-front/pull/260)
- Ajout d'un champ "ouvert aux mineurs" et de la logique correspondante dans les modèles de mission. [#251](https://github.com/betagouv/jeveuxaider-front/pull/251)
- Ajout de directives pour l'accueil de volontaires mineurs dans une nouvelle section d'accordéon. [#278](https://github.com/betagouv/jeveuxaider-front/pull/278)
- Ajout de nouvelles régions pour les DOM-TOM dans la configuration des labels. [#281](https://github.com/betagouv/jeveuxaider-front/pull/281)
- Clarification du libellé pour l'accès des mineurs dans le modèle de mission. [#274](https://github.com/betagouv/jeveuxaider-front/pull/274)

### Évolutions techniques
- Mise à jour de Nuxt à la version 3.21.1. [#264](https://github.com/betagouv/jeveuxaider-front/pull/264)
- Refactorisation de l'utilisation de `useRoute` et `useRouter` pour utiliser `#app` au lieu de `#imports`. [#256](https://github.com/betagouv/jeveuxaider-front/pull/256)
- Amélioration de la gestion des appels en cours lors du changement de route pour éviter les fuites de mémoire. [#255](https://github.com/betagouv/jeveuxaider-front/pull/255)
- Refactorisation de la gestion du crop manuel pour utiliser des tableaux au lieu de chaînes de caractères. [#266](https://github.com/betagouv/jeveuxaider-front/pull/266)
- Mise en place d'un plugin client pour gérer Plausible. [#265](https://github.com/betagouv/jeveuxaider-front/pull/265)
- Correction d'une vulnérabilité dans la dépendance `ajv`. [#270](https://github.com/betagouv/jeveuxaider-front/pull/270)
- Mise à jour de la gestion du token d'impersonation après une mise à niveau de Laravel Passport. [#276](https://github.com/betagouv/jeveuxaider-front/pull/276)
- Correction de la condition de statut de chargement dans le composant `BaseBox`. [#280](https://github.com/betagouv/jeveuxaider-front/pull/280)
- Amélioration de la gestion des erreurs avec des messages plus détaillés et des ajustements de mise en page. [#273](https://github.com/betagouv/jeveuxaider-front/pull/273)

### Autres changements
- Refactorisation des espaces tableau de bord et profil. [#259](https://github.com/betagouv/jeveuxaider-front/pull/259)
- Refactorisation des statistiques d'administration. [#258](https://github.com/betagouv/jeveuxaider-front/pull/258)
- Mise à jour de la validation du numéro RNA pour autoriser les caractères alphanumériques. [#261](https://github.com/betagouv/jeveuxaider-front/pull/261)
- Suppression de sections API Engagement dans le menu latéral et le menu secondaire des statistiques. [#261](https://github.com/betagouv/jeveuxaider-front/pull/261)
- Amélioration de la description des notifications bi-hebdomadaires dans le formulaire de gestion des notifications utilisateur. [#263](https://github.com/betagouv/jeveuxaider-front/pull/263)
- Correction de l'affichage des filtres de facettes pour refléter les tags d'élections actuels. [#277](https://github.com/betagouv/jeveuxaider-front/pull/277)
- Correction d'un bug dans la récupération des dates de filtres. [#277](https://github.com/betagouv/jeveuxaider-front/pull/277)
- Suppression du padding inutile sur le bouton d'ajout d'email. [#267](https://github.com/betagouv/jeveuxaider-front/pull/267)
