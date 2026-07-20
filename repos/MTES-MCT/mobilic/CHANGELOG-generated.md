## Changelog : mobilic (30 derniers jours, au 16 juillet 2026)

### Résumé
Les dernières mises à jour de mobilic se concentrent sur l'amélioration de l'interface utilisateur, notamment la refonte de l'en-tête avec le design systeme DSFR, l'optimisation des performances et la correction de bugs. Des améliorations ont également été apportées à la gestion des missions et des activités, ainsi qu'à l'expérience administrateur.

### Évolutions fonctionnelles
- L'en-tête a été mis à jour avec le design système DSFR, incluant un menu mobile plus accessible et une meilleure gestion des logos des partenaires [#869](https://github.com/MTES-MCT/mobilic/pull/869), [#892](https://github.com/MTES-MCT/mobilic/pull/892).
- Ajout de la possibilité d'annuler une mission en cours [#889](https://github.com/MTES-MCT/mobilic/pull/889).
- Modification du libellé pour les camions lourds dans la gestion des congés [#878](https://github.com/MTES-MCT/mobilic/pull/878).
- Amélioration de la vue des activités pour les administrateurs, avec notamment un affichage plus clair des informations et une meilleure gestion des filtres [#878](https://github.com/MTES-MCT/mobilic/pull/878), [#885](https://github.com/MTES-MCT/mobilic/pull/885).
- Modification du format d'affichage de l'heure des activités pour une meilleure lisibilité [#880](https://github.com/MTES-MCT/mobilic/pull/880).
- Changement du type de bouton "Modifier" pour les activités (utilisation d'un composant DSFR) [#879](https://github.com/MTES-MCT/mobilic/pull/879).
- Ajout du logo Perff sur la page des partenaires [#892](https://github.com/MTES-MCT/mobilic/pull/892).
- Suppression de l'option FranceConnect lors de l'inscription d'un employé [#890](https://github.com/MTES-MCT/mobilic/pull/890).

### Évolutions techniques
- Optimisation des appels API pour la récupération des webinaires afin d'améliorer les performances [#894](https://github.com/MTES-MCT/mobilic/pull/894).
- Refactoring de l'en-tête pour une meilleure lisibilité et maintenabilité du code, incluant la centralisation de constantes et la simplification de la logique de rendu [#892](https://github.com/MTES-MCT/mobilic/pull/892).
- Amélioration de la gestion des filtres après validation d'une mission ou d'un congé [#893](https://github.com/MTES-MCT/mobilic/pull/893), [#883](https://github.com/MTES-MCT/mobilic/pull/883).
- Correction de problèmes de performance liés à des requêtes dupliquées dans l'historique des activités [#886](https://github.com/MTES-MCT/mobilic/pull/886).
- Mise en place de filtres pour ignorer les erreurs réseau récurrentes dans Sentry, réduisant le bruit et facilitant l'identification des problèmes réels [#891](https://github.com/MTES-MCT/mobilic/pull/891).
- Correction de plusieurs avertissements SonarQube et amélioration de la qualité du code.

### Autres changements
- Correction de divers problèmes d'accessibilité dans l'en-tête.
- Amélioration de la gestion des états visuels (hover, actif) des éléments de navigation.
- Ajustements de style et de mise en page pour améliorer l'apparence générale de l'application.
- Correction de bugs mineurs et améliorations de la stabilité.
- Mise à jour de la documentation.
