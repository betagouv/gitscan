## Changelog : statistiques-impact (30 derniers jours, au 18 mai 2026)

### Résumé
Ce changelog présente les améliorations apportées au site statistiques-impact au cours du dernier mois. Les modifications concernent principalement des corrections de bugs et des ajustements techniques au niveau des modèles de données et de l'API, visant à améliorer la stabilité et la fiabilité de la plateforme.

### Évolutions fonctionnelles
Aucune évolution fonctionnelle majeure n'a été déployée durant cette période.

### Évolutions techniques
- Correction d'un bug où les slugs étaient régénérés à chaque sauvegarde des modèles, ce qui pouvait impacter les URLs et le SEO. [#16cf5b2](https://github.com/numerique-gouv/statistiques-impact/commit/16cf5b2)
- Modification du champ utilisé pour la recherche des indicateurs dans l'API, améliorant potentiellement la performance et la précision des requêtes. [#ed708f4](https://github.com/numerique-gouv/statistiques-impact/commit/ed708f4)
- Ajout d'un fichier de migration manquant dans la base de données, corrigeant un problème potentiel lors des déploiements. [#a9bf3c9](https://github.com/numerique-gouv/statistiques-impact/commit/a9bf3c9)
- Amélioration des tests liés à l'authentification pour une meilleure couverture et fiabilité. [#aa2f691](https://github.com/numerique-gouv/statistiques-impact/commit/aa2f691)
- Correction d'un test défaillant suite à une réinitialisation de la démo datagouv. [#f143fff](https://github.com/numerique-gouv/statistiques-impact/commit/f143fff)

### Autres changements
Aucun autre changement significatif à signaler.
