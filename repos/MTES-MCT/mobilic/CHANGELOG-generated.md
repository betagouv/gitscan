## Changelog : mobilic (30 derniers jours, au 13 juillet 2026)

### Résumé
Les dernières mises à jour de mobilic se concentrent sur l'amélioration de l'interface utilisateur, notamment la refonte de l'en-tête et du pied de page avec les composants DSFR, ainsi que des corrections de bugs et des optimisations de performance. Des améliorations ont également été apportées à la gestion des missions et des activités, en particulier dans l'interface administrateur.

### Évolutions fonctionnelles
- Refonte de l'en-tête et du pied de page avec les composants du Design System de la République Française (DSFR) [#900](https://github.com/MTES-MCT/mobilic/pull/900).
- Ajout de la possibilité d'annuler une mission en cours [#889](https://github.com/MTES-MCT/mobilic/pull/889).
- Amélioration de la vue des activités pour les administrateurs : affichage du kilométrage même sans saisie, correction de l'ordre de tri, et amélioration de la présentation générale [#885](https://github.com/MTES-MCT/mobilic/pull/885).
- Modification du format d'affichage de l'heure des activités pour une meilleure lisibilité [#880](https://github.com/MTES-MCT/mobilic/pull/880).
- Modification du type de bouton d'édition d'activité pour utiliser un composant DSFR [#879](https://github.com/MTES-MCT/mobilic/pull/879).
- Ajout du logo Perff à la page des partenaires [#892](https://github.com/MTES-MCT/mobilic/pull/892) et [#869](https://github.com/MTES-MCT/mobilic/pull/869).
- Correction de l'affichage du libellé pour le transport lourd dans les congés [#881](https://github.com/MTES-MCT/mobilic/pull/881).
- Suppression de l'option FranceConnect pour l'inscription des employés [#890](https://github.com/MTES-MCT/mobilic/pull/890) et [#875](https://github.com/MTES-MCT/mobilic/pull/875).
- Ajout de la possibilité d'ajouter des jours de travail modifiés [#859](https://github.com/MTES-MCT/mobilic/pull/859).

### Évolutions techniques
- Optimisation des appels API pour la récupération des webinaires [#894](https://github.com/MTES-MCT/mobilic/pull/894).
- Refactorisation de l'en-tête pour améliorer la lisibilité et la maintenabilité du code.
- Centralisation de la constante `DSFR_BRAND_TOP` pour une meilleure cohérence.
- Amélioration de la performance en dédupliquant les requêtes d'historique [#886](https://github.com/MTES-MCT/mobilic/pull/886).
- Correction de problèmes liés au rafraîchissement des données dans l'interface administrateur [#874](https://github.com/MTES-MCT/mobilic/pull/874) et [#893](https://github.com/MTES-MCT/mobilic/pull/893).
- Utilisation de `Number.parseInt` au lieu de `parseInt` pour éviter des erreurs potentielles.
- Correction de problèmes d'accessibilité liés à l'icône du menu mobile.
- Mise à jour des dépendances et correction de problèmes de linting.

### Autres changements
- Correction de divers problèmes de style et de mise en page.
- Amélioration de la documentation.
- Correction de typos dans la documentation [#871](https://github.com/MTES-MCT/mobilic/pull/871).
- Correction de bugs mineurs et amélioration de la stabilité générale de l'application.
- Correction de problèmes de rendu et d'affichage sur différents écrans.
- Correction de problèmes de style sur la page de contrôle.
