## Changelog : jeveuxaider-front (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment en améliorant la géolocalisation, l'affichage des missions et la gestion des utilisateurs. Des corrections de bugs ont également été apportées pour assurer la stabilité et la fiabilité de la plateforme. Des évolutions liées à France Travail ont été intégrées.

### Évolutions fonctionnelles
- **Géolocalisation :** Amélioration du support de la géolocalisation pour les villes multi-distribuées [#330](https://github.com/betagouv/jeveuxaider-front/pull/330). Ajout de Saint-Paul et d'Avignon à la liste des villes concernées [#329](https://github.com/betagouv/jeveuxaider-front/pull/329).
- **Filtres des notes :** Ajout d'options de filtrage pour les notes autres que les miennes [#328](https://github.com/betagouv/jeveuxaider-front/pull/328).
- **Exports :** Ajout de champs supplémentaires dans les exports de données [#327](https://github.com/betagouv/jeveuxaider-front/pull/327).
- **Pagination :** Ajout d'une pagination simple pour l'index des activités [#323](https://github.com/betagouv/jeveuxaider-front/pull/323).
- **Modals :** Refonte des composants modaux pour utiliser `useForm` pour la gestion et la validation des formulaires [#318](https://github.com/betagouv/jeveuxaider-front/pull/318).
- **Informations missions :** Amélioration de l'affichage des missions avec des détails sur l'activité et la localisation [#321](https://github.com/betagouv/jeveuxaider-front/pull/321).
- **France Travail :** Intégration d'évolutions spécifiques à France Travail [#310](https://github.com/betagouv/jeveuxaider-front/pull/310).
- **Date PPP :** Correction de la plage de dates pour le PPP [#317](https://github.com/betagouv/jeveuxaider-front/pull/317).
- **Affichage des dates :** Correction du formatage des dates pour les missions provenant de l'API "api_engagement" [#316](https://github.com/betagouv/jeveuxaider-front/pull/316).
- **Z-index :** Correction du `z-index` pour l'image de fond du composant `LinkToCityAssociations` [#314](https://github.com/betagouv/jeveuxaider-front/pull/314).

### Évolutions techniques
- **Refactoring :** Refactoring des composants `CardMissionFull`, `mission preview` et `organization box` pour utiliser `BaseTextFormatted` pour le rendu des descriptions [#321](https://github.com/betagouv/jeveuxaider-front/pull/321).
- **Authentification :** Restriction de l'accès au rôle administrateur pour l'index des réseaux [#320](https://github.com/betagouv/jeveuxaider-front/pull/320).
- **Timezone :** Correction d'un décalage de fuseau horaire en SSR et côté client [#317](https://github.com/betagouv/jeveuxaider-front/pull/317).
- **Typescript :** Mise à jour du type accepté par le composant `Select` pour autoriser `null` comme valeur valide [#321](https://github.com/betagouv/jeveuxaider-front/pull/321).

### Autres changements
- Suppression de code inutilisé dans les composants modaux.
- Amélioration de la gestion des erreurs lors du changement de rôle utilisateur.
- Remplacement d'emojis pour les tranches d'âge 16-18.
