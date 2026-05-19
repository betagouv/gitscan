## Changelog : otelo (30 derniers jours, au 18 mai 2026)

### Résumé
Ce mois-ci, otelo a bénéficié d'améliorations significatives sur le tableau de bord, notamment une refonte complète et l'ajout de nouvelles fonctionnalités de comparaison de scénarios. Des corrections et des améliorations de l'expérience utilisateur ont également été apportées, ainsi que des ajustements pour la recette de mai 2026.

### Évolutions fonctionnelles
- Refonte du tableau de bord avec affichage des valeurs dans le tableau comparatif et comparaison des scénarios. [#40](https://github.com/MTES-MCT/otelo/pull/40)
- Ajout de la comparaison en pourcentage entre les valeurs de logement vacant et de logements en attente. [#39](https://github.com/MTES-MCT/otelo/pull/39)
- Prévisualisation des résultats directement dans les formulaires de création/modification. [#39](https://github.com/MTES-MCT/otelo/pull/39)
- Implémentation d'une nouvelle méthode pour gérer les situations sans hébergement. [#42](https://github.com/MTES-MCT/otelo/pull/42)
- Possibilité pour un administrateur d'usurper l'identité d'un autre utilisateur. [#40](https://github.com/MTES-MCT/otelo/pull/40)
- Amélioration de l'expérience utilisateur (UX) générale. [#30](https://github.com/MTES-MCT/otelo/issues/30)
- Correction de bugs liés au recalcul du script CLI pour le millésime. [#40](https://github.com/MTES-MCT/otelo/pull/40)
- Correction de problèmes liés à la recette de mai 2026. [#45](https://github.com/MTES-MCT/otelo/pull/45)

### Évolutions techniques
- Mise à jour de Next.js. [#43](https://github.com/MTES-MCT/otelo/pull/43)
- Amélioration du clonage des données en fonction du millésime et mise en cache des résultats pour optimiser les performances. [#40](https://github.com/MTES-MCT/otelo/pull/40)
- Correction d'un problème empêchant l'envoi d'emails en environnement local. [#40](https://github.com/MTES-MCT/otelo/pull/40)
- Vérification de la propriété des groupes EPCI. [#39](https://github.com/MTES-MCT/otelo/pull/39)

### Autres changements
- Correction de typos.
- Ajustements CSS mineurs.
- Limitation du nombre de groupes EPCI.
- Correction de la construction du projet.
- Correction d'un problème lié aux pics de logements vacants/RS.
