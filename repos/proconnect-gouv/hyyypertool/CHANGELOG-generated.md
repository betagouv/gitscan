## Changelog : hyyypertool (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la fiche utilisateur avec l'ajout de l'historique de connexion OIDC et sa pagination, ainsi que l'ajout de badges d'informations sur les organisations. Des corrections et améliorations ont également été apportées concernant la gestion des motifs de refus et des liens vers les profils utilisateurs. De nombreuses mises à jour de dépendances ont été réalisées pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- Ajout de la pagination de l'historique de connexion OIDC sur la page utilisateur pour une meilleure lisibilité. [#1678](https://github.com/proconnect-gouv/hyyypertool/issues/1678)
- Affichage de l'historique de connexion OIDC sur la fiche utilisateur, permettant de suivre les accès aux services ProConnect. [#1673](https://github.com/proconnect-gouv/hyyypertool/issues/1673)
- Ajout de badges de caractéristiques (type de service public, statut de diffusion, activité, siège social, éligibilité à la vérification) sur les fiches organisation. [#1672](https://github.com/proconnect-gouv/hyyypertool/issues/1672)
- Ajout du champ "raison du refus" lors de la gestion des utilisateurs. [#1652](https://github.com/proconnect-gouv/hyyypertool/issues/1652)
- Le courriel d'alerte a été corrigé pour une meilleure clarté. [#1654](https://github.com/proconnect-gouv/hyyypertool/issues/1654)
- L'email du membre est désormais un lien vers son profil utilisateur. [#1653](https://github.com/proconnect-gouv/hyyypertool/issues/1653)

### Évolutions techniques
- Remplacement des modals SSR par des "Preact islands" auto-contenues pour optimiser le rendu et les performances. [#1627](https://github.com/proconnect-gouv/hyyypertool/issues/1627)
- Mise à jour de la librairie `@proconnect-gouv/proconnect.identite` vers la version 9.1.3. [#1668](https://github.com/proconnect-gouv/hyyypertool/issues/1668)
- Mise à jour de plusieurs dépendances pour améliorer la sécurité et la stabilité de l'application.

### Autres changements
- Mise à jour de la configuration des valeurs ACR (Action Claim Request) pour l'authentification. [#1687](https://github.com/proconnect-gouv/hyyypertool/issues/1687)
- Publication des versions 2026.6.5, 2026.6.4, 2026.6.3, 2026.6.2, 2026.6.1 et 2026.6.0.
