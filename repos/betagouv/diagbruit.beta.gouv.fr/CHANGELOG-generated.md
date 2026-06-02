## Changelog : diagbruit.beta.gouv.fr (30 derniers jours, au 19 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment en ajoutant de la documentation accessible et en affinant la recherche de parcelles. Des corrections ont également été apportées pour améliorer la précision des classifications sonores et la sécurité du système. L'ajout d'un plugin Matomo permet de suivre l'utilisation de l'application pour de futures optimisations.

### Évolutions fonctionnelles
- Ajout d'un lien vers la documentation dans le pied de page pour une meilleure accessibilité. [#81](https://github.com/betagouv/diagbruit.beta.gouv.fr/pull/81)
- Amélioration de la recherche de parcelles avec des paramètres de requête spécifiques pour cibler les références de parcelle. [#80](https://github.com/betagouv/diagbruit.beta.gouv.fr/pull/80)
- Correction de l'affichage du libellé des risques sonores dans le résumé. [#80](https://github.com/betagouv/diagbruit.beta.gouv.fr/pull/80)
- Correction d'un bug dans la recherche de parcelles qui supprimait l'adresse dans l'URL. [#76](https://github.com/betagouv/diagbruit.beta.gouv.fr/pull/76)
- Suppression du lien sur la description des réglementations. [#72](https://github.com/betagouv/diagbruit.beta.gouv.fr/pull/72)
- Amélioration de la sécurité concernant la réception des emails. [#75](https://github.com/betagouv/diagbruit.beta.gouv.fr/pull/75)

### Évolutions techniques
- Ajout d'un plugin Matomo pour le suivi des heatmaps et l'analyse du comportement des utilisateurs. [#78](https://github.com/betagouv/diagbruit.beta.gouv.fr/pull/78)
- Correction du typage de `typesource` en `sound_category` dans `RegulationCls`. [#77](https://github.com/betagouv/diagbruit.beta.gouv.fr/pull/77)
- Amélioration de l'isolation des fonctions de classification sonore avec des règles cumulatives. [#80](https://github.com/betagouv/diagbruit.beta.gouv.fr/pull/80)
- Ajout de tests pour les fonctions d'isolation. [#80](https://github.com/betagouv/diagbruit.beta.gouv.fr/pull/80)

### Autres changements
- Mise à jour de la documentation pour cibler les liens vers des pages vides. [#81](https://github.com/betagouv/diagbruit.beta.gouv.fr/pull/81)
- Amélioration de la formulation de certains textes. [#80](https://github.com/betagouv/diagbruit.beta.gouv.fr/pull/80)
