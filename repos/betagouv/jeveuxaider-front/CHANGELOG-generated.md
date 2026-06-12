## Changelog : jeveuxaider-front (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience d'inscription des organisations et des missions, notamment en simplifiant les formulaires et en ajoutant de nouvelles fonctionnalités de gestion des tags et des ressources. Des corrections ont également été apportées pour améliorer la stabilité et la convivialité de la plateforme, ainsi que des ajustements pour la campagne d'été et la période de canicule.

### Évolutions fonctionnelles
- **Gestion des organisations :** Refonte des formulaires d'inscription des organisations avec une meilleure gestion des adresses, des logos et des informations de contact. [#346](https://github.com/betagouv/jeveuxaider-front/issues/346)
- **Gestion des tags :** Implémentation d'un nouveau formulaire pour la gestion des tags des structures, avec validation et soumission améliorées.
- **Partage de missions :** Amélioration du partage de missions, notamment pour les utilisateurs non-gestionnaires. [#353](https://github.com/betagouv/jeveuxaider-front/issues/353)
- **Campagne d'été :** Mise à jour des composants `MissionInfos` et `Section` pour la campagne d'été.
- **Canicule :** Ajout d'un lien "Canicule" dans la navigation secondaire pour faciliter l'accès aux informations relatives aux événements liés à la canicule.
- **Statistiques :** Affichage du nom au lieu de la clé dans les statistiques de visites. [#337](https://github.com/betagouv/jeveuxaider-front/issues/337)
- **Désinscription des organisations :** Permettre aux organisations de se désinscrire de manière autonome. [#322](https://github.com/betagouv/jeveuxaider-front/issues/322)
- **Fermeture des inscriptions :** Modification du libellé "Fermer les inscriptions" en "Mettre en pause les inscriptions" pour une meilleure clarté.
- **Filtre de localisation :** Mise à jour des options de rayon dans le filtre de localisation, incluant 0 et 1000. [#342](https://github.com/betagouv/jeveuxaider-front/issues/342)

### Évolutions techniques
- **Refactoring :** Plusieurs refactorings ont été effectués pour améliorer la structure du code et la maintenabilité, notamment dans les composants d'organisation et de formulaire.
- **Mise à jour des dépendances :** Mise à jour de plusieurs dépendances, notamment `axios`, `qs`, `brace-expansion` et `shell-quote`.
- **Plausible Analytics :** Mise à jour de l'intégration avec Plausible Analytics pour utiliser l'API v2 et corriger un filtre de date défectueux. [#344](https://github.com/betagouv/jeveuxaider-front/issues/344)
- **ARIA attributes:** Mise à jour des attributs ARIA pour éviter les exigences d'attributs avec tiret. [#349](https://github.com/betagouv/jeveuxaider-front/issues/349)

### Autres changements
- **Documentation :** Mise à jour de la description du projet et de la pile technique dans le fichier README.
- **Dates canicule :** Mise à jour des dates des événements canicule de juin à août.
- **Labels Rolables:** Mise à jour des labels `rolables.fonction`. [#348](https://github.com/betagouv/jeveuxaider-front/issues/348)
- **UTM parameters:** Ajout de paramètres UTM pour le soft gate Invitations.
- **Soft gate Invitations:** Correction du comportement sur certains appareils mobiles.
