## Changelog : jeveuxaider-front (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur et de la gestion des rôles, notamment pour les administrateurs et les référents. Des corrections ont été apportées pour assurer la précision des données affichées et l'amélioration de la gestion des notifications. Plusieurs mises à jour techniques ont également été effectuées pour maintenir la sécurité et la performance de la plateforme.

### Évolutions fonctionnelles
- Ajout d'un modal pour les utilisateurs n'ayant pas renseigné leur numéro de téléphone et leur code postal. [#321](https://github.com/betagouv/jeveuxaider-front/issues/321)
- Amélioration de la carte de mission avec l'ajout de détails sur l'activité et la localisation.
- Ajout de la fonctionnalité de changement de rôle et amélioration de la gestion des erreurs associées. [#318](https://github.com/betagouv/jeveuxaider-front/issues/318)
- Amélioration de l'affichage des dates pour les missions "api_engagement" et gestion des valeurs nulles.
- Correction de l'affichage du fond d'écran sur la page des associations. [#314](https://github.com/betagouv/jeveuxaider-front/issues/314)
- Amélioration des permissions pour les responsables, permettant aux référents de voir les informations sur les personnes qui les ont invités. [#313](https://github.com/betagouv/jeveuxaider-front/issues/313)
- Mise à jour de l'adresse email de support pour les demandes de réinitialisation de mot de passe.
- Ajout d'un bouton pour afficher des statistiques détaillées dans l'interface administrateur et le tableau de bord.
- Adaptation pour les mineurs : ajustements et remplacement d'emojis. [#315](https://github.com/betagouv/jeveuxaider-front/issues/315)
- Mise à jour des statistiques PPG pour les référents. [#280](https://github.com/betagouv/jeveuxaider-front/issues/280)
- Évolutions liées à France Travail. [#310](https://github.com/betagouv/jeveuxaider-front/issues/310)

### Évolutions techniques
- Refactorisation des composants modaux pour utiliser `useForm` pour la gestion des formulaires et la validation.
- Refactorisation des composants de prévisualisation de mission et de la boîte d'organisation pour utiliser `BaseTextFormatted` pour le rendu des descriptions.
- Mise à jour du composant `Select` pour accepter `null` comme valeur valide.
- Restriction de l'accès au rôle administrateur pour la page des réseaux.
- Correction d'un décalage de fuseau horaire en SSR et côté client. [#317](https://github.com/betagouv/jeveuxaider-front/issues/317)
- Refactorisation de la gestion des objectifs de la plateforme. [#304](https://github.com/betagouv/jeveuxaider-front/issues/304)

### Autres changements
- Mise à jour de la documentation pour refléter les changements apportés.
- Correction de la date de la section PPP. [#316](https://github.com/betagouv/jeveuxaider-front/issues/316)
- Ajout d'un test de notification pour les administrateurs. [#303](https://github.com/betagouv/jeveuxaider-front/issues/303)
- Mises à jour de dépendances : `dompurify`, `follow-redirects`, `axios`, `@unhead/vue`, `unhead`, `vite`, `defu`, `lodash`, `lodash-es`, `srvx`, `node-forge`, `brace-expansion`, `serialize-javascript`. (Ces mises à jour sont principalement des correctifs de sécurité et de performance.)
