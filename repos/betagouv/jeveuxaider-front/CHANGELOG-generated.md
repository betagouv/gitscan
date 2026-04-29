## Changelog : jeveuxaider-front (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur et de la gestion des rôles, notamment pour les administrateurs et les référents. Des corrections ont été apportées pour améliorer la précision des données affichées et la gestion des erreurs. Plusieurs améliorations techniques ont également été implémentées pour optimiser la plateforme et préparer les campagnes à venir.

### Évolutions fonctionnelles
- Ajout d'un modal pour les utilisateurs n'ayant pas renseigné leur numéro de téléphone et leur code postal. [#321](https://github.com/betagouv/jeveuxaider-front/issues/321)
- Amélioration de la carte de mission avec l'ajout de détails sur l'activité et la localisation.
- Ajout de la fonctionnalité de changement de rôle et amélioration de la gestion des erreurs associées. [#318](https://github.com/betagouv/jeveuxaider-front/issues/318)
- Amélioration de la gestion des permissions pour les responsables, permettant aux référents de voir les détails des personnes invitées. [#313](https://github.com/betagouv/jeveuxaider-front/issues/313)
- Mise à jour de l'adresse email de support pour les demandes de réinitialisation de mot de passe.
- Ajout d'un bouton pour afficher les statistiques détaillées des objectifs JVA dans l'administration et le tableau de bord.
- Correction de l'affichage de la date pour les missions provenant de l'API "engagement". [#316](https://github.com/betagouv/jeveuxaider-front/issues/316)
- Correction de l'affichage de la date pour les sections PPP. [#317](https://github.com/betagouv/jeveuxaider-front/issues/317)
- Ajustements pour les mineurs bénévoles. [#294](https://github.com/betagouv/jeveuxaider-front/issues/294)
- Statistiques PPG pour les référents. [#280](https://github.com/betagouv/jeveuxaider-front/issues/280)

### Évolutions techniques
- Refactorisation des composants modaux pour utiliser `useForm` pour la gestion et la validation des formulaires.
- Refactorisation des composants de prévisualisation de mission et de la boîte d'organisation pour utiliser `BaseTextFormatted` pour le rendu de la description.
- Mise à jour du composant `Select` pour accepter `null` comme type de valeur valide.
- Restriction de l'accès au rôle administrateur pour l'index des réseaux.
- Correction d'un décalage de fuseau horaire en SSR et côté client.
- Refactorisation de la gestion des objectifs de la plateforme. [#304](https://github.com/betagouv/jeveuxaider-front/issues/304)
- Mise à jour des dépendances : `dompurify`, `follow-redirects`, `axios`, `@unhead/vue`, `unhead`, `vite`, `defu`, `lodash`, `lodash-es`, `serialize-javascript`.

### Autres changements
- Mise à jour des emojis pour les 16-18 ans. [#315](https://github.com/betagouv/jeveuxaider-front/issues/315)
- Correction du `z-index` de l'image de fond pour `LinkToCityAssociations`. [#314](https://github.com/betagouv/jeveuxaider-front/issues/314)
- Ajout d'un test de notification pour l'administrateur. [#303](https://github.com/betagouv/jeveuxaider-front/issues/303)
- Préparation pour la campagne PPP 2026. [#307](https://github.com/betagouv/jeveuxaider-front/issues/307)
- Évolutions France Travail. [#310](https://github.com/betagouv/jeveuxaider-front/issues/310)
