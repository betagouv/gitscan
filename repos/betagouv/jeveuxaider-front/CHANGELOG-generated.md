## Changelog : jeveuxaider-front (30 derniers jours, au 14 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment concernant l'affichage des dates des missions et la gestion des publics mineurs. Des optimisations ont également été apportées à la gestion des objectifs de la plateforme et aux statistiques pour les référents. Enfin, des corrections et améliorations techniques ont été réalisées pour la robustesse et la performance de l'application.

### Évolutions fonctionnelles
- Amélioration de l'affichage des dates des missions, notamment pour les missions provenant de l'API "engagement" [#316](https://github.com/betagouv/jeveuxaider-front/issues/316).
- Possibilité pour les référents de voir les détails des personnes qui ont invité des volontaires [#313](https://github.com/betagouv/jeveuxaider-front/issues/313).
- Ajout d'un bouton pour consulter des statistiques détaillées dans l'administration et les pages de tableau de bord [#303](https://github.com/betagouv/jeveuxaider-front/issues/303).
- Amélioration des statistiques PPG pour les référents [#280](https://github.com/betagouv/jeveuxaider-front/issues/280).
- Prise en compte de l'acceptation des mineurs dans les missions, avec l'ajout de propriétés `isMinor` et `isOpenToMinors` pour le suivi [#297](https://github.com/betagouv/jeveuxaider-front/issues/297).
- Mise à jour des liens vers les fichiers 16-18 pour la modération et les recommandations [#293](https://github.com/betagouv/jeveuxaider-front/issues/293).
- Gestion améliorée des missions pour les publics mineurs [#290](https://github.com/betagouv/jeveuxaider-front/issues/290).
- Ajout d'une propriété `isOpenToMinors` pour les missions "Visite" [#297](https://github.com/betagouv/jeveuxaider-front/issues/297).

### Évolutions techniques
- Correction d'un décalage de fuseau horaire en SSR (Server-Side Rendering) et côté client [#317](https://github.com/betagouv/jeveuxaider-front/issues/317).
- Refactorisation de la gestion des objectifs de la plateforme [#304](https://github.com/betagouv/jeveuxaider-front/issues/304).
- Transmission de l'adresse IP du client en SSR pour une meilleure journalisation et limitation du débit [#295](https://github.com/betagouv/jeveuxaider-front/issues/295).
- Mise à jour de plusieurs dépendances : Axios, @unhead/vue, unhead, vite, defu, lodash, lodash-es, srvx, node-forge, picomatch, devalue, undici.
- Correction de l'index z-index de l'image de fond de `LinkToCityAssociations` [#314](https://github.com/betagouv/jeveuxaider-front/issues/314).
- Mise à jour de la logique de formatage des dates pour le fournisseur d'API 'api_engagement' et gestion correcte des valeurs nulles [#316](https://github.com/betagouv/jeveuxaider-front/issues/316).

### Autres changements
- Mise à jour de l'adresse e-mail de support pour les réinitialisations de mot de passe.
- Ajustements pour les missions pour les mineurs [#294](https://github.com/betagouv/jeveuxaider-front/issues/294).
- Mise à jour des options de rôle dans `SecondaryFiltersAdminProfiles` en fonction du contexte utilisateur.
- Correction de la plage de dates pour la section PPP.
- Remplacement d'emojis pour les missions 16-18 ans [#315](https://github.com/betagouv/jeveuxaider-front/issues/315).
