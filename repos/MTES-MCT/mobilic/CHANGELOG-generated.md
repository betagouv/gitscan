## Changelog : mobilic (30 derniers jours, au 09 juillet 2026)

### Résumé
Les dernières mises à jour de mobilic améliorent l'expérience utilisateur, notamment sur la gestion des missions (annulation, validation), l'interface d'administration et la navigation. Des corrections de bugs et des améliorations de performance ont également été apportées. L'application s'adapte mieux aux différents rôles utilisateurs et aux configurations spécifiques.

### Évolutions fonctionnelles
- Ajout de la possibilité d'annuler une mission en cours. [#889](https://github.com/MTES-MCT/mobilic/issues/889)
- Amélioration de la vue des activités pour les administrateurs, avec des corrections de tri et d'affichage. [#885](https://github.com/MTES-MCT/mobilic/issues/885)
- Modification du libellé pour les missions de transport de marchandises lourdes. [#881](https://github.com/MTES-MCT/mobilic/issues/881)
- Modification du type de bouton d'édition d'activité pour utiliser un composant DSFR. [#879](https://github.com/MTES-MCT/mobilic/issues/879)
- Amélioration de la gestion de la validation des missions dans l'interface d'administration (rafraîchissement des données). [#874](https://github.com/MTES-MCT/mobilic/issues/874) et [#873](https://github.com/MTES-MCT/mobilic/issues/873)
- Ajout de la possibilité de modifier les jours de travail enregistrés. [#859](https://github.com/MTES-MCT/mobilic/issues/859)
- Modification du format d'affichage de l'heure des activités pour les employés. [#880](https://github.com/MTES-MCT/mobilic/issues/880)
- Suppression de l'option FranceConnect lors de l'inscription d'un employé. [#890](https://github.com/MTES-MCT/mobilic/issues/890)
- Ajout de logos de partenaires sur la page dédiée. [#892](https://github.com/MTES-MCT/mobilic/issues/892)

### Évolutions techniques
- Refonte de l'en-tête (header) avec le DSFR, améliorant l'accessibilité et l'adaptabilité mobile.
- Optimisation des requêtes pour éviter les doublons et améliorer les performances. [#886](https://github.com/MTES-MCT/mobilic/issues/886)
- Amélioration de la gestion des filtres après validation d'une mission ou d'un congé. [#893](https://github.com/MTES-MCT/mobilic/issues/893)
- Refactoring du code pour centraliser les constantes et améliorer la lisibilité.
- Mise à jour de la gestion des logos des partenaires pour une meilleure intégration visuelle.
- Amélioration de la persistance de l'ID de l'entreprise sélectionnée dans l'en-tête.
- Optimisation de la barre de validation fixe sur la page de détails de la mission.
- Correction de bugs et amélioration de la qualité du code (linting, suppression de code inutile).

### Autres changements
- Mise à jour de la documentation du contrôleur. [#871](https://github.com/MTES-MCT/mobilic/issues/871)
- Amélioration de la page d'accueil avec l'intégration du DSFR header et footer. [#869](https://github.com/MTES-MCT/mobilic/issues/869)
- Correction de problèmes d'affichage et de style divers.
- Correction de problèmes d'accessibilité.
- Ajustements de style pour améliorer l'expérience utilisateur.
