## Changelog : jeveuxaider-front (30 derniers jours, au 17 mars 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment dans la gestion des missions, des profils et des notifications. Des corrections de bugs et des ajustements ont été apportés pour améliorer la stabilité et la clarté de l'application. Des fonctionnalités liées aux élections municipales et à l'accueil de mineurs ont également été ajoutées ou améliorées.

### Évolutions fonctionnelles
- Ajout de nouvelles régions pour les DOM-TOM dans la configuration des labels [#281](https://github.com/betagouv/jeveuxaider-front/issues/281).
- Ajout d'une section dédiée aux élections municipales et mise à jour des statistiques associées [#274](https://github.com/betagouv/jeveuxaider-front/issues/274).
- Possibilité de sélectionner un référent régional avec un sélecteur multiple [#266](https://github.com/betagouv/jeveuxaider-front/issues/266).
- Ajout de directives pour l'accueil de volontaires mineurs dans une nouvelle section d'accordéon [#278](https://github.com/betagouv/jeveuxaider-front/issues/278).
- Amélioration de la gestion des témoignages avec une fonctionnalité de revue [#271](https://github.com/betagouv/jeveuxaider-front/issues/271).
- Ajout du champ `is_open_to_minors` et de la logique associée dans les modèles de missions [#251](https://github.com/betagouv/jeveuxaider-front/issues/251).
- Amélioration de la gestion des erreurs avec des messages plus détaillés et des ajustements de mise en page [#279](https://github.com/betagouv/jeveuxaider-front/issues/279).
- Amélioration de la clarté des descriptions des notifications dans le formulaire de configuration des notifications utilisateur [#276](https://github.com/betagouv/jeveuxaider-front/issues/276).
- Notification ajoutée lors de l'export de données par email pour informer de la livraison [#288](https://github.com/betagouv/jeveuxaider-front/issues/288).
- Mise à jour du lien vers les élections municipales pour l'ouvrir dans un nouvel onglet [#282](https://github.com/betagouv/jeveuxaider-front/issues/282).

### Évolutions techniques
- Mise à jour de la gestion des tokens d'accès impersonate après la mise à niveau de Laravel Passport 13 [#276](https://github.com/betagouv/jeveuxaider-front/issues/276).
- Refactorisation de la gestion du cropping manuel pour utiliser des tableaux au lieu de chaînes de caractères [#266](https://github.com/betagouv/jeveuxaider-front/issues/266).
- Suppression de la section "Solidarité crises" de la navigation [#288](https://github.com/betagouv/jeveuxaider-front/issues/288).
- Correction de la condition de statut de chargement dans le composant `BaseBox` [#280](https://github.com/betagouv/jeveuxaider-front/issues/280).
- Résolution d'une vulnérabilité dans la dépendance `ajv` en la mettant à jour vers la version 8.18.0 [#270](https://github.com/betagouv/jeveuxaider-front/issues/270).
- Mise à jour de plusieurs dépendances : `swiper`, `devalue`, `fast-xml-parser`, `qs`, `ckeditor5`, `dompurify`, `tar`, `serialize-javascript`, `minimatch` et `undici`.

### Autres changements
- Mise à jour des liens des fichiers pour la modération et les recommandations [#293](https://github.com/betagouv/jeveuxaider-front/issues/293).
- Ajustements mineurs de l'opération [#290](https://github.com/betagouv/jeveuxaider-front/issues/290).
- Correction du filtre de facette pour refléter les tags d'élections actuels [#289](https://github.com/betagouv/jeveuxaider-front/issues/289).
- Suppression du padding inutile du bouton d'ajout d'email [#267](https://github.com/betagouv/jeveuxaider-front/issues/267).
- Correction de l'affichage des options de rôle en fonction du contexte utilisateur [#294](https://github.com/betagouv/jeveuxaider-front/issues/294).
