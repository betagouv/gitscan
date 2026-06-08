## Changelog : resorption-bidonvilles (30 derniers jours, au 03 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse et de la qualité du code, notamment au niveau de l'API, ainsi que sur la modernisation de l'interface utilisateur avec l'intégration du Design System Fr (DSFR). Des corrections de bugs et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- Intégration du Design System Fr (DSFR) pour le header, le footer et les boutons de changement d'année, améliorant l'harmonie visuelle et l'accessibilité.
- Correction du lien LinkedIn dans le footer.
- Ajout d'une pastille indiquant les nouveautés sur le blog.
- Suppression de la page 404 inutilisée, la gestion des erreurs étant désormais centralisée via le LayoutError.

### Évolutions techniques
- **API :** Amélioration significative de la robustesse et de la gestion des erreurs, notamment concernant les transactions et les valeurs `undefined`.
- **API :** Refactorisation importante du code, incluant la simplification de fonctions, l'extraction de logique dans des helpers, la suppression de code obsolète et l'amélioration de la lisibilité.
- **API :** Utilisation d'ISOString pour la gestion des dates, remplaçant les timestamps Unix.
- **Tests :** Ajout et correction de tests unitaires pour l'API, notamment pour les services `action/fetch`, `historize` et `resetAsideData`.
- Correction de problèmes d'isolation dans les tests unitaires avec `rewiremock`.
- Suppression de rollbacks intermédiaires inutiles dans l'API.
- Utilisation de générateurs cryptographiquement sécurisés dans les tests.
- Correction d'alertes SonarQube dans l'API.
- Mise à jour des dépendances (v2.53.0, v2.53.1, v2.53.2).

### Autres changements
- Correction de l'import d'un composant.
- Suppression d'éléments inutilisés dans le header.
- Forcer le yarn lock pour assurer la cohérence des dépendances.
- Correction d'une erreur de condition.
- Suppression de props inutiles.
- Traduction d'un message d'erreur dans l'API.
