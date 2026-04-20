## Changelog : jeveuxaider-front (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur pour les référents et les administrateurs, avec notamment l'ajout de statistiques PPG pour les référents, la possibilité de changer de rôle et l'amélioration de la gestion des permissions. Des corrections ont également été apportées pour améliorer l'affichage des dates et la gestion des missions, ainsi que des ajustements pour les missions destinées aux mineurs.

### Évolutions fonctionnelles
- Ajout de la fonctionnalité de changement de rôle et amélioration de la gestion des erreurs. [#318](https://github.com/betagouv/jeveuxaider-front/issues/318)
- Les référents peuvent désormais consulter les statistiques PPG. [#280](https://github.com/betagouv/jeveuxaider-front/issues/280)
- Amélioration de l'affichage des dates pour les missions provenant de l'API "engagement". [#316](https://github.com/betagouv/jeveuxaider-front/issues/316)
- Correction de l'affichage des dates pour les missions "PPP". [#317](https://github.com/betagouv/jeveuxaider-front/issues/317)
- Ajout d'un bouton pour consulter des statistiques détaillées dans l'administration et les pages de tableau de bord.
- Amélioration des permissions pour les référents, leur permettant de voir les détails des personnes qui les ont invités. [#313](https://github.com/betagouv/jeveuxaider-front/issues/313)
- Ajustements pour les missions destinées aux mineurs, avec l'ajout des propriétés `isMinor` et `isOpenToMinors` pour un meilleur suivi. [#297](https://github.com/betagouv/jeveuxaider-front/issues/297)
- Mise à jour de l'adresse email de support pour la réinitialisation du mot de passe.

### Évolutions techniques
- Refactorisation de la gestion des objectifs de la plateforme. [#304](https://github.com/betagouv/jeveuxaider-front/issues/304)
- Correction d'un problème de décalage horaire entre le serveur et le client.
- Correction du z-index de l'image de fond de `LinkToCityAssociations`. [#314](https://github.com/betagouv/jeveuxaider-front/issues/314)
- Mise à jour de plusieurs dépendances : `axios`, `@unhead/vue`, `unhead`, `vite`, `defu`, `lodash`, `lodash-es`, `node-forge`, `picomatch`, `serialize-javascript`, `dompurify`, `follow-redirects`, `srvx`, `brace-expansion`.

### Autres changements
- Ajout d'une notification de test pour les administrateurs. [#303](https://github.com/betagouv/jeveuxaider-front/issues/303)
- Remplacement d'emojis pour les tranches d'âge 16-18 ans. [#315](https://github.com/betagouv/jeveuxaider-front/issues/315)
- Correction de la plage de dates pour la section PPP. [#310](https://github.com/betagouv/jeveuxaider-front/issues/310)
- Correction de la logique de formatage des dates pour le fournisseur `api_engagement` et gestion des valeurs nulles.
- Ajustements pour les missions de volontariat mineurs. [#294](https://github.com/betagouv/jeveuxaider-front/issues/294)
- Correction d'un bug dans la section "Mission - Visite" concernant la propriété `isOpenToMinors`.
