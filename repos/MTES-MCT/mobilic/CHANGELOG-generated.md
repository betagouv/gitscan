## Changelog : mobilic (30 derniers jours, au 27 juillet 2026)

### Résumé
Les dernières mises à jour de mobilic se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la gestion des litiges et des missions, ainsi que sur la correction de bugs et l'optimisation des performances. L'interface a été modernisée avec l'intégration du Design System de la République Française (DSFR) pour la page d'accueil, et des améliorations ont été apportées à la gestion des demandes de détachement.

### Évolutions fonctionnelles
- Ajout de la possibilité pour les employés de contester une mission directement depuis l'interface [#884](https://github.com/MTES-MCT/mobilic/pulls/884).
- Implémentation d'une fonctionnalité permettant d'abandonner une mission en cours [#7cb1b8bc](https://github.com/MTES-MCT/mobilic/commits/7cb1b8bc).
- Ajout d'une demande de détachement avec une période de refroidissement et une possibilité de relance [#a6bcde6f](https://github.com/MTES-MCT/mobilic/commits/a6bcde6f).
- Amélioration de l'affichage des activités et des validations pour les administrateurs [#33a8abdb](https://github.com/MTES-MCT/mobilic/pulls/33a8abdb).
- Modification de l'étiquette pour les missions impliquant des poids lourds [#95d66294](https://github.com/MTES-MCT/mobilic/commits/95d66294).
- Intégration de nouveaux logos de partenaires sur la page dédiée [#f906d272](https://github.com/MTES-MCT/mobilic/pulls/f906d272).
- Refonte de l'en-tête et du pied de page avec le Design System de la République Française (DSFR) [#164cb3d8](https://github.com/MTES-MCT/mobilic/pulls/164cb3d8).
- Amélioration de l'affichage des informations relatives aux activités et validations dans l'historique des employés [#5d847d6d](https://github.com/MTES-MCT/mobilic/commits/5d847d6d).

### Évolutions techniques
- Optimisation des requêtes pour l'historique des activités afin de réduire les doublons et améliorer les performances [#49919d52](https://github.com/MTES-MCT/mobilic/commits/49919d52).
- Refactorisation du code pour réduire la complexité cognitive dans divers composants (DurationDisplay, notifications, etc.) [#8bbdabae](https://github.com/MTES-MCT/mobilic/commits/8bbdabae).
- Suppression de FranceConnect du processus d'inscription des employés [#f7ccef15](https://github.com/MTES-MCT/mobilic/commits/f7ccef15).
- Mise à jour de l'infrastructure pour éviter les erreurs réseau récurrentes dans Sentry [#835421dd](https://github.com/MTES-MCT/mobilic/commits/835421dd).
- Amélioration de la gestion des erreurs et des validations pour éviter les erreurs 403 et améliorer la robustesse de l'application [#f2f90afe](https://github.com/MTES-MCT/mobilic/commits/f2f90afe).
- Correction de plusieurs problèmes liés à l'interface utilisateur (DSFR, espacements, etc.) [#96915c74](https://github.com/MTES-MCT/mobilic/commits/96915c74).

### Autres changements
- Amélioration de la description des changements dans les bannières de litige pour une meilleure clarté [#b2a76144](https://github.com/MTES-MCT/mobilic/commits/b2a76144).
- Correction de bugs mineurs et améliorations de la qualité du code suite aux revues de pull requests.
- Optimisation du nombre d'appels API pour la récupération des webinaires [#8193ebfa](https://github.com/MTES-MCT/mobilic/commits/8193ebfa).
- Mise à jour de la documentation et des commentaires dans le code.
