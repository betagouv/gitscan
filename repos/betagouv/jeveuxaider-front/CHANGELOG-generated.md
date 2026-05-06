## Changelog : jeveuxaider-front (30 derniers jours, au 5 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur et l'ajout de nouvelles fonctionnalités, notamment concernant la gestion des missions, des utilisateurs et des statistiques. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Ajout de la possibilité de filtrer les notes autres que celles des Mines. [#328](https://github.com/betagouv/jeveuxaider-front/issues/328)
- Ajout de champs supplémentaires dans les exports de données. [#327](https://github.com/betagouv/jeveuxaider-front/issues/327)
- Implémentation d'une pagination simple pour l'index du journal d'activité. [#323](https://github.com/betagouv/jeveuxaider-front/issues/323)
- Ajout d'un modal pour les utilisateurs sans numéro de téléphone ou code postal. [#321](https://github.com/betagouv/jeveuxaider-front/issues/321)
- Amélioration de la carte de mission avec des détails sur l'activité et le lieu. [#320](https://github.com/betagouv/jeveuxaider-front/issues/320)
- Ajout de la fonctionnalité de changement de rôle et amélioration de la gestion des erreurs. [#318](https://github.com/betagouv/jeveuxaider-front/issues/318)
- Amélioration de l'affichage de la date pour les missions provenant de l'API "engagement". [#316](https://github.com/betagouv/jeveuxaider-front/issues/316)
- Correction de l'affichage du fond d'écran sur les liens vers les associations par ville. [#314](https://github.com/betagouv/jeveuxaider-front/issues/314)
- Amélioration des permissions pour les responsables, permettant aux référents de voir les détails des personnes invitées. [#313](https://github.com/betagouv/jeveuxaider-front/issues/313)
- Mise à jour de l'adresse email de support pour la réinitialisation du mot de passe. [#312](https://github.com/betagouv/jeveuxaider-front/issues/312)
- Ajout d'un bouton pour afficher les statistiques détaillées dans l'administration et le tableau de bord. [#309](https://github.com/betagouv/jeveuxaider-front/issues/309)
- Mise à jour des informations pour le Programme Préparation Professionnelle (PPP) 2026. [#307](https://github.com/betagouv/jeveuxaider-front/issues/307)
- Ajout des entrées Saint-Paul et Avignon aux villes multi-distribuées. [#329](https://github.com/betagouv/jeveuxaider-front/issues/329)
- Correction du décalage horaire en SSR et côté client. [#317](https://github.com/betagouv/jeveuxaider-front/issues/317)
- Correction de la plage de dates pour le PPP. [#315](https://github.com/betagouv/jeveuxaider-front/issues/315)
- Évolutions liées à France Travail. [#310](https://github.com/betagouv/jeveuxaider-front/issues/310)

### Évolutions techniques
- Refactorisation des composants modaux pour utiliser `useForm` pour la gestion et la validation des formulaires.
- Refactorisation des composants de prévisualisation de mission et de la boîte d'organisation pour utiliser `BaseTextFormatted` pour le rendu de la description.
- Mise à jour du composant `Select` pour accepter `null` comme type de valeur valide et refactorisation des composants `Modal` pour utiliser `$apiFetch` et supprimer le code inutilisé.
- Restriction de l'accès au rôle administrateur uniquement pour l'index des réseaux.

### Autres changements
- Remplacement des emojis pour l'âge 16-18 ans.
- Mise à jour des dépendances `@unhead/vue` et `unhead` vers la version 2.1.13.
- Mise à jour des dépendances `axios`, `vite`, `defu`, `dompurify` et `follow-redirects`. (Ces mises à jour sont automatiques et gérées par Dependabot)
