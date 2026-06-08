## Changelog : diagbruit.beta.gouv.fr (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur et la correction de bugs. L'ajout d'un lien vers la documentation et l'amélioration de l'affichage des zones bruyantes par alerte facilitent l'utilisation de la plateforme. Des corrections ont également été apportées pour améliorer la précision des informations affichées concernant les risques sonores.

### Évolutions fonctionnelles
- Ajout d'un lien vers la documentation dans le pied de page pour une meilleure accessibilité à l'aide. [#81](https://github.com/betagouv/diagbruit.beta.gouv.fr/pull/81)
- Amélioration de l'affichage des zones bruyantes : affichage des zones uniques par alerte pour une meilleure clarté. [#93](https://github.com/betagouv/diagbruit.beta.gouv.fr/pull/93)
- Correction de l'affichage du libellé des risques sonores dans le résumé.
- Ajout de paramètres de requête spécifiques pour cibler les références de parcelles. [#80](https://github.com/betagouv/diagbruit.beta.gouv.fr/pull/80)

### Évolutions techniques
- Isolation des fonctions de classification sonore avec des règles cumulatives pour une meilleure maintenabilité et testabilité.
- Ajout de tests unitaires pour les fonctions d'isolation.
- Correction d'un problème de ciblage de lien dans la documentation. [#81](https://github.com/betagouv/diagbruit.beta.gouv.fr/pull/81)

### Autres changements
- Aucun autre changement significatif à signaler.
