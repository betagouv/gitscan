## Changelog : jeveuxaider-front (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur et de la gestion administrative de la plateforme. Des corrections ont été apportées pour améliorer la précision des informations affichées, notamment les dates et les informations relatives aux missions.  De nouvelles fonctionnalités ont été implémentées pour faciliter la gestion des rôles utilisateurs et l'accès aux statistiques détaillées.  Enfin, la plateforme a été mise à jour pour prendre en compte les évolutions de France Travail et du Plan de Préparation Professionnelle (PPP) 2026.

### Évolutions fonctionnelles
- Ajout d'une pagination simple pour l'index des logs d'activité [#323](https://github.com/betagouv/jeveuxaider-front/issues/323).
- Ajout d'un modal pour les utilisateurs n'ayant pas renseigné leur numéro de téléphone et leur code postal [#318](https://github.com/betagouv/jeveuxaider-front/issues/318).
- Amélioration de la carte de mission complète avec l'ajout de détails sur l'activité et la localisation [#321](https://github.com/betagouv/jeveuxaider-front/issues/321).
- Possibilité de changer de rôle utilisateur et amélioration de la gestion des erreurs liées à l'authentification [#318](https://github.com/betagouv/jeveuxaider-front/issues/318).
- Ajout d'un bouton pour consulter des statistiques détaillées sur les objectifs de la plateforme, accessible dans l'administration et le tableau de bord [#306](https://github.com/betagouv/jeveuxaider-front/issues/306).
- Mise à jour des informations relatives à France Travail [#310](https://github.com/betagouv/jeveuxaider-front/issues/310).
- Mise à jour des informations relatives au PPP 2026 [#307](https://github.com/betagouv/jeveuxaider-front/issues/307).
- Correction de l'affichage des dates pour les missions provenant de l'API "engagement" [#316](https://github.com/betagouv/jeveuxaider-front/issues/316).
- Correction du z-index de l'image de fond de `LinkToCityAssociations` [#314](https://github.com/betagouv/jeveuxaider-front/issues/314).
- Amélioration des permissions pour les responsables, permettant de voir les détails des invitations [#313](https://github.com/betagouv/jeveuxaider-front/issues/313).
- Mise à jour de l'adresse email de support pour la réinitialisation du mot de passe [#308](https://github.com/betagouv/jeveuxaider-front/issues/308).

### Évolutions techniques
- Refactorisation des composants modaux pour utiliser `useForm` pour la gestion et la validation des formulaires.
- Refactorisation des composants `MissionPreview` et `OrganizationBox` pour utiliser `BaseTextFormatted` pour le rendu des descriptions.
- Mise à jour du composant `Select` pour accepter `null` comme valeur valide.
- Restriction de l'accès à l'index des réseaux à l'administrateur uniquement [#320](https://github.com/betagouv/jeveuxaider-front/issues/320).
- Correction d'un décalage de fuseau horaire en SSR et côté client [#317](https://github.com/betagouv/jeveuxaider-front/issues/317).
- Refactorisation de la gestion des objectifs de la plateforme [#304](https://github.com/betagouv/jeveuxaider-front/issues/304).

### Autres changements
- Ajout de champs supplémentaires dans les exports [#327](https://github.com/betagouv/jeveuxaider-front/issues/327).
- Remplacement des emojis pour les 16-18 ans [#315](https://github.com/betagouv/jeveuxaider-front/issues/315).
- Correction de la plage de dates pour le PPP [#317](https://github.com/betagouv/jeveuxaider-front/issues/317).
- Mises à jour des dépendances : `uuid`, `postcss`, `fast-xml-parser`, `dompurify`, `follow-redirects`, `axios`, `@unhead/vue`, `unhead`, `lodash`, `lodash-es`.
